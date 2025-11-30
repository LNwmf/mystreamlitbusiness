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

#Q2
vibe = ["Dynamic and spontaneous", "Beachy and tranquil", "Nostalgic but homey", "Abundant and soulful", "Scenic and spirited", "Timeless yet therapeutic"] #mariachi, caribbean, irish, middle east, tanzania, japanese
selected_vibe = st.selectbox("What's the vibe of your trip?", vibe, index=None)

#Q3
st.write("What are you craving when you land? (double-click button)")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/ulsterfry.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/chipsimayai.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/tabbouleh.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/chilaquiles.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/hiyayakkomeals.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/doublemeals.jpg",
]

titles=[" 1 ", " 2 ", " 3 ", " 4 ", " 5 ", " 6 "] #ireland-Ulster Fry, tanzania-Chipsi Mayai, middle east-Tabbouleh, mexico-Chilaquiles, japan-Hiyayakko, caribbean-Doubles

if "selected_meal" not in st.session_state:
    st.session_state.selected_meal = None

cols = st.columns(6)

for i, col in enumerate(cols):
    with col:
        if st.button(titles[i], key=f"btn_meal_{i}"):
            st.session_state.selected_meal = i

        border = "4px solid red" if st.session_state.selected_meal == i else "4px solid transparent"

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

selected_meal = (
    titles[st.session_state.selected_meal]
    if st.session_state.get("selected_meal") is not None
    else None
)
#gap
st.write("")

#Q4
stumble = ["A sheep traffic jam on a vacant road", #ireland
           "A sea turtle casually joining you while snorkeling", #caribbean
           "A zebra photobombing your selfie during a safari tour", #tanzania
           "Encountering a bunch of friendly cats while on a stroll in a village", #japan
           "Stumbling into a hidden cenote behind a jungle trail", #mexico
           "A secluded cafe serving rich, warm coffees and teas"] #middle east
selected_stumble = st.selectbox("What's the most unexpected thing you'd be excited to stumble upon?", stumble, index=None)

#Q5
moment = ["In front of the Pyramids of Giza while the sun rises", #middle east
        "Underneath the Arch of Cabo San Lucas during the sunset", #mexico
        "Engulfed by cherry blossoms in Hirosaki Park in the spring", #japan
        "Drifting through Harrison's Cave on an eco-adventure", #caribbean
        "Lost in the Blarney Castle in the summertime", #irish
        "Safari tour in Tarangire National Park surrounded by wildlife "] #tanzania
selected_moment = st.selectbox("If you could teleport to one picture-perfect moment, where would it be?", moment, index=None)

#Q6
st.write("What activity do you look most forward to? (double-click button)")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/culinarytour.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/hikingtanzania.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/snorkeling.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/ancientruins.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/japanfestival.jpg",
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/sightseeing.jpg",
]

titles=["Culinary tour", "Hiking", "Snorkeling", "Exploring ancient ruins", "Visiting festivals", "Scenic drive"] #mexico-culinary tour, tanzania-hiking, caribbean-snorkeling/diving, middle east-explore ancient sites, japan-visit festivals, ireland-scenic drive/sightseeing

if "selected_activity" not in st.session_state:
    st.session_state.selected_activity = None

# ------ FIRST ROW (items 0,1,2) ------
cols = st.columns(3)
for i, col in enumerate(cols):
    with col:
        if st.button(titles[i], key=f"btn_activity_{i}"):
            st.session_state.selected_activity = i

        border = "4px solid red" if st.session_state.selected_activity == i else "4px solid transparent"
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

# ------ SECOND ROW (items 3,4,5) ------
cols = st.columns(3)
for idx, col in enumerate(cols, start=3):
    with col:
        if st.button(titles[idx], key=f"btn_activity_{idx}"):
            st.session_state.selected_activity = idx

        border = "4px solid red" if st.session_state.selected_activity == idx else "4px solid transparent"
        st.markdown(
            f"""
            <div style="
                border:{border};
                border-radius:10px;
                padding:3px;
                display:flex;
                justify-content:center;
            ">
                <img src="{images[idx]}" style="width:170px; border-radius:10px;">
            </div>
            """,
            unsafe_allow_html=True,
        )

selected_activity = (
    titles[st.session_state.selected_activity]
    if st.session_state.get("selected_activity") is not None
    else None
)
#gap
st.write("")

#Q7