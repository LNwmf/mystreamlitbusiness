import streamlit as st

st.title("Image Display based on Radio Selection")

selected_option = st.radio(
    "Choose an image:",
    options=["Image A", "Image B", "Image C"]
)

if selected_option == "Image A":
    st.image("image1.png", caption="This is Image A")
elif selected_option == "Image B":
    st.image("image2.png", caption="This is Image B")
elif selected_option == "Image C":
    st.image("image3.png", caption="This is Image C")