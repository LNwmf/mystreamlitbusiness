import os
import streamlit as st

st.title("Check Page Filenames")

pages_folder = "pages"

if os.path.exists(pages_folder):
    st.write("Files found in `pages/` folder:")
    for file in os.listdir(pages_folder):
        st.write("•", file)
else:
    st.error("No `pages` folder found.")


