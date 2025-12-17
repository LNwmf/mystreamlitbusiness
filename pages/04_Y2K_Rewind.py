from st_copy import copy_button
import streamlit as st


st.set_page_config(
    page_title="Y2K Rewind",
    page_icon="💿",
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
st.title("💿 Y2K Rewind")
st.markdown("""
Welcome! Pick a 2000s music artist below to discover a blended playlist and unlock a surprise for sharing with others.
""")

#Q1
st.write("What Y2K tech do you miss the most? (double-click button)")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/flipphone.jpeg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/mp3.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/nintendo.jpeg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/digitalcamera.png",
]

titles=["Flip phones", "MP3 players", "Nintendo DS", "Digital cameras"]

if "selected_tech" not in st.session_state:
    st.session_state.selected_tech = None

cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        # Clicking the button selects this image
        if st.button(titles[i], key=f"btn_tech_{i}"):
            st.session_state.selected_tech = i

        # Add a red border if selected
        border = "4px solid red" if st.session_state.selected_tech == i else "4px solid transparent"

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

selected_tech = (
    titles[st.session_state.selected_tech]
    if st.session_state.get("selected_tech") is not None
    else None
)
#gap
st.write("")

#Q2
trend = ["Tracksuit with rhinestones", "Chunky sunglasses", "Denim on denim", "Trucker hats"]
selected_trend = st.selectbox("Pick a 2000s fashion trend:", trend, index=None)

#Q3
st.write("If you were teleported into a movie, which one would you prefer to be in? (double-click button)")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/meangirls.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/10tihay.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/lordoftherings.jpg",
        "https://upload.wikimedia.org/wikipedia/en/thumb/a/aa/13_Going_on_30_film_poster.png/250px-13_Going_on_30_film_poster.png",
]

titles=["Mean Girls", "10 Things I Hate About You", "Lord of the Rings Trilogy", "13 Going On 30"]

if "selected_movie" not in st.session_state:
    st.session_state.selected_movie = None

cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        # Clicking the button selects this image
        if st.button(titles[i], key=f"btn_movie_{i}"):
            st.session_state.selected_movie = i

        border = "4px solid red" if st.session_state.selected_movie == i else "4px solid transparent"

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

selected_movie = (
    titles[st.session_state.selected_movie]
    if st.session_state.get("selected_movie") is not None
    else None
)

#gap
st.write("")

#Q4
ppl = ["Cyber kid", "Pop princess", "Fashion icon", "Chill surfer"]
selected_ppl = st.selectbox("Which Y2K character are you?", ppl, index=None)


# Business options and related data
y2k_data = {
    "Britney Spears": {
        "playlist": "Global Hits",
        "playlist_link": "https://open.spotify.com/playlist/21mLluoK8TIHpPmgFIJUxB?si=gVJOo4KuTYKlh-h1hvk0GA",
#        "business_name": "Edgewater Candles",
#        "location": "1050 W Bryn Mawr Ave, Chicago, IL 60660",
#        "website": "https://edgewatercandles.com/?srsltid=AfmBOooOnjGXBIqXVBK-zps-K3C05oH3rcqn72f7BYUijz8L_CN4TsrP",
#        "business_image": "https://edgewatercandles.com/cdn/shop/files/EC_Logo_BW.png?v=1706025877&width=220",
    },
    "Usher": {
    "playlist": "Smooth Grooves",
    "playlist_link": "https://open.spotify.com/playlist/1dFrH8T9DjXR6pK80qz7FC?si=M1Dh0PX-QW-xGbS7sKPQwQ",
#    "business_name": "Ándale Market",
#    "location": "5232 N Clark St, Chicago, IL 60640",
#    "website": "https://andalemarket.com/",
#    "business_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/andalemarket.png",
    },
    "Green Day": {
    "playlist": "Amped Up",
    "playlist_link": "https://open.spotify.com/playlist/5LFR9EXWYS1Xn0FgolkiSy?si=u3-FMgAFSx6fH8G0v2gWjw",
#    "business_name": "AlleyCat Comics",
#    "location": "5304 N Clark St, Chicago, IL 60640",
#    "website": "https://www.alleycatcomics.com/",
#    "business_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/alleycatcomics.png"
    },
    "Destiny's Child": {
    "playlist": "Off the Charts",
    "playlist_link": "https://open.spotify.com/playlist/1YpUBBaQ9hS5P5KpndONGu?si=38KYS0O5RzuSiwnCh098Qg",
#    "business_name": "Five Elements Home",
#    "location": "5239 N Clark St, Chicago, IL 60640",
#    "website": "https://www.fiveelementshome.com/",
#    "business_image": "https://www.fiveelementshome.com/cdn/shop/t/55/assets/logo.png?v=63601364107164957311456001943"
    },
}

info = None

y2k_choice = st.selectbox("Pick an artist!", ["", *y2k_data.keys()])

y2k_map = {
("Flip phones", "Mean Girls", "Cyber kid"): "Green Day",
("Flip phones", "Mean Girls", "Pop princess"): "Britney Spears",
("Flip phones", "Mean Girls", "Fashion icon"): "Destiny's Child",
("Flip phones", "Mean Girls", "Chill surfer"): "Usher",

("Flip phones", "10 Things I Hate About You", "Cyber kid"): "Destiny's Child",
("Flip phones", "10 Things I Hate About You", "Pop princess"): "Britney Spears",
("Flip phones", "10 Things I Hate About You", "Fashion icon"): "Britney Spears",
("Flip phones", "10 Things I Hate About You", "Chill surfer"): "Green Day",

("Flip phones", "Lord of the Rings Trilogy", "Cyber kid"): "Green Day",
("Flip phones", "Lord of the Rings Trilogy", "Pop princess"): "Destiny's Child",
("Flip phones", "Lord of the Rings Trilogy", "Fashion icon"): "Destiny's Child",
("Flip phones", "Lord of the Rings Trilogy", "Chill surfer"): "Usher",

("Flip phones", "13 Going On 30", "Cyber kid"): "Destiny's Child",
("Flip phones", "13 Going On 30", "Pop princess"): "Usher",
("Flip phones", "13 Going On 30", "Fashion icon"): "Usher",
("Flip phones", "13 Going On 30", "Chill surfer"): "Destiny's Child",

("MP3 players", "Mean Girls", "Cyber kid"): "Green Day",
("MP3 players", "Mean Girls", "Pop princess"): "Green Day",
("MP3 players", "Mean Girls", "Fashion icon"): "Britney Spears",
("MP3 players", "Mean Girls", "Chill surfer"): "Britney Spears",

("MP3 players", "10 Things I Hate About You", "Cyber kid"): "Destiny's Child",
("MP3 players", "10 Things I Hate About You", "Pop princess"): "Usher",
("MP3 players", "10 Things I Hate About You", "Fashion icon"): "Usher",
("MP3 players", "10 Things I Hate About You", "Chill surfer"): "Green Day",

("MP3 players", "Lord of the Rings Trilogy", "Cyber kid"): "Britney Spears",
("MP3 players", "Lord of the Rings Trilogy", "Pop princess"): "Destiny's Child",
("MP3 players", "Lord of the Rings Trilogy", "Fashion icon"): "Green Day",
("MP3 players", "Lord of the Rings Trilogy", "Chill surfer"): "Green Day",

("MP3 players", "13 Going On 30", "Cyber kid"): "Destiny's Child",
("MP3 players", "13 Going On 30", "Pop princess"): "Usher",
("MP3 players", "13 Going On 30", "Fashion icon"): "Destiny's Child",
("MP3 players", "13 Going On 30", "Chill surfer"): "Usher",

("Nintendo DS", "Mean Girls", "Cyber kid"): "Green Day",
("Nintendo DS", "Mean Girls", "Pop princess"): "Destiny's Child",
("Nintendo DS", "Mean Girls", "Fashion icon"): "Usher",
("Nintendo DS", "Mean Girls", "Chill surfer"): "Green Day",

("Nintendo DS", "10 Things I Hate About You", "Cyber kid"): "Usher",
("Nintendo DS", "10 Things I Hate About You", "Pop princess"): "Usher",
("Nintendo DS", "10 Things I Hate About You", "Fashion icon"): "Green Day",
("Nintendo DS", "10 Things I Hate About You", "Chill surfer"): "Britney Spears",

("Nintendo DS", "Lord of the Rings Trilogy", "Cyber kid"): "Britney Spears",
("Nintendo DS", "Lord of the Rings Trilogy", "Pop princess"): "Green Day",
("Nintendo DS", "Lord of the Rings Trilogy", "Fashion icon"): "Britney Spears",
("Nintendo DS", "Lord of the Rings Trilogy", "Chill surfer"): "Usher",

("Nintendo DS", "13 Going On 30", "Cyber kid"): "Destiny's Child",
("Nintendo DS", "13 Going On 30", "Pop princess"): "Destiny's Child",
("Nintendo DS", "13 Going On 30", "Fashion icon"): "Usher",
("Nintendo DS", "13 Going On 30", "Chill surfer"): "Green Day",

("Digital cameras", "Mean Girls", "Cyber kid"): "Green Day",
("Digital cameras", "Mean Girls", "Pop princess"): "Destiny's Child",
("Digital cameras", "Mean Girls", "Fashion icon"): "Green Day",
("Digital cameras", "Mean Girls", "Chill surfer"): "Destiny's Child",

("Digital cameras", "10 Things I Hate About You", "Cyber kid"): "Green Day",
("Digital cameras", "10 Things I Hate About You", "Pop princess"): "Green Day",
("Digital cameras", "10 Things I Hate About You", "Fashion icon"): "Usher",
("Digital cameras", "10 Things I Hate About You", "Chill surfer"): "Destiny's Child",

("Digital cameras", "Lord of the Rings Trilogy", "Cyber kid"): "Britney Spears",
("Digital cameras", "Lord of the Rings Trilogy", "Pop princess"): "Usher",
("Digital cameras", "Lord of the Rings Trilogy", "Fashion icon"): "Green Day",
("Digital cameras", "Lord of the Rings Trilogy", "Chill surfer"): "Britney Spears",

("Digital cameras", "13 Going On 30", "Cyber kid"): "Destiny's Child",
("Digital cameras", "13 Going On 30", "Pop princess"): "Green Day",
("Digital cameras", "13 Going On 30", "Fashion icon"): "Destiny's Child",
("Digital cameras", "13 Going On 30", "Chill surfer"): "Usher",

}

if selected_tech and selected_movie and selected_ppl and y2k_choice:
    user_combo = (selected_tech, selected_movie, selected_ppl)
    result_key = y2k_map.get(user_combo)
    if result_key:
        info = y2k_data[result_key]


    # Display playlist and business info
    st.subheader(f"🎵 Your playlist is {info['playlist']}!")
    playlist_link = info["playlist_link"]

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
            st.image(pianocat,width=300)
    else:
            st.warning("⏳ Share your playlist with at least 3 people to unlock your reward!")