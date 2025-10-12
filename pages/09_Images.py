import builtins
print("Is str still built-in?", builtins.str is str)



import streamlit as st

birria = "https://i.imgur.com/3ACcDlF.jpeg"
st.image(birria, caption="Birria tacos", width=200)

pasta = "https://i.imgur.com/8wTBiHb.jpeg"
st.image(pasta, caption="Pasta", width=200)

burger = "https://i.imgur.com/y0Ezg5M.jpeg"
st.image(burger, caption="Burger", width=200)

ice_cream = "https://i.imgur.com/QDmOxZ8.jpeg"
st.image(ice_cream, caption="Ice cream", width=200)

taiyaki = "https://i.imgur.com/CNre03d.jpeg"
st.image(taiyaki, caption="Taiyaki", width=200)

#GIF
dancingcat = "https://i.imgur.com/J7O2RSz.gif"
st.image(dancingcat, caption="Dancing cat", width=200)

#video w/ audio
video_url = "https://i.imgur.com/6qioN0t.mp4"

st.video(video_url, width=300)

guess = ["Piano", "Trumpet", "Guitar", "Clarinet"]
selected_one = st.radio("Guess the instrument:", guess, index=None)

