from st_copy import copy_button
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
Welcome! Pick an artistic value below to discover a blended playlist and unlock a surprise for sharing with others.
""")

#Q1
st.write("Select a performance type: (double-click button)")
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
st.write("Select an ideal creative environment: (double-click button)")
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
#        "business_name": "Paper and Pencil",
#        "location": "1480 W Berwyn Ave, Chicago, IL 60640",
#        "website": "https://paperandpencilchicago.com/",
#        "business_image": "https://paperandpencilchicago.com/cdn/shop/files/Primary_1.png?v=1680104637&width=500",
    },
    "Color": {
    "playlist": "Palette Pop",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
#    "business_name": "Foursided",
#    "location": "5061 N Clark St, Chicago, IL 60640",
#    "website": "https://foursided.com/",
#    "business_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/foursided.png",
    },
    "Texture": {
    "playlist": "Velvet Tunes",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
#    "business_name": "Mercantile M",
#    "location": "5409 1/2 N Clark St, Chicago, Illinois 60640",
#    "website": "https://www.facebook.com/MercantileM//",
#    "business_image": "https://scontent-ord5-1.xx.fbcdn.net/v/t39.30808-6/481456667_1206271091507885_307276287281734569_n.jpg?stp=dst-jpg_s960x960_tt6&_nc_cat=101&cb2=99be929b-a592a72f&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=Wp8qF0hBKD0Q7kNvwHj3DOh&_nc_oc=AdlgUbQ_a0EZXUU2IGiiTJsHP-OEP144byk1RVnJ1JzX3vQBmtp3_2n-gPKHs61yiQoDi7JdtbPW9AtWcLbJf7b3&_nc_zt=23&_nc_ht=scontent-ord5-1.xx&_nc_gid=3TjdTHii2bu4_VLUV8Cxug&oh=00_AfmKRCTfM1SU0m_VTOpU-J3wvpfExUk8CSIQEIro8kwIkA&oe=693E92CA"
    },
    "Storytelling": {
    "playlist": "Memory Lane",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
#    "business_name": "Andersonville Galleria",
#    "location": "5247 N Clark St, Chicago, IL 60640",
#    "website": "https://andersonvillegalleria.com/",
#    "business_image": "https://andersonvillegalleria.com/wp-content/uploads/2024/03/AG-Logo-1.png"
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
    st.subheader(f"🎵 Your playlist is {info3['playlist']}!")
    playlist_link = info3["playlist_link"]

    # Create two columns: one wider for the link, one narrower for the button
    col1, col2 = st.columns([0.2, 1])

    # Put the hyperlink in the first column
    with col1:
        st.markdown(
            f"""
                       <a href="{playlist_link}" target="_blank" style="font-size:20px; font-weight:bold;">
                           Listen Here
                       </a>
                       """,
            unsafe_allow_html=True
        )

    # Put the copy button in the second column
    with col2:
        copy_button(playlist_link)

    # Business info display
#    st.image(info3['business_image'], width=250)
#    st.write(f"🏷️ **Business Name:** {info3['business_name']}")
#    st.write(f"🌐 [Visit Website]({info3['website']})")
#    st.write(f"📍 **Address:** {info3['location']}")

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