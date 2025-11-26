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
Welcome! Pick a 2000s music artist below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
""")

#Q1
st.write("What Y2K tech do you miss the most?")
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
st.write("If you were teleported into a movie, which one would you prefer to be in?")
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
        "playlist": "Oop...I did it again",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "business_name": "Sugar Bliss",
        "offer": "10% off your first order with this screen!",
        "booth_name": "Booth A",
        "website": "https://www.sugarblisscakes.com/",
        "business_image": "https://static.wixstatic.com/media/2859e8_d08aa804763e451fa31e64108db79992~mv2.jpg/v1/fill/w_352,h_110,al_c,q_80,usm_0.66_1.00_0.01,enc_avif,quality_auto/%20Brand%20Guide%20(8_edited.jpg",
    },
    "Usher": {
    "playlist": "Smooth Grooves",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Soule to Soule",
    "offer": "Get 5% off a selected entree with this screen.",
    "booth_name": "Booth B",
    "website": "https://www.souletosoule.com/",
    "business_image": "https://images.squarespace-cdn.com/content/v1/64bf276689b7b563702a2634/f03ab85d-0add-4844-a07f-58b2deca1264/Soule-To-Soule-Logo_gold-.png?format=2500w",
    },
    "Green Day": {
    "playlist": "Amped Up",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Hecky's",
    "offer": "5% off your order!",
    "booth_name": "Booth C",
    "website": "https://www.heckys.com/",
    "business_image": "https://static.spotapps.co/website_images/ab_websites/88743_website/logo.png"
    },
    "Destiny's Child": {
    "playlist": "Off the Charts Pop",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Kokorokoko",
    "offer": "Get 10% discount with your purchase!",
    "booth_name": "Booth D",
    "website": "https://www.kokorokokovintage.com/",
    "business_image": "https://www.kokorokokovintage.com/cdn/shop/files/koko.LOGO_360x.jpg?v=1613785534"
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
    # Retrieve information about selected drink/business
    if result_key:
        info = y2k_data[result_key]


    # Display playlist and business info
    st.subheader(f"🎵 {info['playlist']}")
    st.markdown(f"[Listen Here]({info['playlist_link']})")

    # Business info display
    st.image(info['business_image'], width=250)  # Show business image (if available)
    st.write(f"💼 **Business Name:** {info['business_name']}")
    st.write(f"🌐 [Visit Website]({info['website']})")
    st.write(f"🎁 **Special Offer:** {info['offer']}")

    st.write("👥 How many people did you share your playlist with?")
    shared_count = st.number_input("Number of people:", min_value=0, step=1)

    if st.button("Check Reward Status"):
        if shared_count >= 3:
            st.balloons()  # Add some confetti for fun
            st.success(f"🎁 You unlocked a reward! Show this screen at {info['booth_name']} to claim your prize!")
    else:
            st.warning("⏳ Share your playlist with at least 3 people to unlock your reward!")