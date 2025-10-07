import streamlit as st
from st_clickable_images import clickable_images

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

#clickable images

clicked = clickable_images(
    [
        "https://www.thefoodinmybeard.com/content/taco/whitepeople/wpt10.jpg",
        "https://www.allrecipes.com/thmb/OJ28fIFte6Pyg93ML8IM-APbu1Y=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/AR-14554-sirloin-steak-with-garlic-butter-hero-4x3-d12fa79836754fcf850388e4677bbf55.jpg",
        "https://www.recipetineats.com/tachyon/2022/09/Crispy-Fries_8.jpg?resize=500%2C500",
        "https://www.barleyandsage.com/wp-content/uploads/2022/03/buttermilk-chicken-tenders-1200x1200-1.jpg",
        "https://www.budgetbytes.com/wp-content/uploads/2020/05/CreamyTomatoSpinachPasta_OverheadPlated.jpg",
    ],
    #titles=[f"{str(i)}" for i in range(5)],
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
)

#st.markdown(f"{clicked}" if clicked > -1 else "No image clicked")