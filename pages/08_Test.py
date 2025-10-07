import streamlit as st

st.title("Image Display based on Radio Selection")

selected_option = st.radio(
    "Choose an image:",
    options=["Image A", "Image B", "Image C"]
)

if selected_option == "Image A":
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJvbABjR5D8Ja6B51Y55dbqqL0VMW85XdV6w&s", caption="This is Image A")
elif selected_option == "Image B":
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwBNHTvWu7XJyqeE2yDf3n4ezQAHThGfxjeQ&s", caption="This is Image B")
elif selected_option == "Image C":
    st.image("https://sylviawakana.com/wp-content/uploads/2022/07/Taiyaki-1.jpg", caption="This is Image C")