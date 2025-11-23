import streamlit as st

st.set_page_config(
    page_title="Sweater Weather Tunes",
    page_icon="🍂",
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
st.title("🍂 Sweater Weather Tunes")
st.markdown("""
Welcome! Pick a fall activity below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
""")

#Q1
drink = ["Apple cider", "Pumpkin spice latte", "Chai", "Hot chocolate"]
selected_drink = st.selectbox("Pick a fall drink:", drink, index=None)

#Q2
st.write("Which Halloween movie is your go-to?")
images = [

        "https://lumiere-a.akamaihd.net/v1/images/p_hocuspocus_19880_e000b013.jpeg",
        "https://images.plex.tv/photo?size=large-1280&url=https%3A%2F%2Fmetadata-static.plex.tv%2Fc%2Fgracenote%2Fc990f672e727f896bb52529043bec1c0.jpg",
        "https://images.fathomevents.com/image/upload/w_1200,dpr_2,f_auto,q_auto/v1757097985/Events/2025/2083/Fathom%20Ticket%20Page%20Poster%20%20Press%20Kit_1000x1480%20%28No%20Text%29.png.png",
        "https://upload.wikimedia.org/wikipedia/en/5/5a/It_%282017%29_poster.jpg",
]

titles=["Hocus Pocus", "Halloween", "Trick 'r Treat", "IT"]

if "selected_film" not in st.session_state:
    st.session_state.selected_film = None

cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        # Clicking the button selects this image
        if st.button(titles[i], key=f"btn_film_{i}"):
            st.session_state.selected_film = i

        # Add a red border if selected
        border = "4px solid red" if st.session_state.selected_film == i else "4px solid transparent"

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

selected_film = (
    titles[st.session_state.selected_film]
    if st.session_state.get("selected_film") is not None
    else None
)
#gap
st.write("")


#Q3
element_options = ["Falling leaves", "Long spooky nights", "Crackling fire", "Foggy skies"]
selected_element = st.selectbox("What fall element speaks to you the most?", element_options, index=None)

#Q4
spent = ["Alone", "With family and friends", "In nature", "With lots of food"]
selected_spent = st.selectbox("Fall is best spent...", spent, index=None)

#Q5
st.write("Pick a fall activity")
images = [

        "https://images.ctfassets.net/prxuf37q3ta2/1QXngj3Thd7Qt2EbHi2Yr0/1eca6f277d910946cbc9e3c06434db2f/Primary_Image_1200x900.jpg",
        "https://cdn.outsideonline.com/wp-content/uploads/2022/09/apple_picking-h.jpg",
        "https://hips.hearstapps.com/hmg-prod/images/trick-or-treat-2023-64a886178cfd1.jpg?crop=0.8893081761006288xw:1xh;center,top&resize=1200:*",
        "https://cdn.hswstatic.com/gif/How-to-make-a-bonfire-in-your-backyard.jpg",
]

titles=["Pumpkin carving", "Apple picking", "Trick or treating", "Bonfires"]

if "selected_fall" not in st.session_state:
    st.session_state.selected_fall = None

cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        # Clicking the button selects this image
        if st.button(titles[i], key=f"btn_fall_{i}"):
            st.session_state.selected_fall = i

        # Add a red border if selected
        border = "4px solid red" if st.session_state.selected_fall == i else "4px solid transparent"

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

selected_fall = (
    titles[st.session_state.selected_fall]
    if st.session_state.get("selected_fall") is not None
    else None
)
#gap
st.write("")


# Business options and related data
fall_data = {
    "Pumpkin carving": {
        "playlist": "Chilly Orchards",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "business_name": "Sweet Bean",
        "offer": "10% off your first order with this screen!",
        "booth_name": "Booth A",
        "website": "https://www.sweetbeanchicago.com/",
        "business_image": "https://static.wixstatic.com/media/60e202_65260ab6509e4ba9bea19ced8ec91ec3~mv2.png/v1/fill/w_234,h_160,al_c,q_85,usm_0.66_1.00_0.01,enc_avif,quality_auto/Sweet%20Bean%20logo%20-%20red.png",
    },
    "Apple picking": {
    "playlist": "Good Ol' Times",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Chuck's Southern Comforts Cafe",
    "offer": "Buy 1 Combo, Get 1 Free Appetizer with this screen.",
    "booth_name": "Booth B",
    "website": "https://chuckscafe.com/",
    "business_image": "https://d1w7312wesee68.cloudfront.net/DDMPmNmtnrUxz1PxVDTze2OFtR-QuWFhVWx-Dg15aYo/ext:webp/quality:85/preset:xxl/plain/s3://toast-sites-resources-prod/restaurantImages/1f14af1d-c8f7-4b8b-9d8a-480dbaba7333/restaurant_1592420555.png",
    },
    "Trick or treating": {
    "playlist": "Dark Blues",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "Patch Party Club",
    "offer": "5% off your purchase!",
    "booth_name": "Booth C",
    "website": "https://patchpartyclub.com/",
    "business_image": "https://patchpartyclub.com/cdn/shop/files/logo_180x.png?v=1630341909"
    },
    "Bonfires": {
    "playlist": "Jazz 'n Smores",
    "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    "business_name": "",
    "offer": "Get 5% off a selected candle!",
    "booth_name": "Booth D",
    "website": "https://civinte.com/",
    "business_image": "https://civinte.com/cdn/shop/files/2025_Logo_180x@2x.png?v=1747978532"
    },
}

info = None



fall_map = {
("Hocus Pocus", "Falling leaves", "Pumpkin carving"): "Pumpkin carving",
("Hocus Pocus", "Falling leaves", "Apple picking"): "Bonfires",
("Hocus Pocus", "Falling leaves", "Trick or treating"): "Trick or treating",
("Hocus Pocus", "Falling leaves", "Bonfires"): "Bonfires",
("Hocus Pocus", "Long spooky nights", "Pumpkin carving"): "Trick or treating",
("Hocus Pocus", "Long spooky nights", "Apple picking"): "Apple picking",
("Hocus Pocus", "Long spooky nights", "Trick or treating"): "Bonfires",
("Hocus Pocus", "Long spooky nights", "Bonfires"): "Pumpkin carving",
("Hocus Pocus", "Crackling fire", "Pumpkin carving"): "Bonfires",
("Hocus Pocus", "Crackling fire", "Apple picking"): "Pumpkin carving",
("Hocus Pocus", "Crackling fire", "Trick or treating"): "Apple picking",
("Hocus Pocus", "Crackling fire", "Bonfires"): "Pumpkin carving",
("Hocus Pocus", "Foggy skies", "Pumpkin carving"): "Pumpkin carving",
("Hocus Pocus", "Foggy skies", "Apple picking"): "Bonfires",
("Hocus Pocus", "Foggy skies", "Trick or treating"): "Trick or treating",
("Hocus Pocus", "Foggy skies", "Bonfires"): "Bonfires",

("Halloween", "Falling leaves", "Pumpkin carving"): "Bonfires",
("Halloween", "Falling leaves", "Apple picking"): "Trick or treating",
("Halloween", "Falling leaves", "Trick or treating"): "Trick or treating",
("Halloween", "Falling leaves", "Bonfires"): "Apple picking",
("Halloween", "Long spooky nights", "Pumpkin carving"): "Bonfires",
("Halloween", "Long spooky nights", "Apple picking"): "Bonfires",
("Halloween", "Long spooky nights", "Trick or treating"): "Trick or treating",
("Halloween", "Long spooky nights", "Bonfires"): "Pumpkin carving",
("Halloween", "Crackling fire", "Pumpkin carving"): "Apple picking",
("Halloween", "Crackling fire", "Apple picking"): "Apple picking",
("Halloween", "Crackling fire", "Trick or treating"): "Bonfires",
("Halloween", "Crackling fire", "Bonfires"): "Apple picking",
("Halloween", "Foggy skies", "Pumpkin carving"): "Trick or treating",
("Halloween", "Foggy skies", "Apple picking"): "Trick or treating",
("Halloween", "Foggy skies", "Trick or treating"): "Bonfires",
("Halloween", "Foggy skies", "Bonfires"): "Bonfires",

("Trick 'r Treat", "Falling leaves", "Pumpkin carving"): "Trick or treating",
("Trick 'r Treat", "Falling leaves", "Apple picking"): "Trick or treating",
("Trick 'r Treat", "Falling leaves", "Trick or treating"): "Pumpkin carving",
("Trick 'r Treat", "Falling leaves", "Bonfires"): "Bonfires",
("Trick 'r Treat", "Long spooky nights", "Pumpkin carving"): "Pumpkin carving",
("Trick 'r Treat", "Long spooky nights", "Apple picking"): "Apple picking",
("Trick 'r Treat", "Long spooky nights", "Trick or treating"): "Trick or treating",
("Trick 'r Treat", "Long spooky nights", "Bonfires"): "Trick or treating",
("Trick 'r Treat", "Crackling fire", "Pumpkin carving"): "Bonfires",
("Trick 'r Treat", "Crackling fire", "Apple picking"): "Pumpkin carving",
("Trick 'r Treat", "Crackling fire", "Trick or treating"): "Pumpkin carving",
("Trick 'r Treat", "Crackling fire", "Bonfires"): "Bonfires",
("Trick 'r Treat", "Foggy skies", "Pumpkin carving"): "Pumpkin carving",
("Trick 'r Treat", "Foggy skies", "Apple picking"): "Bonfires",
("Trick 'r Treat", "Foggy skies", "Trick or treating"): "Apple picking",
("Trick 'r Treat", "Foggy skies", "Bonfires"): "Apple picking",

("IT", "Falling leaves", "Pumpkin carving"): "Apple picking",
("IT", "Falling leaves", "Apple picking"): "Bonfires",
("IT", "Falling leaves", "Trick or treating"): "Trick or treating",
("IT", "Falling leaves", "Bonfires"): "Pumpkin carving",
("IT", "Long spooky nights", "Pumpkin carving"): "Bonfires",
("IT", "Long spooky nights", "Apple picking"): "Pumpkin carving",
("IT", "Long spooky nights", "Trick or treating"): "Trick or treating",
("IT", "Long spooky nights", "Bonfires"): "Trick or treating",
("IT", "Crackling fire", "Pumpkin carving"): "Bonfires",
("IT", "Crackling fire", "Apple picking"): "Trick or treating",
("IT", "Crackling fire", "Trick or treating"): "Apple picking",
("IT", "Crackling fire", "Bonfires"): "Apple picking",
("IT", "Foggy skies", "Pumpkin carving"): "Apple picking",
("IT", "Foggy skies", "Apple picking"): "Trick or treating",
("IT", "Foggy skies", "Trick or treating"): "Pumpkin carving",
("IT", "Foggy skies", "Bonfires"): "Pumpkin carving",

}



if selected_film and selected_element and selected_fall:
    user_combo = (selected_film, selected_element, selected_fall)
    result_key = fall_map.get(user_combo)

    if result_key:
        info = fall_data[result_key]


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