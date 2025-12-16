import streamlit as st

st.set_page_config(
    page_title="Sweet Melodies",
    page_icon="🍬",
    layout="centered",
)

st.markdown(
    """
    <style>
    img {
        border-radius: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)

st.title("🍬 Sweet Melodies")
st.markdown("""
Welcome! Pick a dessert below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
""")

#Q1
st.write("Select a flavor: (double-click button)")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/chocolate.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/vanilla.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/strawberry.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/coffee.jpeg",
]

titles=["Chocolate", "Vanilla", "Strawberry", "Coffee"]

if "selected_flavor" not in st.session_state:
    st.session_state.selected_flavor = None

cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        # Clicking the button selects this image
        if st.button(titles[i], key=f"btn_flavor_{i}"):
            st.session_state.selected_flavor = i

        # Add a red border if selected
        border = "4px solid red" if st.session_state.selected_flavor == i else "4px solid transparent"

        st.markdown(
            f"""
            <div style="
                border:{border};
                border-radius:10px;
                padding:3px;
                display:flex;
                justify-content:center;
            ">
                <img src="{images[i]}" style="width:170px; border-radius:10px;">
            </div>
            """,
            unsafe_allow_html=True,
        )

selected_flavor = (
    titles[st.session_state.selected_flavor]
    if st.session_state.get("selected_flavor") is not None
    else None
)

#gap
st.write("")

#Q2
time_options = ["After a morning run", "Late night cravings", "During special occasions", "All day, everyday"]
selected_time = st.selectbox("Best time to have dessert:", time_options, index=None)

#Q3
life_options = ["Layers of experience", "Bittersweet spices", "A tough shell but soft center", "Unexpected textures"]
selected_life = st.selectbox("If your life were a dessert, what would it be made of?", life_options, index=None)

#Q4
st.write("What season defines you? (double-click button)")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/summer.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/winter.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/spring.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/autumn.jpg",
]

titles=["Summer", "Winter", "Spring", "Autumn"]

if "selected_season" not in st.session_state:
    st.session_state.selected_season = None

cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        # Clicking the button selects this image
        if st.button(titles[i], key=f"btn_season_{i}"):
            st.session_state.selected_season = i

        # Add a red border if selected
        border = "4px solid red" if st.session_state.selected_season == i else "4px solid transparent"

        st.markdown(
            f"""
            <div style="
                border:{border};
                border-radius:10px;
                padding:3px;
                display:flex;
                justify-content:center;
            ">
                <img src="{images[i]}" style="width:170px; border-radius:10px;">
            </div>
            """,
            unsafe_allow_html=True,
        )

selected_season = (
    titles[st.session_state.selected_season]
    if st.session_state.get("selected_season") is not None
    else None
)
#gap
st.write("")

# Business options and related data
dessert_data = {
    "Flan": {
        "playlist": "Dancing Jelly",
        "playlist_link": "https://open.spotify.com/playlist/6fYffbVT904xvzDT6irTdU?si=csdoxPo9RY-xZi1GFCHWug",
#        "business_name": "El Rincón de Fabio",
#        "location": "1002 W Argyle St, Chicago, IL 60640",
#        "website": "https://elrincondefabiollc.net/",
#        "business_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/elrincondefabio.png",
    },
    "Souffle": {
    "playlist": "Pastries & Strings",
    "playlist_link": "https://open.spotify.com/playlist/6Q3HvhgG8wMriOzsskGGKe?si=h210zMrdQ5WUDDQqDvL8uQ",
#    "business_name": "BUREK SHOP 3M Restaurant",
#    "location": "5910 N Clark St, Chicago, IL 60660",
#    "website": "https://3mrestaurant.com/",
#    "business_image": "https://3mrestaurant.com/wp-content/uploads/2023/02/3M-LOGO.png",
    },
    "Taiyaki": {
    "playlist": "Chill J-Rock",
    "playlist_link": "https://open.spotify.com/playlist/6bwKvzWbyYgjILrBZctfXC?si=6eTaIJ0HRHGffHBs6YX56g",
#    "business_name": "Sayuri Sushi Bar",
#    "location": "1553 W Devon Ave, Chicago, IL 60660",
#    "website": "https://sayurichicago.com/",
#    "business_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/sayurisushi.jpeg"
    },
    "Mandazi": {
    "playlist": "Bongo Flava Blends",
    "playlist_link": "https://open.spotify.com/playlist/1mg4qAKKFiOYuelShVU1z0?si=EqYt0bVVTfGGy6QI8FHnAA",
#    "business_name": "Afro Taste Cuisine",
#    "location": "1010 W Argyle St, Chicago, IL 60640",
#    "website": "https://www.afrotastecuisine.com/",
#    "business_image": "https://ik.imagekit.io/awwybhhmo/assets/favicons/African/botanic__1_.svg?tr="
    },
}

info = None
    # Dessert Selection
dessert_choice = st.selectbox("Pick a dessert!", ["", *dessert_data.keys()])

dessert_map = {
    # Chocolate #
    ("Chocolate", "After a morning run", "Layers of experience", "Summer"): "Taiyaki",
    ("Chocolate", "After a morning run", "Layers of experience", "Winter"): "Souffle",
    ("Chocolate", "After a morning run", "Layers of experience", "Spring"): "Mandazi",
    ("Chocolate", "After a morning run", "Layers of experience", "Autumn"): "Taiyaki",
    ("Chocolate", "After a morning run", "Bittersweet spices", "Summer"): "Flan",
    ("Chocolate", "After a morning run", "Bittersweet spices", "Winter"): "Souffle",
    ("Chocolate", "After a morning run", "Bittersweet spices", "Spring"): "Mandazi",
    ("Chocolate", "After a morning run", "Bittersweet spices", "Autumn"): "Mandazi",
    ("Chocolate", "After a morning run", "A tough shell but soft center", "Summer"): "Mandazi",
    ("Chocolate", "After a morning run", "A tough shell but soft center", "Winter"): "Souffle",
    ("Chocolate", "After a morning run", "A tough shell but soft center", "Spring"): "Mandazi",
    ("Chocolate", "After a morning run", "A tough shell but soft center", "Autumn"): "Flan",
    ("Chocolate", "After a morning run", "Unexpected textures", "Summer"): "Taiyaki",
    ("Chocolate", "After a morning run", "Unexpected textures", "Winter"): "Flan",
    ("Chocolate", "After a morning run", "Unexpected textures", "Spring"): "Taiyaki",
    ("Chocolate", "After a morning run", "Unexpected textures", "Autumn"): "Souffle",
    ("Chocolate", "Late night cravings", "Layers of experience", "Summer"): "Flan",
    ("Chocolate", "Late night cravings", "Layers of experience", "Winter"): "Souffle",
    ("Chocolate", "Late night cravings", "Layers of experience", "Spring"): "Souffle",
    ("Chocolate", "Late night cravings", "Layers of experience", "Autumn"): "Mandazi",
    ("Chocolate", "Late night cravings", "Bittersweet spices", "Summer"): "Mandazi",
    ("Chocolate", "Late night cravings", "Bittersweet spices", "Winter"): "Flan",
    ("Chocolate", "Late night cravings", "Bittersweet spices", "Spring"): "Flan",
    ("Chocolate", "Late night cravings", "Bittersweet spices", "Autumn"): "Mandazi",
    ("Chocolate", "Late night cravings", "A tough shell but soft center", "Summer"): "Souffle",
    ("Chocolate", "Late night cravings", "A tough shell but soft center", "Winter"): "Taiyaki",
    ("Chocolate", "Late night cravings", "A tough shell but soft center", "Spring"): "Flan",
    ("Chocolate", "Late night cravings", "A tough shell but soft center", "Autumn"): "Taiyaki",
    ("Chocolate", "Late night cravings", "Unexpected textures", "Summer"): "Flan",
    ("Chocolate", "Late night cravings", "Unexpected textures", "Winter"): "Mandazi",
    ("Chocolate", "Late night cravings", "Unexpected textures", "Spring"): "Souffle",
    ("Chocolate", "Late night cravings", "Unexpected textures", "Autumn"): "Taiyaki",
    ("Chocolate", "During special occasions", "Layers of experience", "Summer"): "Flan",
    ("Chocolate", "During special occasions", "Layers of experience", "Winter"): "Taiyaki",
    ("Chocolate", "During special occasions", "Layers of experience", "Spring"): "Flan",
    ("Chocolate", "During special occasions", "Layers of experience", "Autumn"): "Taiyaki",
    ("Chocolate", "During special occasions", "Bittersweet spices", "Summer"): "Flan",
    ("Chocolate", "During special occasions", "Bittersweet spices", "Winter"): "Mandazi",
    ("Chocolate", "During special occasions", "Bittersweet spices", "Spring"): "Flan",
    ("Chocolate", "During special occasions", "Bittersweet spices", "Autumn"): "Souffle",
    ("Chocolate", "During special occasions", "A tough shell but soft center", "Summer"): "Souffle",
    ("Chocolate", "During special occasions", "A tough shell but soft center", "Winter"): "Taiyaki",
    ("Chocolate", "During special occasions", "A tough shell but soft center", "Spring"): "Taiyaki",
    ("Chocolate", "During special occasions", "A tough shell but soft center", "Autumn"): "Flan",
    ("Chocolate", "During special occasions", "Unexpected textures", "Summer"): "Flan",
    ("Chocolate", "During special occasions", "Unexpected textures", "Winter"): "Souffle",
    ("Chocolate", "During special occasions", "Unexpected textures", "Spring"): "Flan",
    ("Chocolate", "During special occasions", "Unexpected textures", "Autumn"): "Mandazi",
    ("Chocolate", "All day, everyday", "Layers of experience", "Summer"): "Souffle",
    ("Chocolate", "All day, everyday", "Layers of experience", "Winter"): "Flan",
    ("Chocolate", "All day, everyday", "Layers of experience", "Spring"): "Flan",
    ("Chocolate", "All day, everyday", "Layers of experience", "Autumn"): "Mandazi",
    ("Chocolate", "All day, everyday", "Bittersweet spices", "Summer"): "Flan",
    ("Chocolate", "All day, everyday", "Bittersweet spices", "Winter"): "Taiyaki",
    ("Chocolate", "All day, everyday", "Bittersweet spices", "Spring"): "Taiyaki",
    ("Chocolate", "All day, everyday", "Bittersweet spices", "Autumn"): "Mandazi",
    ("Chocolate", "All day, everyday", "A tough shell but soft center", "Summer"): "Mandazi",
    ("Chocolate", "All day, everyday", "A tough shell but soft center", "Winter"): "Mandazi",
    ("Chocolate", "All day, everyday", "A tough shell but soft center", "Spring"): "Taiyaki",
    ("Chocolate", "All day, everyday", "A tough shell but soft center", "Autumn"): "Taiyaki",
    ("Chocolate", "All day, everyday", "Unexpected textures", "Summer"): "Souffle",
    ("Chocolate", "All day, everyday", "Unexpected textures", "Winter"): "Flan",
    ("Chocolate", "All day, everyday", "Unexpected textures", "Spring"): "Souffle",
    ("Chocolate", "All day, everyday", "Unexpected textures", "Autumn"): "Flan",

    # Vanilla #

    ("Vanilla", "After a morning run", "Layers of experience", "Summer"): "Flan",
    ("Vanilla", "After a morning run", "Layers of experience", "Winter"): "Souffle",
    ("Vanilla", "After a morning run", "Layers of experience", "Spring"): "Taiyaki",
    ("Vanilla", "After a morning run", "Layers of experience", "Autumn"): "Mandazi",
    ("Vanilla", "After a morning run", "Bittersweet spices", "Summer"): "Mandazi",
    ("Vanilla", "After a morning run", "Bittersweet spices", "Winter"): "Flan",
    ("Vanilla", "After a morning run", "Bittersweet spices", "Spring"): "Flan",
    ("Vanilla", "After a morning run", "Bittersweet spices", "Autumn"): "Mandazi",
    ("Vanilla", "After a morning run", "A tough shell but soft center", "Summer"): "Flan",
    ("Vanilla", "After a morning run", "A tough shell but soft center", "Winter"): "Mandazi",
    ("Vanilla", "After a morning run", "A tough shell but soft center", "Spring"): "Taiyaki",
    ("Vanilla", "After a morning run", "A tough shell but soft center", "Autumn"): "Souffle",
    ("Vanilla", "After a morning run", "Unexpected textures", "Summer"): "Taiyaki",
    ("Vanilla", "After a morning run", "Unexpected textures", "Winter"): "Flan",
    ("Vanilla", "After a morning run", "Unexpected textures", "Spring"): "Flan",
    ("Vanilla", "After a morning run", "Unexpected textures", "Autumn"): "Flan",
    ("Vanilla", "Late night cravings", "Layers of experience", "Summer"): "Souffle",
    ("Vanilla", "Late night cravings", "Layers of experience", "Winter"): "Taiyaki",
    ("Vanilla", "Late night cravings", "Layers of experience", "Spring"): "Taiyaki",
    ("Vanilla", "Late night cravings", "Layers of experience", "Autumn"): "Souffle",
    ("Vanilla", "Late night cravings", "Bittersweet spices", "Summer"): "Taiyaki",
    ("Vanilla", "Late night cravings", "Bittersweet spices", "Winter"): "Mandazi",
    ("Vanilla", "Late night cravings", "Bittersweet spices", "Spring"): "Taiyaki",
    ("Vanilla", "Late night cravings", "Bittersweet spices", "Autumn"): "Mandazi",
    ("Vanilla", "Late night cravings", "A tough shell but soft center", "Summer"): "Taiyaki",
    ("Vanilla", "Late night cravings", "A tough shell but soft center", "Winter"): "Flan",
    ("Vanilla", "Late night cravings", "A tough shell but soft center", "Spring"): "Souffle",
    ("Vanilla", "Late night cravings", "A tough shell but soft center", "Autumn"): "Souffle",
    ("Vanilla", "Late night cravings", "Unexpected textures", "Summer"): "Taiyaki",
    ("Vanilla", "Late night cravings", "Unexpected textures", "Winter"): "Flan",
    ("Vanilla", "Late night cravings", "Unexpected textures", "Spring"): "Taiyaki",
    ("Vanilla", "Late night cravings", "Unexpected textures", "Autumn"): "Flan",
    ("Vanilla", "During special occasions", "Layers of experience", "Summer"): "Mandazi",
    ("Vanilla", "During special occasions", "Layers of experience", "Winter"): "Flan",
    ("Vanilla", "During special occasions", "Layers of experience", "Spring"): "Flan",
    ("Vanilla", "During special occasions", "Layers of experience", "Autumn"): "Souffle",
    ("Vanilla", "During special occasions", "Bittersweet spices", "Summer"): "Souffle",
    ("Vanilla", "During special occasions", "Bittersweet spices", "Winter"): "Souffle",
    ("Vanilla", "During special occasions", "Bittersweet spices", "Spring"): "Mandazi",
    ("Vanilla", "During special occasions", "Bittersweet spices", "Autumn"): "Mandazi",
    ("Vanilla", "During special occasions", "A tough shell but soft center", "Summer"): "Souffle",
    ("Vanilla", "During special occasions", "A tough shell but soft center", "Winter"): "Taiyaki",
    ("Vanilla", "During special occasions", "A tough shell but soft center", "Spring"): "Taiyaki",
    ("Vanilla", "During special occasions", "A tough shell but soft center", "Autumn"): "Flan",
    ("Vanilla", "During special occasions", "Unexpected textures", "Summer"): "Souffle",
    ("Vanilla", "During special occasions", "Unexpected textures", "Winter"): "Mandazi",
    ("Vanilla", "During special occasions", "Unexpected textures", "Spring"): "Mandazi",
    ("Vanilla", "During special occasions", "Unexpected textures", "Autumn"): "Taiyaki",
    ("Vanilla", "All day, everyday", "Layers of experience", "Summer"): "Souffle",
    ("Vanilla", "All day, everyday", "Layers of experience", "Winter"): "Souffle",
    ("Vanilla", "All day, everyday", "Layers of experience", "Spring"): "Flan",
    ("Vanilla", "All day, everyday", "Layers of experience", "Autumn"): "Taiyaki",
    ("Vanilla", "All day, everyday", "Bittersweet spices", "Summer"): "Mandazi",
    ("Vanilla", "All day, everyday", "Bittersweet spices", "Winter"): "Taiyaki",
    ("Vanilla", "All day, everyday", "Bittersweet spices", "Spring"): "Mandazi",
    ("Vanilla", "All day, everyday", "Bittersweet spices", "Autumn"): "Taiyaki",
    ("Vanilla", "All day, everyday", "A tough shell but soft center", "Summer"): "Flan",
    ("Vanilla", "All day, everyday", "A tough shell but soft center", "Winter"): "Mandazi",
    ("Vanilla", "All day, everyday", "A tough shell but soft center", "Spring"): "Mandazi",
    ("Vanilla", "All day, everyday", "A tough shell but soft center", "Autumn"): "Flan",
    ("Vanilla", "All day, everyday", "Unexpected textures", "Summer"): "Souffle",
    ("Vanilla", "All day, everyday", "Unexpected textures", "Winter"): "Taiyaki",
    ("Vanilla", "All day, everyday", "Unexpected textures", "Spring"): "Taiyaki",
    ("Vanilla", "All day, everyday", "Unexpected textures", "Autumn"): "Souffle",

    # Strawberry #

    ("Strawberry", "After a morning run", "Layers of experience", "Summer"): "Taiyaki",
    ("Strawberry", "After a morning run", "Layers of experience", "Winter"): "Taiyaki",
    ("Strawberry", "After a morning run", "Layers of experience", "Spring"): "Flan",
    ("Strawberry", "After a morning run", "Layers of experience", "Autumn"): "Flan",
    ("Strawberry", "After a morning run", "Bittersweet spices", "Summer"): "Mandazi",
    ("Strawberry", "After a morning run", "Bittersweet spices", "Winter"): "Flan",
    ("Strawberry", "After a morning run", "Bittersweet spices", "Spring"): "Mandazi",
    ("Strawberry", "After a morning run", "Bittersweet spices", "Autumn"): "Souffle",
    ("Strawberry", "After a morning run", "A tough shell but soft center", "Summer"): "Taiyaki",
    ("Strawberry", "After a morning run", "A tough shell but soft center", "Winter"): "Taiyaki",
    ("Strawberry", "After a morning run", "A tough shell but soft center", "Spring"): "Flan",
    ("Strawberry", "After a morning run", "A tough shell but soft center", "Autumn"): "Souffle",
    ("Strawberry", "After a morning run", "Unexpected textures", "Summer"): "Taiyaki",
    ("Strawberry", "After a morning run", "Unexpected textures", "Winter"): "Flan",
    ("Strawberry", "After a morning run", "Unexpected textures", "Spring"): "Flan",
    ("Strawberry", "After a morning run", "Unexpected textures", "Autumn"): "Mandazi",
    ("Strawberry", "Late night cravings", "Layers of experience", "Summer"): "Taiyaki",
    ("Strawberry", "Late night cravings", "Layers of experience", "Winter"): "Mandazi",
    ("Strawberry", "Late night cravings", "Layers of experience", "Spring"): "Mandazi",
    ("Strawberry", "Late night cravings", "Layers of experience", "Autumn"): "Mandazi",
    ("Strawberry", "Late night cravings", "Bittersweet spices", "Summer"): "Souffle",
    ("Strawberry", "Late night cravings", "Bittersweet spices", "Winter"): "Souffle",
    ("Strawberry", "Late night cravings", "Bittersweet spices", "Spring"): "Flan",
    ("Strawberry", "Late night cravings", "Bittersweet spices", "Autumn"): "Mandazi",
    ("Strawberry", "Late night cravings", "A tough shell but soft center", "Summer"): "Souffle",
    ("Strawberry", "Late night cravings", "A tough shell but soft center", "Winter"): "Taiyaki",
    ("Strawberry", "Late night cravings", "A tough shell but soft center", "Spring"): "Souffle",
    ("Strawberry", "Late night cravings", "A tough shell but soft center", "Autumn"): "Taiyaki",
    ("Strawberry", "Late night cravings", "Unexpected textures", "Summer"): "Mandazi",
    ("Strawberry", "Late night cravings", "Unexpected textures", "Winter"): "Souffle",
    ("Strawberry", "Late night cravings", "Unexpected textures", "Spring"): "Taiyaki",
    ("Strawberry", "Late night cravings", "Unexpected textures", "Autumn"): "Taiyaki",
    ("Strawberry", "During special occasions", "Layers of experience", "Summer"): "Flan",
    ("Strawberry", "During special occasions", "Layers of experience", "Winter"): "Mandazi",
    ("Strawberry", "During special occasions", "Layers of experience", "Spring"): "Taiyaki",
    ("Strawberry", "During special occasions", "Layers of experience", "Autumn"): "Flan",
    ("Strawberry", "During special occasions", "Bittersweet spices", "Summer"): "Flan",
    ("Strawberry", "During special occasions", "Bittersweet spices", "Winter"): "Souffle",
    ("Strawberry", "During special occasions", "Bittersweet spices", "Spring"): "Mandazi",
    ("Strawberry", "During special occasions", "Bittersweet spices", "Autumn"): "Souffle",
    ("Strawberry", "During special occasions", "A tough shell but soft center", "Summer"): "Taiyaki",
    ("Strawberry", "During special occasions", "A tough shell but soft center", "Winter"): "Taiyaki",
    ("Strawberry", "During special occasions", "A tough shell but soft center", "Spring"): "Flan",
    ("Strawberry", "During special occasions", "A tough shell but soft center", "Autumn"): "Mandazi",
    ("Strawberry", "During special occasions", "Unexpected textures", "Summer"): "Taiyaki",
    ("Strawberry", "During special occasions", "Unexpected textures", "Winter"): "Mandazi",
    ("Strawberry", "During special occasions", "Unexpected textures", "Spring"): "Flan",
    ("Strawberry", "During special occasions", "Unexpected textures", "Autumn"): "Flan",
    ("Strawberry", "All day, everyday", "Layers of experience", "Summer"): "Flan",
    ("Strawberry", "All day, everyday", "Layers of experience", "Winter"): "Taiyaki",
    ("Strawberry", "All day, everyday", "Layers of experience", "Spring"): "Taiyaki",
    ("Strawberry", "All day, everyday", "Layers of experience", "Autumn"): "Mandazi",
    ("Strawberry", "All day, everyday", "Bittersweet spices", "Summer"): "Mandazi",
    ("Strawberry", "All day, everyday", "Bittersweet spices", "Winter"): "Souffle",
    ("Strawberry", "All day, everyday", "Bittersweet spices", "Spring"): "Taiyaki",
    ("Strawberry", "All day, everyday", "Bittersweet spices", "Autumn"): "Mandazi",
    ("Strawberry", "All day, everyday", "A tough shell but soft center", "Summer"): "Mandazi",
    ("Strawberry", "All day, everyday", "A tough shell but soft center", "Winter"): "Taiyaki",
    ("Strawberry", "All day, everyday", "A tough shell but soft center", "Spring"): "Mandazi",
    ("Strawberry", "All day, everyday", "A tough shell but soft center", "Autumn"): "Taiyaki",
    ("Strawberry", "All day, everyday", "Unexpected textures", "Summer"): "Flan",
    ("Strawberry", "All day, everyday", "Unexpected textures", "Winter"): "Souffle",
    ("Strawberry", "All day, everyday", "Unexpected textures", "Spring"): "Souffle",
    ("Strawberry", "All day, everyday", "Unexpected textures", "Autumn"): "Taiyaki",

    # Coffee #

    ("Coffee", "After a morning run", "Layers of experience", "Summer"): "Flan",
    ("Coffee", "After a morning run", "Layers of experience", "Winter"): "Mandazi",
    ("Coffee", "After a morning run", "Layers of experience", "Spring"): "Flan",
    ("Coffee", "After a morning run", "Layers of experience", "Autumn"): "Mandazi",
    ("Coffee", "After a morning run", "Bittersweet spices", "Summer"): "Mandazi",
    ("Coffee", "After a morning run", "Bittersweet spices", "Winter"): "Mandazi",
    ("Coffee", "After a morning run", "Bittersweet spices", "Spring"): "Taiyaki",
    ("Coffee", "After a morning run", "Bittersweet spices", "Autumn"): "Taiyaki",
    ("Coffee", "After a morning run", "A tough shell but soft center", "Summer"): "Taiyaki",
    ("Coffee", "After a morning run", "A tough shell but soft center", "Winter"): "Souffle",
    ("Coffee", "After a morning run", "A tough shell but soft center", "Spring"): "Mandazi",
    ("Coffee", "After a morning run", "A tough shell but soft center", "Autumn"): "Souffle",
    ("Coffee", "After a morning run", "Unexpected textures", "Summer"): "Flan",
    ("Coffee", "After a morning run", "Unexpected textures", "Winter"): "Taiyaki",
    ("Coffee", "After a morning run", "Unexpected textures", "Spring"): "Flan",
    ("Coffee", "After a morning run", "Unexpected textures", "Autumn"): "Mandazi",
    ("Coffee", "Late night cravings", "Layers of experience", "Summer"): "Mandazi",
    ("Coffee", "Late night cravings", "Layers of experience", "Winter"): "Mandazi",
    ("Coffee", "Late night cravings", "Layers of experience", "Spring"): "Flan",
    ("Coffee", "Late night cravings", "Layers of experience", "Autumn"): "Taiyaki",
    ("Coffee", "Late night cravings", "Bittersweet spices", "Summer"): "Souffle",
    ("Coffee", "Late night cravings", "Bittersweet spices", "Winter"): "Taiyaki",
    ("Coffee", "Late night cravings", "Bittersweet spices", "Spring"): "Souffle",
    ("Coffee", "Late night cravings", "Bittersweet spices", "Autumn"): "Mandazi",
    ("Coffee", "Late night cravings", "A tough shell but soft center", "Summer"): "Mandazi",
    ("Coffee", "Late night cravings", "A tough shell but soft center", "Winter"): "Souffle",
    ("Coffee", "Late night cravings", "A tough shell but soft center", "Spring"): "Mandazi",
    ("Coffee", "Late night cravings", "A tough shell but soft center", "Autumn"): "Souffle",
    ("Coffee", "Late night cravings", "Unexpected textures", "Summer"): "Taiyaki",
    ("Coffee", "Late night cravings", "Unexpected textures", "Winter"): "Taiyaki",
    ("Coffee", "Late night cravings", "Unexpected textures", "Spring"): "Mandazi",
    ("Coffee", "Late night cravings", "Unexpected textures", "Autumn"): "Souffle",
    ("Coffee", "During special occasions", "Layers of experience", "Summer"): "Flan",
    ("Coffee", "During special occasions", "Layers of experience", "Winter"): "Flan",
    ("Coffee", "During special occasions", "Layers of experience", "Spring"): "Mandazi",
    ("Coffee", "During special occasions", "Layers of experience", "Autumn"): "Mandazi",
    ("Coffee", "During special occasions", "Bittersweet spices", "Summer"): "Mandazi",
    ("Coffee", "During special occasions", "Bittersweet spices", "Winter"): "Taiyaki",
    ("Coffee", "During special occasions", "Bittersweet spices", "Spring"): "Souffle",
    ("Coffee", "During special occasions", "Bittersweet spices", "Autumn"): "Souffle",
    ("Coffee", "During special occasions", "A tough shell but soft center", "Summer"): "Flan",
    ("Coffee", "During special occasions", "A tough shell but soft center", "Winter"): "Taiyaki",
    ("Coffee", "During special occasions", "A tough shell but soft center", "Spring"): "Flan",
    ("Coffee", "During special occasions", "A tough shell but soft center", "Autumn"): "Mandazi",
    ("Coffee", "During special occasions", "Unexpected textures", "Summer"): "Mandazi",
    ("Coffee", "During special occasions", "Unexpected textures", "Winter"): "Souffle",
    ("Coffee", "During special occasions", "Unexpected textures", "Spring"): "Taiyaki",
    ("Coffee", "During special occasions", "Unexpected textures", "Autumn"): "Souffle",
    ("Coffee", "All day, everyday", "Layers of experience", "Summer"): "Souffle",
    ("Coffee", "All day, everyday", "Layers of experience", "Winter"): "Flan",
    ("Coffee", "All day, everyday", "Layers of experience", "Spring"): "Mandazi",
    ("Coffee", "All day, everyday", "Layers of experience", "Autumn"): "Taiyaki",
    ("Coffee", "All day, everyday", "Bittersweet spices", "Summer"): "Mandazi",
    ("Coffee", "All day, everyday", "Bittersweet spices", "Winter"): "Taiyaki",
    ("Coffee", "All day, everyday", "Bittersweet spices", "Spring"): "Souffle",
    ("Coffee", "All day, everyday", "Bittersweet spices", "Autumn"): "Taiyaki",
    ("Coffee", "All day, everyday", "A tough shell but soft center", "Summer"): "Mandazi",
    ("Coffee", "All day, everyday", "A tough shell but soft center", "Winter"): "Mandazi",
    ("Coffee", "All day, everyday", "A tough shell but soft center", "Spring"): "Souffle",
    ("Coffee", "All day, everyday", "A tough shell but soft center", "Autumn"): "Taiyaki",
    ("Coffee", "All day, everyday", "Unexpected textures", "Summer"): "Souffle",
    ("Coffee", "All day, everyday", "Unexpected textures", "Winter"): "Flan",
    ("Coffee", "All day, everyday", "Unexpected textures", "Spring"): "Mandazi",
    ("Coffee", "All day, everyday", "Unexpected textures", "Autumn"): "Flan",
}


if selected_flavor and selected_time and selected_life and selected_season and dessert_choice:
    user_combo = (selected_flavor, selected_time, selected_life, selected_season)
    result_key = dessert_map.get(user_combo)

    if result_key:
        info = dessert_data[result_key]

    # Display playlist and business info
    st.subheader(f"🎵 Your playlist is {info['playlist']}!")
    st.markdown(f"[Listen Here]({info['playlist_link']})")

    # Business info display
#    st.image(info['business_image'], width=250)
#    st.write(f"🏷️ **Business Name:** {info['business_name']}")
#    st.write(f"🌐 [Visit Website]({info['website']})")
#    st.write(f"📍 **Address:** {info['location']}")

    st.write("")
    st.subheader("Share your playlist!", divider="grey")
    st.write("")
    st.write("How many people did you share your playlist with?")
    shared_count = st.number_input("Number of people:", min_value=0, step=1)
    pianocat = "https://i.imgur.com/zZgJvo5.gif"

    if st.button("Check Reward Status"):
        if shared_count >= 3:
            st.balloons()
            st.success(f"🎊 Surprise!")
            st.image(pianocat, width=300)
    else:
            st.warning("⏳ Share your playlist with at least 3 people to unlock your reward!")