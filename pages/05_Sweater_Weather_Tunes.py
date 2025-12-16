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
st.write("Which Halloween movie is your go-to? (double-click button)")
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
st.write("Pick a fall activity: (double-click button)")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/pumpkin.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/applepicking.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/tricktreating.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/bonfire1.jpg",
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


fall_data = {
    "Pumpkin carving": {
        "playlist": "Chilly Orchards",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
#        "business_name": "pHlour Bakery & Cafe",
#        "location": "1138 W Bryn Mawr Ave, Chicago, IL 60660",
#        "website": "https://www.phlour.com/",
#        "business_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/phlour.png",
    },
    "Apple picking": {
        "playlist": "Good Ol' Times",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
#        "business_name": "Eli Tea Bar",
#        "location": "5507 N Clark St, Chicago, IL 60640",
#        "website": "https://www.eliteabar.com/pages/chicago?srsltid=AfmBOoqZ9MveNUGO0oLPMFnIerXvvwttDi_PocAmQXuax6clgCdgzJp7",
#        "business_image": "https://cdn.shopify.com/s/files/1/0171/0582/t/12/assets/andersonville-circle-logo-white-1632947388908.jpg?v=1632947390",
    },
    "Trick or treating": {
        "playlist": "Dark Blues",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
#        "business_name": "Loaves and Witches",
#        "location": "6034 N Broadway, Chicago, IL 60660",
#        "website": "https://loavesandwitches.com/",
#        "business_image": "https://static.spotapps.co/website_images/ab_websites/307737_website_v1/logo.png"
    },
    "Bonfires": {
        "playlist": "Jazz 'n Smores",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
#        "business_name": "Isabella Bakery",
#        "location": "1659 W Foster Ave, Chicago, IL 60640",
#        "website": "https://www.yelp.com/biz/isabella-bakery-chicago-2",
#        "business_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/isabellabakery.png"
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
    st.subheader(f"🎵 Your playlist is {info['playlist']}!")
    st.markdown(f"[Listen Here]({info['playlist_link']})")

    # Business info display
#    st.image(info['business_image'], width=250)
#    st.write(f"🏷️ **Business Name:** {info['business_name']}")
#    st.write(f"🌐 [Visit Website]({info['website']})")
#    st.write(f"📍 **Address:** {info['location']}")

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
            st.image(pianocat,width=300)
        else:
            st.warning("⏳ Share your playlist with at least 3 people to unlock your reward!")