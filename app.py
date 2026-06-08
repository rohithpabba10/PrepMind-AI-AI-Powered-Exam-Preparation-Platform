import streamlit as st

st.set_page_config(
    page_title="PrepMind AI",
    layout="wide"
)

html_file = open("preview.html", "r", encoding="utf-8")

source_code = html_file.read()

st.components.v1.html(
    source_code,
    height=1000,
    scrolling=True
)