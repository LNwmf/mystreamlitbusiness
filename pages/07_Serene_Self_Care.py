from st_copy import copy_button
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
Welcome! Pick an energy below to discover a blended playlist and unlock a surprise for sharing with others.
""")

#Q1
st.write("Deciding to treat yourself after a long day, you... (double-click button)")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/bath.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/naturewalk.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/shopping.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/dinner.jpg",
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
st.write("Pick a getaway place: (double-click button)")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/ambientbeach.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/mountainside.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/city.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/forest.png",
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
        "playlist_link": "https://open.spotify.com/playlist/3KqR0JO9SyVChRmtJl3h8E?si=0Az8nnoaQuy28BdsvTd_Cg",
#        "business_name": "Apothecary EO",
#        "location": "5601 N Clark St, Chicago, IL 60660",
#        "website": "https://www.apothecaryeo.com/",
#        "business_image": "https://static.wixstatic.com/media/d5bbda_fd6fbc09537f4e1480e3a6b0bcb91d1a~mv2.png/v1/fill/w_788,h_328,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/Apothecary%20EO.png",
    },
    "Clear": {
    "playlist": "Drifting in the Sun",
    "playlist_link": "https://open.spotify.com/playlist/56XDtYltTtWDNm3vHXrpsy?si=6qcxLaEJQFCI_mZSvNsRXQ",
#    "business_name": "105F Hot Yoga, Pilates, & Wellness",
#    "location": "5715 N Clark St, Chicago, IL 60660",
#    "website": "https://105f.com/classes/",
#    "business_image": "https://105f.com/wp-content/uploads/2020/01/105f_logo_without-Background-1.gif",
    },
    "Soft": {
    "playlist": "Bubbles & Wine",
    "playlist_link": "https://open.spotify.com/playlist/5rMYIk7cKoUZe7TqX3Alm9?si=2M6fFiVCRE6EQl_7-A7uDg",
#    "business_name": "AMK Massage",
#    "location": "5347 N Clark St #2, Chicago, Illinois 60640",
#    "website": "https://www.amkmassage.com/",
#    "business_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/massage.png"
    },
    "Reflective": {
    "playlist": "Still Thinking...",
    "playlist_link": "https://open.spotify.com/playlist/30rsriukBie1aX6feryzMu?si=EVtDnaFAQQ2wiYm6hhJqQA",
#    "business_name": "Freestyle Ceramics & Tufting",
#    "location": "5127 N Clark St, Chicago, IL 60640",
#    "website": "https://www.freestyletufting.com/",
#    "business_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/freestyleceramicsandtufting.png"
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

    st.subheader(f"🎵 Your playlist is {info3['playlist']}!")
    playlist_link = info3["playlist_link"]

    # Create two columns: one wider for the link, one narrower for the button
    col1, col2 = st.columns([0.2, 1])

    # Put the hyperlink in the first column
    with col1:
        st.markdown(
            f"""
                        <a href="{playlist_link}" target="_blank" style="font-size:20px; font-weight:bold;">
                            Listen Here
                        </a>
                        """,
            unsafe_allow_html=True
        )

    # Put the copy button in the second column
    with col2:
        copy_button(playlist_link)

    # Business info display
#    st.image(info3['business_image'], width=250)
#    st.write(f"🏷️ **Business Name:** {info3['business_name']}")
#    st.write(f"🌐 [Visit Website]({info3['website']})")
#    st.write(f"📍 **Address:** {info3['location']}")

    st.write("")
    st.subheader("Share your playlist!", divider="grey")
    st.write("")
    st.write("How many people did you share your playlist with?")
    shared_count = st.number_input("Number of people:", min_value=0, step=1)
    pianocat = "https://i.imgur.com/zZgJvo5.gif"

    if st.button("Check Reward Status"):
        if shared_count >= 3:
            st.balloons()
            st.success(f"🎊 Surprise!")
            st.image(pianocat, width=300)
        else:
            st.warning("⏳ Share your playlist with at least 3 people to unlock your reward!")