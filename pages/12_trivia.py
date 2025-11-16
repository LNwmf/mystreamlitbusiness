import streamlit as st

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
        "question": "Which Brazilian genre is characterized by a blend of samba and smooth jazz rhythms?",
        "options": ["Bossa Nova", "Reggaeton", "Sertanejo", "Choro"],
        "answer": "Bossa Nova",
        "image": "https://static01.nyt.com/images/2013/07/14/travel/14PURSUITS7/14PURSUITS7-articleLarge.jpg?quality=75&auto=webp&disable=upscale"
    },
    {
        "type": "multiple_choice",
        "question": "Which Lebanese artist is famous for songs like 'Enta Tani' and 'Woseltelha'?",
        "options": ["Elissa", "Fairuz", "Nancy Ajram", "Haifa Wehbe"],
        "answer": "Haifa Wehbe",
        "image": "https://viberate-upload.ams3.cdn.digitaloceanspaces.com/prod/entity/artist/haifa-wehbe-8xk0u"
    },
    {
        "type": "true_false",
        "question": "'Kafi' is a classical Sufi poetic form set to music in the Sindh and Punjab region.",
        "answer": "True",
        "image": "https://i.tribune.com.pk/media/images/649674-muic-1387836794/649674-muic-1387836794.jpg"
    },
]

# ---------------------
# SESSION STATE SETUP
# ---------------------
if "question_index" not in st.session_state:
    st.session_state.question_index = 0
if "answered" not in st.session_state:
    st.session_state.answered = False
if "user_answer" not in st.session_state:
    st.session_state.user_answer = None
if "question_key" not in st.session_state:
    st.session_state.question_key = 0
if "score" not in st.session_state:
    st.session_state.score = 0

# ---------------------
# RESTART QUIZ FUNCTION
# ---------------------
def restart_quiz():
    st.session_state.question_index = 0
    st.session_state.answered = False
    st.session_state.user_answer = None
    st.session_state.question_key = 0
    st.session_state.score = 0

# ---------------------
# CHECK IF QUIZ IS FINISHED
# ---------------------
if st.session_state.question_index >= len(trivia_questions):
    st.success(f"🎉 You completed the quiz! Your final score is **{st.session_state.score} / {len(trivia_questions)}**.")
    if st.button("Restart Quiz"):
        restart_quiz()
        st.experimental_rerun()
else:
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
        # Check if correct and increment score
        if st.session_state.user_answer == question["answer"]:
            st.session_state.score += 1
        st.experimental_rerun()

    # ---------------------
    # FEEDBACK SECTION
    # ---------------------
    if st.session_state.answered:
        correct = st.session_state.user_answer == question["answer"]
        if correct:
            st.success(f"✅ Correct! The answer is **{question['answer']}**.")
        else:
            st.error(f"❌ Incorrect. The correct answer is **{question['answer']}**.")

        # Next Question button
        if st.button("Next Question", key=f"next_{st.session_state.question_key}"):
            st.session_state.question_index += 1
            st.session_state.answered = False
            st.session_state.user_answer = None
            st.session_state.question_key += 1
            st.experimental_rerun()
