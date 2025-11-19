import streamlit as st

birria = "https://i.imgur.com/3ACcDlF.jpeg"
st.image(birria, caption="Birria tacos", width=200)

pasta = "https://i.imgur.com/8wTBiHb.jpeg"
st.image(pasta, caption="Pasta", width=200)

burger = "https://i.imgur.com/y0Ezg5M.jpeg"
st.image(burger, caption="Burger", width=200)

ice_cream = "https://i.imgur.com/QDmOxZ8.jpeg"
st.image(ice_cream, caption="Ice cream", width=200)

taiyaki = "https://i.imgur.com/CNre03d.jpeg"
st.image(taiyaki, caption="Taiyaki", width=200)

#GIF
dancingcat = "https://i.imgur.com/J7O2RSz.gif"
st.image(dancingcat, caption="Dancing cat", width=200)

#video w/ audio
video_url = "https://i.imgur.com/6qioN0t.mp4"

st.video(video_url, width=300)

guess = ["Piano", "Trumpet", "Guitar", "Clarinet"]
selected_one = st.radio("Guess the instrument:", guess, index=None)



# Define pages with emojis
pages = {
    "🍹 Jams & Juice": "02_Jams_and_Juice",
    "🍬 Sweet Melodies": "03_Sweet_Melodies",
    "💿 Y2K Rewind": "04_Y2K_Rewind",
    "🍂 Sweater Weather Tunes": "05_Sweater_Weather_Tunes",
    "🎨 Craft & Sip": "06_Craft_and_CoSip",
    "🪞 Serene Self-Care": "07_Serene_Self_Care",
    "🎉 Press Play to Party": "08_Press_Play_to_Party",
    "🎶 Guess the Instrument": "09_Guess_the_Instrument",
    "🎵 Music Trivia": "10_Music_Trivia",
    "🖼️ Images": "11_Images",
}

# Number of columns in the grid
cols_num = 3
cols = st.columns(cols_num)

i = 0
for label, file in pages.items():
    with cols[i % cols_num]:
        # Card style using markdown inside a button
        button_html = f"""
        <div style="
            background-color: #1DB954; 
            color: white; 
            padding: 20px; 
            text-align: center; 
            border-radius: 12px; 
            margin-bottom: 15px;
            font-weight: bold;
            font-size: 16px;
            cursor: pointer;
        ">
            {label}
        </div>
        """
        if st.button(label, key=file, use_container_width=True):
            st.switch_page(f"pages/{file}.py")
    i += 1

