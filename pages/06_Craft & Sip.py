import streamlit as st
from st_clickable_images import clickable_images

st.set_page_config(
    page_title="Craft & Sip",
    page_icon="🎨",
    layout="centered",
)

st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("🎨 Craft & Sip")
st.markdown("""
Welcome! Pick an artistic word below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
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

clicked = clickable_images(
    images,
    titles=titles,
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
)

if clicked > -1:
    st.markdown(f"**{titles[clicked]} selected**")
else:
    st.markdown("**No image selected**")
# Get the selected image title if one is clicked
selected_perform = titles[clicked] if clicked > -1 else None


#Q2
era_options = ["Renaissance", "Medieval", "Contemporary", "Romanticism"]
selected_era = st.selectbox("Which art era do you resonate with most?", era_options, index=None)

#Q3
st.write("Select an ideal creative environment:")
images = [

        "https://cielcreativespace.com/wp-content/uploads/2021/05/CIEL_EDIT3_-75-scaled.jpg", #confetti, chill rooftop, chicken wings, burger, hot dog
        "https://img.bucketlisters.com/image_uploads/1712007681349.png",
        "https://media.istockphoto.com/id/1053651024/photo/wooden-chair-on-lakeside-pier.jpg?s=612x612&w=0&k=20&c=kWbMg_LrlwMeWeuaDW-OkoUjjXVybzzbpB61fHtNvRI=",
        "https://www.arch2o.com/wp-content/uploads/2023/01/Arch2O-modern-fireplace-design-ideas.jpg",
]

titles=["Quiet loft studio", "Cozy cafe on a gloomy day", "Sunny lakeside dock", "Late nights by the fire"]

clicked = clickable_images(
    images,
    titles=titles,
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "200px"},
)

if clicked > -1:
    st.markdown(f"**{titles[clicked]} selected**")
else:
    st.markdown("**No image selected**")
# Get the selected image title if one is clicked
selected_place = titles[clicked] if clicked > -1 else None


#Q4
word = ["Abstract", "Surreal", "Intense", "Tranquil", "Chaos"]
selected_word = st.selectbox("If you were to describe your life in one artistic word, which one would it be?", object, index=None)

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
    ("Plays", "Quiet loft studio", "Emotion"): "Emotion",
    ("Plays", "Quiet loft studio", "Color"): "Texture",
    ("Plays", "Quiet loft studio", "Texture"): "Emotion",
    ("Plays", "Quiet loft studio", "Storytelling"): "Color",
    ("Plays", "Cozy cafe on a gloomy day", "Emotion"): "Storytelling",
    ("Plays", "Cozy cafe on a gloomy day", "Color"): "Texture",
    ("Plays", "Cozy cafe on a gloomy day", "Texture"): "Emotion",
    ("Plays", "Cozy cafe on a gloomy day", "Storytelling"): "Storytelling",
    ("Plays", "Sunny lakeside dock", "Emotion"): "Color",
    ("Plays", "Sunny lakeside dock", "Color"): "Emotion",
    ("Plays", "Sunny lakeside dock", "Texture"): "Texture",
    ("Plays", "Sunny lakeside dock", "Storytelling"): "Emotion",
    ("Plays", "Late nights by the fire", "Emotion"): "Storytelling",
    ("Plays", "Late nights by the fire", "Color"): "Color",
    ("Plays", "Late nights by the fire", "Texture"): "Texture",
    ("Plays", "Late nights by the fire", "Storytelling"): "Texture",

    ("Musicals", "Quiet loft studio", "Emotion"): "Color",
    ("Musicals", "Quiet loft studio", "Color"): "Color",
    ("Musicals", "Quiet loft studio", "Texture"): "Emotion",
    ("Musicals", "Quiet loft studio", "Storytelling"): "Color",
    ("Musicals", "Cozy cafe on a gloomy day", "Emotion"): "Emotion",
    ("Musicals", "Cozy cafe on a gloomy day", "Color"): "Emotion",
    ("Musicals", "Cozy cafe on a gloomy day", "Texture"): "Storytelling",
    ("Musicals", "Cozy cafe on a gloomy day", "Storytelling"): "Color",
    ("Musicals", "Sunny lakeside dock", "Emotion"): "Texture",
    ("Musicals", "Sunny lakeside dock", "Color"): "Storytelling",
    ("Musicals", "Sunny lakeside dock", "Texture"): "Color",
    ("Musicals", "Sunny lakeside dock", "Storytelling"): "Emotion",
    ("Musicals", "Late nights by the fire", "Emotion"): "Storytelling",
    ("Musicals", "Late nights by the fire", "Color"): "Storytelling",
    ("Musicals", "Late nights by the fire", "Texture"): "Texture",
    ("Musicals", "Late nights by the fire", "Storytelling"): "Color",

    ("Concerts", "Quiet loft studio", "Emotion"): "Color",
    ("Concerts", "Quiet loft studio", "Color"): "Texture",
    ("Concerts", "Quiet loft studio", "Texture"): "Texture",
    ("Concerts", "Quiet loft studio", "Storytelling"): "Emotion",
    ("Concerts", "Cozy cafe on a gloomy day", "Emotion"): "Emotion",
    ("Concerts", "Cozy cafe on a gloomy day", "Color"): "Color",
    ("Concerts", "Cozy cafe on a gloomy day", "Texture"): "Emotion",
    ("Concerts", "Cozy cafe on a gloomy day", "Storytelling"): "Texture",
    ("Concerts", "Sunny lakeside dock", "Emotion"): "Color",
    ("Concerts", "Sunny lakeside dock", "Color"): "Color",
    ("Concerts", "Sunny lakeside dock", "Texture"): "Emotion",
    ("Concerts", "Sunny lakeside dock", "Storytelling"): "Emotion",
    ("Concerts", "Late nights by the fire", "Emotion"): "Texture",
    ("Concerts", "Late nights by the fire", "Color"): "Storytelling",
    ("Concerts", "Late nights by the fire", "Texture"): "Storytelling",
    ("Concerts", "Late nights by the fire", "Storytelling"): "Color",

    ("Dance", "Quiet loft studio", "Emotion"): "Emotion",
    ("Dance", "Quiet loft studio", "Color"): "Emotion",
    ("Dance", "Quiet loft studio", "Texture"): "Storytelling",
    ("Dance", "Quiet loft studio", "Storytelling"): "Emotion",
    ("Dance", "Cozy cafe on a gloomy day", "Emotion"): "Texture",
    ("Dance", "Cozy cafe on a gloomy day", "Color"): "Emotion",
    ("Dance", "Cozy cafe on a gloomy day", "Texture"): "Emotion",
    ("Dance", "Cozy cafe on a gloomy day", "Storytelling"): "Color",
    ("Dance", "Sunny lakeside dock", "Emotion"): "Storytelling",
    ("Dance", "Sunny lakeside dock", "Color"): "Storytelling",
    ("Dance", "Sunny lakeside dock", "Texture"): "Color",
    ("Dance", "Sunny lakeside dock", "Storytelling"): "Texture",
    ("Dance", "Late nights by the fire", "Emotion"): "Storytelling",
    ("Dance", "Late nights by the fire", "Color"): "Emotion",
    ("Dance", "Late nights by the fire", "Texture"): "Emotion",
    ("Dance", "Late nights by the fire", "Storytelling"): "Storytelling",
}

if selected_perform and selected_place and value_choice:
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