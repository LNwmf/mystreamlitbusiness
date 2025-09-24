import streamlit as st

st.set_page_config(
    page_title="Y2K Rewind",
    page_icon="💿",
    layout="centered",
)

st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("💿 Y2K Rewind")
st.markdown("""
Welcome! Pick a 2000s music artist below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
""")

# Business options and related data
business_data = {
    "Britney Spears": {
        "playlist": "Oop...I did it again",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "business_name": "Tapas Valencia",
        "offer": "10% off your first order with this screen!",
        "booth_name": "Booth A",
        "website": "https://www.tapasvalencia.com/",
        "business_image": "https://www.tapasvalencia.com/wp-content/uploads/2017/08/Valencia-TRANSPARENT.png",
    },
    "Usher": {
    "playlist": "Smooth Grooves",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Petite Vie Brasserie",
    "offer": "Buy 1 Combo, Get 1 Free Chicken Sandwich with this screen.",
    "booth_name": "Booth B",
    "website": "https://www.petite-vie.com/",
    "business_image": "https://images.squarespace-cdn.com/content/v1/652e9491cec326539e621efe/2d266898-08ee-4747-8242-8a59a020b47b/large+white+backless.png?format=1000w",
    },
    "Green Day": {
    "playlist": "Amped Up",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Izakaya",
    "offer": "5% off your drink order!",
    "booth_name": "Booth C",
    "website": "https://www.momotarochicago.com/izakaya",
    "business_image": "https://cdn.prod.website-files.com/621e6fe3c0a99283c0cc87fb/65f86e09a6e239d1ffac94dd_zakaya-Logo-black-Transparent.svg"
    },
    "Destiny's Child": {
    "playlist": "Off the Charts Pop",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "SAMIFLORENCIA AFRICAN CUISINE",
    "offer": "Get 1 free appetizer with your order!",
    "booth_name": "Booth D",
    "website": "https://samiflorenciacatering.com/",
    "business_image": "https://samiflorenciacatering.com/wp-content/uploads/2024/02/Florencia-logo.jpg.webp"
    },
}
    # Dessert Selection
y2k_choice = st.selectbox("Pick an artist to get started:", ["", *business_data.keys()])

if y2k_choice:
    # Retrieve information about selected drink/business
    info = business_data[y2k_choice]

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