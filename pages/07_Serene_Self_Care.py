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

energy_map = {
    ("Take a warm bath", "Confidence", "Ambient beach", "Glowing"): "Glowing",
    ("Take a warm bath", "Confidence", "Ambient beach", "Clear"): "Clear",
    ("Take a warm bath", "Confidence", "Ambient beach", "Soft"): "Soft",
    ("Take a warm bath", "Confidence", "Ambient beach", "Reflective"): "Reflective",
    ("Take a warm bath", "Confidence", "Quiet mountainside", "Glowing"): "Soft",
    ("Take a warm bath", "Confidence", "Quiet mountainside", "Clear"): "Glowing",
    ("Take a warm bath", "Confidence", "Quiet mountainside", "Soft"): "Reflective",
    ("Take a warm bath", "Confidence", "Quiet mountainside", "Reflective"): "Clear",
    ("Take a warm bath", "Confidence", "Bustling city", "Glowing"): "Clear",
    ("Take a warm bath", "Confidence", "Bustling city", "Clear"): "Reflective",
    ("Take a warm bath", "Confidence", "Bustling city", "Soft"): "Glowing",
    ("Take a warm bath", "Confidence", "Bustling city", "Reflective"): "Soft",
    ("Take a warm bath", "Confidence", "Lush forest", "Glowing"): "Clear",
    ("Take a warm bath", "Confidence", "Lush forest", "Clear"): "Glowing",
    ("Take a warm bath", "Confidence", "Lush forest", "Soft"): "Soft",
    ("Take a warm bath", "Confidence", "Lush forest", "Reflective"): "Reflective",
    ("Take a warm bath", "Wonder", "Ambient beach", "Glowing"): "Reflective",
    ("Take a warm bath", "Wonder", "Ambient beach", "Clear"): "Reflective",
    ("Take a warm bath", "Wonder", "Ambient beach", "Soft"): "Glowing",
    ("Take a warm bath", "Wonder", "Ambient beach", "Reflective"): "Soft",
    ("Take a warm bath", "Wonder", "Quiet mountainside", "Glowing"): "Soft",
    ("Take a warm bath", "Wonder", "Quiet mountainside", "Clear"): "Glowing",
    ("Take a warm bath", "Wonder", "Quiet mountainside", "Soft"): "Clear",
    ("Take a warm bath", "Wonder", "Quiet mountainside", "Reflective"): "Reflective",
    ("Take a warm bath", "Wonder", "Bustling city", "Glowing"): "Reflective",
    ("Take a warm bath", "Wonder", "Bustling city", "Clear"): "Soft",
    ("Take a warm bath", "Wonder", "Bustling city", "Soft"): "Clear",
    ("Take a warm bath", "Wonder", "Bustling city", "Reflective"): "Glowing",
    ("Take a warm bath", "Wonder", "Lush forest", "Glowing"): "Soft",
    ("Take a warm bath", "Wonder", "Lush forest", "Clear"): "Glowing",
    ("Take a warm bath", "Wonder", "Lush forest", "Soft"): "Reflective",
    ("Take a warm bath", "Wonder", "Lush forest", "Reflective"): "Clear",
    ("Take a warm bath", "Relaxation", "Ambient beach", "Glowing"): "Clear",
    ("Take a warm bath", "Relaxation", "Ambient beach", "Clear"): "Soft",
    ("Take a warm bath", "Relaxation", "Ambient beach", "Soft"): "Glowing",
    ("Take a warm bath", "Relaxation", "Ambient beach", "Reflective"): "Reflective",
    ("Take a warm bath", "Relaxation", "Quiet mountainside", "Glowing"): "Soft",
    ("Take a warm bath", "Relaxation", "Quiet mountainside", "Clear"): "Reflective",
    ("Take a warm bath", "Relaxation", "Quiet mountainside", "Soft"): "Soft",
    ("Take a warm bath", "Relaxation", "Quiet mountainside", "Reflective"): "Glowing",
    ("Take a warm bath", "Relaxation", "Bustling city", "Glowing"): "Clear",
    ("Take a warm bath", "Relaxation", "Bustling city", "Clear"): "Soft",
    ("Take a warm bath", "Relaxation", "Bustling city", "Soft"): "Reflective",
    ("Take a warm bath", "Relaxation", "Bustling city", "Reflective"): "Glowing",
    ("Take a warm bath", "Relaxation", "Lush forest", "Glowing"): "Soft",
    ("Take a warm bath", "Relaxation", "Lush forest", "Clear"): "Glowing",
    ("Take a warm bath", "Relaxation", "Lush forest", "Soft"): "Reflective",
    ("Take a warm bath", "Relaxation", "Lush forest", "Reflective"): "Soft",
    ("Take a warm bath", "Magic", "Ambient beach", "Glowing"): "Soft",
    ("Take a warm bath", "Magic", "Ambient beach", "Clear"): "Glowing",
    ("Take a warm bath", "Magic", "Ambient beach", "Soft"): "Glowing",
    ("Take a warm bath", "Magic", "Ambient beach", "Reflective"): "Clear",
    ("Take a warm bath", "Magic", "Quiet mountainside", "Glowing"): "Clear",
    ("Take a warm bath", "Magic", "Quiet mountainside", "Clear"): "Reflective",
    ("Take a warm bath", "Magic", "Quiet mountainside", "Soft"): "Glowing",
    ("Take a warm bath", "Magic", "Quiet mountainside", "Reflective"): "Reflective",
    ("Take a warm bath", "Magic", "Bustling city", "Glowing"): "Glowing",
    ("Take a warm bath", "Magic", "Bustling city", "Clear"): "Clear",
    ("Take a warm bath", "Magic", "Bustling city", "Soft"): "Soft",
    ("Take a warm bath", "Magic", "Bustling city", "Reflective"): "Clear",
    ("Take a warm bath", "Magic", "Lush forest", "Glowing"): "Soft",
    ("Take a warm bath", "Magic", "Lush forest", "Clear"): "Reflective",
    ("Take a warm bath", "Magic", "Lush forest", "Soft"): "Glowing",
    ("Take a warm bath", "Magic", "Lush forest", "Reflective"): "Glowing",

    ("Go on a nature walk", "Confidence", "Ambient beach", "Glowing"): "Clear",
    ("Go on a nature walk", "Confidence", "Ambient beach", "Clear"): "Clear",
    ("Go on a nature walk", "Confidence", "Ambient beach", "Soft"): "Soft",
    ("Go on a nature walk", "Confidence", "Ambient beach", "Reflective"): "Reflective",
    ("Go on a nature walk", "Confidence", "Quiet mountainside", "Glowing"): "Clear",
    ("Go on a nature walk", "Confidence", "Quiet mountainside", "Clear"): "Soft",
    ("Go on a nature walk", "Confidence", "Quiet mountainside", "Soft"): "Glowing",
    ("Go on a nature walk", "Confidence", "Quiet mountainside", "Reflective"): "Glowing",
    ("Go on a nature walk", "Confidence", "Bustling city", "Glowing"): "Soft",
    ("Go on a nature walk", "Confidence", "Bustling city", "Clear"): "Reflective",
    ("Go on a nature walk", "Confidence", "Bustling city", "Soft"): "Clear",
    ("Go on a nature walk", "Confidence", "Bustling city", "Reflective"): "Glowing",
    ("Go on a nature walk", "Confidence", "Lush forest", "Glowing"): "Reflective",
    ("Go on a nature walk", "Confidence", "Lush forest", "Clear"): "Glowing",
    ("Go on a nature walk", "Confidence", "Lush forest", "Soft"): "Soft",
    ("Go on a nature walk", "Confidence", "Lush forest", "Reflective"): "Clear",
    ("Go on a nature walk", "Wonder", "Ambient beach", "Glowing"): "Glowing",
    ("Go on a nature walk", "Wonder", "Ambient beach", "Clear"): "Soft",
    ("Go on a nature walk", "Wonder", "Ambient beach", "Soft"): "Clear",
    ("Go on a nature walk", "Wonder", "Ambient beach", "Reflective"): "Reflective",
    ("Go on a nature walk", "Wonder", "Quiet mountainside", "Glowing"): "Clear",
    ("Go on a nature walk", "Wonder", "Quiet mountainside", "Clear"): "Glowing",
    ("Go on a nature walk", "Wonder", "Quiet mountainside", "Soft"): "Soft",
    ("Go on a nature walk", "Wonder", "Quiet mountainside", "Reflective"): "Soft",
    ("Go on a nature walk", "Wonder", "Bustling city", "Glowing"): "Reflective",
    ("Go on a nature walk", "Wonder", "Bustling city", "Clear"): "Soft",
    ("Go on a nature walk", "Wonder", "Bustling city", "Soft"): "Clear",
    ("Go on a nature walk", "Wonder", "Bustling city", "Reflective"): "Clear",
    ("Go on a nature walk", "Wonder", "Lush forest", "Glowing"): "Clear",
    ("Go on a nature walk", "Wonder", "Lush forest", "Clear"): "Soft",
    ("Go on a nature walk", "Wonder", "Lush forest", "Soft"): "Glowing",
    ("Go on a nature walk", "Wonder", "Lush forest", "Reflective"): "Soft",
    ("Go on a nature walk", "Relaxation", "Ambient beach", "Glowing"): "Clear",
    ("Go on a nature walk", "Relaxation", "Ambient beach", "Clear"): "Reflective",
    ("Go on a nature walk", "Relaxation", "Ambient beach", "Soft"): "Reflective",
    ("Go on a nature walk", "Relaxation", "Ambient beach", "Reflective"): "Clear",
    ("Go on a nature walk", "Relaxation", "Quiet mountainside", "Glowing"): "Clear",
    ("Go on a nature walk", "Relaxation", "Quiet mountainside", "Clear"): "Glowing",
    ("Go on a nature walk", "Relaxation", "Quiet mountainside", "Soft"): "Soft",
    ("Go on a nature walk", "Relaxation", "Quiet mountainside", "Reflective"): "Clear",
    ("Go on a nature walk", "Relaxation", "Bustling city", "Glowing"): "Glowing",
    ("Go on a nature walk", "Relaxation", "Bustling city", "Clear"): "Glowing",
    ("Go on a nature walk", "Relaxation", "Bustling city", "Soft"): "Reflective",
    ("Go on a nature walk", "Relaxation", "Bustling city", "Reflective"): "Clear",
    ("Go on a nature walk", "Relaxation", "Lush forest", "Glowing"): "Glowing",
    ("Go on a nature walk", "Relaxation", "Lush forest", "Clear"): "Clear",
    ("Go on a nature walk", "Relaxation", "Lush forest", "Soft"): "Reflective",
    ("Go on a nature walk", "Relaxation", "Lush forest", "Reflective"): "Glowing",
    ("Go on a nature walk", "Magic", "Ambient beach", "Glowing"): "Soft",
    ("Go on a nature walk", "Magic", "Ambient beach", "Clear"): "Reflective",
    ("Go on a nature walk", "Magic", "Ambient beach", "Soft"): "Soft",
    ("Go on a nature walk", "Magic", "Ambient beach", "Reflective"): "Glowing",
    ("Go on a nature walk", "Magic", "Quiet mountainside", "Glowing"): "Reflective",
    ("Go on a nature walk", "Magic", "Quiet mountainside", "Clear"): "Clear",
    ("Go on a nature walk", "Magic", "Quiet mountainside", "Soft"): "Glowing",
    ("Go on a nature walk", "Magic", "Quiet mountainside", "Reflective"): "Glowing",
    ("Go on a nature walk", "Magic", "Bustling city", "Glowing"): "Soft",
    ("Go on a nature walk", "Magic", "Bustling city", "Clear"): "Glowing",
    ("Go on a nature walk", "Magic", "Bustling city", "Soft"): "Clear",
    ("Go on a nature walk", "Magic", "Bustling city", "Reflective"): "Reflective",
    ("Go on a nature walk", "Magic", "Lush forest", "Glowing"): "Soft",
    ("Go on a nature walk", "Magic", "Lush forest", "Clear"): "Soft",
    ("Go on a nature walk", "Magic", "Lush forest", "Soft"): "Reflective",
    ("Go on a nature walk", "Magic", "Lush forest", "Reflective"): "Clear",

    ("Shop at the mall", "Confidence", "Ambient beach", "Glowing"): "Soft",
    ("Shop at the mall", "Confidence", "Ambient beach", "Clear"): "Glowing",
    ("Shop at the mall", "Confidence", "Ambient beach", "Soft"): "Clear",
    ("Shop at the mall", "Confidence", "Ambient beach", "Reflective"): "Soft",
    ("Shop at the mall", "Confidence", "Quiet mountainside", "Glowing"): "Reflective",
    ("Shop at the mall", "Confidence", "Quiet mountainside", "Clear"): "Soft",
    ("Shop at the mall", "Confidence", "Quiet mountainside", "Soft"): "Reflective",
    ("Shop at the mall", "Confidence", "Quiet mountainside", "Reflective"): "Clear",
    ("Shop at the mall", "Confidence", "Bustling city", "Glowing"): "Reflective",
    ("Shop at the mall", "Confidence", "Bustling city", "Clear"): "Glowing",
    ("Shop at the mall", "Confidence", "Bustling city", "Soft"): "Glowing",
    ("Shop at the mall", "Confidence", "Bustling city", "Reflective"): "Soft",
    ("Shop at the mall", "Confidence", "Lush forest", "Glowing"): "Clear",
    ("Shop at the mall", "Confidence", "Lush forest", "Clear"): "Soft",
    ("Shop at the mall", "Confidence", "Lush forest", "Soft"): "Soft",
    ("Shop at the mall", "Confidence", "Lush forest", "Reflective"): "Glowing",
    ("Shop at the mall", "Wonder", "Ambient beach", "Glowing"): "Glowing",
    ("Shop at the mall", "Wonder", "Ambient beach", "Clear"): "Clear",
    ("Shop at the mall", "Wonder", "Ambient beach", "Soft"): "Reflective",
    ("Shop at the mall", "Wonder", "Ambient beach", "Reflective"): "Clear",
    ("Shop at the mall", "Wonder", "Quiet mountainside", "Glowing"): "Clear",
    ("Shop at the mall", "Wonder", "Quiet mountainside", "Clear"): "Glowing",
    ("Shop at the mall", "Wonder", "Quiet mountainside", "Soft"): "Glowing",
    ("Shop at the mall", "Wonder", "Quiet mountainside", "Reflective"): "Reflective",
    ("Shop at the mall", "Wonder", "Bustling city", "Glowing"): "Soft",
    ("Shop at the mall", "Wonder", "Bustling city", "Clear"): "Reflective",
    ("Shop at the mall", "Wonder", "Bustling city", "Soft"): "Reflective",
    ("Shop at the mall", "Wonder", "Bustling city", "Reflective"): "Glowing",
    ("Shop at the mall", "Wonder", "Lush forest", "Glowing"): "Glowing",
    ("Shop at the mall", "Wonder", "Lush forest", "Clear"): "Clear",
    ("Shop at the mall", "Wonder", "Lush forest", "Soft"): "Soft",
    ("Shop at the mall", "Wonder", "Lush forest", "Reflective"): "Reflective",
    ("Shop at the mall", "Relaxation", "Ambient beach", "Glowing"): "Glowing",
    ("Shop at the mall", "Relaxation", "Ambient beach", "Clear"): "Glowing",
    ("Shop at the mall", "Relaxation", "Ambient beach", "Soft"): "Soft",
    ("Shop at the mall", "Relaxation", "Ambient beach", "Reflective"): "Clear",
    ("Shop at the mall", "Relaxation", "Quiet mountainside", "Glowing"): "Soft",
    ("Shop at the mall", "Relaxation", "Quiet mountainside", "Clear"): "Reflective",
    ("Shop at the mall", "Relaxation", "Quiet mountainside", "Soft"): "Glowing",
    ("Shop at the mall", "Relaxation", "Quiet mountainside", "Reflective"): "Clear",
    ("Shop at the mall", "Relaxation", "Bustling city", "Glowing"): "Glowing",
    ("Shop at the mall", "Relaxation", "Bustling city", "Clear"): "Soft",
    ("Shop at the mall", "Relaxation", "Bustling city", "Soft"): "Clear",
    ("Shop at the mall", "Relaxation", "Bustling city", "Reflective"): "Reflective",
    ("Shop at the mall", "Relaxation", "Lush forest", "Glowing"): "Clear",
    ("Shop at the mall", "Relaxation", "Lush forest", "Clear"): "Glowing",
    ("Shop at the mall", "Relaxation", "Lush forest", "Soft"): "Soft",
    ("Shop at the mall", "Relaxation", "Lush forest", "Reflective"): "Glowing",
    ("Shop at the mall", "Magic", "Ambient beach", "Glowing"): "Glowing",
    ("Shop at the mall", "Magic", "Ambient beach", "Clear"): "Reflective",
    ("Shop at the mall", "Magic", "Ambient beach", "Soft"): "Soft",
    ("Shop at the mall", "Magic", "Ambient beach", "Reflective"): "Clear",
    ("Shop at the mall", "Magic", "Quiet mountainside", "Glowing"): "Reflective",
    ("Shop at the mall", "Magic", "Quiet mountainside", "Clear"): "Clear",
    ("Shop at the mall", "Magic", "Quiet mountainside", "Soft"): "Glowing",
    ("Shop at the mall", "Magic", "Quiet mountainside", "Reflective"): "Soft",
    ("Shop at the mall", "Magic", "Bustling city", "Glowing"): "Clear",
    ("Shop at the mall", "Magic", "Bustling city", "Clear"): "Reflective",
    ("Shop at the mall", "Magic", "Bustling city", "Soft"): "Soft",
    ("Shop at the mall", "Magic", "Bustling city", "Reflective"): "Glowing",
    ("Shop at the mall", "Magic", "Lush forest", "Glowing"): "Reflective",
    ("Shop at the mall", "Magic", "Lush forest", "Clear"): "Soft",
    ("Shop at the mall", "Magic", "Lush forest", "Soft"): "Clear",
    ("Shop at the mall", "Magic", "Lush forest", "Reflective"): "Glowing",

    ("Eat a delicious meal", "Confidence", "Ambient beach", "Glowing"): "Soft",
    ("Eat a delicious meal", "Confidence", "Ambient beach", "Clear"): "Reflective",
    ("Eat a delicious meal", "Confidence", "Ambient beach", "Soft"): "Clear",
    ("Eat a delicious meal", "Confidence", "Ambient beach", "Reflective"): "Glowing",
    ("Eat a delicious meal", "Confidence", "Quiet mountainside", "Glowing"): "Clear",
    ("Eat a delicious meal", "Confidence", "Quiet mountainside", "Clear"): "Glowing",
    ("Eat a delicious meal", "Confidence", "Quiet mountainside", "Soft"): "Soft",
    ("Eat a delicious meal", "Confidence", "Quiet mountainside", "Reflective"): "Reflective",
    ("Eat a delicious meal", "Confidence", "Bustling city", "Glowing"): "Clear",
    ("Eat a delicious meal", "Confidence", "Bustling city", "Clear"): "Soft",
    ("Eat a delicious meal", "Confidence", "Bustling city", "Soft"): "Soft",
    ("Eat a delicious meal", "Confidence", "Bustling city", "Reflective"): "Glowing",
    ("Eat a delicious meal", "Confidence", "Lush forest", "Glowing"): "Clear",
    ("Eat a delicious meal", "Confidence", "Lush forest", "Clear"): "Reflective",
    ("Eat a delicious meal", "Confidence", "Lush forest", "Soft"): "Soft",
    ("Eat a delicious meal", "Confidence", "Lush forest", "Reflective"): "Glowing",
    ("Eat a delicious meal", "Wonder", "Ambient beach", "Glowing"): "Glowing",
    ("Eat a delicious meal", "Wonder", "Ambient beach", "Clear"): "Clear",
    ("Eat a delicious meal", "Wonder", "Ambient beach", "Soft"): "Reflective",
    ("Eat a delicious meal", "Wonder", "Ambient beach", "Reflective"): "Soft",
    ("Eat a delicious meal", "Wonder", "Quiet mountainside", "Glowing"): "Glowing",
    ("Eat a delicious meal", "Wonder", "Quiet mountainside", "Clear"): "Clear",
    ("Eat a delicious meal", "Wonder", "Quiet mountainside", "Soft"): "Soft",
    ("Eat a delicious meal", "Wonder", "Quiet mountainside", "Reflective"): "Reflective",
    ("Eat a delicious meal", "Wonder", "Bustling city", "Glowing"): "Soft",
    ("Eat a delicious meal", "Wonder", "Bustling city", "Clear"): "Soft",
    ("Eat a delicious meal", "Wonder", "Bustling city", "Soft"): "Reflective",
    ("Eat a delicious meal", "Wonder", "Bustling city", "Reflective"): "Glowing",
    ("Eat a delicious meal", "Wonder", "Lush forest", "Glowing"): "Reflective",
    ("Eat a delicious meal", "Wonder", "Lush forest", "Clear"): "Soft",
    ("Eat a delicious meal", "Wonder", "Lush forest", "Soft"): "Clear",
    ("Eat a delicious meal", "Wonder", "Lush forest", "Reflective"): "Glowing",
    ("Eat a delicious meal", "Relaxation", "Ambient beach", "Glowing"): "Clear",
    ("Eat a delicious meal", "Relaxation", "Ambient beach", "Clear"): "Reflective",
    ("Eat a delicious meal", "Relaxation", "Ambient beach", "Soft"): "Glowing",
    ("Eat a delicious meal", "Relaxation", "Ambient beach", "Reflective"): "Clear",
    ("Eat a delicious meal", "Relaxation", "Quiet mountainside", "Glowing"): "Reflective",
    ("Eat a delicious meal", "Relaxation", "Quiet mountainside", "Clear"): "Glowing",
    ("Eat a delicious meal", "Relaxation", "Quiet mountainside", "Soft"): "Reflective",
    ("Eat a delicious meal", "Relaxation", "Quiet mountainside", "Reflective"): "Soft",
    ("Eat a delicious meal", "Relaxation", "Bustling city", "Glowing"): "Clear",
    ("Eat a delicious meal", "Relaxation", "Bustling city", "Clear"): "Soft",
    ("Eat a delicious meal", "Relaxation", "Bustling city", "Soft"): "Soft",
    ("Eat a delicious meal", "Relaxation", "Bustling city", "Reflective"): "Glowing",
    ("Eat a delicious meal", "Relaxation", "Lush forest", "Glowing"): "Clear",
    ("Eat a delicious meal", "Relaxation", "Lush forest", "Clear"): "Glowing",
    ("Eat a delicious meal", "Relaxation", "Lush forest", "Soft"): "Soft",
    ("Eat a delicious meal", "Relaxation", "Lush forest", "Reflective"): "Reflective",
    ("Eat a delicious meal", "Magic", "Ambient beach", "Glowing"): "Clear",
    ("Eat a delicious meal", "Magic", "Ambient beach", "Clear"): "Glowing",
    ("Eat a delicious meal", "Magic", "Ambient beach", "Soft"): "Reflective",
    ("Eat a delicious meal", "Magic", "Ambient beach", "Reflective"): "Reflective",
    ("Eat a delicious meal", "Magic", "Quiet mountainside", "Glowing"): "Soft",
    ("Eat a delicious meal", "Magic", "Quiet mountainside", "Clear"): "Reflective",
    ("Eat a delicious meal", "Magic", "Quiet mountainside", "Soft"): "Glowing",
    ("Eat a delicious meal", "Magic", "Quiet mountainside", "Reflective"): "Clear",
    ("Eat a delicious meal", "Magic", "Bustling city", "Glowing"): "Soft",
    ("Eat a delicious meal", "Magic", "Bustling city", "Clear"): "Clear",
    ("Eat a delicious meal", "Magic", "Bustling city", "Soft"): "Clear",
    ("Eat a delicious meal", "Magic", "Bustling city", "Reflective"): "Glowing",
    ("Eat a delicious meal", "Magic", "Lush forest", "Glowing"): "Clear",
    ("Eat a delicious meal", "Magic", "Lush forest", "Clear"): "Reflective",
    ("Eat a delicious meal", "Magic", "Lush forest", "Soft"): "Glowing",
    ("Eat a delicious meal", "Magic", "Lush forest", "Reflective"): "Clear",
}

if selected_unwind and selected_act and selected_secret and selected_getaway and energy_choice:
    key = (selected_unwind, selected_secret, selected_getaway, energy_choice)
    output = energy_map.get(key)

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