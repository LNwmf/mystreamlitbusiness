import streamlit as st

st.set_page_config(
    page_title="Sweater Weather Tunes",
    page_icon="🍂",
    layout="centered",
)

st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("🍂 Sweater Weather Tunes")
st.markdown("""
Welcome! Pick a fall activity below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
""")

#Q1
falldrink_options = ["Apple cider", "Pumpkin spice latte", "Chai", "Hot chocolate"]
selected_fall = st.selectbox("Select a Fall Drink:", falldrink_options, index=None)
drink_data = {
    "Apple cider": {
    "drink_image": "https://sallysbakingaddiction.com/wp-content/uploads/2015/09/homemade-apple-cider-1.jpg",
    },
    "Pumpkin spice latte": {
    "drink_image": "https://joyfullymad.com/wp-content/uploads/2024/10/pumpkin-spice-latte-8.jpg",
    },
    "Chai": {
    "drink_image": "https://www.allrecipes.com/thmb/MCdBf6nSW7JVmpdFbc8LeaxWYAQ=/1500x0/filters:no_upscale():max_bytes(150000):strip_icc()/222513-chai-tea-latte-ddmfs-3x4-13181362-b0a92ea6efb442a4b8b7c240a7bfa9f4.jpg"
    },
    "Hot chocolate": {
    "drink_image": "https://assets.epicurious.com/photos/672aa2e70dd597529f332818/4:3/w_4444,h_3333,c_limit/hot-cocoa-vs-hot-chocolate_RECIPE_V1_103124_7088_VOG_final.jpg"
    },
}
selected_drink = st.selectbox("Which Halloween movie is your go-to?", ["", *drink_data.keys()])

if selected_drink:
    info1 = drink_data[selected_drink]

    st.image(info1['drink_image'], width=250)
#Q2
film_data = {
    "Hocus Pocus": {
    "film_image": "https://static.wikia.nocookie.net/hocuspocus/images/4/47/Hocus_Pocus_poster_2.jpg/revision/latest/scale-to-width-down/1200?cb=20220911122635",
    },
    "Halloween": {
    "film_image": "https://images.plex.tv/photo?size=large-1280&url=https%3A%2F%2Fmetadata-static.plex.tv%2Fc%2Fgracenote%2Fc990f672e727f896bb52529043bec1c0.jpg",
    },
    "Trick 'r Treat": {
    "film_image": "https://images.fathomevents.com/image/upload/w_1200,dpr_2,f_auto,q_auto/v1757097985/Events/2025/2083/Fathom%20Ticket%20Page%20Poster%20%20Press%20Kit_1000x1480%20%28No%20Text%29.png.png"
    },
    "IT": {
    "film_image": "https://upload.wikimedia.org/wikipedia/en/5/5a/It_%282017%29_poster.jpg"
    },
}
selected_film = st.selectbox("Which Halloween movie is your go-to?", ["", *film_data.keys()])

if selected_film:
    info2 = film_data[selected_film]

    st.image(info2['film_image'], width=250)
#Q3
element_options = ["Falling leaves", "Long spooky nights", "Crackling fire", "Foggy skies"]
selected_element = st.selectbox("What fall element speaks to you the most?", element_options, index=None)

#Q4
spent = ["Alone", "With family and friends", "In nature", "In love"]
selected_spent = st.selectbox("Fall is best spent...", spent, index=None)

# Business options and related data
business_data = {
    "Pumpkin Carving": {
        "playlist": "Chilly Orchards",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "business_name": "Alwatan Bakery",
        "offer": "10% off your first order with this screen!",
        "booth_name": "Booth A",
        "website": "https://www.alwatanbakery.com/",
        "business_image": "",
    },
    "Apple Picking": {
    "playlist": "Good Ol' Times",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Chuck's Southern Comforts Cafe",
    "offer": "Buy 1 Combo, Get 1 Free Appetizer with this screen.",
    "booth_name": "Booth B",
    "website": "https://chuckscafe.com/",
    "business_image": "https://d1w7312wesee68.cloudfront.net/DDMPmNmtnrUxz1PxVDTze2OFtR-QuWFhVWx-Dg15aYo/ext:webp/quality:85/preset:xxl/plain/s3://toast-sites-resources-prod/restaurantImages/1f14af1d-c8f7-4b8b-9d8a-480dbaba7333/restaurant_1592420555.png",
    },
    "Trick or Treating": {
    "playlist": "Dark Blues",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Patch Party Club",
    "offer": "5% off your purchase!",
    "booth_name": "Booth C",
    "website": "https://patchpartyclub.com/",
    "business_image": "https://patchpartyclub.com/cdn/shop/files/logo_180x.png?v=1630341909"
    },
    "Bonfires": {
    "playlist": "Jazz & Smores",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "",
    "offer": "Get 5% off a selected candle!",
    "booth_name": "Booth D",
    "website": "https://civinte.com/",
    "business_image": "https://civinte.com/cdn/shop/files/2025_Logo_180x@2x.png?v=1747978532"
    },
}
    # Activity Selection
fall_choice = st.selectbox("Pick a fall activity!", ["", *business_data.keys()])

if fall_choice:
    # Retrieve information about selected drink/business
    info = business_data[fall_choice]

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