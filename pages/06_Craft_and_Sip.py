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

        "https://www.nycastings.com/wp-content/uploads/2017/05/theatre-pup.jpg",
        "https://marvel-b1-cdn.bc0a.com/f00000000271534/musicaltheatre.missouristate.edu/_Files/MSU-MusicalTheatre-LegallyBlonde-1920x1080.jpg",
        "https://static.vecteezy.com/system/resources/thumbnails/027/104/127/small_2x/cheering-crowd-illuminated-by-vibrant-stage-lights-at-concert-photo.jpg",
        "https://www.smu.edu/-/media/site/meadows/newsstories/2014/meadowsdanceperformance.jpg",
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

        "https://cielcreativespace.com/wp-content/uploads/2021/05/CIEL_EDIT3_-75-scaled.jpg",
        "https://img.bucketlisters.com/image_uploads/1712007681349.png",
        "https://media.istockphoto.com/id/1053651024/photo/wooden-chair-on-lakeside-pier.jpg?s=612x612&w=0&k=20&c=kWbMg_LrlwMeWeuaDW-OkoUjjXVybzzbpB61fHtNvRI=",
        "https://www.arch2o.com/wp-content/uploads/2023/01/Arch2O-modern-fireplace-design-ideas.jpg",
]

titles=["Quiet loft studio", "Cozy cafe on a gloomy day", "Sunny lakeside dock", "Late nights by the fire"]

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
        "business_name": "The Wasteshed",
        "offer": "10% off your first purchase with this screen!",
        "booth_name": "Booth A",
        "website": "https://www.thewasteshed.com/",
        "business_image": "https://images.squarespace-cdn.com/content/v1/5462e7eae4b047a3e78ccc67/d681968b-111a-4180-9fed-c22e228f3773/general-brandmark-white-wider.png?format=1500w",
    },
    "Color": {
    "playlist": "Palette Pop",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Ancestry Moon Art Studio",
    "offer": "Get $10 off your first class!",
    "booth_name": "Booth B",
    "website": "https://www.facebook.com/AmMoon103",
    "business_image": "https://scontent-ord5-2.xx.fbcdn.net/v/t39.30808-6/476198914_1106877391451064_5406431294276183812_n.jpg?_nc_cat=104&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=Hz-pOZ2KOtoQ7kNvwEl-RT3&_nc_oc=Adn0Gl9SANmYu6nLfQxT0F-27vQ4I5-wn6vZaguWWWt0ZKbMahL6Kepv948zfvXdUSvuMpzaVOvrZqHJ7FsG1uVf&_nc_zt=23&_nc_ht=scontent-ord5-2.xx&_nc_gid=Y-DW2ZLnLbwIaQ63Bjpv9w&oh=00_AfdHxO8trkyJtFnEYdyYv6mUCDHhKQWSRGt1Z1X8w2dGuA&oe=68E8C29A",
    },
    "Texture": {
    "playlist": "Velvet Tunes",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "David Leonardis Gallery",
    "offer": "Receive exclusive access to collections!",
    "booth_name": "Booth C",
    "website": "https://dlgalleries.com/",
    "business_image": "https://dlgalleries.com/wp-content/uploads/2025/01/IMG_9449-scaled.jpg"
    },
    "Storytelling": {
    "playlist": "Memory Lane",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Art & Company",
    "offer": "Get a 5% discount with your first order!",
    "booth_name": "Booth D",
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

if selected_place and selected_word and value_choice:
    user_combo = (selected_perform, selected_place, value_choice)
    result_key = craft_map.get(user_combo)
    # Retrieve information about selected drink/business

    if result_key:
        info3 = value_data[result_key]

    # Display playlist and business info
    st.subheader(f"🎵 {info3['playlist']}")
    st.markdown(f"[Listen Here]({info3['playlist_link']})")

    # Business info display
    st.image(info3['business_image'], width=250)  # Show business image (if available)
    st.write(f"💼 **Business Name:** {info3['business_name']}")
    st.write(f"🌐 [Visit Website]({info3['website']})")
    st.write(f"🎁 **Special Offer:** {info3['offer']}")

    st.write("👥 How many people did you share your playlist with?")
    shared_count = st.number_input("Number of people:", min_value=0, step=1)

    if st.button("Check Reward Status"):
        if shared_count >= 3:
            st.balloons()  # Add some confetti for fun
            st.success(f"🎁 You unlocked a reward! Show this screen at {info3['booth_name']} to claim your prize!")
        else:
            st.warning("⏳ Share your playlist with at least 3 people to unlock your reward!")