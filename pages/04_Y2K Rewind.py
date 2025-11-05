import streamlit as st
from st_clickable_images import clickable_images

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
st.write("What Y2K tech do you miss the most?")
images = [

        "https://m.media-amazon.com/images/I/61-mqYsNMEL.jpg",
        "https://retrospekt.com/cdn/shop/files/MP-VR-1006_1-newphones.jpg?v=1719506839&width=3000",
        "https://media.gameshop.se/wp-content/uploads/2019/10/01010522/37635.jpg",
        "https://i.etsystatic.com/57193956/r/il/5ec242/6867084797/il_fullxfull.6867084797_ed68.jpg",
]

titles=["Flip phones", "MP3 players", "Nintendo DS", "Digital cameras"]

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
selected_tech = titles[clicked] if clicked > -1 else None

#Q2
trend = ["Tracksuit with rhinestones", "Chunky sunglasses", "Denim on denim", "Trucker hats"]
selected_trend = st.selectbox("Pick a 2000s fashion trend:", trend, index=None)

#Q3
movie_options = ["Mean Girls", "10 Things I Hate About You", "Lord of the Rings Trilogy", "13 Going On 30"]
selected_movie = st.selectbox("If you were teleported into a movie, which one would you prefer to be in?", movie_options, index=None)

#Q4
ppl_data = {
    "Cyber kid": {
    "ppl_image": "https://preview.redd.it/i50tlz0frw881.jpg?width=640&crop=smart&auto=webp&s=b2ca22d81b586b8af2ed79b3cbbcbabe08426749",
    },
    "Pop princess": {
    "ppl_image": "https://www.lemon8-app.com/seo/image?item_id=7455214455610278443&index=8&sign=43ec144c3e2ad90e5330db38c2f0458a",
    },
    "Fashion icon": {
    "ppl_image": "https://media.glamourmagazine.co.uk/photos/633d964a11a32370a8bb3b9e/4:3/w_1920,h_1440,c_limit/Y2K%20TRENDS%20051022%20SQUARE.jpg"
    },
    "Chill surfer": {
    "ppl_image": "https://i.pinimg.com/236x/78/69/2e/78692ec92ddeae0a4d83424f34f29206.jpg"
    },
}
selected_ppl = st.selectbox("Which Y2K character are you?", ["", *ppl_data.keys()])

if selected_ppl:
    info2 = ppl_data[selected_ppl]
    st.image(info2['ppl_image'], width=250)
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