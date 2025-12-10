import streamlit as st

st.set_page_config(
    page_title="Craft & Sip",
    page_icon="🎨",
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
st.title("🎨 Craft & Sip")
st.markdown("""
Welcome! Pick an artistic value below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
""")

#Q1
st.write("Select a performance type:")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/play.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/musical.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/concert.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/dance.jpg",
]

titles=["Plays", "Musicals", "Concerts", "Dance"]

if "selected_perform" not in st.session_state:
    st.session_state.selected_perform = None

cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        if st.button(titles[i], key=f"btn_perform_{i}"):
            st.session_state.selected_perform = i

        border = "4px solid red" if st.session_state.selected_perform == i else "4px solid transparent"

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

selected_perform = (
    titles[st.session_state.selected_perform]
    if st.session_state.get("selected_perform") is not None
    else None
)
#gap
st.write("")

#Q2
era_options = ["Renaissance", "Medieval", "Contemporary", "Romanticism"]
selected_era = st.selectbox("Which art era do you resonate with most?", era_options, index=None)

#Q3
st.write("Select an ideal creative environment:")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/loft.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/cafe.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/lakeside.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/fireplace.jpg",
]

titles=["Quiet loft studio", "Cozy cafe on a gloomy day", "Sunny lakeside", "Late nights by the fire"]

if "selected_place" not in st.session_state:
    st.session_state.selected_place = None

cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        if st.button(titles[i], key=f"btn_place_{i}"):
            st.session_state.selected_place = i

        border = "4px solid red" if st.session_state.selected_place == i else "4px solid transparent"

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

selected_place = (
    titles[st.session_state.selected_place]
    if st.session_state.get("selected_place") is not None
    else None
)
#gap
st.write("")

#Q4
word = ["Abstract", "Surreal", "Intense", "Tranquil"]
selected_word = st.selectbox("If you were to describe your life in one artistic word, which one would it be?", word, index=None)

#Q5
value_data = {
    "Emotion": {
        "playlist": "Happy Accidents",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "business_name": "Paper and Pencil",
        "location": "1480 W Berwyn Ave, Chicago, IL 60640",
        "website": "https://paperandpencilchicago.com/",
        "business_image": "https://paperandpencilchicago.com/cdn/shop/files/Primary_1.png?v=1680104637&width=500",
    },
    "Color": {
    "playlist": "Palette Pop",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Foursided",
    "location": "5061 N Clark St, Chicago, IL 60640",
    "website": "https://foursided.com/",
    "business_image": "https://foursided.com/cdn/shop/files/foursided_2025_holiday_logo_trans_trimmed_290x@2x.png?v=1763072139",
    },
    "Texture": {
    "playlist": "Velvet Tunes",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "David Leonardis Gallery",
    "location": "Receive exclusive access to collections!",
    "website": "https://dlgalleries.com/",
    "business_image": "https://dlgalleries.com/wp-content/uploads/2025/01/IMG_9449-scaled.jpg"
    },
    "Storytelling": {
    "playlist": "Memory Lane",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Art & Company",
    "location": "Get a 5% discount with your first order!",
    "website": "https://www.artandcompany.net/#/",
    "business_image": "https://www.artandcompany.net/uploads/9/3/5/2/9352723/1427560359.png"
    },
}

info3 = None
#Value Selection
value_choice = st.selectbox("What do you value most in your world?", ["", *value_data.keys()])

craft_map = {
    ("Quiet loft studio", "Abstract", "Emotion"): "Texture",
    ("Quiet loft studio", "Abstract", "Color"): "Emotion",
    ("Quiet loft studio", "Abstract", "Texture"): "Texture",
    ("Quiet loft studio", "Abstract", "Storytelling"): "Storytelling",
    ("Quiet loft studio", "Surreal", "Emotion"): "Emotion",
    ("Quiet loft studio", "Surreal", "Color"): "Color",
    ("Quiet loft studio", "Surreal", "Texture"): "Storytelling",
    ("Quiet loft studio", "Surreal", "Storytelling"): "Color",
    ("Quiet loft studio", "Intense", "Emotion"): "Emotion",
    ("Quiet loft studio", "Intense", "Color"): "Texture",
    ("Quiet loft studio", "Intense", "Texture"): "Storytelling",
    ("Quiet loft studio", "Intense", "Storytelling"): "Color",
    ("Quiet loft studio", "Tranquil", "Emotion"): "Color",
    ("Quiet loft studio", "Tranquil", "Color"): "Texture",
    ("Quiet loft studio", "Tranquil", "Texture"): "Color",
    ("Quiet loft studio", "Tranquil", "Storytelling"): "Emotion",
    ("Cozy cafe on a gloomy day", "Abstract", "Emotion"): "Storytelling",
    ("Cozy cafe on a gloomy day", "Abstract", "Color"): "Color",
    ("Cozy cafe on a gloomy day", "Abstract", "Texture"): "Texture",
    ("Cozy cafe on a gloomy day", "Abstract", "Storytelling"): "Emotion",
    ("Cozy cafe on a gloomy day", "Surreal", "Emotion"): "Storytelling",
    ("Cozy cafe on a gloomy day", "Surreal", "Color"): "Texture",
    ("Cozy cafe on a gloomy day", "Surreal", "Texture"): "Texture",
    ("Cozy cafe on a gloomy day", "Surreal", "Storytelling"): "Color",
    ("Cozy cafe on a gloomy day", "Intense", "Emotion"): "Color",
    ("Cozy cafe on a gloomy day", "Intense", "Color"): "Emotion",
    ("Cozy cafe on a gloomy day", "Intense", "Texture"): "Emotion",
    ("Cozy cafe on a gloomy day", "Intense", "Storytelling"): "Storytelling",
    ("Cozy cafe on a gloomy day", "Tranquil", "Emotion"): "Texture",
    ("Cozy cafe on a gloomy day", "Tranquil", "Color"): "Emotion",
    ("Cozy cafe on a gloomy day", "Tranquil", "Texture"): "Emotion",
    ("Cozy cafe on a gloomy day", "Tranquil", "Storytelling"): "Color",
    ("Sunny lakeside", "Abstract", "Emotion"): "Color",
    ("Sunny lakeside", "Abstract", "Color"): "Color",
    ("Sunny lakeside", "Abstract", "Texture"): "Emotion",
    ("Sunny lakeside", "Abstract", "Storytelling"): "Texture",
    ("Sunny lakeside", "Surreal", "Emotion"): "Storytelling",
    ("Sunny lakeside", "Surreal", "Color"): "Texture",
    ("Sunny lakeside", "Surreal", "Texture"): "Emotion",
    ("Sunny lakeside", "Surreal", "Storytelling"): "Color",
    ("Sunny lakeside", "Intense", "Emotion"): "Texture",
    ("Sunny lakeside", "Intense", "Color"): "Storytelling",
    ("Sunny lakeside", "Intense", "Texture"): "Color",
    ("Sunny lakeside", "Intense", "Storytelling"): "Emotion",
    ("Sunny lakeside", "Tranquil", "Emotion"): "Color",
    ("Sunny lakeside", "Tranquil", "Color"): "Texture",
    ("Sunny lakeside", "Tranquil", "Texture"): "Texture",
    ("Sunny lakeside", "Tranquil", "Storytelling"): "Storytelling",
    ("Late nights by the fire", "Abstract", "Emotion"): "Storytelling",
    ("Late nights by the fire", "Abstract", "Color"): "Color",
    ("Late nights by the fire", "Abstract", "Texture"): "Emotion",
    ("Late nights by the fire", "Abstract", "Storytelling"): "Texture",
    ("Late nights by the fire", "Surreal", "Emotion"): "Emotion",
    ("Late nights by the fire", "Surreal", "Color"): "Color",
    ("Late nights by the fire", "Surreal", "Texture"): "Storytelling",
    ("Late nights by the fire", "Surreal", "Storytelling"): "Texture",
    ("Late nights by the fire", "Intense", "Emotion"): "Emotion",
    ("Late nights by the fire", "Intense", "Color"): "Color",
    ("Late nights by the fire", "Intense", "Texture"): "Texture",
    ("Late nights by the fire", "Intense", "Storytelling"): "Storytelling",
    ("Late nights by the fire", "Tranquil", "Emotion"): "Storytelling",
    ("Late nights by the fire", "Tranquil", "Color"): "Texture",
    ("Late nights by the fire", "Tranquil", "Texture"): "Emotion",
    ("Late nights by the fire", "Tranquil", "Storytelling"): "Color",
}

if selected_perform and selected_era and selected_place and selected_word and value_choice:
    user_combo = (selected_place, selected_word, value_choice)
    result_key = craft_map.get(user_combo)

    if result_key:
        info3 = value_data[result_key]

    # Display playlist and business info
    st.subheader(f"🎵 {info3['playlist']}")
    st.markdown(f"[Listen Here]({info3['playlist_link']})")

    # Business info display
    st.image(info3['business_image'], width=250)
    st.write(f"🏷️ **Business Name:** {info3['business_name']}")
    st.write(f"🌐 [Visit Website]({info3['website']})")
    st.write(f"📍 **Address:** {info3['offer']}")

    st.write("")
    st.subheader("Share your playlist!", divider="grey")
    st.write("")
    st.write("How many people did you share your playlist with?")
    shared_count = st.number_input("Number of people:", min_value=0, step=1)

    if st.button("Check Reward Status"):
        if shared_count >= 3:
            st.balloons()
            st.success(f"🎁 You unlocked a reward!")
        else:
            st.warning("⏳ Share your playlist with at least 3 people to unlock your reward!")