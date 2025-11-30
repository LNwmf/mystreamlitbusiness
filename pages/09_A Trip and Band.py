import streamlit as st

st.set_page_config(
    page_title="Plan a Trip!",
    page_icon="✈️",
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

st.title("✈️ Plan a Trip!")
st.markdown("""
You're preparing for a dream vacation in the summer. Based on your preferences, you'll be matched with a traditional band around the world!
""")

#Q1
destinations = ["Vibrant Tanzanian coastal city full of wildlife",
                "Cozy Irish village infused with lively music",
                "Japanese countryside dotted with hot springs",
                "Bustling Mexican town with thrilling celebrations",
                "Refreshing waters of the tropical Caribbean islands",
                "Vast monuments and arts of a Middle Eastern city"]
selected_destination = st.selectbox("Choose a destination:", destinations, index=None)