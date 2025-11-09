import streamlit as st
import random

st.set_page_config(
    page_title="Guess the Song!",
    page_icon="🎶",
    layout="centered",
)

st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("🎶 Guess the Song!")
st.markdown("""
Welcome! Play the audio clip below and guess the instrument. Listen and discover different types of cultural music instruments!
""")

#video_url = "https://imgur.com/3ppJb3W"

#st.video(video_url, width=300)


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
            "Clue 4: It is played by plucking metal tines on a wooden board ."
        ],
        "options": ["Mbira", "Djembe", "Harpsichord", "Carillon"],
        "audio": "https://i.imgur.com/KORLtbB.mp4"
    },
    "Guiro": {
        "clues": [
            "Clue 1: A percussion instrument played with scraping a stick across its surface.",
            "Clue 2: This instrument is heard in all types of music genres, especially salsa and jazz.",
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
            "Clue 3: Often played for Chinese special celebrations.",
            "Clue 4: One of the oldest instruments to use a free reed, allowing one to play multiple notes at once."
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

#st.title("🎵 Guess the Instrument Quiz")

# --- Start New Quiz ---
if st.button("Start New Quiz", key="start_quiz_btn"):
    st.session_state.instrument = random.choice(list(quiz.keys()))
    st.session_state.clue_index = 0
    st.session_state.game_over = False
    st.success("Quiz Started!")

# --- Show Clue and Options ---
if st.session_state.instrument and not st.session_state.game_over:
    instrument_data = quiz[st.session_state.instrument]

    #display audio snippet
    st.audio(instrument_data["audio"], format="audio/mp4")

    with st.form(key="instrument_form"):
    # Display multiple-choice options
    guess = st.radio("Pick your guess:", instrument_data["options"], key="mc_guess_radio")

    # Form buttons
    submit_guess = st.form_submit_button("Submit Guess")
    show_next = st.form_submit_button("Show Next Clue")
    give_up = st.form_submit_button("Give Up")

        # Handle actions
        if submit_guess:
            if guess.lower() == st.session_state.instrument.lower():
                st.success(f"🎉 Correct! The instrument is **{st.session_state.instrument}**")
                st.session_state.game_over = True
            else:
                st.error("❌ Wrong guess. Try another clue!")

        if show_next:
            if st.session_state.clue_index < len(instrument_data["clues"]) - 1:
                st.session_state.clue_index += 1
            else:
                st.warning("No more clues available!")

        if give_up:
            st.info(f"The instrument was **{st.session_state.instrument}**.")
            st.session_state.game_over = True

    # Display all clues up to the current index
    for i in range(st.session_state.clue_index + 1):
        st.write(instrument_data["clues"][i])
        st.write("")  # blank line between clues

#    if st.button("Submit Guess", key="submit_guess_btn"):
#        if guess.lower() == st.session_state.instrument.lower():
#            st.success(f"🎉 Correct! The instrument is **{st.session_state.instrument}**")
#            st.session_state.game_over = True
#        else:
#            st.error("❌ Wrong guess. Try another clue!")

#    if st.button("Show Next Clue", key="show_next_clue_btn"):
#        if st.session_state.clue_index < len(instrument_data["clues"]) - 1:
#            st.session_state.clue_index += 1
#        else:
#            st.warning("No more clues available!")

#    if st.button("Give Up", key="give_up_btn"):
#        st.info(f"The instrument was **{st.session_state.instrument}**.")
#        st.session_state.game_over = True

#Questions
#with st.form("instrument_form"):
#    selected_instrument = st.selectbox("What type of instrument is this?", ["String", "Percussion", "Wind", "Brass"])
#    selected_country = st.selectbox("Guess the origi:n", ["","","",""])
#    selected_country = st.selectbox("This instrument is widely played in Indian classical and pop music. What could it be?", ["Cuatro", "Bouzouki", "Sitar", "Koto"])
#video_url = "https://imgur.com/3ppJb3W"

#st.video(video_url, width=300)

#guess = ["Piano", "Trumpet", "Guitar", "Clarinet"]
#selected_one = st.radio("Guess the instrument:", guess, index=None)

#Q2: Guess the Country Origin
#guess = ["Piano", "Trumpet", "Guitar", "Clarinet"]
#selected_one = st.radio("Guess the instrument:", guess, index=None)


#Q3: Guess the Song Title
#guess = ["Piano", "Trumpet", "Guitar", "Clarinet"]
#selected_one = st.radio("Guess the instrument:", guess, index=None)