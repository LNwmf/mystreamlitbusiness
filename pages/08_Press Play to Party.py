import streamlit as st
from st_clickable_images import clickable_images

st.set_page_config(
    page_title="Press Play to Party",
    page_icon="🎉",
    layout="centered",
)

st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("🎉 Press Play to Party")
st.markdown("""
Welcome! Pick a party trick below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
""")
st.write("")

#Q1: clickable images
st.write("Pick a classic party food:")
images = [

        "https://assets.surlatable.com/m/15a89c2d9c6c1345/72_dpi_webp-REC-283110_Pizza.jpg", #pizza, salsa and chips, chicken wings, burger, hot dog
        "https://food.fnr.sndimg.com/content/dam/images/food/fullset/2013/12/9/0/FNK_Salsa-and-Chips_s4x3.jpg.rend.hgtvcom.1280.1280.suffix/1387411410179.webp",
        "https://tastesbetterfromscratch.com/wp-content/uploads/2014/09/Baked-Chicken-Wings-3.jpg",
        "https://static01.nyt.com/images/2022/06/27/dining/kc-mushroom-beef-burgers/merlin_209008674_b3fa58fa-9bb1-4cfe-a08a-40b4dda0de78-jumbo.jpg",
        "https://www.foodandwine.com/thmb/2kinp7BXi4eE-QG8u1rLS3z_o5M=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/Hawaiian-Hot-Dog-FT-RECIPE0724-8b45189237284cf5bf8efb1e8ea9626c.jpeg",
]

titles=["Pizza", "Salsa & chips", "Chicken wings", "Burger", "Hot dog"]

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

#Q2
genre = ["Pop", "Rap/Hip-hop", "EDM", "Country", "Rock n Roll"]
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
selected_theme = titles[clicked] if clicked > -1 else None

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

combination_map = {
    ("Chaos & confetti", "Drinks!", "Karaoke master"): "Karaoke master",
    ("Chaos & confetti", "Drinks!", "Professional breakdancer"): "Karaoke master",
    ("Chaos & confetti", "Drinks!", "Magician"): "Magician",
    ("Chaos & confetti", "Drinks!", "Stage comedian"): "Stage comedian",
    ("Chaos & confetti", "Nonstop dancing", "Karaoke master"): "Professional breakdancer",
    ("Chaos & confetti", "Nonstop dancing", "Professional breakdancer"): "Karaoke master",
    ("Chaos & confetti", "Nonstop dancing", "Magician"): "Professional breakdancer",
    ("Chaos & confetti", "Nonstop dancing", "Stage comedian"): "Magician",
    ("Chaos & confetti", "Loud music", "Karaoke master"): "Karaoke master",
    ("Chaos & confetti", "Loud music", "Professional breakdancer"): "Professional breakdancer",
    ("Chaos & confetti", "Loud music", "Magician"): "Magician",
    ("Chaos & confetti", "Loud music", "Stage comedian"): "Stage comedian",
    ("Chaos & confetti", "A group selfie", "Karaoke master"): "Stage comedian",
    ("Chaos & confetti", "A group selfie", "Professional breakdancer"): "Magician",
    ("Chaos & confetti", "A group selfie", "Magician"): "Karaoke master",
    ("Chaos & confetti", "A group selfie", "Stage comedian"): "Magician",
    ("Chill rooftop", "Drinks!", "Karaoke master"): "Stage comedian",
    ("Chill rooftop", "Drinks!", "Professional breakdancer"): "Magician",
    ("Chill rooftop", "Drinks!", "Magician"): "Karaoke master",
    ("Chill rooftop", "Drinks!", "Stage comedian"): "Professional breakdancer",
    ("Chill rooftop", "Nonstop dancing", "Karaoke master"): "Stage comedian",
    ("Chill rooftop", "Nonstop dancing", "Professional breakdancer"): "Stage comedian",
    ("Chill rooftop", "Nonstop dancing", "Magician"): "Magician",
    ("Chill rooftop", "Nonstop dancing", "Stage comedian"): "Karaoke master",
    ("Chill rooftop", "Loud music", "Karaoke master"): "Magician",
    ("Chill rooftop", "Loud music", "Professional breakdancer"): "Stage comedian",
    ("Chill rooftop", "Loud music", "Magician"): "Stage comedian",
    ("Chill rooftop", "Loud music", "Stage comedian"): "Karaoke master",


}

if selected_theme and selected_complete and trick_choice:
    user_combo = (selected_theme, selected_complete, trick_choice)
    result_key = combination_map.get(user_combo)

    if result_key:
    # Retrieve information about selected drink/business
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

#st.title("Image Display based on Radio Selection")

#selected_option = st.radio(
#    "Choose an image:",
#    options=["Image A", "Image B", "Image C"]
#)

#if selected_option == "Image A":
#    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTJvbABjR5D8Ja6B51Y55dbqqL0VMW85XdV6w&s", caption="This is Image A")
#elif selected_option == "Image B":
#    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRwBNHTvWu7XJyqeE2yDf3n4ezQAHThGfxjeQ&s", caption="This is Image B")
#elif selected_option == "Image C":
#    st.image("https://sylviawakana.com/wp-content/uploads/2022/07/Taiyaki-1.jpg", caption="This is Image C")

#clickable images