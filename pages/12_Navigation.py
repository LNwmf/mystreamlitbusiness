import streamlit as st


# --- Define each page as a function ---
def jams_and_juice():
    st.title("🍹 Jams & Juice")
    st.markdown("Pick a drink!")

def jams_and_juice():
    st.title("🍹 Jams & Juice")
    st.markdown("Pick a drink and discover a blended playlist!")

def sweet_melodies():
    st.title("🍬 Sweet Melodies")
    st.markdown("Check out your rewards and special offers!")

def y2k_rewind():
    st.title("💿 Y2K Rewind")
    st.markdown("Select a 2000s artist!")

def sweater_weather_tunes():
    st.title("🍂 Sweater Weather Tunes")
    st.markdown("Select a fall activity!")

def craft_and_sip():
    st.title("🎨 Craft & Sip")
    st.markdown("Pick an artistic value!")

def serene_self_care():
    st.title("🪞 Serene Self-Care")
    st.markdown("Pick an energy!")

def press_play_to_party():
    st.title("🎉 Press Play to Party")
    st.markdown("Select a party trick!")

def guess_the_instrument():
    st.title("🎶 Guess the Instrument!")
    st.markdown("Play an audio snippet and guess the instrument!")

def music_trivia():
    st.title("🎵 Music Trivia Game")
    st.markdown("Test your musical knowledge!")
# --- Navigation logic ---
pages = {
    "Jams & Juice": jams_and_juice,
    "Sweet Melodies": sweet_melodies,
    "Y2K Rewind": y2k_rewind,
    "Sweater Weather Tunes": sweater_weather_tunes,
    "Craft & Sip": craft_and_sip,
    "Serene Self-Care": serene_self_care,
    "Press Play to Party": press_play_to_party,
    "Guess the Instrument!": guess_the_instrument,
    "Music Trivia": music_trivia
}

# Track selected page
if "page" not in st.session_state:
    st.session_state.page = "Home"

# --- Home Page as navigation ---
if st.session_state.page == "Home":
    st.title("🏠 Navigation")
    st.markdown("Welcome! Pick a page below:")

    # Layout buttons in 3 columns
    cols = st.columns(3)
    for idx, page_name in enumerate(pages.keys()):
        with cols[idx % 3]:
            if st.button(page_name):
                st.session_state.page = page_name

# --- Render the selected page ---
if st.session_state.page != "Home":
    pages[st.session_state.page]()
    if st.button("⬅️ Back to Navigation"):
        st.session_state.page = "Home"