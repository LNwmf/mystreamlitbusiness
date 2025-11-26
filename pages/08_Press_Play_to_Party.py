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

        "https://assets.surlatable.com/m/15a89c2d9c6c1345/72_dpi_webp-REC-283110_Pizza.jpg", #pizza, salsa and chips, chicken wings, burger, hot dog
        "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2013/12/9/0/FNK_Salsa-and-Chips_s4x3.jpg.rend.hgtvcom.1280.1280.suffix/1387411410179.webp",
        "https://tastesbetterfromscratch.com/wp-content/uploads/2014/09/Baked-Chicken-Wings-3.jpg",
        "https://static01.nyt.com/images/2022/06/27/dining/kc-mushroom-beef-burgers/merlin_209008674_b3fa58fa-9bb1-4cfe-a08a-40b4dda0de78-jumbo.jpg",
        "https://www.foodandwine.com/thmb/2kinp7BXi4eE-QG8u1rLS3z_o5M=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Hawaiian-Hot-Dog-FT-RECIPE0724-8b45189237284cf5bf8efb1e8ea9626c.jpeg",
]

titles=["Pizza", "Salsa & chips", "Chicken wings", "Burger", "Hot dog"]

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
st.write("Pick a theme for the night:")
images = [

        "https://thumbs.dreamstime.com/b/young-party-cheerful-people-showered-confetti-club-31137048.jpg", #confetti, chill rooftop, chicken wings, burger, hot dog
        "https://images.stockcake.com/public/c/e/1/ce1b2237-6357-4c04-a757-f6482dfb2acc_large/evening-rooftop-party-stockcake.jpg",
        "https://www.gigsalad.com/blog/wp-content/uploads/2022/12/iStock-539471504.jpg",
        "https://koa.com/blog/images/family-at-the-grill.jpg?preset=heroimagecropped",
        "https://cdn.shopify.com/s/files/1/0042/0390/5136/files/elegant-people.jpg?v=1697615969",
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
    ("Reggae", "Chaos & confetti", "Karaoke master"): "",
    ("Reggae", "Chaos & confetti", "Professional breakdancer"): "",
    ("Reggae", "Chaos & confetti", "Magician"): "",
    ("Reggae", "Chaos & confetti", "Stage comedian"): "",
    ("Reggae", "Chill rooftop", "Karaoke master"): "",
    ("Reggae", "Chill rooftop", "Professional breakdancer"): "",
    ("Reggae", "Chill rooftop", "Magician"): "",
    ("Reggae", "Chill rooftop", "Stage comedian"): "",
    ("Reggae", "Holiday fun", "Karaoke master"): "",
    ("Reggae", "Holiday fun", "Professional breakdancer"): "",
    ("Reggae", "Holiday fun", "Magician"): "",
    ("Reggae", "Holiday fun", "Stage comedian"): "",
    ("Reggae", "Family gathering", "Karaoke master"): "",
    ("Reggae", "Family gathering", "Professional breakdancer"): "",
    ("Reggae", "Family gathering", "Magician"): "",
    ("Reggae", "Family gathering", "Stage comedian"): "",

    ("Carnatic", "Chaos & confetti", "Karaoke master"): "",
    ("Carnatic", "Chaos & confetti", "Professional breakdancer"): "",
    ("Carnatic", "Chaos & confetti", "Magician"): "",
    ("Carnatic", "Chaos & confetti", "Stage comedian"): "",
    ("Carnatic", "Chill rooftop", "Karaoke master"): "",
    ("Carnatic", "Chill rooftop", "Professional breakdancer"): "",
    ("Carnatic", "Chill rooftop", "Magician"): "",
    ("Carnatic", "Chill rooftop", "Stage comedian"): "",
    ("Carnatic", "Holiday fun", "Karaoke master"): "",
    ("Carnatic", "Holiday fun", "Professional breakdancer"): "",
    ("Carnatic", "Holiday fun", "Magician"): "",
    ("Carnatic", "Holiday fun", "Stage comedian"): "",
    ("Carnatic", "Family gathering", "Karaoke master"): "",
    ("Carnatic", "Family gathering", "Professional breakdancer"): "",
    ("Carnatic", "Family gathering", "Magician"): "",
    ("Carnatic", "Family gathering", "Stage comedian"): "",

    ("Bachata", "Chaos & confetti", "Karaoke master"): "",
    ("Bachata", "Chaos & confetti", "Professional breakdancer"): "",
    ("Bachata", "Chaos & confetti", "Magician"): "",
    ("Bachata", "Chaos & confetti", "Stage comedian"): "",
    ("Bachata", "Chill rooftop", "Karaoke master"): "",
    ("Bachata", "Chill rooftop", "Professional breakdancer"): "",
    ("Bachata", "Chill rooftop", "Magician"): "",
    ("Bachata", "Chill rooftop", "Stage comedian"): "",
    ("Bachata", "Holiday fun", "Karaoke master"): "",
    ("Bachata", "Holiday fun", "Professional breakdancer"): "",
    ("Bachata", "Holiday fun", "Magician"): "",
    ("Bachata", "Holiday fun", "Stage comedian"): "",
    ("Bachata", "Family gathering", "Karaoke master"): "",
    ("Bachata", "Family gathering", "Professional breakdancer"): "",
    ("Bachata", "Family gathering", "Magician"): "",
    ("Bachata", "Family gathering", "Stage comedian"): "",

    ("Blues", "Chaos & confetti", "Karaoke master"): "",
    ("Blues", "Chaos & confetti", "Professional breakdancer"): "",
    ("Blues", "Chaos & confetti", "Magician"): "",
    ("Blues", "Chaos & confetti", "Stage comedian"): "",
    ("Blues", "Chill rooftop", "Karaoke master"): "",
    ("Blues", "Chill rooftop", "Professional breakdancer"): "",
    ("Blues", "Chill rooftop", "Magician"): "",
    ("Blues", "Chill rooftop", "Stage comedian"): "",
    ("Blues", "Holiday fun", "Karaoke master"): "",
    ("Blues", "Holiday fun", "Professional breakdancer"): "",
    ("Blues", "Holiday fun", "Magician"): "",
    ("Blues", "Holiday fun", "Stage comedian"): "",
    ("Blues", "Family gathering", "Karaoke master"): "",
    ("Blues", "Family gathering", "Professional breakdancer"): "",
    ("Blues", "Family gathering", "Magician"): "",
    ("Blues", "Family gathering", "Stage comedian"): "",
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

