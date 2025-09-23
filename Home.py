import streamlit as st
#streamlit run Home.py
st.set_page_config(page_title="About Us", layout="centered")

st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("About Us")
st.write("This app is created by the World Music Foundation to share music and uplift local businesses.")


st.markdown("---")
with st.expander("Our purpose"):
    st.write("The World Music Foundation is a 501(c)(3) non-profit organization dedicated to a simple mission: opening minds through Music. We believe, and research shows, that experiencing music of other cultures increases tolerance and cultural empathy in people, and everything that we do is based on effecting this social change. Racism continues to be one of the world’s greatest problems and Music is a proven armament in this fight.")
