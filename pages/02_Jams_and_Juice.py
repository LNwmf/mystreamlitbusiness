from st_copy import copy_button
import streamlit as st

#streamlit run sl1.py

st.set_page_config(
    page_title="Jams & Juice",
    page_icon="🍹",
    layout="centered",
)
# CSS to remove rounded corners from all images
st.markdown(
    """
    <style>
    /* Remove rounding from all images rendered by Streamlit */
    img {
        border-radius: 0 !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)

st.title("🍹 Jams & Juice")
st.markdown("""
Welcome! Pick a drink below to discover a blended playlist and unlock a surprise for sharing with others.
""")

#Q1
flavor_options = ["Sweet", "Salty", "Bitter", "Sour"]
selected_flavor = st.selectbox("Select a flavor:", flavor_options, index=None)

#Q2
travel_options = ["Africa", "Antarctica", "Asia", "Australia", "Europe", "Latin America", "North America"]
selected_travel = st.selectbox("Which place do you wish to travel to one day?", travel_options, index=None)

#Q3
st.write("Pick a secret ingredient: (double-click)")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/realroses.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/tamarind-fruit-snack-1432243224.jpeg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/hothoney.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/realginger.jpg",
]

titles=["Rose", "Tamarind", "Hot honey", "Ginger"]

if "selected_ingredient" not in st.session_state:
    st.session_state.selected_ingredient = None

# Layout the images in 4 columns
cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        # Clicking the button selects this image
        if st.button(titles[i], key=f"btn_ingredient_{i}"):
            st.session_state.selected_ingredient = i

        # Add a red border if selected
        border = "4px solid red" if st.session_state.selected_ingredient == i else "4px solid transparent"

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
selected_ingredient = (
    titles[st.session_state.selected_ingredient]
    if st.session_state.get("selected_ingredient") is not None
    else None
)
#gap
st.write("")

#Q4
st.write("Which scenario sounds the most enjoyable? (double-click button)")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/hotchocolate.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/wine.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/lemonade.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/applecider.jpg",
]

titles=["Hot chocolate on a chilly night", "Wine during a thunderstorm", "Fresh lemonade on the beach", "Warm apple cider in a cabin"]

if "selected_mood" not in st.session_state:
    st.session_state.selected_mood = None

# Layout the images in 4 columns
cols = st.columns(4)

for i, col in enumerate(cols):
    with col:
        # Clicking the button selects this image
        if st.button(titles[i], key=f"btn_mood_{i}"):
            st.session_state.selected_mood = i

        # Add a red border if selected
        border = "4px solid red" if st.session_state.selected_mood == i else "4px solid transparent"

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
selected_mood = (
    titles[st.session_state.selected_mood]
    if st.session_state.get("selected_mood") is not None
    else None
)
#gap
st.write("")

# Business options and related data
drink_data = {
    "Caramel macchiato": {
        "playlist": "Maqamat Rhythms",
        "playlist_link": "https://open.spotify.com/playlist/6v1R5ZRQFn9m1JhD3WMAcV?si=q8KTnYuFTZyc7aVaYQxojQ",
#        "business_name": "Turkish Doner",
#        "location": "1007 W Argyle St, Chicago, IL 60640",
#        "website": "https://www.facebook.com/profile.php?id=61579383426862",
#        "business_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/turkishdoner.png",
    },
    "Chai latte": {
        "playlist": "World Country Beats",
        "playlist_link": "https://open.spotify.com/playlist/1KREbVZKOsE1T6vHuPbyrD?si=IwKmga-dSpaTogbSML0bqw",
#        "business_name": "Roggenart European Bakery, Bistro & Cafe",
#        "location": "3500 N Halsted St, Chicago, IL 60657",
#        "website": "https://roggenart.com/",
#        "business_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/roggenart.png",
    },
    "Milk tea boba": {
        "playlist": "Sweet Mellow Blues",
        "playlist_link": "https://open.spotify.com/playlist/3CpxGMwxThdLq76N98iqkP?si=rMhgl1S0S5SWnY1AmyW1jg",
#        "business_name": "Little Vietnam",
#        "location": "1132 W Bryn Mawr Ave, Chicago, IL 60660",
#        "website": "https://orderlittlevietnam.com/",
#        "business_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/littlevietnam.png"
    },
    "Horchata": {
        "playlist": "Reggaeton Fusions",
        "playlist_link": "https://open.spotify.com/playlist/34kBrKBySt0SqcP5YpvZM9?si=wbQYA-0hQtu9oCfVOP0abw",
#        "business_name": "Curry Kitchen",
#        "location": "5304 W Devon Ave, Chicago, IL 60646",
#        "website": "https://currykitchenchicago.com/",
#        "business_image": "https://currykitchenchicago.com/wp-content/uploads/2024/08/logo.jpg"
    }
}

info = None

drink_choice = st.selectbox("Pick a drink!", ["", *drink_data.keys()])

drink_map = {
    ("Sweet", "Rose", "Hot chocolate on a chilly night"): "Milk tea boba",
    ("Sweet", "Rose", "Wine during a thunderstorm"): "Chai latte",
    ("Sweet", "Rose", "Fresh lemonade on the beach"): "Horchata",
    ("Sweet", "Rose", "Warm apple cider in a cabin"): "Caramel macchiato",
    ("Sweet", "Tamarind", "Hot chocolate on a chilly night"): "Horchata",
    ("Sweet", "Tamarind", "Wine during a thunderstorm"): "Chai latte",
    ("Sweet", "Tamarind", "Fresh lemonade on the beach"): "Milk tea boba",
    ("Sweet", "Tamarind", "Warm apple cider in a cabin"): "Caramel macchiato",
    ("Sweet", "Hot honey", "Hot chocolate on a chilly night"): "Chai latte",
    ("Sweet", "Hot honey", "Wine during a thunderstorm"): "Caramel macchiato",
    ("Sweet", "Hot honey", "Fresh lemonade on the beach"): "Horchata",
    ("Sweet", "Hot honey", "Warm apple cider in a cabin"): "Milk tea boba",
    ("Sweet", "Ginger", "Hot chocolate on a chilly night"): "Horchata",
    ("Sweet", "Ginger", "Wine during a thunderstorm"): "Horchata",
    ("Sweet", "Ginger", "Fresh lemonade on the beach"): "Milk tea boba",
    ("Sweet", "Ginger", "Warm apple cider in a cabin"): "Chai latte",

    ("Salty", "Rose", "Hot chocolate on a chilly night"): "Chai latte",
    ("Salty", "Rose", "Wine during a thunderstorm"): "Horchata",
    ("Salty", "Rose", "Fresh lemonade on the beach"): "Milk tea boba",
    ("Salty", "Rose", "Warm apple cider in a cabin"): "Caramel macchiato",
    ("Salty", "Tamarind", "Hot chocolate on a chilly night"): "Caramel macchiato",
    ("Salty", "Tamarind", "Wine during a thunderstorm"): "Horchata",
    ("Salty", "Tamarind", "Fresh lemonade on the beach"): "Chai latte",
    ("Salty", "Tamarind", "Warm apple cider in a cabin"): "Milk tea boba",
    ("Salty", "Hot honey", "Hot chocolate on a chilly night"): "Horchata",
    ("Salty", "Hot honey", "Wine during a thunderstorm"): "Milk tea boba",
    ("Salty", "Hot honey", "Fresh lemonade on the beach"): "Chai latte",
    ("Salty", "Hot honey", "Warm apple cider in a cabin"): "Caramel macchiato",
    ("Salty", "Ginger", "Hot chocolate on a chilly night"): "Caramel macchiato",
    ("Salty", "Ginger", "Wine during a thunderstorm"): "Chai latte",
    ("Salty", "Ginger", "Fresh lemonade on the beach"): "Horchata",
    ("Salty", "Ginger", "Warm apple cider in a cabin"): "Horchata",

    ("Bitter", "Rose", "Hot chocolate on a chilly night"): "Horchata",
    ("Bitter", "Rose", "Wine during a thunderstorm"): "Horchata",
    ("Bitter", "Rose", "Fresh lemonade on the beach"): "Chai latte",
    ("Bitter", "Rose", "Warm apple cider in a cabin"): "Chai latte",
    ("Bitter", "Tamarind", "Hot chocolate on a chilly night"): "Milk tea boba",
    ("Bitter", "Tamarind", "Wine during a thunderstorm"): "Horchata",
    ("Bitter", "Tamarind", "Fresh lemonade on the beach"): "Caramel macchiato",
    ("Bitter", "Tamarind", "Warm apple cider in a cabin"): "Chai latte",
    ("Bitter", "Hot honey", "Hot chocolate on a chilly night"): "Chai latte",
    ("Bitter", "Hot honey", "Wine during a thunderstorm"): "Caramel macchiato",
    ("Bitter", "Hot honey", "Fresh lemonade on the beach"): "Milk tea boba",
    ("Bitter", "Hot honey", "Warm apple cider in a cabin"): "Horchata",
    ("Bitter", "Ginger", "Hot chocolate on a chilly night"): "Horchata",
    ("Bitter", "Ginger", "Wine during a thunderstorm"): "Chai latte",
    ("Bitter", "Ginger", "Fresh lemonade on the beach"): "Chai latte",
    ("Bitter", "Ginger", "Warm apple cider in a cabin"): "Caramel macchiato",

    ("Sour", "Rose", "Hot chocolate on a chilly night"): "Chai latte",
    ("Sour", "Rose", "Wine during a thunderstorm"): "Horchata",
    ("Sour", "Rose", "Fresh lemonade on the beach"): "Chai latte",
    ("Sour", "Rose", "Warm apple cider in a cabin"): "Milk tea boba",
    ("Sour", "Tamarind", "Hot chocolate on a chilly night"): "Caramel macchiato",
    ("Sour", "Tamarind", "Wine during a thunderstorm"): "Milk tea boba",
    ("Sour", "Tamarind", "Fresh lemonade on the beach"): "Horchata",
    ("Sour", "Tamarind", "Warm apple cider in a cabin"): "Chai latte",
    ("Sour", "Hot honey", "Hot chocolate on a chilly night"): "Milk tea boba",
    ("Sour", "Hot honey", "Wine during a thunderstorm"): "Horchata",
    ("Sour", "Hot honey", "Fresh lemonade on the beach"): "Caramel macchiato",
    ("Sour", "Hot honey", "Warm apple cider in a cabin"): "Chai latte",
    ("Sour", "Ginger", "Hot chocolate on a chilly night"): "Caramel macchiato",
    ("Sour", "Ginger", "Wine during a thunderstorm"): "Horchata",
    ("Sour", "Ginger", "Fresh lemonade on the beach"): "Caramel macchiato",
    ("Sour", "Ginger", "Warm apple cider in a cabin"): "Milk tea boba",
}


if selected_flavor and selected_travel and selected_ingredient and selected_mood and drink_choice:
    user_combo = (selected_flavor, selected_ingredient, selected_mood)
    result_key = drink_map.get(user_combo)

    if result_key:
        info = drink_data[result_key]

    # Display playlist and business info
    st.subheader(f"🎵 Your playlist is {info['playlist']}!")
    playlist_link = info["playlist_link"]

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
#    st.image(info['business_image'], width=250)  # Show business image (if available)
#    st.write(f"🏷️ **Business Name:** {info['business_name']}")
#    st.write(f"🌐 [Visit Website]({info['website']})")
#    st.write(f"📍 **Address:** {info['location']}")

    st.write("")
    st.subheader("Share your playlist!", divider="grey")
    st.write("")

    # Share Playlist with Others
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

