import streamlit as st

st.title("🏠 Music Hub")
st.markdown("Welcome! Select a page to explore:")

# List of pages
pages = [
    "Jams & Juice",
    "Sweet Melodies",
    "Y2K Rewind",
    "Sweater Weather Tunes",
    "Craft & Sip",
    "Serene Self-Care",
    "Press Play to Party",
    "Guess the Instrument!",
    "Music Trivia"
]

for page in pages:
    st.page_link(page, label=page)

