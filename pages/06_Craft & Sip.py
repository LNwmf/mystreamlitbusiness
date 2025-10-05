import streamlit as st

st.set_page_config(
    page_title="Craft & Sip",
    page_icon="🎨",
    layout="centered",
)

st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("🎨 Craft & Sip")
st.markdown("""
Welcome! Pick a dessert below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
""")

#Q1
business_data = {
    "Plays": {
    "business_image": "https://www.nycastings.com/wp-content/uploads/2017/05/theatre-pup.jpg",
    },
    "Musicals": {
    "business_image": "https://marvel-b1-cdn.bc0a.com/f00000000271534/musicaltheatre.missouristate.edu/_Files/MSU-MusicalTheatre-LegallyBlonde-1920x1080.jpg",
    },
    "Concerts": {
    "business_image": "https://static.vecteezy.com/system/resources/thumbnails/027/104/127/small_2x/cheering-crowd-illuminated-by-vibrant-stage-lights-at-concert-photo.jpg"
    },
    "Dance": {
    "business_image": "https://www.smu.edu/-/media/site/meadows/newsstories/2014/meadowsdanceperformance.jpg"
    },
}
#perform_type = ["Plays", "Musicals", "Concerts", "Dance"]
selected_perform = st.selectbox("Select a Performance Type:", ["", *business_data.keys()])

if selected_perform:
    info1 = business_data[selected_perform]

    st.image(info1['business_image'], width=250)

#Q2
era_options = ["Renaissance", "Medieval", "Contemporary", "Romanticism"]
selected_era = st.selectbox("Which art era do you resonate with most?", era_options, index=None)

#Q3
place_data = {
    "Quiet loft studio": {
    "place_image": "https://cielcreativespace.com/wp-content/uploads/2021/05/CIEL_EDIT3_-75-scaled.jpg",
    },
    "Cozy cafe on a gloomy day": {
    "place_image": "https://img.bucketlisters.com/image_uploads/1712007681349.png",
    },
    "Sunny lakeside dock": {
    "place_image": "https://media.istockphoto.com/id/1053651024/photo/wooden-chair-on-lakeside-pier.jpg?s=612x612&w=0&k=20&c=kWbMg_LrlwMeWeuaDW-OkoUjjXVybzzbpB61fHtNvRI="
    },
    "Late nights by the fire": {
    "place_image": "https://i.pinimg.com/736x/f8/6e/5d/f86e5d0d356bbf633065e1e2454ef8c5.jpg"
    },
}
selected_place = st.selectbox("Select an ideal creative environment:", ["", *place_data.keys()])

if selected_place:
    info2 = place_data[selected_perform]

    st.image(info2['place_image'], width=250)

