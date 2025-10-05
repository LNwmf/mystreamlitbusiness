import streamlit as st

st.set_page_config(
    page_title="Serene Self-Care",
    page_icon="🪞",
    layout="centered",
)

st.image("https://theworldmusicfoundation.org/wp-content/uploads/2016/11/wmf_small_logo.png.webp", width=180)
st.title("🪞 Serene Self-Care")
st.markdown("""
Welcome! Pick an energy below to discover a blended playlist, support a local BIPOC business, and unlock a reward for sharing with others.
""")

#Q1
unwind_options = ["Taking a warm bath", "Going on a nature walk", "Listening to music", "Treating myself to a meal"]
selected_unwind = st.selectbox("How do you unwind after a long day?", unwind_options, index=None)

#Q2
scent_data = {
    "Lavender": {
    "scent_image": "https://bouqs.com/blog/wp-content/uploads/2024/08/shutterstock_2485398557-min-1080x720.jpg",
    },
    "Jasmine": {
    "scent_image": "https://www.chicagobotanic.org/sites/default/files/2025/01/09/jasmine-1400x787.jpg",
    },
    "Eucalyptus": {
    "scent_image": "https://mimosanurseryonline.com/cdn/shop/products/64c02307da09d05022a2eb01.png?v=1690474428"
    },
    "Sandalwood": {
    "scent_image": "https://www.carrementbelle.com/blog/wp-content/uploads/2020/08/sandalwood.jpg"
    },
}
selected_scent = st.selectbox("Select a scent:", ["", *scent_data.keys()])

if selected_scent:
    info1 = scent_data[selected_scent]

    st.image(info1['scent_image'], width=250)

#Q3
secret = ["Confidence", "Wonder", "Relaxation", "Magic"]
selected_secret = st.selectbox("What's the secret ingredient to feeling your absolute best?", secret, index=None)

#Q4
calm_data = {
    "Ambient beach": {
    "calm_image": "https://www.rd.com/wp-content/uploads/2025/05/This-Stunningly-Beautiful-Beach_GettyImages-482612302_FT.jpg",
    },
    "Quiet mountainside": {
    "calm_image": "https://www.dyangarrismusic.com/wp-content/uploads/edd/konigssee-2522545_1920-mountains.jpg",
    },
    "Bustling city": {
    "calm_image": "https://sharedeasy.club/wp-content/uploads/blog/new-york-city-evening-NYCTG0221-52492d6ccab44f328a1c89f41ac02aea.jpg"
    },
    "Lush forest": {
    "calm_image": "https://www.shutterstock.com/image-photo/beautiful-sunlight-green-forest-majestic-600nw-2458222501.jpg"
    },
}
selected_calm = st.selectbox("Pick a getaway place:", ["", *calm_data.keys()])

if selected_calm:
    info2 = calm_data[selected_calm]

    st.image(info2['calm_image'], width=250)

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
    # Dessert Selection
energy_choice = st.selectbox("How would you describe your current energy?", ["", *energy_data.keys()])

if energy_choice:
    # Retrieve information about selected drink/business
    info3 = energy_data[energy_choice]

    # Display playlist and business info
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