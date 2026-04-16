import asyncio
import json
import os
from datetime import datetime
from pathlib import Path
from typing import Any

import pandas as pd
import streamlit as st


# Page setup

st.set_page_config(
    page_title="Competitive Research Tool",
    page_icon="🔍",
    layout="wide",
    initial_sidebar_state="expanded",
)


APP_CSS = """
<style>
html, body, [class*="css"] {
    font-family: 'uncut-sans', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif !important;
}

:root {
    --bg-main: #0E1117;
    --bg-sidebar: #172529;
    --bg-card: #111827;
    --brand-green: #173E3F;
    --brand-green-hover: #446464;
    --brand-blue: #5B93A4;
    --brand-blue-soft: rgba(91, 147, 164, 0.2);
    --info-bg: #1E3A5F;
    --text-main: #FFFFFF;
    --text-muted: #CBD5E1;
    --text-sidebar: #E6F4F1;
}

.stApp {
    background-color: var(--bg-main);
}

section[data-testid="stSidebar"] {
    background-color: var(--bg-sidebar);
}

section[data-testid="stSidebar"] * {
    color: var(--text-sidebar);
}

h1, h2, h3, h4, h5, h6 {
    color: var(--text-main);
}

p {
    color: var(--text-muted);
}

.main-header {
    font-size: 2.6rem;
    font-weight: 800;
    margin-bottom: 0.25rem;
}

.sub-header {
    font-size: 1.05rem;
    color: #9aa0a6;
    margin-bottom: 1.75rem;
}

.card {
    background-color: var(--bg-card);
    padding: 20px;
    margin-bottom: 20px;
    border-radius: 12px;
}

div[data-testid="stRadio"] label {
    font-weight: 500;
}

div[role="radiogroup"] label[data-baseweb="radio"] > div:first-child {
    border-color: var(--brand-blue) !important;
}

div[role="radiogroup"] label[data-baseweb="radio"][aria-checked="true"] span {
    color: var(--brand-blue) !important;
}

.stSidebar label[data-baseweb="radio"][aria-checked="true"] {
    background-color: var(--brand-blue-soft);
}

div.stButton > button,
section[data-testid="stSidebar"] div.stButton > button {
    background-color: var(--brand-green) !important;
    color: white !important;
    border-radius: 10px !important;
    border: none !important;
    padding: 14px 18px !important;
    font-weight: 700 !important;
    font-size: 22px !important;
    width: 100% !important;
    min-height: 56px !important;
}

div.stButton > button:hover,
section[data-testid="stSidebar"] div.stButton > button:hover {
    background-color: var(--brand-green-hover) !important;
    color: white !important;
}

div[data-baseweb="select"] > div,
input,
textarea {
    background-color: var(--bg-card) !important;
    color: white !important;
    border: 1px solid var(--brand-green) !important;
    border-radius: 8px !important;
}

.stAlert {
    background-color: var(--info-bg);
    border: 1px solid var(--brand-blue);
    border-radius: 8px;
}

.stAlert p,
.stAlert div {
    font-size: 18px !important;
    font-weight: 500;
    line-height: 1.5;
}

.sidebar-section-label {
    font-size: 0.8rem;
    font-weight: 800;
    text-transform: uppercase;
    letter-spacing: 0.04em;
    color: var(--text-sidebar);
    opacity: 0.9;
    margin-top: 0.2rem;
    margin-bottom: 0.5rem;
}

.sidebar-summary-card {
    background: rgba(91, 147, 164, 0.14);
    border: 1px solid rgba(91, 147, 164, 0.35);
    border-radius: 12px;
    padding: 0.85rem 0.9rem;
    margin: 0.35rem 0 0.8rem 0;
}

.sidebar-summary-kicker {
    font-size: 0.72rem;
    text-transform: uppercase;
    letter-spacing: 0.05em;
    opacity: 0.8;
    margin-bottom: 0.35rem;
}

.sidebar-summary-main {
    font-size: 0.95rem;
    font-weight: 700;
    line-height: 1.4;
    color: white;
}

.sidebar-helper {
    font-size: 0.84rem;
    color: var(--text-sidebar);
    opacity: 0.88;
    margin-top: -0.15rem;
    margin-bottom: 0.45rem;
}

</style>
"""

SPINNER_HTML = """
<div style="display:flex; align-items:center; gap:10px;">
  <div class="loader"></div>
  <span style="font-size: 1.5rem; font-weight:600;">Research in Progress</span>
</div>

<style>
.loader {
  border: 4px solid rgba(255,255,255,0.1);
  border-top: 4px solid #5B93A4;
  border-radius: 50%;
  width: 18px;
  height: 18px;
  animation: spin 1s linear infinite;
}

@keyframes spin {
  0% { transform: rotate(0deg); }
  100% { transform: rotate(360deg); }
}
</style>
"""

st.markdown(APP_CSS, unsafe_allow_html=True)


# External imports

try:
    from cache_manager import (
        clear_old_cache_entries,
        get_all_cached_items,
        load_from_cache,
        save_to_cache,
    )
    from compile_to_csv_enhanced import compile_json_to_csv
    from config_manager import (
        add_research_config,
        delete_research_config,
        get_config_by_name,
        get_config_names,
        load_research_configs,
        update_research_config,
    )
    from deepcomp_enhanced import COMPETITORS, DeepCompScraper
except ImportError as exc:
    st.error(f"⚠️ Missing required files: {exc}")
    st.stop()


# Session state

DEFAULT_SESSION_STATE = {
    "research_complete": False,
    "current_output_folder": None,
    "research_running": False,
    "loading_cache": None,
    "loading_competitor": None,
    "loading_focus": None,
}


def init_session_state() -> None:
    for key, value in DEFAULT_SESSION_STATE.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session_state()



# Helpers

RESEARCH_GOALS = [
    "Explore Competitor",
    "Compare multiple competitors",
    "Compare with SimplePractice"
]



def check_api_key() -> bool:
    """Check if Firecrawl API key is configured."""
    try:
        if "FIRECRAWL_API_KEY" in st.secrets:
            os.environ["FIRECRAWL_API_KEY"] = st.secrets["FIRECRAWL_API_KEY"]
            return True
    except Exception:
        pass

    return bool(os.getenv("FIRECRAWL_API_KEY"))


def show_api_key_error() -> None:
    st.error("⚠️ **Firecrawl API Key Required**")
    st.info(
        """
Please configure your Firecrawl API key:

**For local development:**
1. Create a `.env` file in the same directory as this app
2. Add: `FIRECRAWL_API_KEY=your_api_key_here`

**For Streamlit Cloud deployment:**
1. Go to your app settings on Streamlit Cloud
2. Add a secret named `FIRECRAWL_API_KEY` with your API key value
"""
    )
    st.stop()


def get_cache_key(competitor_name: str, research_focus_id: str) -> str:
    slug = competitor_name.lower().replace(" ", "_")
    return f"{slug}_{research_focus_id}"

def make_output_folder_name(competitor_name: str, focus_name: str) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_competitor = competitor_name.lower().replace(" ", "_")
    safe_focus = focus_name.lower().replace(" ", "_")
    return f"{safe_competitor}_{safe_focus}_{timestamp}"

def make_multi_output_folder_name(competitors: list[str], focus_name: str) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_focus = focus_name.lower().replace(" ", "_")
    joined_names = "_vs_".join(name.lower().replace(" ", "_") for name in competitors[:3])
    return f"{joined_names}_{safe_focus}_{timestamp}"

def make_comparison_output_folder_name(competitors: list[str], focus_name: str) -> str:
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    safe_focus = focus_name.lower().replace(" ", "_")
    joined_names = "_vs_".join(name.lower().replace(" ", "_") for name in competitors[:2])
    return f"sp_vs_{joined_names}_{safe_focus}_{timestamp}"

def build_scraper(
    *,
    competitor_name: str | None,
    compare_targets: list[str] | None,
    groups_focus: bool,
    custom_prompt: str | None,
    focus_name: str,
    output_folder_name: str | None = None,
) -> DeepCompScraper:
    return DeepCompScraper(
        target_competitor=competitor_name,
        compare_targets=compare_targets,
        groups_focus=groups_focus,
        custom_prompt=custom_prompt,
        focus_name=focus_name,
        output_folder_name=output_folder_name,
    )


def reset_loading_state() -> None:
    st.session_state.loading_cache = None
    st.session_state.loading_competitor = None
    st.session_state.loading_focus = None


def set_research_complete(output_folder_name: str) -> None:
    st.session_state.research_complete = True
    st.session_state.current_output_folder = output_folder_name
    st.session_state.research_running = False


def reset_research_state() -> None:
    st.session_state.research_complete = False
    st.session_state.current_output_folder = None
    st.session_state.research_running = False
    reset_loading_state()


def read_text_file(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def render_home() -> None:
    st.markdown(
        '<div class="main-header">Competitive Research Tool</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<div class="sub-header">Research competitors, compare offerings, and generate reusable insights.</div>',
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2)

    with col1:
        st.markdown(
            """
            <div class="card">
                <h5>Deep dive on a competitor</h5>
                <p>Get a detailed breakdown of a single competitor’s features, pricing, and positioning.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="card">
                <h5>Compare with SimplePractice</h5>
                <p>See how a competitor stacks up against SimplePractice across key capabilities.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with col2:
        st.markdown(
            """
            <div class="card">
                <h5>Compare multiple competitors</h5>
                <p>Analyze patterns across competitors to understand the market and identify gaps.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )
        st.markdown(
            """
            <div class="card">
                <h5>Reuse previous analyses</h5>
                <p>Reopen past research without running a new scrape.</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.info("Start in the sidebar: choose a goal, select a focus area, and pick a competitor.")

    with st.expander("📋 View Available Competitors"):
        competitors_df = pd.DataFrame(
            [
                {"Competitor": name, "Website": url}
                for name, url in sorted(COMPETITORS.items())
            ]
        )
        st.dataframe(competitors_df, use_container_width=True, hide_index=True)


def render_focus_area_manager(config_names: list[str]) -> None:
    with st.expander("🔧 Create Research Lens", expanded=False):
        st.caption("Add, edit, or delete research focus areas")

        management_tab = st.radio(
            "Action",
            ["Add New", "Edit Existing", "Delete Custom"],
            horizontal=True,
            label_visibility="collapsed",
        )

        if management_tab == "Add New":
            render_add_focus_area_form()
        elif management_tab == "Edit Existing":
            render_edit_focus_area_form(config_names)
        else:
            render_delete_focus_area_form()


def render_add_focus_area_form() -> None:
    st.subheader("Add New Focus Area")
    st.info("💡 Tip: The placeholders `{competitor_name}` and `{competitor_url}` are optional but recommended.")

    default_template = """Analyze {competitor_name} ({competitor_url}) for [YOUR FOCUS AREA].

WHAT TO EXTRACT:
- [List specific things to look for]
- [Be detailed about what you want]
- [Include any specific categories]

INSTRUCTIONS:
- Prioritize product documentation and pricing pages
- Mark inferences with "likely" or "appears to"
- If information isn't found, state "Not publicly disclosed"
"""

    with st.form("add_config_form"):
        new_name = st.text_input("Focus Area Name", placeholder="e.g., Pricing & Billing Analysis")
        new_desc = st.text_area(
            "Description",
            placeholder="Brief description of what this focus analyzes",
            height=60,
        )
        new_prompt = st.text_area(
            "Prompt Template",
            value=default_template,
            height=300,
            help="Placeholders like {competitor_name} and {competitor_url} are automatically replaced when research runs.",
        )

        submitted = st.form_submit_button("Add Focus Area")
        if submitted:
            if not new_name or not new_prompt:
                st.error("Name and Prompt Template are required")
            else:
                success = add_research_config(new_name, new_desc, new_prompt)
                if success:
                    st.success(f"✅ Added '{new_name}' successfully!")
                    st.rerun()
                st.error("❌ A focus area with this name already exists")


def render_edit_focus_area_form(config_names: list[str]) -> None:
    st.subheader("✏️ Edit Focus Area")

    edit_config_name = st.selectbox("Select Focus Area to Edit", config_names)
    edit_config = get_config_by_name(edit_config_name)

    if not edit_config:
        return

    if edit_config.get("is_builtin", False):
        st.info("ℹ️ Built-in focus areas can be edited, but may reset if the app is updated")

    with st.form("edit_config_form"):
        edit_name = st.text_input("Focus Area Name", value=edit_config["name"])
        edit_desc = st.text_area("Description", value=edit_config.get("description", ""), height=60)
        edit_prompt = st.text_area(
            "Prompt Template",
            value=edit_config["prompt_template"],
            height=300,
        )

        submitted = st.form_submit_button("Save Changes")
        if submitted:
            success = update_research_config(
                edit_config["id"],
                edit_name,
                edit_desc,
                edit_prompt,
            )
            if success:
                st.success(f"✅ Updated '{edit_name}' successfully!")
                st.rerun()
            st.error("❌ Failed to update")


def render_delete_focus_area_form() -> None:
    st.subheader("🗑️ Delete Custom Focus Area")

    all_configs = load_research_configs()
    custom_configs = {k: v for k, v in all_configs.items() if not v.get("is_builtin", False)}

    if not custom_configs:
        st.info("No custom focus areas to delete.")
        return

    custom_names = [config["name"] for config in custom_configs.values()]
    delete_config_name = st.selectbox("Select Focus Area to Delete", custom_names)
    delete_config = get_config_by_name(delete_config_name)

    if not delete_config:
        return

    st.warning(f"⚠️ Are you sure you want to delete '{delete_config_name}'?")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🗑️ Yes, Delete", type="primary"):
            success = delete_research_config(delete_config["id"])
            if success:
                st.success(f"✅ Deleted '{delete_config_name}'")
                st.rerun()
            st.error("❌ Failed to delete")

    with col2:
        if st.button("Cancel"):
            st.info("Cancelled")


def render_cache_section() -> None:
    cached_items = get_all_cached_items()
    valid_cache = {key: value for key, value in cached_items.items() if value["valid"]}

    if not valid_cache:
        st.caption("No saved analyses yet.")
        return

    st.caption(f"{len(valid_cache)} saved dataset(s) available")

    for cache_key, info in valid_cache.items():
        col1, col2 = st.columns([3, 1])

        with col1:
            button_label = f"📊 {info['competitor']} — {info['focus']}"
            if st.button(button_label, key=f"load_{cache_key}"):
                st.session_state.loading_cache = cache_key
                st.session_state.loading_competitor = info["competitor"]
                st.session_state.loading_focus = info["focus"]
                st.rerun()

        with col2:
            st.caption(f"_{info['age']}_")

    with st.expander("🧹 Cache Maintenance"):
        if st.button("Clear Expired Cache"):
            removed = clear_old_cache_entries()
            if removed > 0:
                suffix = "y" if removed == 1 else "ies"
                st.success(f"Removed {removed} expired cache entr{suffix}")
                st.rerun()
            else:
                st.info("No expired cache to clear")


def render_sidebar() -> dict[str, Any]:
    with st.sidebar:
        st.header("Run Research")
        st.caption("Choose a goal, pick a lens, then select who to analyze.")

        config_names = get_config_names()

        st.markdown('<div class="sidebar-section-label">Research setup</div>', unsafe_allow_html=True)
        research_goal = st.radio(
            "Goal",
            RESEARCH_GOALS,
            label_visibility="collapsed",
        )

        research_mode = st.selectbox(
            "Focus area",
            options=config_names,
            help="Choose what aspect of competitors to analyze",
        )

        selected_config = get_config_by_name(research_mode)
        if selected_config and selected_config.get("description"):
            st.markdown(
                f'<div class="sidebar-helper">ℹ️ {selected_config["description"]}</div>',
                unsafe_allow_html=True,
            )

        st.markdown('<div class="sidebar-section-label">Competitors</div>', unsafe_allow_html=True)

        competitors_to_research: list[str]
        selected_competitor: str | None = None
        comparison_mode = False

        if research_goal == "Explore Competitor":
            selected_competitor = st.selectbox(
                "Competitor",
                options=sorted(COMPETITORS.keys()),
                help="Choose one competitor to research",
            )
            competitors_to_research = [selected_competitor]

        elif research_goal == "Compare multiple competitors":
            competitors_to_research = st.multiselect(
                "Competitors",
                options=sorted(COMPETITORS.keys()),
                default=[],
                placeholder="Select competitors",
                help="Choose multiple competitors to analyze",
            )
        else:
            competitors_to_research = st.multiselect(
                "Competitors to compare",
                options=[c for c in sorted(COMPETITORS.keys()) if c != "SimplePractice"],
                max_selections=1,
                placeholder="Select 1 competitor",
                help="Select 1 competitor for detailed comparison to SimplePractice",
            )
            comparison_mode = True

        if research_goal == "Explore Competitor" and selected_competitor:
            summary_main = f"{research_mode}<br>{selected_competitor}"
        else:
            noun = "competitor" if len(competitors_to_research) == 1 else "competitors"
            summary_main = f"{research_mode}<br>{len(competitors_to_research)} {noun} selected"

        st.markdown(
            f"""
            <div class="sidebar-summary-card">
                <div class="sidebar-summary-kicker">{research_goal}</div>
                <div class="sidebar-summary-main">{summary_main}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

        run_clicked = st.button(
            "Running analysis..." if st.session_state.research_running else "Run analysis",
            type="primary",
            disabled=st.session_state.research_running,
            use_container_width=True,
        )

        if run_clicked:
            if not competitors_to_research:
                error_text = (
                    "Please select at least one competitor for comparison"
                    if comparison_mode
                    else "Please select at least one competitor"
                )
                st.error(error_text)
            else:
                st.session_state.research_running = True
                st.rerun()

        if st.session_state.research_running:
            st.info("Analysis in progress...")

        st.divider()

        with st.expander("Advanced options", expanded=False):
            force_refresh = st.checkbox(
                "Bypass cache when running research",
                value=False,
                help="Always fetch fresh data instead of using cached results",
            )

            st.markdown("")
            render_focus_area_manager(config_names)

        st.divider()

        with st.expander("Recent analyses", expanded=False):
            render_cache_section()

    return {
        "research_goal": research_goal,
        "research_mode": research_mode,
        "selected_config": selected_config,
        "competitors_to_research": competitors_to_research,
        "force_refresh": force_refresh,
    }

def load_cached_output() -> None:
    st.header("📦 Loading Cached Data")

    progress_bar = st.progress(0)
    status_text = st.empty()

    try:
        cache_key = st.session_state.loading_cache
        competitor_name = st.session_state.loading_competitor
        focus_name = st.session_state.loading_focus

        status_text.text(f"Loading {competitor_name} - {focus_name}...")
        progress_bar.progress(30)

        target_folder_name = f"cached_restore_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}"

        progress_bar.progress(50)
        status_text.text("Restoring cached output...")

        success = load_from_cache(cache_key, target_folder_name)
        if not success:
            st.error("Failed to load cached data")
            reset_loading_state()
            return

        progress_bar.progress(100)
        status_text.text("✅ Loaded!")

        cached_items = get_all_cached_items()
        cache_info = cached_items.get(cache_key, {})

        st.success(f"📦 **Loaded cached data for {competitor_name}**")
        st.info(f"**Last updated:** {cache_info.get('age', 'Unknown')}")

        st.session_state.research_complete = True
        st.session_state.current_output_folder = target_folder_name

        reset_loading_state()
        st.rerun()

    except Exception as exc:
        st.error(f"Failed to load cached data: {exc}")
        reset_loading_state()


def run_research(
    *,
    research_goal: str,
    research_mode: str,
    selected_config: dict[str, Any] | None,
    competitors_to_research: list[str],
    force_refresh: bool,
) -> None:
    st.markdown(SPINNER_HTML, unsafe_allow_html=True)

    progress_bar = st.progress(0)
    status_text = st.empty()

    try:
        custom_prompt = selected_config["prompt_template"] if selected_config else None
        groups_focus = research_mode == "Groups & Service Offerings"

        if research_goal == "Compare with SimplePractice":
            run_head_to_head(
                competitors_to_research=competitors_to_research,
                research_mode=research_mode,
                custom_prompt=custom_prompt,
                groups_focus=groups_focus,
                progress_bar=progress_bar,
                status_text=status_text,
            )
            return

        if research_goal == "Explore Competitor":
            run_single_competitor(
                competitor_name=competitors_to_research[0],
                research_mode=research_mode,
                selected_config=selected_config,
                custom_prompt=custom_prompt,
                groups_focus=groups_focus,
                force_refresh=force_refresh,
                progress_bar=progress_bar,
                status_text=status_text,
            )
            return

        run_multi_competitor(
            competitors_to_research=competitors_to_research,
            research_mode=research_mode,
            custom_prompt=custom_prompt,
            groups_focus=groups_focus,
            progress_bar=progress_bar,
            status_text=status_text,
        )

    except Exception as exc:
        st.error(f"❌ Error during research: {exc}")
        st.session_state.research_running = False
        st.stop()


def run_head_to_head(
    *,
    competitors_to_research: list[str],
    research_mode: str,
    custom_prompt: str | None,
    groups_focus: bool,
    progress_bar,
    status_text,
) -> None:
    status_text.text(f"Running detailed comparison with {len(competitors_to_research)} competitor(s)...")
    progress_bar.progress(10)

    output_folder_name = make_comparison_output_folder_name(
        competitors_to_research,
        research_mode,
    )

    scraper = build_scraper(
        competitor_name=None,
        compare_targets=competitors_to_research,
        groups_focus=groups_focus,
        custom_prompt=custom_prompt,
        focus_name=research_mode,
        output_folder_name=output_folder_name,
    )

    progress_bar.progress(30)
    status_text.text("Scraping competitor data with Firecrawl...")
    asyncio.run(scraper.run())

    progress_bar.progress(70)
    status_text.text("Compiling results to CSV...")
    compile_json_to_csv(
        output_folder_name=output_folder_name,
        focus_name=research_mode,
        selected_competitors=competitors_to_research,
    )

    progress_bar.progress(100)
    status_text.text("✅ Research complete!")

    set_research_complete(output_folder_name)
    st.success("Research completed successfully! View results below.")
    st.rerun()


def run_single_competitor(
    *,
    competitor_name: str,
    research_mode: str,
    selected_config: dict[str, Any] | None,
    custom_prompt: str | None,
    groups_focus: bool,
    force_refresh: bool,
    progress_bar,
    status_text,
) -> None:
    research_focus_id = selected_config["id"] if selected_config else "unknown"

    status_text.text(f"Researching {competitor_name}...")
    progress_bar.progress(10)

    output_folder_name = make_output_folder_name(competitor_name, research_mode)

    scraper = build_scraper(
        competitor_name=competitor_name,
        compare_targets=None,
        groups_focus=groups_focus,
        custom_prompt=custom_prompt,
        focus_name=research_mode,
        output_folder_name=output_folder_name,
    )

    progress_bar.progress(30)
    status_text.text("Scraping competitor data with Firecrawl...")
    asyncio.run(scraper.run())

    progress_bar.progress(70)
    status_text.text("Compiling results to CSV...")
    compile_json_to_csv(
        output_folder_name=output_folder_name,
        focus_name=research_mode,
        selected_competitors=[competitor_name],
    )

    if not force_refresh:
        status_text.text("Saving to cache...")
        saved = save_to_cache(
            competitor_name,
            research_focus_id,
            output_folder_name,
            focus_name=research_mode,
        )
        if not saved:
            st.warning("Research completed, but cache save failed.")

    progress_bar.progress(100)
    status_text.text("✅ Research complete!")

    set_research_complete(output_folder_name)
    st.success("Research completed successfully! View results below.")

    if not force_refresh:
        st.info("💾 Data saved to cache for future use")

    st.rerun()

def run_multi_competitor(
    *,
    competitors_to_research: list[str],
    research_mode: str,
    custom_prompt: str | None,
    groups_focus: bool,
    progress_bar,
    status_text,
) -> None:
    if not competitors_to_research:
        st.error("Please select at least one competitor.")
        st.session_state.research_running = False
        st.stop()

    status_text.text(f"Researching {len(competitors_to_research)} competitor(s)...")
    progress_bar.progress(10)

    output_folder_name = make_multi_output_folder_name(
        competitors_to_research,
        research_mode,
    )

    for idx, competitor_name in enumerate(competitors_to_research, start=1):
        status_text.text(f"Researching {competitor_name} ({idx}/{len(competitors_to_research)})...")

        scraper = build_scraper(
            competitor_name=competitor_name,
            compare_targets=None,
            groups_focus=groups_focus,
            custom_prompt=custom_prompt,
            focus_name=research_mode,
            output_folder_name=output_folder_name,
        )
        asyncio.run(scraper.run())

        progress = 10 + int((idx / len(competitors_to_research)) * 60)
        progress_bar.progress(progress)

    status_text.text("Compiling results to CSV...")
    compile_json_to_csv(
        output_folder_name=output_folder_name,
        focus_name=research_mode,
        selected_competitors=competitors_to_research,
)

    progress_bar.progress(100)
    status_text.text("✅ Research complete!")

    set_research_complete(output_folder_name)
    st.success("Research completed successfully! View results below.")
    st.rerun()


def render_results(research_goal: str) -> None:
    st.header("Research Results")

    output_dir = Path("outputs") / st.session_state.current_output_folder
    if not output_dir.exists():
        st.warning("Output directory not found. The app state was updated, but the scraper/CSV pipeline may still be writing to a different folder.")
        st.stop()

    tab1, tab2, tab3 = st.tabs(["📄 Summary Reports", "📊 Data Tables", "💾 Download Files"])

    with tab1:
        render_summary_reports(output_dir, research_goal)

    with tab2:
        render_data_tables(output_dir)

    with tab3:
        render_downloads(output_dir)


def render_summary_reports(output_dir: Path, research_goal: str) -> None:
    st.subheader("Summary Reports")

    report_files = list(output_dir.glob("*.txt")) + list(output_dir.glob("*.md"))
    comparison_json_files = list(output_dir.glob("comparisons/*.json"))

    if research_goal == "Compare with SimplePractice":
        st.caption("View the comparison summary and underlying comparison files")

        comparison_summary_path = output_dir / "comparison_summary.txt"
        if comparison_summary_path.exists():
            comparison_summary = read_text_file(comparison_summary_path)

            st.markdown("### SimplePractice Comparison Summary")
            st.text_area(
                "Comparison Summary",
                value=comparison_summary,
                height=500,
                label_visibility="collapsed",
            )

            st.download_button(
                label="⬇️ Download Comparison Summary",
                data=comparison_summary,
                file_name="comparison_summary.txt",
                mime="text/plain",
            )
        else:
            st.info("No comparison summary found.")

        if comparison_json_files:
            st.markdown("### 📁 Comparison JSON Files")
            selected_json = st.selectbox(
                "Select comparison file",
                options=[f.name for f in comparison_json_files],
            )

            if selected_json:
                json_path = output_dir / "comparisons" / selected_json
                json_content = json.loads(read_text_file(json_path))
                st.json(json_content)

                st.download_button(
                    label="⬇️ Download Comparison JSON",
                    data=json.dumps(json_content, indent=2),
                    file_name=selected_json,
                    mime="application/json",
                )
        else:
            st.info("No comparison JSON files found.")
        return

    if not report_files:
        st.info("No summary reports found.")
        return

    st.caption("Switch between a single competitor deep dive or a market-wide summary")

    md_reports = [report for report in report_files if report.suffix == ".md"]
    txt_reports = [report for report in report_files if report.suffix == ".txt"]
    preferred_reports = md_reports if md_reports else txt_reports

    selected_report = st.selectbox(
        "Select Report",
        options=[report.name for report in preferred_reports],
    )

    if not selected_report:
        st.info("No summary reports found.")
        return

    report_path = output_dir / selected_report
    report_content = read_text_file(report_path)

    if selected_report.endswith(".md"):
        st.markdown(report_content)
    else:
        st.text_area(
            "Report Content",
            value=report_content,
            height=500,
            label_visibility="collapsed",
        )

    st.download_button(
        label="⬇️ Download Report",
        data=report_content,
        file_name=selected_report,
        mime="text/markdown" if selected_report.endswith(".md") else "text/plain",
    )


def render_data_tables(output_dir: Path) -> None:
    st.subheader("Data Tables")

    csv_files = list(output_dir.glob("*.csv"))
    if not csv_files:
        st.info("No data tables found.")
        return

    selected_csv = st.selectbox(
        "Select Data Table",
        options=[csv.name for csv in csv_files],
        format_func=lambda name: name.replace("_", " ").replace(".csv", "").title(),
    )

    if not selected_csv:
        return

    csv_path = output_dir / selected_csv

    try:
        df = pd.read_csv(csv_path)

        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Rows", len(df))
        with col2:
            st.metric("Total Columns", len(df.columns))
        with col3:
            if "competitor" in df.columns:
                st.metric("Competitors", df["competitor"].nunique())

        st.dataframe(df, use_container_width=True, height=400)

        csv_data = df.to_csv(index=False).encode("utf-8")
        st.download_button(
            label="⬇️ Download CSV",
            data=csv_data,
            file_name=selected_csv,
            mime="text/csv",
        )
    except Exception as exc:
        st.error(f"Error loading CSV: {exc}")


def render_downloads(output_dir: Path) -> None:
    st.subheader("Download All Files")
    st.info(f"All research outputs are located in: `{output_dir}`")

    all_files = [path for path in output_dir.rglob("*") if path.is_file()]
    file_list = [str(file.relative_to(output_dir)) for file in all_files]

    if file_list:
        st.write(f"**{len(file_list)} files generated:**")
        for file in sorted(file_list):
            st.text(f"📄 {file}")

    st.divider()

    if st.button("Start New Research"):
        reset_research_state()
        st.rerun()


# App

if not check_api_key():
    show_api_key_error()

sidebar_state = render_sidebar()

if st.session_state.loading_cache:
    load_cached_output()
elif st.session_state.research_running:
    run_research(
        research_goal=sidebar_state["research_goal"],
        research_mode=sidebar_state["research_mode"],
        selected_config=sidebar_state["selected_config"],
        competitors_to_research=sidebar_state["competitors_to_research"],
        force_refresh=sidebar_state["force_refresh"],
    )
elif st.session_state.research_complete and st.session_state.current_output_folder:
    render_results(sidebar_state["research_goal"])
else:
    render_home()

st.divider()
st.caption("Built with Streamlit • Powered by Firecrawl")
