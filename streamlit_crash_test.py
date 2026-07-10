import streamlit as st
import pandas as pd

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
    [
        "SimplePractice",
        "TherapyNotes",
        "PracticeBetter",
        "Upheal",
    ],
)

st.success("The app is still running.")
st.write("Selected focus:", focus)
st.write("Selected competitor:", competitor)