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
fall_choice = st.selectbox("Pick a fall activity to get started:", ["", *business_data.keys()])

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