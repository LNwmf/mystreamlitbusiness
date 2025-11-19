import streamlit as st
import random

st.set_page_config(
    page_title="Guess the Instrument!",
    page_icon="💭",
    layout="centered",
)
st.markdown(
    """
    <style>
    /* Remove rounding from all images rendered by Streamlit */
    img {
        border-radius: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("💭 Guess the Instrument!")
st.markdown("""
Welcome! Play the audio clip below and guess the instrument. Listen and discover different types of cultural music instruments!
""")

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
    },
    "Valiha": {
        "clues": [
            "Clue 1: National instrument of Madagascar.",
            "Clue 2: Typically used for spiritual and ceremonial ceremonies.",
            "Clue 3: It belongs to the chordophone family and classified as a tube zither.",
            "Clue 4: Made out of bamboo."
        ],
        "options": ["Didgeridoo", "Valiha", "Qanun", "Harp"],
        "audio": "https://i.imgur.com/lEroSAB.mp4"
    },
    "Atumpan": {
        "clues": [
            "Clue 1: It is played with two L-shaped sticks or hands.",
            "Clue 2: Referred to as a 'talking drum' due to its extensive range of sound and ability to imitate language.",
            "Clue 3: The instrument is played in pairs, one male and female.",
            "Clue 4: A traditional instrument of Ghana."
        ],
        "options": ["Steel drum", "Darbuka", "Bongo", "Bata drum"],
        "audio": "https://i.imgur.com/jC2jK7p.mp4"
    },
    "Santur": {
        "clues": [
            "Clue 1: This has 18 bridges, each with 4 strings for a total of 72.",
            "Clue 2: Famous artist Pandit Shivkumar Sharma popularized the instrument through classical music.",
            "Clue 3: Two small wooden sticks are used to play it.",
            "Clue 4: A traditional instrument of Iran."
        ],
        "options": ["Santur", "Yangqin", "Dutar", "Lyre"],
        "audio": "https://i.imgur.com/O3E44tr.mp4"
    },
    "Ngoni": {
        "clues": [
            "Clue 1: Originated from Mali.",
            "Clue 2: This is a string instrument and apart of the lute family.",
            "Clue 3: It is made of a single, hollowed piece of wood and animal skin.",
            "Clue 4: Significant in traditional ceremonies and festivals in West Africa."
        ],
        "options": ["Morinkhuur", "Ukulele", "Ardin", "Ngoni"],
        "audio": "https://i.imgur.com/of9y4pB.mp4"
    },
    "Hardanger fiddle": {
        "clues": [
            "Clue 1: This is a traditional Norwegian instrument.",
            "Clue 2: It has four primary strings.",
            "Clue 3: Has a controversial history and sometimes banned from churches because it was thought to be associated with the devil and malevolent spirits.",
            "Clue 4: Notable musician Ole Bull helped popularize the instrument."
        ],
        "options": ["Hardanger fiddle", "Violin", "Sitar", "Nyckelharpa"],
        "audio": "https://i.imgur.com/rUCyalx.mp4"
    },
    "Nzumari": {
        "clues": [
            "Clue 1: A technique called circular breathing is used to play this instrument.",
            "Clue 2: It is traditionally only played by men and for special occasions.",
            "Clue 3: Originated from Kenya.",
            "Clue 4: Played similar to an oboe and includes a double reed."
        ],
        "options": ["Zurna", "Nzumari", "Algaita", "Siwa"],
        "audio": "https://i.imgur.com/AWcjohn.mp4"
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
# Initialize flag
new_quiz_started = False  # will be True if user clicks "Start New Quiz"

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
        st.session_state.message = f"The correct answer was: **{st.session_state.instrument}**."
        st.session_state.game_over = True

with col3:
    if st.button("Start New Quiz", key="start_new_top"):
        start_new_quiz()
        new_quiz_started = True  # set flag

# Full-width success message
if new_quiz_started:
    st.markdown(
        """
        <div style="
            background-color: #AECCE4;  /* Blue background */
            padding: 0.70em 1em;        /* Compact height */
            border-radius: 0.25em;
            color: black;
            font-weight: bold;
            margin: 0.5em 0;             /* Space above & below */
            display: block;              /* Full-width block */
            width: 100%;                 /* Ensure full width */
            box-sizing: border-box;      /* Include padding in width */
        ">
            New quiz started!
        </div>
        """,
        unsafe_allow_html=True
    )

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
            st.session_state.message = f"Correct! The instrument is **{st.session_state.instrument}**."
            st.session_state.game_over = True
        else:
            st.session_state.message = "Wrong guess. Try another clue!"

# --- Feedback ---
if st.session_state.message:
    if "Correct!" in st.session_state.message or "correct answer" in st.session_state.message:
        st.success(st.session_state.message)
    elif "Wrong" in st.session_state.message:
        st.error(st.session_state.message)