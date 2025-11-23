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
    ("Taking a warm bath", "Confidence", "Glowing"): "Glowing",
    ("Taking a warm bath", "Confidence", "Clear"): "Soft",
    ("Taking a warm bath", "Confidence", "Soft"): "Soft",
    ("Taking a warm bath", "Confidence", "Reflective"): "Clear",
    ("Taking a warm bath", "Wonder", "Glowing"): "Reflective",
    ("Taking a warm bath", "Wonder", "Clear"): "Glowing",
    ("Taking a warm bath", "Wonder", "Soft"): "Soft",
    ("Taking a warm bath", "Wonder", "Reflective"): "Clear",
    ("Taking a warm bath", "Relaxation", "Glowing"): "Clear",
    ("Taking a warm bath", "Relaxation", "Clear"): "Glowing",
    ("Taking a warm bath", "Relaxation", "Soft"): "Clear",
    ("Taking a warm bath", "Relaxation", "Reflective"): "Clear",
    ("Taking a warm bath", "Magic", "Glowing"): "Clear",
    ("Taking a warm bath", "Magic", "Clear"): "Glowing",
    ("Taking a warm bath", "Magic", "Soft"): "Reflective",
    ("Taking a warm bath", "Magic", "Reflective"): "Soft",
    ("Going on a nature walk", "Confidence", "Glowing"): "Clear",
    ("Going on a nature walk", "Confidence", "Clear"): "Reflective",
    ("Going on a nature walk", "Confidence", "Soft"): "Soft",
    ("Going on a nature walk", "Confidence", "Reflective"): "Clear",
    ("Going on a nature walk", "Wonder", "Glowing"): "Clear",
    ("Going on a nature walk", "Wonder", "Clear"): "Soft",
    ("Going on a nature walk", "Wonder", "Soft"): "Reflective",
    ("Going on a nature walk", "Wonder", "Reflective"): "Soft",
    ("Going on a nature walk", "Relaxation", "Glowing"): "Reflective",
    ("Going on a nature walk", "Relaxation", "Clear"): "Clear",
    ("Going on a nature walk", "Relaxation", "Soft"): "Glowing",
    ("Going on a nature walk", "Relaxation", "Reflective"): "Soft",
    ("Going on a nature walk", "Magic", "Glowing"): "Glowing",
    ("Going on a nature walk", "Magic", "Clear"): "Clear",
    ("Going on a nature walk", "Magic", "Soft"): "Reflective",
    ("Going on a nature walk", "Magic", "Reflective"): "Clear",
    ("Listening to music", "Confidence", "Glowing"): "Glowing",
    ("Listening to music", "Confidence", "Clear"): "Soft",
    ("Listening to music", "Confidence", "Soft"): "Clear",
    ("Listening to music", "Confidence", "Reflective"): "Clear",
    ("Listening to music", "Wonder", "Glowing"): "Soft",
    ("Listening to music", "Wonder", "Clear"): "Soft",
    ("Listening to music", "Wonder", "Soft"): "Reflective",
    ("Listening to music", "Wonder", "Reflective"): "Glowing",
    ("Listening to music", "Relaxation", "Glowing"): "Reflective",
    ("Listening to music", "Relaxation", "Clear"): "Soft",
    ("Listening to music", "Relaxation", "Soft"): "Glowing",
    ("Listening to music", "Relaxation", "Reflective"): "Clear",
    ("Listening to music", "Magic", "Glowing"): "Reflective",
    ("Listening to music", "Magic", "Clear"): "Reflective",
    ("Listening to music", "Magic", "Soft"): "Glowing",
    ("Listening to music", "Magic", "Reflective"): "Clear",
    ("Treating myself to a meal", "Confidence", "Glowing"): "Glowing",
    ("Treating myself to a meal", "Confidence", "Clear"): "Glowing",
    ("Treating myself to a meal", "Confidence", "Soft"): "Clear",
    ("Treating myself to a meal", "Confidence", "Reflective"): "Soft",
    ("Treating myself to a meal", "Wonder", "Glowing"): "Clear",
    ("Treating myself to a meal", "Wonder", "Clear"): "Soft",
    ("Treating myself to a meal", "Wonder", "Soft"): "Clear",
    ("Treating myself to a meal", "Wonder", "Reflective"): "Glowing",
    ("Treating myself to a meal", "Relaxation", "Glowing"): "Soft",
    ("Treating myself to a meal", "Relaxation", "Clear"): "Soft",
    ("Treating myself to a meal", "Relaxation", "Soft"): "Glowing",
    ("Treating myself to a meal", "Relaxation", "Reflective"): "Clear",
    ("Treating myself to a meal", "Magic", "Glowing"): "Soft",
    ("Treating myself to a meal", "Magic", "Clear"): "Clear",
    ("Treating myself to a meal", "Magic", "Soft"): "Glowing",
    ("Treating myself to a meal", "Magic", "Reflective"): "Soft",

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