import streamlit as st
from st_clickable_images import clickable_images

st.set_page_config(
    page_title="Sweet Melodies",
    page_icon="🍬",
    layout="centered",
)

st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("🍬 Sweet Melodies")
st.markdown("""
Welcome! Pick a dessert below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
""")

#Q1
st.write("Select a flavor:")
images = [

        "https://www.thespruceeats.com/thmb/FhHcgQni8lgV0griUeDJMTAszxI=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/chocolate_hero1-d62e5444a8734f8d8fe91f5631d51ca5.jpg", #confetti, chill rooftop, chicken wings, burger, hot dog
        "https://images.prismic.io/bareblends/4becbce8-cc6e-4292-a25c-93d6136a5df7_vanilla+bean+hero.jpg?auto=compress%2Cformat&width=1920&height=800&crop=center",
        "https://clv.h-cdn.co/assets/15/22/2048x2048/square-1432664914-strawberry-facts1.jpg",
        "https://daylighthilliard.com/wp-content/uploads/2021/04/great-coffee-bean.jpeg",
]

titles=["Chocolate", "Vanilla", "Strawberry", "Coffee"]

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
selected_flavor = titles[clicked] if clicked > -1 else None


#Q2
time_options = ["After a morning run", "Late night cravings", "During special occasions", "All day, everyday"]
selected_time = st.selectbox("Best time to have dessert:", time_options, index=None)

#Q3
life_options = ["Layers of experience", "Bittersweet spices", "A tough shell but soft center", "Unexpected textures"]
selected_life = st.selectbox("If your life were a dessert, what would it be made of?", life_options, index=None)

#Q4
st.write("What season defines you?")
images = [

        "https://content.thriveglobal.com/wp-content/uploads/2020/06/summer.jpg",
        "https://watchandlearn.scholastic.com/content/dam/classroom-magazines/watchandlearn/videos/earth-and-space/seasons/signs-of-winter/english/wall-2018-signsofwintermp4.transform/content-tile-large/image.png",
        "https://www.abc27.com/wp-content/uploads/sites/55/2022/03/GettyImages-1130636356.jpg?w=1280",
        "https://images.pexels.com/photos/33109/fall-autumn-red-season.jpg?cs=srgb&dl=pexels-pixabay-33109.jpg&fm=jpg",
]

titles=["Summer", "Winter", "Spring", "Autumn"]

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
selected_season = titles[clicked] if clicked > -1 else None


# Business options and related data
dessert_data = {
    "Flan": {
        "playlist": "Dancing Jelly",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "business_name": "Tapas Valencia",
        "offer": "10% off your first order with this screen!",
        "booth_name": "Booth A",
        "website": "https://www.tapasvalencia.com/",
        "business_image": "https://www.tapasvalencia.com/wp-content/uploads/2017/08/Valencia-TRANSPARENT.png",
    },
    "Souffle": {
    "playlist": "Pastries & Strings",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Petite Vie Brasserie",
    "offer": "Buy 1 Combo, Get 1 Free Chicken Sandwich with this screen.",
    "booth_name": "Booth B",
    "website": "https://www.petite-vie.com/",
    "business_image": "https://images.squarespace-cdn.com/content/v1/652e9491cec326539e621efe/2d266898-08ee-4747-8242-8a59a020b47b/large+white+backless.png?format=1000w",
    },
    "Taiyaki": {
    "playlist": "Chill J-Rock",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Izakaya",
    "offer": "5% off your drink order!",
    "booth_name": "Booth C",
    "website": "https://www.momotarochicago.com/izakaya",
    "business_image": "https://cdn.prod.website-files.com/621e6fe3c0a99283c0cc87fb/65f86e09a6e239d1ffac94dd_zakaya-Logo-black-Transparent.svg"
    },
    "Mandazi": {
    "playlist": "Reggaeton Fusions",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "SAMIFLORENCIA AFRICAN CUISINE",
    "offer": "Get 1 free appetizer with your order!",
    "booth_name": "Booth D",
    "website": "https://samiflorenciacatering.com/",
    "business_image": "https://samiflorenciacatering.com/wp-content/uploads/2024/02/Florencia-logo.jpg.webp"
    },
}

info = None
    # Dessert Selection
dessert_choice = st.selectbox("Pick a dessert!", ["", *dessert_data.keys()])

dessert_map = {

}









if selected_flavor and selected_life and dessert_choice:
    user_combo = (selected_flavor, selected_life, dessert_choice)
    result_key = dessert_map.get(user_combo)
    # Retrieve information about selected drink/business
    if result_key:
        info = dessert_data[result_key]



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