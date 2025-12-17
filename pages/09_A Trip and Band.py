from st_copy import copy_button
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
You're preparing for a dream vacation in the summer. Your answers will determine which traditional band you should join around the world!
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
vibe = ["Dynamic and spontaneous", "Beachy and tranquil", "Nostalgic but homey", "Abundant and soulful", "Scenic and spirited", "Timeless yet therapeutic"]
#mariachi, caribbean, irish, middle east, tanzania, japanese
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

titles=["Ulster Fry", "Chipsi Mayai", "Tabbouleh", "Chilaquiles", "Hiyayakko", "Doubles"]
#ireland-Ulster Fry, tanzania-Chipsi Mayai, middle east-Tabbouleh, mexico-Chilaquiles, japan-Hiyayakko, caribbean-Doubles

if "selected_meal" not in st.session_state:
    st.session_state.selected_meal = None

# ------ FIRST ROW (items 0,1,2) ------
cols = st.columns(3)
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
#gap
st.write("")

# ------ SECOND ROW (items 3,4,5) ------
cols = st.columns(3)
for idx, col in enumerate(cols, start=3):
    with col:
        if st.button(titles[idx], key=f"btn_meal_{idx}"):
            st.session_state.selected_meal = idx

        border = "4px solid red" if st.session_state.selected_meal == idx else "4px solid transparent"
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
        "Safari tour in Tarangire National Park surrounded by wildlife"] #tanzania
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

titles=["Culinary tour", "Hiking", "Snorkeling", "Exploring ancient ruins", "Visiting festivals", "Scenic drive"]
#mexico-culinary tour, tanzania-hiking, caribbean-snorkeling/diving, middle east-explore ancient sites, japan-visit festivals, ireland-scenic drive/sightseeing

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
#gap
st.write("")

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
day = ["Lanterns transform into different shapes in the sky", #japan
        "Flowers bloom on trees as you walk past", #tanzania
        "Red foxes start walking backwards in a grassland", #irish
        "Desert sand shimmers like gold at night", #middle east
        "Ocean waves grow and fall like they're breathing", #caribbean
        "Murals animate and dance to tell stories"] #mexico
selected_day = st.selectbox("If your day suddenly became surreal, what would happen?", day, index=None)

#Q8
st.write("Pick a souvenir to tell your vacation journey: (double-click button)")
images = [

        "https://theworldmusicfoundation.org/wp-content/streamlitimages/sweater1.jpg", #ireland-Aran sweater that smells like the vast landscapes and cliffs
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/miningomadrum.jpg", #tanzania-Mini ngoma drum that plays catchy rhythms
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/jarrito.jpg", #mexico-A jarrito to represent the deep artistry and culture
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/molas.jpg", #caribbean-Molas that depict the strong Guna identity and freedom
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/omamori.png", #japan-An omamori that provides good luck and protection in life
        "https://theworldmusicfoundation.org/wp-content/streamlitimages/maamoul.png", #middle east-Maamouls to remember the hospitality and rich heritage
]

titles=["Aran sweater", "Mini ngoma drum", "Jarrito", "Molas", "Omamori", "Maamouls"]

if "selected_souvenir" not in st.session_state:
    st.session_state.selected_souvenir = None

# ------ FIRST ROW (items 0,1,2) ------
cols = st.columns(3)
for i, col in enumerate(cols):
    with col:
        if st.button(titles[i], key=f"btn_souvenir_{i}"):
            st.session_state.selected_souvenir = i

        border = "4px solid red" if st.session_state.selected_souvenir == i else "4px solid transparent"
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
#gap
st.write("")

# ------ SECOND ROW (items 3,4,5) ------
cols = st.columns(3)
for idx, col in enumerate(cols, start=3):
    with col:
        if st.button(titles[idx], key=f"btn_souvenir_{idx}"):
            st.session_state.selected_souvenir = idx

        border = "4px solid red" if st.session_state.selected_souvenir == idx else "4px solid transparent"
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

selected_souvenir = (
    titles[st.session_state.selected_souvenir]
    if st.session_state.get("selected_souvenir") is not None
    else None
)
#gap
st.write("")
st.write("")
st.write("")

logic_data = {
    "Folk": {
        "join": "You should join a...",
        "band": "Celtic Folk Band",
        "fun_fact": "Traditional Irish folk music was passed down through oral tradition in informal pubs 'sessions'. Today, people continue to gather and learn tunes from each other, usually by ear.",
        "music": "https://youtu.be/tcYx62F6FVM?si=L5ebSR0x-tpsZqLT",
        "band_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/thechieftains.jpg",
    },

    "Mariachi": {
    "join": "You should join a...",
    "band": "Mariachi Band",
    "fun_fact": "There's no lead singer in mariachi music. Each musician take turns singing and playing for songs. They are expected to be both skilled singers and instrumentalists.",
    "music": "https://youtu.be/XxBAwr_FkoQ?si=ZutpTUIFUIulwzvt",
    "band_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/mariachisoldemexico.jpg",
    },

    "Taiko": {
    "join": "You should join a...",
    "band": "Taiko Ensemble",
    "fun_fact": "Taiko drumming combines athleticism, dance, and art. It requires great physical and mental stamina to play, memorize, and coordinate rhythms.",
    "music": "https://youtu.be/kcQt0W72o-M?si=TaRLytXLJgZgnljw",
    "band_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/taikotsukasa.jpg",
    },

    "Taarab": {
    "join": "You should join a...",
    "band": "Taarab Ensemble",
    "fun_fact": "Having roots in Zanzibar, taarab music often consists of poetic lyrics about love, politics, and social issues. It helps communities express their hopes and dreams.",
    "music": "https://youtu.be/NO014wZWFNA?si=f_vvBsd9L4JDeMpV",
    "band_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/taarab.jpg",
    },

    "Calypso": {
        "join": "You should join a...",
        "band": "Calypso Band",
        "fun_fact": "Calypso music addressed social and political issues in witty, satirical lyrics, making it a powerful tool for free speech. Competing in calypso tents, calypsonians battle for the best songs during the Carnival season.",
        "music": "https://youtu.be/l-j-tPbOfYQ?si=KAErgz3_cVrJzg80",
        "band_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/kawecalypso.jpg",
    },

    "Takht": {
        "join": "You should join a...",
        "band": "Takht Ensemble",
        "fun_fact": "Typically, a takht is comprised of 6 instruments: the oud, ney, qanun, riq, kamancheh, and darbuka.",
        "music": "https://youtu.be/ET2bgLiqjaY?si=Hj7gqbRgvwxyah6E",
        "band_image": "https://theworldmusicfoundation.org/wp-content/streamlitimages/takht.jpg",
    },
}

band_answer_map = {
    "Folk": {
        "Cozy Irish village infused with lively music",
        "Nostalgic but homey",
        "Ulster Fry",
        "A sheep traffic jam on a vacant road",
        "Lost in the Blarney Castle in the summertime",
        "Scenic drive",
        "Red foxes start walking backwards in a grassland",
        "Aran sweater",
    },

    "Mariachi": {
        "Bustling Mexican town with thrilling celebrations",
        "Dynamic and spontaneous",
        "Chilaquiles",
        "Stumbling into a hidden cenote behind a jungle trail",
        "Underneath the Arch of Cabo San Lucas during the sunset",
        "Culinary tour",
        "Murals animate and dance to tell stories",
        "Jarrito",
    },

    "Taiko": {
        "Japanese countryside dotted with hot springs",
        "Timeless yet therapeutic",
        "Hiyayakko",
        "Encountering a bunch of friendly cats while on a stroll in a village",
        "Engulfed by cherry blossoms in Hirosaki Park in the spring",
        "Visiting festivals",
        "Lanterns transform into different shapes in the sky",
        "Omamori",
    },

    "Taarab": {
        "Vibrant Tanzanian coastal city full of wildlife",
        "Scenic and spirited",
        "Chipsi Mayai",
        "A zebra photobombing your selfie during a safari tour",
        "Safari tour in Tarangire National Park surrounded by wildlife",
        "Hiking",
        "Flowers bloom on trees as you walk past",
        "Mini ngoma drum",
    },

    "Calypso": {
        "Refreshing waters of the tropical Caribbean islands",
        "Beachy and tranquil",
        "Doubles",
        "A sea turtle casually joining you while snorkeling",
        "Drifting through Harrison's Cave on an eco-adventure",
        "Snorkeling",
        "Ocean waves grow and fall like they're breathing",
        "Molas",
    },

    "Takht": {
        "Vast monuments and arts of a Middle Eastern city",
        "Abundant and soulful",
        "Tabbouleh",
        "A secluded cafe serving rich, warm coffees and teas",
        "In front of the Pyramids of Giza while the sun rises",
        "Exploring ancient ruins",
        "Desert sand shimmers like gold at night",
        "Maamouls",
    },
}

user_answers = {
    selected_destination,
    selected_vibe,
    selected_meal,
    selected_stumble,
    selected_moment,
    selected_activity,
    selected_day,
    selected_souvenir,
}


band_scores = {
    band: len(user_answers & answers)
    for band, answers in band_answer_map.items()
}

best_band = max(band_scores, key=band_scores.get)

result = logic_data[best_band]


if result:
    st.subheader(result["join"])
    st.header(result["band"])
    st.write(result["fun_fact"])
    if result["band_image"]:
        st.image(result["band_image"], width=400)

    if result["music"]:
        music_link = result["music"]
        col1, col2 = st.columns([0.5, 1])
        with col1:
            st.markdown(
                f"""
                         <a href="{music_link}" target="_blank" style="font-size:20px; font-weight:bold;">
                             Music recommendation
                         </a>
                         """,
                unsafe_allow_html=True
            )
        with col2:
            copy_button(music_link)  # copies the music link


