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
        "question": "Who is known as the 'King of Pop'?",
        "options": ["Elvis Presley", "Michael Jackson", "Prince", "Freddie Mercury"],
        "answer": "Michael Jackson",
        "image": "https://upload.wikimedia.org/wikipedia/commons/7/72/Michael_Jackson_in_1988.jpg"
    },
    {
        "type": "true_false",
        "question": "The Beatles were originally from London.",
        "answer": "False",
        "image": "https://upload.wikimedia.org/wikipedia/commons/0/0d/The_Fabs.JPG"
    },
    {
        "type": "multiple_choice",
        "question": "Which artist released the album '1989'?",
        "options": ["Adele", "Taylor Swift", "Katy Perry", "Lorde"],
        "answer": "Taylor Swift",
        "image": "https://upload.wikimedia.org/wikipedia/en/f/f6/Taylor_Swift_-_1989.png"
    },
    {
        "type": "true_false",
        "question": "Beethoven was completely deaf when he composed his Ninth Symphony.",
        "answer": "True",
        "image": "https://upload.wikimedia.org/wikipedia/commons/6/6f/Beethoven.jpg"
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

# ---------------------
# HELPER FUNCTION
# ---------------------
def load_new_question():
    st.session_state.question_index = random.randint(0, len(trivia_questions) - 1)
    st.session_state.answered = False
    st.session_state.user_answer = None
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
        key=f"radio_{st.session_state.question_index}"
    )

elif question["type"] == "true_false":
    st.session_state.user_answer = st.radio(
        "Choose:",
        ["True", "False"],
        key=f"radio_{st.session_state.question_index}"
    )

# ---------------------
# SUBMIT ANSWER
# ---------------------
if st.button("Submit Answer", disabled=st.session_state.answered):
    st.session_state.answered = True
    st.rerun()  # Forces the display to refresh and show feedback

# ---------------------
# FEEDBACK SECTION
# ---------------------
if st.session_state.answered:
    correct = st.session_state.user_answer == question["answer"]
    if correct:
        st.success(f"✅ Correct! The answer is **{question['answer']}**.")
    else:
        st.error(f"❌ Incorrect. The correct answer is **{question['answer']}**.")

    # "Next Question" button now properly loads a new one
    if st.button("Next Question"):
        load_new_question()

st.write("---")
st.caption("Created with ❤️ using Streamlit")




