import streamlit as st

st.title("Check Streamlit Pages")

pages = st.get_pages()  # Get all pages
st.write("Pages detected by Streamlit:")
st.write(pages)

