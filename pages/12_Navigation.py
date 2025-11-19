import streamlit as st

st.title("🎵 Explore Your Pages")

pages = {
    "Jams & Juice": "02_Jams_and_Juice",
    "Sweet Melodies": "03_Sweet_Melodies",
    "Y2K Rewind": "04_Y2K_Rewind",
    "Sweater Weather Tunes": "05_Sweater_Weather_Tunes",
    "Craft & Sip": "06_Craft_and_Sip",
    "Serene Self-Care": "07_Serene_Self_Care",
    "Press Play to Party": "08_Press_Play_to_Party",
    "Guess the Instrument": "09_Guess_the_Instrument",
    "Music Trivia": "10_Music_Trivia",
    "Images": "11_Images",
}

cols = st.columns(2)

i = 0
for label, file in pages.items():
    with cols[i % 2]:
        if st.button(f"🎧 {label}", use_container_width=True):
            st.switch_page(f"pages/{file}.py")
    i += 1




