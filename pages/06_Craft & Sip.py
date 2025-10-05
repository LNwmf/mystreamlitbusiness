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
selected_perform = st.selectbox("Select a Performance:", ["", *business_data.keys()])

if selected_perform:
    info = business_data[selected_perform]

    st.image(info['business_image'], width=250)