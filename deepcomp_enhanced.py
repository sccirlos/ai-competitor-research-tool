import os
import json
import asyncio
import argparse
from datetime import datetime
from typing import List, Dict, Any, Optional
from dotenv import load_dotenv
from firecrawl import FirecrawlApp
from pydantic import BaseModel, Field

load_dotenv()

# Configuration
COMPETITORS = {
    "SimplePractice": "https://www.simplepractice.com/",
    "Jane": "https://www.janeapp.com",
    "TherapyNotes": "https://www.therapynotes.com/",
    "Ensora": "https://ensorahealth.com/product/theranest-mental-health/",
    "Healthie": "https://www.gethealthie.com/",
    "Blueprint": "https://www.blueprint.ai/",
    "Mentalyc": "https://www.mentalyc.com/",
    "YungSidekick": "https://yung-sidekick.com/",
    "Upheal": "https://www.upheal.io/",
    "Freed": "https://www.getfreed.ai/",
    "Headway": "https://headway.co",
    "Berries": "https://heyberries.com/",
    "Quill": "https://quilltherapysolutions.com/",
    "PracticeFusion": "https://https://www.practicefusion.com/",
    "Tebra": "https://https://www.tebra.com/",
    "OfficeAlly": "https://https://cms.officeally.com/",
}

# Care Aide definition — reflects current SimplePractice AI capabilities
CARE_AIDE_DESCRIPTION = """
Care Aide is SimplePractice's AI-powered clinical assistant, powered by Claude (Anthropic).
All features are HIPAA-compliant; PHI never leaves SimplePractice infrastructure.
All outputs require clinician review and approval before finalizing (human-in-the-loop).
Note Taker is a $35/month per-clinician add-on, available on Starter, Essential, and Plus plans.
Care Aide (broader suite) is not yet priced; will be available on Starter, Essential, and Plus plans.

CURRENT CAPABILITIES (live in production):

1. Note Taker — Telehealth
   Real-time transcription of virtual telehealth sessions → AI-generated draft progress note.
   Audio deleted after transcription; transcripts retained 7 days or until note is signed.

2. Note Taker — Dictation
   Clinician records audio post-session (mobile or web) → AI-generated draft progress note.
   Same data handling as Telehealth mode.

3. Note Taker — Audio Upload
   Clinician uploads a pre-recorded audio file → AI-generated draft progress note.
   Uploaded audio deleted after processing.

4. Note Taker — Text Upload
   Clinician uploads a text file → AI-generated draft progress note.
   Uploaded file deleted after processing; draft retained 7 days or until note is signed.

5. Note Taker — Refinements
   Clinician provides custom instructions to iteratively refine an existing Note Taker draft.
   Allows targeted edits and style adjustments before finalizing.

6. Pre-Appointment Summaries (live)
   AI synthesizes chart notes, admin notes, and prior progress notes into a concise pre-session
   brief. Fully automated with human review; helps clinicians prepare without manually scanning records.

IN DEVELOPMENT (not yet publicly announced, planned April 2026 unless noted):

7. Create Treatment Plan (beta, April 2026)
   AI uses EHR data — progress notes and scored measures — to generate a new treatment plan draft.

8. Edit Treatment Plan (April 2026)
   AI makes targeted modifications to an existing treatment plan using EHR data.

9. Post-Session Summary (April 2026)
   AI generates client-friendly summaries from session transcripts; clinicians can share key
   takeaways and homework directly to the Client Portal.

10. Session Sidekick — Reminders (in development, no release date)
    AI surfaces a checklist of key themes, homework, and upcoming appointments in the telehealth
    sidebar, helping clinicians stay focused during sessions without switching tabs.

11. Session Sidekick — Client Chart Search (in development, no release date)
    Clinicians can prompt the LLM to search past progress notes and return relevant snippets
    directly within the in-session sidebar, maintaining engagement without leaving the call.

12. Session Sidekick — In-Session Suggestions (in development, no release date)
    Clinicians can prompt the LLM for insightful suggestions sourced from trusted resources
    (e.g., SimplePractice blog) while remaining in session.

13. Session Sidekick — Replay, Recap & Session Prep (in development, no release date)
    Quick actions in the telehealth sidebar: pull up last note, session prep summary, live
    transcript replay, or a running session recap without leaving the call.

ON ROADMAP (discovery only — not yet in development):

14. CPT Code Suggestions
    AI analyzes clinical documentation to suggest appropriate billing codes with confidence
    scores and rationale to reduce denials and capture missed revenue.

15. Diagnosis Code Suggestions
    AI synthesizes scored measures, notes, and patient history to suggest DSM-5/ICD-10
    diagnoses during treatment plan creation, improving specificity and capturing comorbidities.

TECHNICAL CONSTRAINTS:
- Underlying model: Claude by Anthropic (publicly disclosed by SimplePractice)
- No API access to AI outputs (Enterprise API covers scheduling only)
- No disclosed accuracy rates, error metrics, or clinical validation studies
- No usage caps; Note Taker is unlimited for the flat $35/mo add-on fee
- Multi-device: desktop, tablet, iOS, Android
- Language support: Multiple languages supported

Care Aide does NOT currently offer:
- ICD-10 / CPT auto-coding or billing code suggestions (on roadmap, not yet built)
- Risk flagging, crisis detection, or suicide risk assessment
- Predictive analytics or treatment outcome modeling
- Diagnostic support or differential diagnosis (on roadmap, not yet built)
- Ambient listening without explicit session recording / consent flow
- API access for AI-generated outputs
- Real-time in-person session transcription (dictation and upload modes only for in-person)
"""


# ---------------------------------------------------------------------------
# Pydantic Models
# ---------------------------------------------------------------------------

class PricingTier(BaseModel):
    tier_name: str
    price: str
    billing_cycle: Optional[str] = None
    key_features: List[str] = Field(default_factory=list)


class Feature(BaseModel):
    feature_name: str
    category: Optional[str] = None
    description: Optional[str] = None
    is_gated: bool = False
    available_in_tiers: List[str] = Field(default_factory=list)


class AIFeature(BaseModel):
    feature_name: str
    underlying_technology: Optional[str] = None
    description: str
    automation_level: Optional[str] = None
    data_privacy_notes: Optional[str] = None
    is_gated: bool = False
    available_in_tiers: List[str] = Field(default_factory=list)


class BrandedSolution(BaseModel):
    """A named, marketed AI product or bundle offered by a competitor (e.g., 'Alliance Genie', 'TherapyFuel')."""
    solution_name: str
    thematic_description: str  # Plain-English summary of what the bundle does / its positioning
    core_capabilities: List[str] = Field(default_factory=list)  # Functional capability list
    target_user: Optional[str] = None  # e.g., "solo therapist", "group practice", "psychiatric prescribers"
    ai_powered: bool = False
    pricing_model: Optional[str] = None  # included / add-on / standalone / not disclosed
    url_or_source: Optional[str] = None


class GroupsOffering(BaseModel):
    """Groups-specific product features and capabilities."""
    feature_name: str
    description: str
    included_in_base_plan: bool = False
    available_in_tiers: List[str] = Field(default_factory=list)
    groups_capacity_limits: Optional[str] = None  # e.g., "unlimited groups", "max 50 groups"
    pricing_model: Optional[str] = None  # per clinician, per group, flat fee, etc.
    customer_benefit: Optional[str] = None
    comparison_to_simplepractice: Optional[str] = None


class ServiceOffering(BaseModel):
    """Service and support capabilities."""
    category: str  # "Data Transfer/Switching", "Onboarding", "Customer Success"
    offering_name: str
    description: str
    is_dedicated_resource: bool = False  # e.g., dedicated CS agent
    number_of_sessions: Optional[str] = None  # e.g., "Multiple onboarding meetings"
    availability: Optional[str] = None  # e.g., "24/7", "business hours", "self-service only"
    pricing: Optional[str] = None  # included / premium tier / additional cost
    publicly_documented: bool = False  # Can info be found without being a prospect?


class MarketIntelligence(BaseModel):
    """Market presence and recent developments."""
    market_scope: Optional[str] = None  # "national", "regional", "international"
    target_market_segments: List[str] = Field(default_factory=list)  # e.g., ["group practices", "solo clinicians"]
    recent_news: List[str] = Field(default_factory=list)  # acquisitions, funding, downtime, pricing changes
    known_challenges: List[str] = Field(default_factory=list)  # documented issues or concerns
    market_positioning: Optional[str] = None  # how they position themselves vs competitors


class InsuranceOffering(BaseModel):
    """Insurance and billing capabilities."""
    offering_name: str
    description: str
    supported_payers: Optional[str] = None  # "all major payers", "limited network", etc.
    claim_submission: Optional[str] = None  # "automated", "manual", "both"
    era_support: bool = False  # Electronic Remittance Advice
    eligibility_verification: bool = False
    available_in_tiers: List[str] = Field(default_factory=list)
    pricing_model: Optional[str] = None


class CompetitorData(BaseModel):
    pricing_tiers: List[PricingTier] = Field(default_factory=list)
    ai_features: List[AIFeature] = Field(default_factory=list)
    all_features: List[Feature] = Field(default_factory=list)
    branded_solutions: List[BrandedSolution] = Field(default_factory=list)
    groups_offerings: List[GroupsOffering] = Field(default_factory=list)
    service_offerings: List[ServiceOffering] = Field(default_factory=list)
    insurance_offerings: List[InsuranceOffering] = Field(default_factory=list)
    market_intelligence: Optional[MarketIntelligence] = None
    technical_constraints: List[str] = Field(default_factory=list)
    additional_costs: List[str] = Field(default_factory=list)
    ai_maturity_summary: Optional[str] = None


# ---------------------------------------------------------------------------
# Comparison / Gap Models
# ---------------------------------------------------------------------------

class ComparisonFeature(BaseModel):
    feature_name: str
    simple_practice_offering: str
    competitor_offering: str
    comparison_notes: str


class CareAideCapabilityComparison(BaseModel):
    """Row-level comparison of a single capability between Care Aide and a competitor solution."""
    capability_area: str          # e.g., "Clinical Note Generation", "Session Transcription"
    care_aide_status: str         # "present" | "partial" | "absent"
    care_aide_description: str    # What Care Aide does (or doesn't do) for this capability
    competitor_branded_name: Optional[str] = None   # e.g., "TherapyFuel" if they have one
    competitor_status: str        # "present" | "partial" | "absent"
    competitor_description: str   # What the competitor does
    gap_direction: str            # "Care Aide leads" | "Competitor leads" | "Parity" | "Both absent"
    gap_severity: str             # "critical" | "moderate" | "minor" | "none"
    gap_notes: Optional[str] = None  # Actionable context or caveats


class ComparisonData(BaseModel):
    competitor_name: str
    overall_summary: str
    feature_comparison: List[ComparisonFeature] = Field(default_factory=list)
    pricing_comparison: str
    winning_points_simple_practice: List[str] = Field(default_factory=list)
    winning_points_competitor: List[str] = Field(default_factory=list)
    # New: branded solutions from the competitor
    branded_solutions: List[BrandedSolution] = Field(default_factory=list)
    # New: granular Care Aide vs competitor capability breakdown
    care_aide_capability_comparison: List[CareAideCapabilityComparison] = Field(default_factory=list)


# ---------------------------------------------------------------------------
# Scraper
# ---------------------------------------------------------------------------

class DeepCompScraper:
    def __init__(
        self,
        target_competitor: str = None,
        compare_targets: List[str] = None,
        groups_focus: bool = False,
        custom_prompt: str = None,
        focus_name: str = None,
        output_folder_name: str = None,
    ):
        api_key = os.getenv("FIRECRAWL_API_KEY")
        if not api_key:
            raise ValueError("FIRECRAWL_API_KEY not found in environment")
        self.app = FirecrawlApp(api_key=api_key)

        # Keep a human-readable generation date for reports,
        # but allow each run to write into its own unique output folder.
        self.date_str = datetime.now().strftime("%Y-%m-%d")
        self.output_folder_name = output_folder_name or self.date_str
        self.output_dir = f"outputs/{self.output_folder_name}"

        self.target_competitor = target_competitor
        self.compare_targets = compare_targets
        self.groups_focus = groups_focus
        self.custom_prompt = custom_prompt
        self.focus_name = focus_name

        os.makedirs(f"{self.output_dir}/raw", exist_ok=True)
        os.makedirs(f"{self.output_dir}/comparisons", exist_ok=True)

    def _build_extraction_prompt(self, name: str, url: str) -> str:
        """Build the appropriate extraction prompt based on focus mode or custom prompt."""
        
        # If a custom prompt was provided, use it
        if self.custom_prompt:
            prompt = self.custom_prompt
            # Replace placeholders
            prompt = prompt.replace('{competitor_name}', name)
            prompt = prompt.replace('{competitor_url}', url)
            return prompt
        
        # Otherwise use the default behavior
        if self.groups_focus:
            return f"""Analyze {name} ({url}) with a specific focus on GROUPS-RELATED OFFERINGS and service capabilities.

PRIORITY 1: GROUPS-SPECIFIC PRODUCT OFFERINGS
Extract detailed information about features designed for group practices, multi-clinician organizations, or therapy groups:
- Group session scheduling and management features
- Multi-clinician coordination tools
- Group billing and invoicing capabilities
- Shared resources and templates for group practices
- Permissions and role management for practice administrators
- Group capacity limits (e.g., max number of groups, clinicians per practice)
- Pricing structure: per clinician, per group, flat fee, or tiered based on practice size
- Which features are included in base plans vs. paid add-ons for group practices
- Customer benefits specifically for group practices vs. solo practitioners
- How their groups offerings compare to SimplePractice (if mentioned)

PRIORITY 2: INSURANCE & BILLING
- Insurance claim submission capabilities (automated, manual, both)
- Supported insurance payers and networks
- Electronic Remittance Advice (ERA) support
- Eligibility verification features
- Clearinghouse integrations
- Which tiers include insurance billing features
- Pricing model for insurance features

PRIORITY 3: SERVICE OFFERINGS
A. Data Transfer / Switching Capabilities:
   - What data can be migrated from other EHR systems?
   - Is there an automated migration tool or manual process?
   - Are migration services publicly documented or require contacting sales?
   - Is data transfer included or an additional cost?
   - Any documented limitations or challenges with data migration?

B. Onboarding / Implementation:
   - Dedicated onboarding agent or self-service?
   - Number of onboarding sessions provided
   - Availability of onboarding support (business hours, 24/7, etc.)
   - Is onboarding included or premium service?
   - Group practice-specific onboarding vs. solo practitioner onboarding

C. Customer Success / Support:
   - Ongoing customer success programs or check-ins
   - Support channels (phone, email, chat, etc.)
   - Support hours and response times
   - Dedicated account managers for group practices
   - Is support included or tiered by plan?
   - Can this information be found publicly or requires being a prospect?

PRIORITY 4: MARKET INTELLIGENCE (Lower Priority)
- Market scope: national, regional, or international
- Target market segments (group practices, solo clinicians, specific specialties)
- Recent news: acquisitions, funding rounds, pricing changes, downtime issues
- Known challenges or reputation concerns
- How they position themselves in the market

ALSO EXTRACT (Standard Data):
- Pricing tiers with features breakdown
- AI-powered features (if any)
- Branded solutions or product bundles
- Technical constraints or limitations

INSTRUCTIONS:
- Prioritize groups-related and service information above all else
- Be specific about what applies to group practices vs. solo practitioners
- Mark information found in public documentation vs. requiring prospect status
- If pricing structures differ by practice size, capture all variants
- State "Not publicly disclosed" if information isn't found
- Focus on functional descriptions, not marketing language"""

        else:
            # Original AI-focused prompt
            return f"""Analyze {name} ({url}) with a focus on AI-powered capabilities. Extract the following:

BRANDED AI SOLUTIONS:
- Does {name} market any named AI product, suite, or bundle (e.g., "TherapyFuel", "Alliance Genie", "SmartCare AI")?
- For each branded solution, describe: its thematic positioning (what problem it solves), its core capabilities in plain functional terms, who it targets (solo clinician, group practice, etc.), whether it's an add-on or included, and whether it is AI-powered.
- Translate marketing names into functional descriptions. E.g., "TherapyFuel" → "AI progress note generation + treatment plan drafting bundled for solo therapists."

AI FEATURES & AUTOMATION:
- List every AI-powered feature (e.g., auto-generated progress notes, transcription, treatment plan suggestions, coding assistance, risk flagging)
- For each feature, describe the *underlying functionality* — not the marketing name.
- Note the AI model or technology used if disclosed (e.g., GPT-4, Whisper, proprietary)
- Distinguish between fully automated outputs vs. human-in-the-loop (clinician reviews/approves before finalizing)

DATA PRIVACY & COMPLIANCE:
- Is patient data sent to third-party AI providers? What does their BAA cover?
- Are AI features HIPAA-compliant? Any opt-in/opt-out mechanisms?
- Where is data processed and stored?

AI PRICING & ACCESS:
- Are AI features included in base plans or gated behind add-ons?
- Any usage-based pricing for AI (e.g., per note, per session)?
- Are there usage caps on AI features?

TECHNICAL DETAILS:
- Does the product offer an API for AI outputs?
- Any mention of accuracy rates, hallucination handling, or clinical validation?
- Supported input types (audio, video, text, EHR data)?

INSTRUCTIONS:
- Prioritize product documentation, changelogs, and pricing pages over marketing copy
- Mark inferences with "likely" or "appears to"
- If information isn't found, state "Not publicly disclosed"
- Translate branded feature names into plain functional descriptions"""

    async def discover_and_extract(self, name: str, url: str) -> Dict[str, Any]:
        """
        Uses Firecrawl Agent to discover features, pricing, and (optionally) groups offerings for a competitor.
        """
        focus_label = "Custom" if self.custom_prompt else ("Groups-Focused" if self.groups_focus else "AI-Focused")
        print(f"\n--- {focus_label} Deep Research: {name} using Agent ---")

        prompt = self._build_extraction_prompt(name, url)

        try:
            result = self.app.agent(prompt=prompt, schema=CompetitorData)

            if result.success:
                if result.data:
                    return result.data.model_dump() if hasattr(result.data, "model_dump") else result.data
                return {}
            else:
                print(f"Agent failed for {name}: {result.error}")
                return {}

        except Exception as e:
            print(f"Error during agent execution for {name}: {e}")
            return {}

    async def run_detailed_comparison(self, competitor_name: str, competitor_url: str):
        """
        Runs a detailed comparison agent: SimplePractice/Care Aide vs a target competitor.
        Captures branded solutions and a granular capability gap table.
        """
        print(f"\n--- Running Detailed Comparison: SimplePractice vs {competitor_name} ---")

        sp_url = COMPETITORS["SimplePractice"]

        prompt = f"""Compare the AI capabilities of SimplePractice / Care Aide ({sp_url}) and {competitor_name} ({competitor_url}) side-by-side.

CARE AIDE CONTEXT (SimplePractice's AI product):
{CARE_AIDE_DESCRIPTION}

YOUR TASKS:

1. BRANDED SOLUTIONS
   - Identify any named AI product or bundle {competitor_name} markets (e.g., "Alliance Genie", "TherapyFuel").
   - For each: name, thematic description (plain English), core capabilities, target user, pricing model, and whether it's AI-powered.

2. FEATURE COMPARISON
   - Compare the following capability areas side-by-side: AI-generated clinical documentation (progress notes, SOAP, DAP), session transcription and summarization, treatment plan drafting, AI-assisted billing and coding, risk flagging / crisis detection, predictive analytics, ambient listening, API access for AI outputs, data privacy / BAA coverage.
   - Use functional descriptions, not marketing language.

3. CARE AIDE CAPABILITY GAPS
   - For each capability area, produce a row with:
     * capability_area
     * care_aide_status (present / partial / absent)
     * care_aide_description
     * competitor_branded_name (if {competitor_name} has a named product for this)
     * competitor_status (present / partial / absent)
     * competitor_description
     * gap_direction (Care Aide leads / Competitor leads / Parity / Both absent)
     * gap_severity (critical / moderate / minor / none)
     * gap_notes (actionable insight — what would close the gap, or why it matters)

4. OVERALL ASSESSMENT
   - Summarize where SimplePractice / Care Aide leads on AI innovation and where {competitor_name} has an edge.
   - List distinct winning points for each side."""

        try:
            result = self.app.agent(prompt=prompt, schema=ComparisonData)

            if result.success:
                data = result.data
                output_data = data.model_dump() if hasattr(data, "model_dump") else data

                comp_file = f"{self.output_dir}/comparisons/sp_vs_{competitor_name.lower()}.json"
                with open(comp_file, "w") as f:
                    json.dump(output_data, f, indent=2)

                print(f"Detailed comparison saved to {comp_file}")
                return output_data
            else:
                print(f"Comparison agent failed for {competitor_name}: {result.error}")
                return None

        except Exception as e:
            print(f"Error during comparison agent execution: {e}")
            return None

    async def run(self):
        if self.compare_targets:
            all_comparisons = []
            for name in self.compare_targets[:2]:
                if name in COMPETITORS:
                    comp_data = await self.run_detailed_comparison(name, COMPETITORS[name])
                    if comp_data:
                        all_comparisons.append(comp_data)
                else:
                    print(f"Warning: Competitor '{name}' not found in configuration.")

            if all_comparisons:
                self.generate_comparison_reports(all_comparisons)
            return

        targets = COMPETITORS
        if self.target_competitor:
            if self.target_competitor in COMPETITORS:
                targets = {self.target_competitor: COMPETITORS[self.target_competitor]}
            else:
                print(f"Error: Competitor '{self.target_competitor}' not found in configuration.")
                print(f"Available competitors: {', '.join(COMPETITORS.keys())}")
                return

        all_data = {}
        for name, url in targets.items():
            data = await self.discover_and_extract(name, url)
            all_data[name] = data

            with open(f"{self.output_dir}/raw/{name.lower()}.json", "w") as f:
                json.dump(data, f, indent=2)

        self.summarize_findings(all_data)

    # -----------------------------------------------------------------------
    # Report Generators
    # -----------------------------------------------------------------------

    def generate_comparison_reports(self, comparisons: List[Dict]):
        report_path = f"{self.output_dir}/comparison_summary.txt"
        with open(report_path, "w") as f:
            f.write(f"SimplePractice / Care Aide — Competitor Comparison Summary\n")
            f.write(f"Generated: {self.date_str}\n")
            f.write("=" * 80 + "\n\n")

            for comp in comparisons:
                name = comp.get("competitor_name", "Unknown")

                # ---- Branded Solutions ----
                branded = comp.get("branded_solutions", [])
                if branded:
                    f.write(f"VS {name.upper()} — BRANDED AI SOLUTIONS\n")
                    f.write("-" * 40 + "\n")
                    for sol in branded:
                        f.write(f"  Product: {sol.get('solution_name', 'N/A')}\n")
                        f.write(f"  Theme:   {sol.get('thematic_description', '')}\n")
                        caps = sol.get("core_capabilities", [])
                        if caps:
                            f.write(f"  Capabilities:\n")
                            for c in caps:
                                f.write(f"    • {c}\n")
                        f.write(f"  Target:  {sol.get('target_user', 'N/A')}\n")
                        f.write(f"  Pricing: {sol.get('pricing_model', 'Not disclosed')}\n")
                        f.write(f"  AI:      {'Yes' if sol.get('ai_powered') else 'No/Unknown'}\n\n")

                # ---- Feature Comparison Table ----
                f.write(f"VS {name.upper()} — FEATURE COMPARISON\n")
                f.write("-" * 40 + "\n")
                f.write(f"Summary: {comp.get('overall_summary', '')}\n\n")
                f.write(f"{'Feature':<25} | {'SimplePractice':<30} | {name:<30}\n")
                f.write("-" * 90 + "\n")
                for feat in comp.get("feature_comparison", []):
                    f_name = feat.get("feature_name", "N/A")[:23]
                    sp_off = feat.get("simple_practice_offering", "N/A")[:28]
                    c_off = feat.get("competitor_offering", "N/A")[:28]
                    f.write(f"{f_name:<25} | {sp_off:<30} | {c_off:<30}\n")

                # ---- Care Aide Capability Gaps ----
                gaps = comp.get("care_aide_capability_comparison", [])
                if gaps:
                    f.write(f"\nVS {name.upper()} — CARE AIDE CAPABILITY GAPS\n")
                    f.write("-" * 40 + "\n")
                    header = f"{'Capability':<28} | {'Care Aide':<10} | {'Competitor':<10} | {'Direction':<22} | {'Severity':<10}\n"
                    f.write(header)
                    f.write("-" * 90 + "\n")
                    for gap in gaps:
                        cap = gap.get("capability_area", "N/A")[:26]
                        ca_status = gap.get("care_aide_status", "N/A")[:8]
                        comp_status = gap.get("competitor_status", "N/A")[:8]
                        direction = gap.get("gap_direction", "N/A")[:20]
                        severity = gap.get("gap_severity", "N/A")[:8]
                        f.write(f"{cap:<28} | {ca_status:<10} | {comp_status:<10} | {direction:<22} | {severity:<10}\n")
                        notes = gap.get("gap_notes", "")
                        if notes:
                            f.write(f"  → {notes}\n")

                # ---- Win/Loss ----
                f.write(f"\nSimplePractice / Care Aide Wins:\n")
                for win in comp.get("winning_points_simple_practice", []):
                    f.write(f"  [+] {win}\n")

                f.write(f"\n{name} Wins:\n")
                for win in comp.get("winning_points_competitor", []):
                    f.write(f"  [-] {win}\n")

                f.write("\n" + "=" * 80 + "\n\n")

        print(f"Comprehensive comparison report generated: {report_path}")

    def summarize_findings(self, all_data: Dict):
        focus_label = self.focus_name or (
            "Custom" if self.custom_prompt else ("Groups-Focused" if self.groups_focus else "General")
        )
        summary_path = f"{self.output_dir}/summary_report.txt"

        with open(summary_path, "w") as f:
            f.write(f"{focus_label} Competitor Research Summary - {self.date_str}\n")
            f.write("=" * 60 + "\n")

            for name, data in all_data.items():
                f.write(f"\nCOMPETITOR: {name}\n")
                f.write("-" * 60 + "\n")

                # AI Features & Capabilities
                if self.focus_name == "AI Features & Capabilities":
                    f.write("1. AI Product Overview\n")
                    f.write(f"- AI features found: {len(data.get('ai_features', []))}\n")
                    f.write(f"- Branded AI solutions found: {len(data.get('branded_solutions', []))}\n")

                    if data.get("ai_features"):
                        f.write("\n2. Core AI Features\n")
                        for feat in data["ai_features"]:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            gated = " [GATED]" if ft.get("is_gated") else ""
                            f.write(f"- {ft.get('feature_name', 'N/A')}: {ft.get('description', '')}{gated}\n")

                    if data.get("branded_solutions"):
                        f.write("\n3. Branded AI Solutions\n")
                        for sol in data["branded_solutions"]:
                            s = sol if isinstance(sol, dict) else sol.__dict__
                            f.write(f"- {s.get('solution_name', 'N/A')}: {s.get('thematic_description', '')}\n")

                    if data.get("technical_constraints"):
                        f.write("\n4. AI Privacy, Compliance, and Technical Notes\n")
                        for item in data["technical_constraints"]:
                            f.write(f"- {item}\n")

                    if data.get("additional_costs"):
                        f.write("\n5. AI Pricing / Gating\n")
                        for item in data["additional_costs"]:
                            f.write(f"- {item}\n")

                    if data.get("ai_maturity_summary"):
                        f.write("\n6. Short Summary\n")
                        f.write(f"{data['ai_maturity_summary']}\n")

                # Groups & Service Offerings
                elif self.focus_name == "Groups & Service Offerings":
                    f.write("1. Group Practice Capabilities\n")
                    f.write(f"- Groups offerings found: {len(data.get('groups_offerings', []))}\n")

                    if data.get("groups_offerings"):
                        for offering in data["groups_offerings"]:
                            o = offering if isinstance(offering, dict) else offering.__dict__
                            f.write(f"- {o.get('feature_name', 'N/A')}: {o.get('description', '')}\n")

                    if data.get("insurance_offerings"):
                        f.write("\n2. Insurance & Billing Support for Group Practices\n")
                        for ins in data["insurance_offerings"]:
                            i = ins if isinstance(ins, dict) else ins.__dict__
                            f.write(f"- {i.get('offering_name', 'N/A')}: {i.get('description', '')}\n")

                    if data.get("service_offerings"):
                        f.write("\n3. Service Offerings\n")
                        for svc in data["service_offerings"]:
                            sv = svc if isinstance(svc, dict) else svc.__dict__
                            f.write(f"- [{sv.get('category', 'N/A')}] {sv.get('offering_name', 'N/A')}: {sv.get('description', '')}\n")

                    if data.get("ai_features"):
                        f.write("\n4. Relevant AI in This Area\n")
                        for feat in data["ai_features"]:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            f.write(f"- {ft.get('feature_name', 'N/A')}: {ft.get('description', '')}\n")

                    if data.get("additional_costs"):
                        f.write("\n5. Pricing / Gating Notes\n")
                        for item in data["additional_costs"]:
                            f.write(f"- {item}\n")

                # Pricing & Packaging
                elif self.focus_name == "Pricing & Packaging":
                    f.write("1. Pricing Model Overview\n")
                    f.write(f"- Pricing tiers found: {len(data.get('pricing_tiers', []))}\n")

                    if data.get("pricing_tiers"):
                        f.write("\n2. Pricing Tiers and What's Included\n")
                        for tier in data["pricing_tiers"]:
                            t = tier if isinstance(tier, dict) else tier.__dict__
                            features = t.get("key_features", [])
                            feature_text = ", ".join(features) if features else "No feature details provided"
                            f.write(f"- {t.get('tier_name', 'N/A')}: {t.get('price', 'N/A')} — {feature_text}\n")

                    if data.get("additional_costs"):
                        f.write("\n3. Add-Ons, Gating, and Upsell Strategy\n")
                        for item in data["additional_costs"]:
                            f.write(f"- {item}\n")

                    if data.get("ai_features"):
                        f.write("\n4. Relevant AI / Premium Packaging Notes\n")
                        for feat in data["ai_features"]:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            f.write(f"- {ft.get('feature_name', 'N/A')}: {ft.get('description', '')}\n")

                    if data.get("technical_constraints"):
                        f.write("\n5. Key Limitations or Complexity in Pricing\n")
                        for item in data["technical_constraints"]:
                            f.write(f"- {item}\n")

                # Documentation & Clinical Workflows
                elif self.focus_name == "Documentation & Clinical Workflows":
                    f.write("1. Documentation Workflow Overview\n")
                    f.write(f"- Features found: {len(data.get('all_features', []))}\n")

                    if data.get("all_features"):
                        f.write("\n2. Core Note and Treatment Plan Capabilities\n")
                        for feat in data["all_features"]:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            f.write(f"- {ft.get('feature_name', 'N/A')}: {ft.get('description', '')}\n")

                    if data.get("ai_features"):
                        f.write("\n3. Relevant AI Features in This Area\n")
                        for feat in data["ai_features"]:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            f.write(f"- {ft.get('feature_name', 'N/A')}: {ft.get('description', '')}\n")

                    if data.get("technical_constraints"):
                        f.write("\n4. Key Limitations or Missing Capabilities\n")
                        for item in data["technical_constraints"]:
                            f.write(f"- {item}\n")

                    if data.get("additional_costs"):
                        f.write("\n5. Pricing / Gating Notes\n")
                        for item in data["additional_costs"]:
                            f.write(f"- {item}\n")

                # Messaging & Collaboration
                elif self.focus_name == "Messaging & Collaboration":
                    f.write("1. Messaging Capabilities\n")
                    if data.get("all_features"):
                        for feat in data["all_features"]:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            f.write(f"- {ft.get('feature_name', 'N/A')}: {ft.get('description', '')}\n")
                    else:
                        f.write("- No messaging-specific features clearly identified\n")

                    if data.get("service_offerings"):
                        f.write("\n2. Internal Collaboration Capabilities\n")
                        for svc in data["service_offerings"]:
                            sv = svc if isinstance(svc, dict) else svc.__dict__
                            f.write(f"- {sv.get('offering_name', 'N/A')}: {sv.get('description', '')}\n")

                    if data.get("ai_features"):
                        f.write("\n3. Relevant AI Features in This Area\n")
                        for feat in data["ai_features"]:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            f.write(f"- {ft.get('feature_name', 'N/A')}: {ft.get('description', '')}\n")
                    else:
                        f.write("\n3. Relevant AI Features in This Area\n")
                        f.write("- No relevant AI features tied directly to messaging/collaboration were identified\n")

                    if data.get("technical_constraints"):
                        f.write("\n4. Key Limitations or Missing Capabilities\n")
                        for item in data["technical_constraints"]:
                            f.write(f"- {item}\n")

                    if data.get("additional_costs"):
                        f.write("\n5. Pricing / Gating Notes\n")
                        for item in data["additional_costs"]:
                            f.write(f"- {item}\n")

                # Billing & Insurance
                elif self.focus_name == "Billing & Insurance":
                    f.write("1. Billing & Insurance Workflow Overview\n")
                    f.write(f"- Insurance offerings found: {len(data.get('insurance_offerings', []))}\n")

                    if data.get("insurance_offerings"):
                        f.write("\n2. Core Insurance and Claim Capabilities\n")
                        for ins in data["insurance_offerings"]:
                            i = ins if isinstance(ins, dict) else ins.__dict__
                            f.write(f"- {i.get('offering_name', 'N/A')}: {i.get('description', '')}\n")

                    if data.get("service_offerings"):
                        f.write("\n3. Payment Collection and Revenue Cycle Support\n")
                        for svc in data["service_offerings"]:
                            sv = svc if isinstance(svc, dict) else svc.__dict__
                            f.write(f"- {sv.get('offering_name', 'N/A')}: {sv.get('description', '')}\n")

                    if data.get("ai_features"):
                        f.write("\n4. Relevant AI Features in This Area\n")
                        for feat in data["ai_features"]:
                            ft = feat if isinstance(feat, dict) else feat.__dict__
                            f.write(f"- {ft.get('feature_name', 'N/A')}: {ft.get('description', '')}\n")

                    if data.get("technical_constraints"):
                        f.write("\n5. Key Limitations or Missing Capabilities\n")
                        for item in data["technical_constraints"]:
                            f.write(f"- {item}\n")

                    if data.get("additional_costs"):
                        f.write("\n6. Pricing / Gating Notes\n")
                        for item in data["additional_costs"]:
                            f.write(f"- {item}\n")

                # Fallback generic summary
                else:
                    f.write(f"Pricing Tiers found: {len(data.get('pricing_tiers', []))}\n")
                    f.write(f"Total Features found: {len(data.get('all_features', []))}\n")
                    f.write(f"AI Features found: {len(data.get('ai_features', []))}\n")
                    f.write(f"Branded Solutions found: {len(data.get('branded_solutions', []))}\n")

                    if data.get("technical_constraints"):
                        f.write(f"Technical Constraints: {', '.join(data.get('technical_constraints', []))}\n")
                    if data.get("additional_costs"):
                        f.write(f"Additional Costs: {', '.join(data.get('additional_costs', []))}\n")

                f.write(f"\nRaw data stored in raw/{name.lower()}.json\n")
                f.write("\n" + "=" * 60 + "\n")

        print(f"\nResearch phase complete. Focus-aware report generated in {summary_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Deep Competitor Research Scraper")
    parser.add_argument(
        "--competitor",
        type=str,
        help="Run only for a specific competitor (e.g., SimplePractice)",
    )
    parser.add_argument(
        "--compare",
        nargs="+",
        help="Compare SimplePractice/Care Aide with up to two competitors (e.g., --compare Blueprint Jane)",
    )
    parser.add_argument(
        "--groups",
        action="store_true",
        help="Focus research on groups-related offerings, service capabilities, and insurance features",
    )
    args = parser.parse_args()

    scraper = DeepCompScraper(
        target_competitor=args.competitor,
        compare_targets=args.compare,
        groups_focus=args.groups,
    )
    asyncio.run(scraper.run())
