import streamlit as st

st.title("🏠 Music Hub")
st.markdown("Welcome! Select a page to explore:")

# List of pages
pages = {
    "Jams & Juice": "jams_and_juice",
    "Sweet Melodies": "sweet_melodies",
    "Y2K Rewind": "y2k_rewind",
    "Sweater Weather Tunes": "sweater_weather_tunes",
    "Craft & Sip": "craft_and_sip",
    "Serene Self-Care": "serene_self_care",
    "Press Play to Party": "press_play_to_party",
    "Guess the Instrument!": "guess_the_instrument",
    "Music Trivia": "music_trivia"
}

for page_name, page_key in pages.items():
    if st.button(page_name):
        # Set query param to redirect
        st.experimental_set_query_params(page=page_key)
        st.rerun()
