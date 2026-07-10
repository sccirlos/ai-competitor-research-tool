import streamlit as st
import pandas as pd
from config_manager import get_config_names, get_config_by_name
from deepcomp_enhanced import COMPETITORS, DeepCompScraper


st.set_page_config(page_title="Streamlit Crash Test")

st.title("Crash Test")

focus = st.selectbox(
    "Focus area",
    [
        "AI Features & Capabilities",
        "Documentation & Clinical Workflows",
        "Golden Thread & Clinical Care Journey",
        "Revenue Cycle Management",
    ],
)

competitor = st.selectbox(
    "Competitor",
    sorted(COMPETITORS.keys()),
)

st.success("The app is still running.")
st.write("Selected focus:", focus)
st.write("Selected competitor:", competitor)