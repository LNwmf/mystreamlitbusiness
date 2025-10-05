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
    "playlist": "Dancing Jelly",
    "business_image": "https://www.tapasvalencia.com/wp-content/uploads/2017/08/Valencia-TRANSPARENT.png",
    },
    "Musicals": {
    "playlist": "Pastries & Strings",
    "business_image": "https://images.squarespace-cdn.com/content/v1/652e9491cec326539e621efe/2d266898-08ee-4747-8242-8a59a020b47b/large+white+backless.png?format=1000w",
    },
    "Concerts": {
    "playlist": "Chill J-Rock",
    "business_image": "https://cdn.prod.website-files.com/621e6fe3c0a99283c0cc87fb/65f86e09a6e239d1ffac94dd_zakaya-Logo-black-Transparent.svg"
    },
    "Dance": {
    "playlist": "Reggaeton Fusions",
    "business_image": "https://samiflorenciacatering.com/wp-content/uploads/2024/02/Florencia-logo.jpg.webp"
    },
}
#perform_type = ["Plays", "Musicals", "Concerts", "Dance"]
selected_perform = st.selectbox("Select a Performance:", ["", *business_data.keys()])

if selected_perform:
    info = business_data[selected_perform]

    st.subheader(f"🎵 {info['playlist']}")
    st.image(info['business_image'], width=250)