import streamlit as st


st.set_page_config(
    page_title="Guess the Instrument!",
    page_icon="🎶",
    layout="centered",
)

st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("🎶 Guess the Instrument!")
st.markdown("""
Welcome! Play the audio clip below and guess the instrument. Listen and discover different types of cultural music instruments!
""")

import streamlit as st
import random

# --- Quiz Data ---
quiz = {
    "Sitar": {
        "clues": [
            "Clue 1: This instrument has 18-21 strings.",
            "Clue 2: It is often used in Indian classical and pop music.",
            "Clue 3: The player typically sits cross-legged with the instrument at a 45 degree angle.",
            "Clue 4: Famous artists like Ravi Shankar, The Beatles and The Rolling Stones incorporated it into their music."
        ],
        "options": ["Cuatro", "Bouzouki", "Sitar", "Koto"],
        "audio": "https://i.imgur.com/3ppJb3W.mp4"
    },
    "Mbira": {
        "clues": [
            "Clue 1: This percussion instrument is often used in traditional and ceremonial music.",
            "Clue 2: It originated from Zimbabwe.",
            "Clue 3: Often referred to as a thumb piano.",
            "Clue 4: It is played by plucking metal tines on a wooden board."
        ],
        "options": ["Mbira", "Djembe", "Harpsichord", "Carillon"],
        "audio": "https://i.imgur.com/KORLtbB.mp4"
    },
    "Guiro": {
        "clues": [
            "Clue 1: A percussion instrument played by scraping a stick across its surface.",
            "Clue 2: This instrument is heard in salsa and jazz.",
            "Clue 3: Originated from the Caribbean.",
            "Clue 4: It is traditionally made from gourds."
        ],
        "options": ["Slapstick", "Guiro", "Castanets", "Claves"],
        "audio": "https://i.imgur.com/EuCqgr6.mp4"
    },
    "Sheng": {
        "clues": [
            "Clue 1: It is a wind instrument.",
            "Clue 2: This instrument is traditionally made from bamboo.",
            "Clue 3: Often played during Chinese celebrations.",
            "Clue 4: One of the oldest instruments to use a free reed, allowing multiple notes at once."
        ],
        "options": ["Dizi", "Bagpipes", "Pan flute", "Sheng"],
        "audio": "https://i.imgur.com/csz0rsf.mp4"
    }
}

# --- Initialize Session State ---
if "instrument" not in st.session_state:
    st.session_state.instrument = None
if "clue_index" not in st.session_state:
    st.session_state.clue_index = 0
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "message" not in st.session_state:
    st.session_state.message = ""  # feedback message

# Flags for top-row buttons
if "show_next_click" not in st.session_state:
    st.session_state.show_next_click = False
if "give_up_click" not in st.session_state:
    st.session_state.give_up_click = False
if "start_new_click" not in st.session_state:
    st.session_state.start_new_click = False



# --- Start New Quiz Button (when game over or no quiz) ---
if st.session_state.instrument is None or st.session_state.game_over:
    if st.button("Start New Quiz"):
        st.session_state.instrument = random.choice(list(quiz.keys()))
        st.session_state.clue_index = 0
        st.session_state.game_over = False
        st.session_state.message = ""
        st.success("Quiz Started!")

# --- Main Game Logic ---
if st.session_state.instrument and not st.session_state.game_over:
    instrument_data = quiz[st.session_state.instrument]

    # --- Horizontal Buttons Row ---
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Show Next Clue"):
            st.session_state.show_next_click = True
    with col2:
        if st.button("Give Up"):
            st.session_state.give_up_click = True
    with col3:
        if st.button("Start New Quiz"):
            st.session_state.start_new_click = True

    # --- Handle top-row button clicks safely ---
    if st.session_state.show_next_click:
        if st.session_state.clue_index < len(instrument_data["clues"]) - 1:
            st.session_state.clue_index += 1
        else:
            st.warning("No more clues available!")
        st.session_state.show_next_click = False  # reset click

    if st.session_state.give_up_click:
        st.session_state.message = f"The correct answer was **{st.session_state.instrument}**"
        st.session_state.game_over = True
        st.session_state.give_up_click = False  # reset click

    if st.session_state.start_new_click:
        st.session_state.instrument = random.choice(list(quiz.keys()))
        st.session_state.clue_index = 0
        st.session_state.game_over = False
        st.session_state.message = ""
        st.success("New quiz started!")
        st.session_state.start_new_click = False  # reset click

    # --- Audio Snippet ---
    st.audio(instrument_data["audio"], format="audio/mp4")

    # --- Show Clues ---
    for i in range(st.session_state.clue_index + 1):
        st.write(instrument_data["clues"][i])
        st.write("")

    # --- Multiple Choice ---
    guess = st.radio("Pick your guess:", instrument_data["options"], key="mc_guess_radio")

    # --- Submit Guess ---
    if st.button("Submit Guess"):
        if guess.lower() == st.session_state.instrument.lower():
            st.session_state.message = f"Correct! The instrument is **{st.session_state.instrument}**"
            st.session_state.game_over = True
        else:
            st.session_state.message = "Wrong guess. Try another clue!"

    # --- Feedback Message ---
    if st.session_state.message:
        if "Correct!" in st.session_state.message or "The correct answer" in st.session_state.message:
            st.success(st.session_state.message)
        elif "Wrong guess" in st.session_state.message:
            st.error(st.session_state.message)

# --- Game Over Play Again ---
if st.session_state.game_over:
    if st.button("Play Again"):
        st.session_state.instrument = None
        st.session_state.clue_index = 0
        st.session_state.game_over = False
        st.session_state.message = ""

