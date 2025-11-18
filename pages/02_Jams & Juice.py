import streamlit as st
from st_clickable_images import clickable_images

#streamlit run sl1.py

st.set_page_config(
    page_title="Jams & Juice",
    page_icon="🍹",
    layout="centered",
)

st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("🍹 Jams & Juice")
st.markdown("""
Welcome! Pick a drink below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
""")

#Q1
flavor_options = ["Sweet", "Salty", "Bitter", "Sour"]
selected_flavor = st.selectbox("Select a flavor:", flavor_options, index=None)

#Q2
travel_options = ["Africa", "Antarctica", "Asia", "Australia", "Europe", "Latin America", "North America"]
selected_travel = st.selectbox("Which place do you wish to travel to one day?", travel_options, index=None)

#Q3
st.write("Pick a secret ingredient:")
images = [

        "https://bouqs.com/blog/wp-content/uploads/2018/08/shutterstock_1662182848-min.jpg",
        "https://assets.clevelandclinic.org/transform/809a0d11-7f04-4b7f-b5f5-bd8b47a63c9a/tamarind-fruit-snack-1432243224",
        "https://noshingwiththenolands.com/wp-content/uploads/2023/07/Hot-Honey-IMG_8472.jpg",
        "https://5.imimg.com/data5/SELLER/Default/2024/11/469407212/QS/ZB/WD/21684370/1kg-fresh-ginger-500x500.jpeg",
]

titles=["Rose", "Tamarind", "Hot honey", "Ginger"]

clicked = clickable_images(
    images,
    titles=titles,
    div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
    img_style={"margin": "5px", "height": "170px", "border": "3px solid transparent", "border-radius": "10px"},
)

if clicked > -1:
    st.markdown(f"**{titles[clicked]} selected**")
    st.markdown(
        f"""
        <style>
            .image-container:nth-child({clicked+1}) img {{
                border: 3px solid #ff4b4b !important;
                border-radius: 10px !important;
                box-shadow: 0 0 8px rgba(255, 75, 75, 0.6);
            }}
        </style>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown("**No image selected**")

#Q4
mood = ["Hot chocolate on a chilly night", "Wine during a thunderstorm", "Fresh lemonade on the beach", "Warm apple cider in a cabin"]
selected_mood = st.selectbox("Which scenario sounds the most enjoyable?", mood, index=None)

# Business options and related data
business_data = {
    "Caramel Macchiato": {
        "playlist": "Maqamat Rhythms",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "business_name": "Melt n Dip",
        "offer": "10% off your first order with this screen!",
        "booth_name": "Booth A",
        "website": "https://meltndip.com/",
        "business_image": "https://meltndip.com/wp-content/uploads/2019/06/meltndip_logo.png",  # Insert real image URL or file path
    },
    "Chai Latte": {
        "playlist": "World Country Beats",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "business_name": "Hangry Cluck",
        "offer": "Buy 1 Combo, Get 1 Free Chicken Sandwich with this screen.",
        "booth_name": "Booth B",
        "website": "https://www.hangryclucks.com/",
        "business_image": "https://static.wixstatic.com/media/16edcb_02bad294e43540c883ab0178e1a8833a~mv2.jpg/v1/fill/w_161,h_114,al_c,q_80,usm_0.66_1.00_0.01,enc_auto/5f478e3d-f953-4e49-878b-842c22c4e9d2.jpg",  # Insert real image URL or file path
    },
    "Milk Tea Boba": {
        "playlist": "Sweet Mellow Blues",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "business_name": "Tea yard",
        "offer": "5% off your boba order!",
        "booth_name": "Booth C",
        "website": "https://www.teayardil.com/",
        "business_image": "https://www.teayardil.com/images/logo.png"
    },
    "Horchata": {
        "playlist": "Reggaeton Fusions",
        "playlist_link": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        "business_name": "La Cocina de Mama",
        "offer": "Get 1 free appetizer with your order!",
        "booth_name": "Booth D",
        "website": "https://lacocinademama.info/#e850eae8-0ae1-47ef-b319-d9414f8fa562",
        "business_image": "https://img1.wsimg.com/isteam/ip/48776d13-0db9-455e-8e2c-79b6ef95f77b/9B4F57B4-DAC7-44B6-9866-0965466D36F5.png/:/rs=w:588,h:202,cg:true,m/cr=w:588,h:202/qt=q:95"
    }

    # Add other drinks and related data here
}

info = None

# Drink Selection
#combination_map = {
#    ("Sweet", "Hot chocolate on a chilly night", "Caramel Macchiato"): "Caramel Macchiato",
#    ("Sweet", "Hot chocolate on a chilly night", "Chai Latte"): "Horchata",
#    ...
#}

#key = (selected_flavor, selected_mood, drink_choice)
#info = business_data[combination_map.get(key)] if combination_map.get(key) else None

drink_choice = st.selectbox("Pick a drink!", ["", *business_data.keys()])

if selected_flavor == "Sweet" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Caramel Macchiato":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Sweet" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Chai Latte":
    info = business_data["Horchata"]
elif selected_flavor == "Sweet" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Milk Tea Boba":
    info = business_data["Milk Tea Boba"]
elif selected_flavor == "Sweet" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Horchata":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Sweet" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Caramel Macchiato":
    info = business_data["Chai Latte"]
elif selected_flavor == "Sweet" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Chai Latte":
    info = business_data["Horchata"]
elif selected_flavor == "Sweet" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Milk Tea Boba":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Sweet" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Horchata":
    info = business_data["Chai Latte"]
elif selected_flavor == "Sweet" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Caramel Macchiato":
    info = business_data["Milk Tea Boba"]
elif selected_flavor == "Sweet" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Chai Latte":
    info = business_data["Horchata"]
elif selected_flavor == "Sweet" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Milk Tea Boba":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Sweet" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Horchata":
    info = business_data["Chai Latte"]
elif selected_flavor == "Sweet" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Caramel Macchiato":
    info = business_data["Horchata"]
elif selected_flavor == "Sweet" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Chai Latte":
    info = business_data["Milk Tea Boba"]
elif selected_flavor == "Sweet" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Milk Tea Boba":
    info = business_data["Chai Latte"]
elif selected_flavor == "Sweet" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Horchata":
    info = business_data["Chai Latte"]
elif selected_flavor == "Salty" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Caramel Macchiato":
    info = business_data["Chai Latte"]
elif selected_flavor == "Salty" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Chai Latte":
    info = business_data["Horchata"]
elif selected_flavor == "Salty" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Milk Tea Boba":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Salty" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Horchata":
    info = business_data["Chai Latte"]
elif selected_flavor == "Salty" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Caramel Macchiato":
    info = business_data["Milk Tea Boba"]
elif selected_flavor == "Salty" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Chai Latte":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Salty" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Milk Tea Boba":
    info = business_data["Chai Latte"]
elif selected_flavor == "Salty" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Horchata":
    info = business_data["Chai Latte"]
elif selected_flavor == "Salty" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Caramel Macchiato":
    info = business_data["Horchata"]
elif selected_flavor == "Salty" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Chai Latte":
    info = business_data["Milk Tea Boba"]
elif selected_flavor == "Salty" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Milk Tea Boba":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Salty" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Horchata":
    info = business_data["Chai Latte"]
elif selected_flavor == "Salty" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Caramel Macchiato":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Salty" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Chai Latte":
    info = business_data["Milk Tea Boba"]
elif selected_flavor == "Salty" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Milk Tea Boba":
    info = business_data["Chai Latte"]
elif selected_flavor == "Salty" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Horchata":
    info = business_data["Horchata"]
elif selected_flavor == "Bitter" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Caramel Macchiato":
    info = business_data["Chai Latte"]
elif selected_flavor == "Bitter" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Chai Latte":
    info = business_data["Horchata"]
elif selected_flavor == "Bitter" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Milk Tea Boba":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Bitter" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Horchata":
    info = business_data["Chai Latte"]
elif selected_flavor == "Bitter" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Caramel Macchiato":
    info = business_data["Chai Latte"]
elif selected_flavor == "Bitter" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Chai Latte":
    info = business_data["Horchata"]
elif selected_flavor == "Bitter" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Milk Tea Boba":
    info = business_data["Chai Latte"]
elif selected_flavor == "Bitter" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Horchata":
    info = business_data["Chai Latte"]
elif selected_flavor == "Bitter" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Caramel Macchiato":
    info = business_data["Horchata"]
elif selected_flavor == "Bitter" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Chai Latte":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Bitter" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Milk Tea Boba":
    info = business_data["Chai Latte"]
elif selected_flavor == "Bitter" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Horchata":
    info = business_data["Milk Tea Boba"]
elif selected_flavor == "Bitter" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Caramel Macchiato":
    info = business_data["Milk Tea Boba"]
elif selected_flavor == "Bitter" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Chai Latte":
    info = business_data["Horchata"]
elif selected_flavor == "Bitter" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Milk Tea Boba":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Bitter" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Horchata":
    info = business_data["Chai Latte"]
elif selected_flavor == "Sour" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Caramel Macchiato":
    info = business_data["Horchata"]
elif selected_flavor == "Sour" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Chai Latte":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Sour" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Milk Tea Boba":
    info = business_data["Milk Tea Boba"]
elif selected_flavor == "Sour" and selected_mood == "Hot chocolate on a chilly night" and drink_choice == "Horchata":
    info = business_data["Chai Latte"]
elif selected_flavor == "Sour" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Caramel Macchiato":
    info = business_data["Chai Latte"]
elif selected_flavor == "Sour" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Chai Latte":
    info = business_data["Horchata"]
elif selected_flavor == "Sour" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Milk Tea Boba":
    info = business_data["Chai Latte"]
elif selected_flavor == "Sour" and selected_mood == "Wine during a thunderstorm" and drink_choice == "Horchata":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Sour" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Caramel Macchiato":
    info = business_data["Milk Tea Boba"]
elif selected_flavor == "Sour" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Chai Latte":
    info = business_data["Horchata"]
elif selected_flavor == "Sour" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Milk Tea Boba":
    info = business_data["Chai Latte"]
elif selected_flavor == "Sour" and selected_mood == "Fresh lemonade on the beach" and drink_choice == "Horchata":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Sour" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Caramel Macchiato":
    info = business_data["Caramel Macchiato"]
elif selected_flavor == "Sour" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Chai Latte":
    info = business_data["Milk Tea Boba"]
elif selected_flavor == "Sour" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Milk Tea Boba":
    info = business_data["Horchata"]
elif selected_flavor == "Sour" and selected_mood == "Warm apple cider in a cabin" and drink_choice == "Horchata":
    info = business_data["Chai Latte"]


    # Display playlist and business info
if info:
    st.subheader(f"🎵 {info['playlist']}")
    st.markdown(f"[Listen Here]({info['playlist_link']})")

    # Business info display
    st.image(info['business_image'], width=250)  # Show business image (if available)
    st.write(f"💼 **Business Name:** {info['business_name']}")
    st.write(f"🌐 [Visit Website]({info['website']})")
    st.write(f"🎁 **Special Offer:** {info['offer']}")

    st.write("")
    st.subheader("Share your playlist!", divider="grey")
    st.write("")

    # Share Playlist with Others (social sharing feature)
    st.write("👥 How many people did you share your playlist with?")
    shared_count = st.number_input("Number of people:", min_value=0, step=1)

    if st.button("Check Reward Status"):
        if shared_count >= 3:
            st.balloons()  # Add some confetti for fun
            st.success(f"🎁 You unlocked a reward! Show this screen at {info['booth_name']} to claim your prize!")
        else:
            st.warning("⏳ Share your playlist with at least 3 people to unlock your reward!")

# Weekly Business Spotlight
#st.markdown("---")
#st.subheader("Business Spotlight")

#with st.expander("Click to see this week's featured businesses"):
    #st.markdown("**1. Hangry Cluck**")
    #st.markdown("**1. Tea yard**")