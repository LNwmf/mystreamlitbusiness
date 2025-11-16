import streamlit as st
import random

# ---------------------
# PAGE CONFIG
# ---------------------
st.set_page_config(page_title="🎶 Music Trivia Game", page_icon="🎵", layout="centered")

st.title("🎶 Music Trivia Game")
st.subheader("Test your knowledge of music history and pop culture!")
st.write("---")

# ---------------------
# TRIVIA QUESTIONS
# ---------------------
trivia_questions = [
    {
        "type": "multiple_choice",
        "question": "This famous tango composed in Uruguay in 1916 is called...",
        "options": ["El Choclo", "Por una cabeza", "La Cumparsita", "Libertango"],
        "answer": "La Cumparsita",
        "image": "https://i.ytimg.com/vi/I2kbPVQDlvM/maxresdefault.jpg"
    },
    {
        "type": "true_false",
        "question": "Amapiano is a subgenre of house music that incorporates piano, jazz, and distinctive basslines. It originated from South Africa in the 2010s.",
        "answer": "True",
        "image": "https://cms.forbesafrica.com/wp-content/uploads/2021/10/Screenshot-2021-10-22-at-14.32.24-1.png"
    },
    {
        "type": "multiple_choice",
        "question": "In Indonesia, gamelan orchestras primarily feature which type of instruments?",
        "options": ["String instruments", "Metallic instruments", "Brass instruments", "Wind instruments"],
        "answer": "Metallic instruments",
        "image": "https://study.com/cimages/multimages/16/gamelan-orchester_ethnm_berlin949695582522616000.jpg"
    },
    {
        "type": "true_false",
        "question": "Famous Bulgarian composer Pancho Vladigerov is best known for his work 'Balkan Suites'.",
        "answer": "False",
        "image": "https://operasofia.bg/uploads/people/1814.png?_=1733060649"
    },
    {
        "type": "multiple_choice",
        "question": "Which Brazilian genre is characterized by a blend of samba and smooth jazz rhythms.",
        "options": ["Bossa Nova", "Reggaeton", "Sertanejo", "Choro"],
        "answer": "Bossa Nova",
        "image": "https://static01.nyt.com/images/2013/07/14/travel/14PURSUITS7/14PURSUITS7-articleLarge.jpg?quality=75&auto=webp&disable=upscale"
    },
    {
        "type": "true_false",
        "question": "Italian composer Claudio Monteverdi is known as the 'Father of Opera'.",
        "answer": "False",
        "image": "https://www.kennedy-center.org/link/8851036a87e2480e921ef2c4580d3e33.aspx"
    },
    {
        "type": "multiple_choice",
        "question": "Which Lebanese artist is famous for songs like 'Enta Tani' and 'Woseltelha'?",
        "options": ["Elissa", "Fairuz", "Nancu Ajram", "Haifa Wehbe"],
        "answer": "Haifa Wehbe",
        "image": "https://viberate-upload.ams3.cdn.digitaloceanspaces.com/prod/entity/artist/haifa-wehbe-8xk0u"
    },
    {
        "type": "true_false",
        "question": "'Kafi' is a classical Sufi poetic form set to music in the Sindh and Punjab region.",
        "answer": "True",
        "image": "https://i.tribune.com.pk/media/images/649674-muic-1387836794/649674-muic-1387836794.jpg"
    },
    {
        "type": "multiple_choice",
        "question": "'Ndombolo' is a Congolese subgenre of dance music from which African music style?",
        "options": ["Soukous", "Mbalax", "Taarab", "Afrobeats"],
        "answer": "Soukous",
        "image": "https://culturalvibrancy.org/wp-content/uploads/2023/05/Champe-Soukous-Collective.jpg"
    },
    {
        "type": "true_false",
        "question": "A corrido is a traditional narrative ballad song style that tells stories about heroes, history, and social events.",
        "answer": "True",
        "image": "https://static.standard.co.uk/2024/02/01/8/53/corridos-tumbados-2%20%281%29.jpg?crop=8:5,smart&quality=75&auto=webp&width=1000"
    },
    {
        "type": "multiple_choice",
        "question": "Taqsim is a type of...",
        "options": ["Vocal chant", "Improvised instrumental solo", "Music instrument", "Classical music genre"],
        "answer": "Metallic instruments",
        "image": "https://study.com/cimages/multimages/16/gamelan-orchester_ethnm_berlin949695582522616000.jpg"
    }
]

# ---------------------
# SESSION STATE SETUP
# ---------------------
if "question_index" not in st.session_state:
    st.session_state.question_index = random.randint(0, len(trivia_questions) - 1)
if "answered" not in st.session_state:
    st.session_state.answered = False
if "user_answer" not in st.session_state:
    st.session_state.user_answer = None
if "question_key" not in st.session_state:
    st.session_state.question_key = 0  # for unique widget keys

# ---------------------
# HELPER FUNCTION
# ---------------------
def load_new_question():
    previous = st.session_state.question_index
    choices = [i for i in range(len(trivia_questions)) if i != previous]
    st.session_state.question_index = random.choice(choices)
    st.session_state.answered = False
    st.session_state.user_answer = None
    st.session_state.question_key += 1
    st.rerun()


# ---------------------
# GET CURRENT QUESTION
# ---------------------
question = trivia_questions[st.session_state.question_index]

# ---------------------
# DISPLAY QUESTION
# ---------------------
st.image(question["image"], use_container_width=True)
st.markdown(f"### {question['question']}")

# ---------------------
# ANSWER INPUT
# ---------------------
if question["type"] == "multiple_choice":
    st.session_state.user_answer = st.radio(
        "Choose your answer:",
        question["options"],
        key=f"radio_{st.session_state.question_key}"
    )
else:
    st.session_state.user_answer = st.radio(
        "Choose:",
        ["True", "False"],
        key=f"radio_{st.session_state.question_key}"
    )

# ---------------------
# SUBMIT ANSWER
# ---------------------
if st.button("Submit Answer", disabled=st.session_state.answered, key=f"submit_{st.session_state.question_key}"):
    st.session_state.answered = True
    st.rerun()

# ---------------------
# FEEDBACK SECTION
# ---------------------
if st.session_state.answered:
    correct = st.session_state.user_answer == question["answer"]
    if correct:
        st.success(f"✅ Correct! The answer is **{question['answer']}**.")
    else:
        st.error(f"❌ Incorrect. The correct answer is **{question['answer']}**.")

    # Next Question button (now always works instantly)
    if st.button("Next Question", key=f"next_{st.session_state.question_key}"):
        load_new_question()






