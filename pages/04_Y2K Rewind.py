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

#Q1
tech_type = ["Flip phones", "MP3 players", "Nintendo DS", "Digital cameras"]
selected_tech = st.selectbox("What Y2K tech do you miss the most?", tech_type, index=None)

#Q2
trend_data = {
    "Tracksuit with rhinestones": {
    "trend_image": "https://di2ponv0v5otw.cloudfront.net/posts/2025/01/26/679710d59a76ef110dc078e5/m_679710dfd3309f00594c1daf.jpg",
    },
    "Chunky sunglasses": {
    "trend_image": "https://charmingcharlie.com/cdn/shop/files/C3-2_ecf75579-4d56-4c77-99b5-7a25d26bb20e.jpg?v=1719575450&width=800",
    },
    "Denim on denim": {
    "trend_image": "https://finesse.us/cdn/shop/files/1_0dd49d3d-de01-4c55-a7f8-3454e02e5dcf.jpg?v=1738924628&width=1946"
    },
    "Trucker hats": {
    "trend_image": "https://scene7.zumiez.com/is/image/zumiez/product_main_medium/Empyre-Y2K-Black-Trucker-Hat-_382120.jpg"
    },
}
selected_trend = st.selectbox("Pick a 2000s fashion trend:", ["", *trend_data.keys()])

if selected_trend:
    info1 = trend_data[selected_trend]

    st.image(info1['trend_image'], width=250)
#Q3
movie_options = ["Mean Girls", "10 Things I Hate About You", "Lord of the Rings Trilogy", "13 Going On 30"]
selected_movie = st.selectbox("If you were teleported into a movie, which one would you prefer to be in?", movie_options, index=None)

#Q4 cyber kid, pop princess, tv junkie, chill surfer
char_data = {
    "Cyber kid": {
    "char_image": "https://static.wikia.nocookie.net/aesthetics/images/0/0c/Y2K_Futurism.png/revision/latest/scale-to-width-down/1000?cb=20250831170930",
    },
    "Pop princess": {
    "char_image": "https://www.lemon8-app.com/seo/image?item_id=7455214455610278443&index=8&sign=43ec144c3e2ad90e5330db38c2f0458a",
    },
    "Fashion icon": {
    "char_image": "https://media.glamourmagazine.co.uk/photos/633d964a11a32370a8bb3b9e/4:3/w_1920,h_1440,c_limit/Y2K%20TRENDS%20051022%20SQUARE.jpg"
    },
    "Chill surfer": {
    "char_image": "https://static.wikia.nocookie.net/aesthetics/images/b/ba/Surfer.webp/revision/latest?cb=20250515104627"
    },
}
selected_char = st.selectbox("Which Y2K character are you?", ["", *char_data.keys()])

if selected_trend:
    info2 = char_data[selected_char]

    st.image(info2['char_image'], width=250)

# Business options and related data
business_data = {
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
    # Dessert Selection
y2k_choice = st.selectbox("Pick an artist!", ["", *business_data.keys()])

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