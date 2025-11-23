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

        "https://m.media-amazon.com/images/I/61-mqYsNMEL.jpg",
        "https://retrospekt.com/cdn/shop/files/MP-VR-1006_1-newphones.jpg?v=1719506839&width=3000",
        "https://media.gameshop.se/wp-content/uploads/2019/10/01010522/37635.jpg",
        "https://i.etsystatic.com/57193956/r/il/5ec242/6867084797/il_fullxfull.6867084797_ed68.jpg",
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

        "https://m.media-amazon.com/images/M/MV5BMjE1MDQ4MjI1OV5BMl5BanBnXkFtZTcwNzcwODAzMw@@._V1_.jpg",
        "https://m.media-amazon.com/images/M/MV5BOTQwYmRhNGQtODI2Mi00ZTRlLTk0Y2QtY2NkNjE1MGNhNTgwXkEyXkFqcGc@._V1_.jpg",
        "https://m.media-amazon.com/images/M/MV5BNzIxMDQ2YTctNDY4MC00ZTRhLTk4ODQtMTVlOWY4NTdiYmMwXkEyXkFqcGc@._V1_.jpg",
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

        # Add a red border if selected
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

selected_tech = (
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
("Flip phones", "Mean Girls", "Britney Spears"): "Britney Spears",
("Flip phones", "Mean Girls", "Usher"): "Usher",
("Flip phones", "Mean Girls", "Green Day"): "Green Day",
("Flip phones", "Mean Girls", "Destiny's Child"): "Destiny's Child",
("Flip phones", "10 Things I Hate About You", "Britney Spears"): "Green Day",
("Flip phones", "10 Things I Hate About You", "Usher"): "Usher",
("Flip phones", "10 Things I Hate About You", "Green Day"): "Britney Spears",
("Flip phones", "10 Things I Hate About You", "Destiny's Child"): "Britney Spears",
("Flip phones", "Lord of the Rings Trilogy", "Britney Spears"): "Green Day",
("Flip phones", "Lord of the Rings Trilogy", "Usher"): "Green Day",
("Flip phones", "Lord of the Rings Trilogy", "Green Day"): "Britney Spears",
("Flip phones", "Lord of the Rings Trilogy", "Destiny's Child"): "Usher",
("Flip phones", "13 Going On 30", "Britney Spears"): "Destiny's Child",
("Flip phones", "13 Going On 30", "Usher"): "Destiny's Child",
("Flip phones", "13 Going On 30", "Green Day"): "Britney Spears",
("Flip phones", "13 Going On 30", "Destiny's Child"): "Usher",

("MP3 players", "Mean Girls", "Britney Spears"): "Britney Spears",
("MP3 players", "Mean Girls", "Usher"): "Green Day",
("MP3 players", "Mean Girls", "Green Day"): "Destiny's Child",
("MP3 players", "Mean Girls", "Destiny's Child"): "Destiny's Child",
("MP3 players", "10 Things I Hate About You", "Britney Spears"): "Usher",
("MP3 players", "10 Things I Hate About You", "Usher"): "Usher",
("MP3 players", "10 Things I Hate About You", "Green Day"): "Britney Spears",
("MP3 players", "10 Things I Hate About You", "Destiny's Child"): "Britney Spears",
("MP3 players", "Lord of the Rings Trilogy", "Britney Spears"): "Green Day",
("MP3 players", "Lord of the Rings Trilogy", "Usher"): "Britney Spears",
("MP3 players", "Lord of the Rings Trilogy", "Green Day"): "Green Day",
("MP3 players", "Lord of the Rings Trilogy", "Destiny's Child"): "Usher",
("MP3 players", "13 Going On 30", "Britney Spears"): "Britney Spears",
("MP3 players", "13 Going On 30", "Usher"): "Green Day",
("MP3 players", "13 Going On 30", "Green Day"): "Usher",
("MP3 players", "13 Going On 30", "Destiny's Child"): "Britney Spears",

("Nintendo DS", "Mean Girls", "Britney Spears"): "Usher",
("Nintendo DS", "Mean Girls", "Usher"): "Usher",
("Nintendo DS", "Mean Girls", "Green Day"): "Green Day",
("Nintendo DS", "Mean Girls", "Destiny's Child"): "Destiny's Child",
("Nintendo DS", "10 Things I Hate About You", "Britney Spears"): "Destiny's Child",
("Nintendo DS", "10 Things I Hate About You", "Usher"): "Destiny's Child",
("Nintendo DS", "10 Things I Hate About You", "Green Day"): "Britney Spears",
("Nintendo DS", "10 Things I Hate About You", "Destiny's Child"): "Green Day",
("Nintendo DS", "Lord of the Rings Trilogy", "Britney Spears"): "Usher",
("Nintendo DS", "Lord of the Rings Trilogy", "Usher"): "Usher",
("Nintendo DS", "Lord of the Rings Trilogy", "Green Day"): "Britney Spears",
("Nintendo DS", "Lord of the Rings Trilogy", "Destiny's Child"): "Green Day",
("Nintendo DS", "13 Going On 30", "Britney Spears"): "Destiny's Child",
("Nintendo DS", "13 Going On 30", "Usher"): "Green Day",
("Nintendo DS", "13 Going On 30", "Green Day"): "Britney Spears",
("Nintendo DS", "13 Going On 30", "Destiny's Child"): "Usher",

("Digital cameras", "Mean Girls", "Britney Spears"): "Britney Spears",
("Digital cameras", "Mean Girls", "Usher"): "Usher",
("Digital cameras", "Mean Girls", "Green Day"): "Green Day",
("Digital cameras", "Mean Girls", "Destiny's Child"): "Destiny's Child",
("Digital cameras", "10 Things I Hate About You", "Britney Spears"): "Usher",
("Digital cameras", "10 Things I Hate About You", "Usher"): "Green Day",
("Digital cameras", "10 Things I Hate About You", "Green Day"): "Green Day",
("Digital cameras", "10 Things I Hate About You", "Destiny's Child"): "Britney Spears",
("Digital cameras", "Lord of the Rings Trilogy", "Britney Spears"): "Green Day",
("Digital cameras", "Lord of the Rings Trilogy", "Usher"): "Green Day",
("Digital cameras", "Lord of the Rings Trilogy", "Green Day"): "Britney Spears",
("Digital cameras", "Lord of the Rings Trilogy", "Destiny's Child"): "Britney Spears",
("Digital cameras", "13 Going On 30", "Britney Spears"): "Destiny's Child",
("Digital cameras", "13 Going On 30", "Usher"): "Destiny's Child",
("Digital cameras", "13 Going On 30", "Green Day"): "Britney Spears",
("Digital cameras", "13 Going On 30", "Destiny's Child"): "Green Day",
}

if selected_tech and selected_movie and y2k_choice:
    user_combo = (selected_tech, selected_movie, y2k_choice)
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