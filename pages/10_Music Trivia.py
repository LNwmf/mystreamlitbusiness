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

# Randomly select one question
question = random.choice(trivia_questions)

# ---------------------
# DISPLAY QUESTION
# ---------------------
st.image(question["image"], use_container_width=True)
st.markdown(f"### {question['question']}")

# ---------------------
# MULTIPLE CHOICE TYPE
# ---------------------
if question["type"] == "multiple_choice":
    user_answer = st.radio("Choose your answer:", question["options"])

# ---------------------
# TRUE/FALSE TYPE
# ---------------------
elif question["type"] == "true_false":
    user_answer = st.radio("Choose:", ["True", "False"])

# ---------------------
# CHECK ANSWER
# ---------------------
if st.button("Submit Answer"):
    if user_answer == question["answer"]:
        st.success("✅ Correct! You really know your music!")
    else:
        st.error(f"❌ Nope! The correct answer was **{question['answer']}**.")

st.write("---")
st.caption("Created with ❤️ using Streamlit")

