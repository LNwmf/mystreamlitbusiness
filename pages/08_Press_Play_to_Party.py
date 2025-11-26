import streamlit as st

st.set_page_config(
    page_title="Press Play to Party",
    page_icon="🎉",
    layout="centered",
)
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
st.title("🎉 Press Play to Party")
st.markdown("""
Welcome! Pick a party trick below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
""")
st.write("")

#Q1
st.write("Pick a classic party food: (double-click button)")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/pizza1.png",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/salsachips.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/chicken.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/burger1.jpg",
]

titles=["Pizza", "Salsa & chips", "Chicken wings", "Burger"]

if "selected_food" not in st.session_state:
    st.session_state.selected_food = None

cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        if st.button(titles[i], key=f"btn_food_{i}"):
            st.session_state.selected_food = i

        border = "4px solid red" if st.session_state.selected_food == i else "4px solid transparent"

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

selected_food = (
    titles[st.session_state.selected_food]
    if st.session_state.get("selected_food") is not None
    else None
)

#gap
st.write("")

#Q2
genre = ["Reggae", "Carnatic", "Bachata", "Blues"]
selected_genre = st.selectbox("Which music genre would you prefer?", genre, index=None)

#Q3
st.write("Pick a theme for the night: (double-click button)")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/confettichaos.jpg",
        "",
        "",
        "",
        "",
]

titles=["Chaos & confetti", "Chill rooftop", "Holiday fun", "Family gathering", "Formal makeover"]

if "selected_theme" not in st.session_state:
    st.session_state.selected_theme = None

cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        if st.button(titles[i], key=f"btn_theme_{i}"):
            st.session_state.selected_theme = i

        border = "4px solid red" if st.session_state.selected_theme == i else "4px solid transparent"

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

selected_theme = (
    titles[st.session_state.selected_theme]
    if st.session_state.get("selected_theme") is not None
    else None
)
#gap
st.write("")

#Q4
complete = ["Drinks!", "Nonstop dancing", "Loud music", "A group selfie"]
selected_complete = st.selectbox("No party is complete without:", complete, index=None)

#Q5
trick_data = {
    "Karaoke master": {
        "playlist": "Throwback Classics",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "business_name": "Birdies Sports Bar & Grill",
        "offer": "$5 off your drinks!",
        "booth_name": "Booth A",
        "website": "https://www.birdies111.com/",
        "business_image": "https://lirp.cdn-website.com/a1e30411/dms3rep/multi/opt/birdies-logo-199w.png",
    },
    "Professional breakdancer": {
    "playlist": "Like No One's Watching",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Dance Center of LaGrange",
    "offer": "$10 off your first class!",
    "booth_name": "Booth B",
    "website": "https://www.dclagrange.com/",
    "business_image": "https://static.wixstatic.com/media/6b5ba9_a48e15c2f68349d083a7dbbe559cdc4a~mv2.png/v1/fill/w_344,h_376,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/image1.png",
    },
    "Magician": {
    "playlist": "Now You See Me, Now You Don't",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "LaGrange Art League",
    "offer": "$5 off your first class with this screen!",
    "booth_name": "Booth C",
    "website": "https://www.lagrangeartleague.org/",
    "business_image": "https://www.lagrangeartleague.org/cdn/shop/files/LGAL_Logo-New.png?v=1738705768&width=450"
    },
    "Stage comedian": {
    "playlist": "Turn Up the Vibes!",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "LIV Entertainment",
    "offer": "Get a 5% discount off your first booking!",
    "booth_name": "Booth D",
    "website": "https://liventertainment.co/",
    "business_image": "https://liventertainment.co/wp-content/uploads/2024/12/Logo-transperancy.png"
    },
}

info = None
    # Trick Selection
trick_choice = st.selectbox("What's your go-to party trick?", ["", *trick_data.keys()])

party_map = {
    ("Reggae", "Chaos & confetti", "Karaoke master"): "Karaoke master",
    ("Reggae", "Chaos & confetti", "Professional breakdancer"): "Stage comedian",
    ("Reggae", "Chaos & confetti", "Magician"): "Professional breakdancer",
    ("Reggae", "Chaos & confetti", "Stage comedian"): "Magician",
    ("Reggae", "Chill rooftop", "Karaoke master"): "Stage comedian",
    ("Reggae", "Chill rooftop", "Professional breakdancer"): "Magician",
    ("Reggae", "Chill rooftop", "Magician"): "Professional breakdancer",
    ("Reggae", "Chill rooftop", "Stage comedian"): "Karaoke master",
    ("Reggae", "Holiday fun", "Karaoke master"): "Professional breakdancer",
    ("Reggae", "Holiday fun", "Professional breakdancer"): "Karaoke master",
    ("Reggae", "Holiday fun", "Magician"): "Stage comedian",
    ("Reggae", "Holiday fun", "Stage comedian"): "Magician",
    ("Reggae", "Family gathering", "Karaoke master"): "Karaoke master",
    ("Reggae", "Family gathering", "Professional breakdancer"): "Magician",
    ("Reggae", "Family gathering", "Magician"): "Stage comedian",
    ("Reggae", "Family gathering", "Stage comedian"): "Professional breakdancer",

    ("Carnatic", "Chaos & confetti", "Karaoke master"): "Karaoke master",
    ("Carnatic", "Chaos & confetti", "Professional breakdancer"): "Professional breakdancer",
    ("Carnatic", "Chaos & confetti", "Magician"): "Magician",
    ("Carnatic", "Chaos & confetti", "Stage comedian"): "Stage comedian",
    ("Carnatic", "Chill rooftop", "Karaoke master"): "Magician",
    ("Carnatic", "Chill rooftop", "Professional breakdancer"): "Stage comedian",
    ("Carnatic", "Chill rooftop", "Magician"): "Stage comedian",
    ("Carnatic", "Chill rooftop", "Stage comedian"): "Karaoke master",
    ("Carnatic", "Holiday fun", "Karaoke master"): "Professional breakdancer",
    ("Carnatic", "Holiday fun", "Professional breakdancer"): "Stage comedian",
    ("Carnatic", "Holiday fun", "Magician"): "Magician",
    ("Carnatic", "Holiday fun", "Stage comedian"): "Stage comedian",
    ("Carnatic", "Family gathering", "Karaoke master"): "Karaoke master",
    ("Carnatic", "Family gathering", "Professional breakdancer"): "Stage comedian",
    ("Carnatic", "Family gathering", "Magician"): "Professional breakdancer",
    ("Carnatic", "Family gathering", "Stage comedian"): "Karaoke master",

    ("Bachata", "Chaos & confetti", "Karaoke master"): "Professional breakdancer",
    ("Bachata", "Chaos & confetti", "Professional breakdancer"): "Magician",
    ("Bachata", "Chaos & confetti", "Magician"): "Karaoke master",
    ("Bachata", "Chaos & confetti", "Stage comedian"): "Stage comedian",
    ("Bachata", "Chill rooftop", "Karaoke master"): "Magician",
    ("Bachata", "Chill rooftop", "Professional breakdancer"): "Magician",
    ("Bachata", "Chill rooftop", "Magician"): "Karaoke master",
    ("Bachata", "Chill rooftop", "Stage comedian"): "Professional breakdancer",
    ("Bachata", "Holiday fun", "Karaoke master"): "Stage comedian",
    ("Bachata", "Holiday fun", "Professional breakdancer"): "Magician",
    ("Bachata", "Holiday fun", "Magician"): "Professional breakdancer",
    ("Bachata", "Holiday fun", "Stage comedian"): "Karaoke master",
    ("Bachata", "Family gathering", "Karaoke master"): "Stage comedian",
    ("Bachata", "Family gathering", "Professional breakdancer"): "Magician",
    ("Bachata", "Family gathering", "Magician"): "Professional breakdancer",
    ("Bachata", "Family gathering", "Stage comedian"): "Karaoke master",

    ("Blues", "Chaos & confetti", "Karaoke master"): "Professional breakdancer",
    ("Blues", "Chaos & confetti", "Professional breakdancer"): "Magician",
    ("Blues", "Chaos & confetti", "Magician"): "Karaoke master",
    ("Blues", "Chaos & confetti", "Stage comedian"): "Stage comedian",
    ("Blues", "Chill rooftop", "Karaoke master"): "Magician",
    ("Blues", "Chill rooftop", "Professional breakdancer"): "Magician",
    ("Blues", "Chill rooftop", "Magician"): "Professional breakdancer",
    ("Blues", "Chill rooftop", "Stage comedian"): "Stage comedian",
    ("Blues", "Holiday fun", "Karaoke master"): "Stage comedian",
    ("Blues", "Holiday fun", "Professional breakdancer"): "Magician",
    ("Blues", "Holiday fun", "Magician"): "Professional breakdancer",
    ("Blues", "Holiday fun", "Stage comedian"): "Magician",
    ("Blues", "Family gathering", "Karaoke master"): "Karaoke master",
    ("Blues", "Family gathering", "Professional breakdancer"): "Professional breakdancer",
    ("Blues", "Family gathering", "Magician"): "Magician",
    ("Blues", "Family gathering", "Stage comedian"): "Stage comedian",
}

if selected_food and selected_genre and selected_theme and selected_complete and trick_choice:
    user_combo = (selected_genre, selected_theme, trick_choice)
    result_key = party_map.get(user_combo)

    if result_key:
        info = trick_data[result_key]

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

