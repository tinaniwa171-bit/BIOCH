import streamlit as st
import streamlit.components.v1 as components

# Set the page configuration (title, wide layout)
st.set_page_config(layout="wide", page_title="Biochem Quiz")

# Read your HTML file
with open("index.html", "r", encoding='utf-8') as f:
    html_content = f.read()

# Render the HTML
# height=1000 ensures the whole quiz fits; scrolling=True allows scrolling if needed
components.html(html_content, height=1000, scrolling=True)