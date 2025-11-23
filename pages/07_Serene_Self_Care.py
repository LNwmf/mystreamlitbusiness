import streamlit as st

st.set_page_config(
    page_title="Serene Self-Care",
    page_icon="🪞",
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
st.title("🪞 Serene Self-Care")
st.markdown("""
Welcome! Pick an energy below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
""")

#Q1
st.write("Deciding to treat yourself after a long day, you...")
images = [

        "https://images.squarespace-cdn.com/content/v1/5d48448a48f65e000146a3d1/1707418465705-6D8U9Z7P1FHDL1ZIU8S4/Bubble+Bath.png?format=2500w",
        "https://www.weljii.com/wp-content/uploads/2025/03/Blog-4-3-scaled.jpg",
        "https://cdn.vox-cdn.com/thumbor/USWpDJAcNwhQQ6e0r-9ZYyCguDU=/0x0:7360x4912/1200x800/filters:focal(3092x1868:4268x3044)/cdn.vox-cdn.com/uploads/chorus_image/image/60114163/shoppingbags.0.jpg",
        "https://travelswitherica.com/wp-content/uploads/2021/05/Depositphotos_199645174_xl-2015.jpg",
]

titles=["Take a warm bath", "Go on a nature walk", "Shop at the mall", "Eat a delicious meal"]

if "selected_unwind" not in st.session_state:
    st.session_state.selected_unwind = None

cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        # Clicking the button selects this image
        if st.button(titles[i], key=f"btn_unwind_{i}"):
            st.session_state.selected_unwind = i

        # Add a red border if selected
        border = "4px solid red" if st.session_state.selected_unwind == i else "4px solid transparent"

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

selected_unwind = (
    titles[st.session_state.selected_unwind]
    if st.session_state.get("selected_unwind") is not None
    else None
)

#gap
st.write("")

#Q2
act = ["Paint or draw", "Listen to music", "Journal", "Cook new recipes"]
selected_act = st.selectbox("If you had one hour to completely relax, what activity would you do?", act, index=None)

#Q3
secret = ["Confidence", "Wonder", "Relaxation", "Magic"]
selected_secret = st.selectbox("What's the secret ingredient to feeling your absolute best?", secret, index=None)

#Q4
st.write("Pick a getaway place:")
images = [

        "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxzZWFyY2h8Mnx8YmVhY2h8ZW58MHx8MHx8fDA%3D&fm=jpg&q=60&w=3000",
        "https://previews.123rf.com/images/ncikname/ncikname1811/ncikname181100012/117447994-beautiful-landscape-on-the-mountainside-at-sunrise-time.jpg",
        "https://www.gladsbuy.com/media/catalog/product/cache/e32693469ddc6d481df161d4366da519/X/L/XLX-497_10X10.jpg",
        "https://www.green.earth/hubfs/photos/shutterstock_601970732.jpg",
]

titles=["Ambient beach", "Quiet mountainside", "Bustling city", "Lush forest"]

if "selected_getaway" not in st.session_state:
    st.session_state.selected_getaway= None

cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        # Clicking the button selects this image
        if st.button(titles[i], key=f"btn_getaway_{i}"):
            st.session_state.selected_getaway = i

        # Add a red border if selected
        border = "4px solid red" if st.session_state.selected_getaway == i else "4px solid transparent"

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

selected_getaway = (
    titles[st.session_state.selected_getaway]
    if st.session_state.get("selected_getaway") is not None
    else None
)

#gap
st.write("")

#Q5
energy_data = {
    "Glowing": {
        "playlist": "Mood: Dewy",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "business_name": "DNA Beauty Supply",
        "offer": "5% off your first purchase with this screen!",
        "booth_name": "Booth A",
        "website": "https://www.facebook.com/people/DNA-Beauty-Supply/100057497137026/",
        "business_image": "https://scontent-ord5-2.xx.fbcdn.net/v/t39.30808-6/384267987_785169260076305_2783627709022071207_n.png?_nc_cat=103&ccb=1-7&_nc_sid=cc71e4&_nc_ohc=AstFGP_v9DMQ7kNvwHoQWnf&_nc_oc=AdltzZ0X8GSFxfbQ0SH-pfABYxT09p-s9__zt1aO1Sl-LsfiNIrPqiXOM3n7Wb6mCgYw5Xjz1bCGtMMadGoLv7J1&_nc_zt=23&_nc_ht=scontent-ord5-2.xx&_nc_gid=zfCdymUeFbj-kSw49LKJRw&oh=00_AffkftEEO_9FaTrYh4OUPTg8_ZuK_RVY1eodY5y-pAFj4g&oe=68E8DCE2",
    },
    "Clear": {
    "playlist": "Drifting in the Sun",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "BIOCARE LABS",
    "offer": "Get $10 off your first purchase!",
    "booth_name": "Booth B",
    "website": "https://www.biocarelabs.com/",
    "business_image": "https://www.biocarelabs.com/cdn/shop/files/biocare-logo-black-340x125_096f22c6-3c73-46b7-86d8-d6d48a15e66a.png?v=1641779618&width=240",
    },
    "Soft": {
    "playlist": "Bubbles & Wine",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Scratch Goods",
    "offer": "Buy one, get one 5% off!",
    "booth_name": "Booth C",
    "website": "https://www.scratchgoods.com/",
    "business_image": "https://www.scratchgoods.com/cdn/shop/files/horizontal_logo_290x@2x.png?v=1732846781"
    },
    "Reflective": {
    "playlist": "Nostalgic Strings",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Yin Yang Skin Studio",
    "offer": "Get a 5% discount!",
    "booth_name": "Booth D",
    "website": "https://yinyangskinstudio.com/",
    "business_image": "https://yinyangskinstudio.com/wp-content/uploads/2024/10/YIN-YANG-CHOSEN-small-31-2048x905.png"
    },
}

info3 = None
    # Energy Selection
energy_choice = st.selectbox("How would you describe your current energy?", ["", *energy_data.keys()])

combination_map = {
    ("Take a warm bath", "Confidence", "Ambient beach", "Glowing"): "",
    ("Take a warm bath", "Confidence", "Ambient beach", "Clear"): "",
    ("Take a warm bath", "Confidence", "Ambient beach", "Soft"): "",
    ("Take a warm bath", "Confidence", "Ambient beach", "Reflective"): "",
    ("Take a warm bath", "Confidence", "Quiet mountainside", "Glowing"): "",
    ("Take a warm bath", "Confidence", "Quiet mountainside", "Clear"): "",
    ("Take a warm bath", "Confidence", "Quiet mountainside", "Soft"): "",
    ("Take a warm bath", "Confidence", "Quiet mountainside", "Reflective"): "",
    ("Take a warm bath", "Confidence", "Bustling city", "Glowing"): "",
    ("Take a warm bath", "Confidence", "Bustling city", "Clear"): "",
    ("Take a warm bath", "Confidence", "Bustling city", "Soft"): "",
    ("Take a warm bath", "Confidence", "Bustling city", "Reflective"): "",
    ("Take a warm bath", "Confidence", "Lush forest", "Glowing"): "",
    ("Take a warm bath", "Confidence", "Lush forest", "Clear"): "",
    ("Take a warm bath", "Confidence", "Lush forest", "Soft"): "",
    ("Take a warm bath", "Confidence", "Lush forest", "Reflective"): "",
    ("Take a warm bath", "Wonder", "Ambient beach", "Glowing"): "",
    ("Take a warm bath", "Wonder", "Ambient beach", "Clear"): "",
    ("Take a warm bath", "Wonder", "Ambient beach", "Soft"): "",
    ("Take a warm bath", "Wonder", "Ambient beach", "Reflective"): "",
    ("Take a warm bath", "Wonder", "Quiet mountainside", "Glowing"): "",
    ("Take a warm bath", "Wonder", "Quiet mountainside", "Clear"): "",
    ("Take a warm bath", "Wonder", "Quiet mountainside", "Soft"): "",
    ("Take a warm bath", "Wonder", "Quiet mountainside", "Reflective"): "",
    ("Take a warm bath", "Wonder", "Bustling city", "Glowing"): "",
    ("Take a warm bath", "Wonder", "Bustling city", "Clear"): "",
    ("Take a warm bath", "Wonder", "Bustling city", "Soft"): "",
    ("Take a warm bath", "Wonder", "Bustling city", "Reflective"): "",
    ("Take a warm bath", "Wonder", "Lush forest", "Glowing"): "",
    ("Take a warm bath", "Wonder", "Lush forest", "Clear"): "",
    ("Take a warm bath", "Wonder", "Lush forest", "Soft"): "",
    ("Take a warm bath", "Wonder", "Lush forest", "Reflective"): "",
    ("Take a warm bath", "Relaxation", "Ambient beach", "Glowing"): "",
    ("Take a warm bath", "Relaxation", "Ambient beach", "Clear"): "",
    ("Take a warm bath", "Relaxation", "Ambient beach", "Soft"): "",
    ("Take a warm bath", "Relaxation", "Ambient beach", "Reflective"): "",
    ("Take a warm bath", "Relaxation", "Quiet mountainside", "Glowing"): "",
    ("Take a warm bath", "Relaxation", "Quiet mountainside", "Clear"): "",
    ("Take a warm bath", "Relaxation", "Quiet mountainside", "Soft"): "",
    ("Take a warm bath", "Relaxation", "Quiet mountainside", "Reflective"): "",
    ("Take a warm bath", "Relaxation", "Bustling city", "Glowing"): "",
    ("Take a warm bath", "Relaxation", "Bustling city", "Clear"): "",
    ("Take a warm bath", "Relaxation", "Bustling city", "Soft"): "",
    ("Take a warm bath", "Relaxation", "Bustling city", "Reflective"): "",
    ("Take a warm bath", "Relaxation", "Lush forest", "Glowing"): "",
    ("Take a warm bath", "Relaxation", "Lush forest", "Clear"): "",
    ("Take a warm bath", "Relaxation", "Lush forest", "Soft"): "",
    ("Take a warm bath", "Relaxation", "Lush forest", "Reflective"): "",
    ("Take a warm bath", "Magic", "Ambient beach", "Glowing"): "",
    ("Take a warm bath", "Magic", "Ambient beach", "Clear"): "",
    ("Take a warm bath", "Magic", "Ambient beach", "Soft"): "",
    ("Take a warm bath", "Magic", "Ambient beach", "Reflective"): "",
    ("Take a warm bath", "Magic", "Quiet mountainside", "Glowing"): "",
    ("Take a warm bath", "Magic", "Quiet mountainside", "Clear"): "",
    ("Take a warm bath", "Magic", "Quiet mountainside", "Soft"): "",
    ("Take a warm bath", "Magic", "Quiet mountainside", "Reflective"): "",
    ("Take a warm bath", "Magic", "Bustling city", "Glowing"): "",
    ("Take a warm bath", "Magic", "Bustling city", "Clear"): "",
    ("Take a warm bath", "Magic", "Bustling city", "Soft"): "",
    ("Take a warm bath", "Magic", "Bustling city", "Reflective"): "",
    ("Take a warm bath", "Magic", "Lush forest", "Glowing"): "",
    ("Take a warm bath", "Magic", "Lush forest", "Clear"): "",
    ("Take a warm bath", "Magic", "Lush forest", "Soft"): "",
    ("Take a warm bath", "Magic", "Lush forest", "Reflective"): "",

("Go on a nature walk", "Confidence", "Ambient beach", "Glowing"): "",
("Go on a nature walk", "Confidence", "Ambient beach", "Clear"): "",
("Go on a nature walk", "Confidence", "Ambient beach", "Soft"): "",
("Go on a nature walk", "Confidence", "Ambient beach", "Reflective"): "",
("Go on a nature walk", "Confidence", "Quiet mountainside", "Glowing"): "",
("Go on a nature walk", "Confidence", "Quiet mountainside", "Clear"): "",
("Go on a nature walk", "Confidence", "Quiet mountainside", "Soft"): "",
("Go on a nature walk", "Confidence", "Quiet mountainside", "Reflective"): "",
("Go on a nature walk", "Confidence", "Bustling city", "Glowing"): "",
("Go on a nature walk", "Confidence", "Bustling city", "Clear"): "",
("Go on a nature walk", "Confidence", "Bustling city", "Soft"): "",
("Go on a nature walk", "Confidence", "Bustling city", "Reflective"): "",
("Go on a nature walk", "Confidence", "Lush forest", "Glowing"): "",
("Go on a nature walk", "Confidence", "Lush forest", "Clear"): "",
("Go on a nature walk", "Confidence", "Lush forest", "Soft"): "",
("Go on a nature walk", "Confidence", "Lush forest", "Reflective"): "",
("Go on a nature walk", "Wonder", "Ambient beach", "Glowing"): "",
("Go on a nature walk", "Wonder", "Ambient beach", "Clear"): "",
("Go on a nature walk", "Wonder", "Ambient beach", "Soft"): "",
("Go on a nature walk", "Wonder", "Ambient beach", "Reflective"): "",
("Go on a nature walk", "Wonder", "Quiet mountainside", "Glowing"): "",
("Go on a nature walk", "Wonder", "Quiet mountainside", "Clear"): "",
("Go on a nature walk", "Wonder", "Quiet mountainside", "Soft"): "",
("Go on a nature walk", "Wonder", "Quiet mountainside", "Reflective"): "",
("Go on a nature walk", "Wonder", "Bustling city", "Glowing"): "",
("Go on a nature walk", "Wonder", "Bustling city", "Clear"): "",
("Go on a nature walk", "Wonder", "Bustling city", "Soft"): "",
("Go on a nature walk", "Wonder", "Bustling city", "Reflective"): "",
("Go on a nature walk", "Wonder", "Lush forest", "Glowing"): "",
("Go on a nature walk", "Wonder", "Lush forest", "Clear"): "",
("Go on a nature walk", "Wonder", "Lush forest", "Soft"): "",
("Go on a nature walk", "Wonder", "Lush forest", "Reflective"): "",
("Go on a nature walk", "Relaxation", "Ambient beach", "Glowing"): "",
("Go on a nature walk", "Relaxation", "Ambient beach", "Clear"): "",
("Go on a nature walk", "Relaxation", "Ambient beach", "Soft"): "",
("Go on a nature walk", "Relaxation", "Ambient beach", "Reflective"): "",
("Go on a nature walk", "Relaxation", "Quiet mountainside", "Glowing"): "",
("Go on a nature walk", "Relaxation", "Quiet mountainside", "Clear"): "",
("Go on a nature walk", "Relaxation", "Quiet mountainside", "Soft"): "",
("Go on a nature walk", "Relaxation", "Quiet mountainside", "Reflective"): "",
("Go on a nature walk", "Relaxation", "Bustling city", "Glowing"): "",
("Go on a nature walk", "Relaxation", "Bustling city", "Clear"): "",
("Go on a nature walk", "Relaxation", "Bustling city", "Soft"): "",
("Go on a nature walk", "Relaxation", "Bustling city", "Reflective"): "",
("Go on a nature walk", "Relaxation", "Lush forest", "Glowing"): "",
("Go on a nature walk", "Relaxation", "Lush forest", "Clear"): "",
("Go on a nature walk", "Relaxation", "Lush forest", "Soft"): "",
    ("Go on a nature walk", "Relaxation", "Lush forest", "Reflective"): "",
    ("Go on a nature walk", "Magic", "Ambient beach", "Glowing"): "",
    ("Go on a nature walk", "Magic", "Ambient beach", "Clear"): "",
    ("Go on a nature walk", "Magic", "Ambient beach", "Soft"): "",
    ("Go on a nature walk", "Magic", "Ambient beach", "Reflective"): "",
    ("Go on a nature walk", "Magic", "Quiet mountainside", "Glowing"): "",
    ("Go on a nature walk", "Magic", "Quiet mountainside", "Clear"): "",
    ("Go on a nature walk", "Magic", "Quiet mountainside", "Soft"): "",
    ("Go on a nature walk", "Magic", "Quiet mountainside", "Reflective"): "",
    ("Go on a nature walk", "Magic", "Bustling city", "Glowing"): "",
    ("Go on a nature walk", "Magic", "Bustling city", "Clear"): "",
    ("Go on a nature walk", "Magic", "Bustling city", "Soft"): "",
    ("Go on a nature walk", "Magic", "Bustling city", "Reflective"): "",
    ("Go on a nature walk", "Magic", "Lush forest", "Glowing"): "",
    ("Go on a nature walk", "Magic", "Lush forest", "Clear"): "",
    ("Go on a nature walk", "Magic", "Lush forest", "Soft"): "",
    ("Go on a nature walk", "Magic", "Lush forest", "Reflective"): "",

    ("Take a warm bath", "Confidence", "Ambient beach", "Glowing"): "",
    ("Take a warm bath", "Confidence", "Ambient beach", "Clear"): "",
    ("Take a warm bath", "Confidence", "Ambient beach", "Soft"): "",
    ("Take a warm bath", "Confidence", "Ambient beach", "Reflective"): "",
    ("Take a warm bath", "Confidence", "Quiet mountainside", "Glowing"): "",
    ("Take a warm bath", "Confidence", "Quiet mountainside", "Clear"): "",
    ("Take a warm bath", "Confidence", "Quiet mountainside", "Soft"): "",
    ("Take a warm bath", "Confidence", "Quiet mountainside", "Reflective"): "",
    ("Take a warm bath", "Confidence", "Bustling city", "Glowing"): "",
    ("Take a warm bath", "Confidence", "Bustling city", "Clear"): "",
    ("Take a warm bath", "Confidence", "Bustling city", "Soft"): "",
    ("Take a warm bath", "Confidence", "Bustling city", "Reflective"): "",
    ("Take a warm bath", "Confidence", "Lush forest", "Glowing"): "",
    ("Take a warm bath", "Confidence", "Lush forest", "Clear"): "",
    ("Take a warm bath", "Confidence", "Lush forest", "Soft"): "",
    ("Take a warm bath", "Confidence", "Lush forest", "Reflective"): "",
    ("Take a warm bath", "Wonder", "Ambient beach", "Glowing"): "",
    ("Take a warm bath", "Wonder", "Ambient beach", "Clear"): "",
    ("Take a warm bath", "Wonder", "Ambient beach", "Soft"): "",
    ("Take a warm bath", "Wonder", "Ambient beach", "Reflective"): "",
    ("Take a warm bath", "Wonder", "Quiet mountainside", "Glowing"): "",
    ("Take a warm bath", "Wonder", "Quiet mountainside", "Clear"): "",
    ("Take a warm bath", "Wonder", "Quiet mountainside", "Soft"): "",
    ("Take a warm bath", "Wonder", "Quiet mountainside", "Reflective"): "",
    ("Take a warm bath", "Wonder", "Bustling city", "Glowing"): "",
    ("Take a warm bath", "Wonder", "Bustling city", "Clear"): "",
    ("Take a warm bath", "Wonder", "Bustling city", "Soft"): "",
    ("Take a warm bath", "Wonder", "Bustling city", "Reflective"): "",
    ("Take a warm bath", "Wonder", "Lush forest", "Glowing"): "",
    ("Take a warm bath", "Wonder", "Lush forest", "Clear"): "",
    ("Take a warm bath", "Wonder", "Lush forest", "Soft"): "",
    ("Take a warm bath", "Wonder", "Lush forest", "Reflective"): "",
    ("Take a warm bath", "Relaxation", "Ambient beach", "Glowing"): "",
    ("Take a warm bath", "Relaxation", "Ambient beach", "Clear"): "",
    ("Take a warm bath", "Relaxation", "Ambient beach", "Soft"): "",
    ("Take a warm bath", "Relaxation", "Ambient beach", "Reflective"): "",
    ("Take a warm bath", "Relaxation", "Quiet mountainside", "Glowing"): "",
    ("Take a warm bath", "Relaxation", "Quiet mountainside", "Clear"): "",
    ("Take a warm bath", "Relaxation", "Quiet mountainside", "Soft"): "",
    ("Take a warm bath", "Relaxation", "Quiet mountainside", "Reflective"): "",
    ("Take a warm bath", "Relaxation", "Bustling city", "Glowing"): "",
    ("Take a warm bath", "Relaxation", "Bustling city", "Clear"): "",
    ("Take a warm bath", "Relaxation", "Bustling city", "Soft"): "",
    ("Take a warm bath", "Relaxation", "Bustling city", "Reflective"): "",
    ("Take a warm bath", "Relaxation", "Lush forest", "Glowing"): "",
    ("Take a warm bath", "Relaxation", "Lush forest", "Clear"): "",
    ("Take a warm bath", "Relaxation", "Lush forest", "Soft"): "",
    ("Take a warm bath", "Relaxation", "Lush forest", "Reflective"): "",
    ("Take a warm bath", "Magic", "Ambient beach", "Glowing"): "",
    ("Take a warm bath", "Magic", "Ambient beach", "Clear"): "",
    ("Take a warm bath", "Magic", "Ambient beach", "Soft"): "",
    ("Take a warm bath", "Magic", "Ambient beach", "Reflective"): "",
    ("Take a warm bath", "Magic", "Quiet mountainside", "Glowing"): "",
    ("Take a warm bath", "Magic", "Quiet mountainside", "Clear"): "",
    ("Take a warm bath", "Magic", "Quiet mountainside", "Soft"): "",
    ("Take a warm bath", "Magic", "Quiet mountainside", "Reflective"): "",
    ("Take a warm bath", "Magic", "Bustling city", "Glowing"): "",
    ("Take a warm bath", "Magic", "Bustling city", "Clear"): "",
    ("Take a warm bath", "Magic", "Bustling city", "Soft"): "",
    ("Take a warm bath", "Magic", "Bustling city", "Reflective"): "",
    ("Take a warm bath", "Magic", "Lush forest", "Glowing"): "",
    ("Take a warm bath", "Magic", "Lush forest", "Clear"): "",
    ("Take a warm bath", "Magic", "Lush forest", "Soft"): "",
    ("Take a warm bath", "Magic", "Lush forest", "Reflective"): "",
}

if selected_unwind and selected_act and selected_secret and selected_getaway and energy_choice:
    key = (selected_unwind, selected_secret, selected_getaway, energy_choice)
    output = combination_map.get(key)

    # Display playlist and business info
    if output:
        info3 = energy_data[output]

    st.subheader(f"🎵 {info3['playlist']}")
    st.markdown(f"[Listen Here]({info3['playlist_link']})")

    # Business info display
    st.image(info3['business_image'], width=250)  # Show business image (if available)
    st.write(f"💼 **Business Name:** {info3['business_name']}")
    st.write(f"🌐 [Visit Website]({info3['website']})")
    st.write(f"🎁 **Special Offer:** {info3['offer']}")

    st.write("👥 How many people did you share your playlist with?")
    shared_count = st.number_input("Number of people:", min_value=0, step=1)

    if st.button("Check Reward Status"):
        if shared_count >= 3:
            st.balloons()  # Add some confetti for fun
            st.success(f"🎁 You unlocked a reward! Show this screen at {info3['booth_name']} to claim your prize!")
        else:
            st.warning("⏳ Share your playlist with at least 3 people to unlock your reward!")