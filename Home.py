import streamlit as st
#streamlit run Home.py
st.set_page_config(page_title="About Us", layout="centered")
st.markdown(
    """
    <style>
    /* Remove rounding from all images rendered by Streamlit */
    img {
        border-radius: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)
st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("About Us")
st.write("Welcome! This app is created by the World Music Foundation to share music and uplift local businesses. Each page includes a series of questions that returns a playlist and promotes a small business. There's also a guessing and trivia game to test your musical knowledge!")


#st.markdown("---")
with st.expander("Our Purpose", icon=":material/target:"):
    st.write("The World Music Foundation is a 501(c)(3) non-profit organization dedicated to a simple mission: opening minds through Music. We believe, and research shows, that experiencing music of other cultures increases tolerance and cultural empathy in people, and everything that we do is based on effecting this social change. Racism continues to be one of the world’s greatest problems and Music is a proven armament in this fight.")

#st.markdown("")
with st.expander("Contact Us", icon=":material/emoji_people:"):
    st.write("Inquires: info@theworldmusicfoundation.org")
    st.write()
    st.write("Events: events@theworldmusicfoundation.org")
    st.write()
    st.write("Lessons: classes@theworldmusicfoundation.org")
    st.write()
    st.write("Podcasts: podcast@theworldmusicfoundation.org")

with st.expander("Support Us", icon=":material/store:"):
    st.write("Merchandise: https://theworldmusicfoundation.org/products/")
    st.write()
    st.write("Donate: https://www.paypal.com/donate/?hosted_button_id=QXGAJ7QC8TKZL")
    st.write()
    st.write("Instagram: https://www.instagram.com/theworldmusicfoundation/")
    st.write()
    st.write("Facebook: https://www.facebook.com/TheWorldMusicFoundation")
    st.write()
    st.write("TikTok: https://www.tiktok.com/@theworldmusicfoundation")

st.write("")
st.markdown("---")
st.write("")
#st.write("")

st.header("Navigation")
st.write("Click a page to be automatically redirected.")
#st.markdown("---")

pages = {
    "🍹 Jams & Juice": "02_Jams_and_Juice",
    "🍬 Sweet Melodies": "03_Sweet_Melodies",
    "💿 Y2K Rewind": "04_Y2K_Rewind",
    "🍂 Sweater Weather Tunes": "05_Sweater_Weather_Tunes",
    "🎨 Craft & Sip": "06_Craft_and_Sip",
    "🪞 Serene Self-Care": "07_Serene_Self_Care",
    "🎉 Press Play to Party": "08_Press_Play_to_Party",
    "💭 Guess the Instrument": "09_Guess_the_Instrument",
    "❓ Music Trivia": "10_Music_Trivia",
}

cols = st.columns(2)

i = 0
for label, file in pages.items():
    with cols[i % 2]:
        if st.button(label, use_container_width=True):
            st.switch_page(f"pages/{file}.py")
    i += 1