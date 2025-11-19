import streamlit as st

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

choice = st.selectbox("Choose a page:", pages.keys())

if st.button("Go"):
    st.switch_page(f"pages/{pages[choice]}.py")



