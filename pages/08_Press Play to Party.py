import streamlit as st
from st_clickable_images import clickable_images

st.set_page_config(
    page_title="Press Play to Party",
    page_icon="🎉",
    layout="centered",
)

st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("🎉 Press Play to Party")
st.markdown("""
Welcome! Pick an energy below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
""")
st.write("")

#Q1: clickable images
st.write("Pick a classic party food:")
images = [

        "https://assets.surlatable.com/m/15a89c2d9c6c1345/72_dpi_webp-REC-283110_Pizza.jpg", #pizza, salsa and chips, chicken wings, burger, hot dog
        "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2013/12/9/0/FNK_Salsa-and-Chips_s4x3.jpg.rend.hgtvcom.1280.1280.suffix/1387411410179.webp",
        "https://tastesbetterfromscratch.com/wp-content/uploads/2014/09/Baked-Chicken-Wings-3.jpg",
        "https://static01.nyt.com/images/2022/06/27/dining/kc-mushroom-beef-burgers/merlin_209008674_b3fa58fa-9bb1-4cfe-a08a-40b4dda0de78-jumbo.jpg",
        "https://www.foodandwine.com/thmb/2kinp7BXi4eE-QG8u1rLS3z_o5M=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Hawaiian-Hot-Dog-FT-RECIPE0724-8b45189237284cf5bf8efb1e8ea9626c.jpeg",
]

titles=["Pizza", "Salsa & chips", "Chicken wings", "Burger", "Hot dog"]

clicked = clickable_images(
    images,
    titles=titles,
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
)

if clicked > -1:
    st.markdown(f"**{titles[clicked]}** selected")
else:
    st.markdown("No image clicked")

#Q2


#st.title("Image Display based on Radio Selection")

#selected_option = st.radio(
#    "Choose an image:",
#    options=["Image A", "Image B", "Image C"]
#)

#if selected_option == "Image A":
#    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJvbABjR5D8Ja6B51Y55dbqqL0VMW85XdV6w&s", caption="This is Image A")
#elif selected_option == "Image B":
#    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwBNHTvWu7XJyqeE2yDf3n4ezQAHThGfxjeQ&s", caption="This is Image B")
#elif selected_option == "Image C":
#    st.image("https://sylviawakana.com/wp-content/uploads/2022/07/Taiyaki-1.jpg", caption="This is Image C")

#clickable images