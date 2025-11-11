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
for key in ["instrument", "clue_index", "game_over", "message"]:
    if key not in st.session_state:
        if key == "instrument":
            st.session_state[key] = None
        elif key == "clue_index":
            st.session_state[key] = 0
        elif key == "game_over":
            st.session_state[key] = False
        else:
            st.session_state[key] = ""

# --- Function to start a new quiz ---
def start_new_quiz():
    st.session_state.instrument = random.choice(list(quiz.keys()))
    st.session_state.clue_index = 0
    st.session_state.game_over = False
    st.session_state.message = ""

# --- Automatically start quiz on first load ---
if st.session_state.instrument is None:
    start_new_quiz()

# --- Top horizontal buttons ---
col1, col2, col3 = st.columns([1, 1, 1])
with col1:
    if st.button("Show Next Clue", key="show_next"):
        if st.session_state.clue_index < len(quiz[st.session_state.instrument]["clues"]) - 1:
            st.session_state.clue_index += 1
        else:
            st.warning("No more clues available!")

with col2:
    if st.button("Give Up", key="give_up"):
        st.session_state.message = f"The correct answer was: **{st.session_state.instrument}**"
        st.session_state.game_over = True

with col3:
    if st.button("Start New Quiz", key="start_new_top"):
        start_new_quiz()
        new_quiz_started = True  # set flag to show message below

# Show full-width success message outside columns
    if new_quiz_started:
        st.success("New quiz started!")

# --- Main Game (audio, clues, multiple choice) ---
if st.session_state.instrument:
    instrument_data = quiz[st.session_state.instrument]

    # Audio
    st.audio(instrument_data["audio"], format="audio/mp4")

    # Show clues up to current clue index
    for i in range(st.session_state.clue_index + 1):
        st.write(instrument_data["clues"][i])

    # Multiple choice
    guess = st.radio("Pick your guess:", instrument_data["options"], key="mc_guess")
    if st.button("Submit Guess", key="submit_guess"):
        if guess.lower() == st.session_state.instrument.lower():
            st.session_state.message = f"Correct! The instrument is **{st.session_state.instrument}**"
            st.session_state.game_over = True
        else:
            st.session_state.message = "Wrong guess. Try another clue!"

# --- Feedback ---
if st.session_state.message:
    if "Correct!" in st.session_state.message or "correct answer" in st.session_state.message:
        st.success(st.session_state.message)
    elif "Wrong" in st.session_state.message:
        st.error(st.session_state.message)
