import streamlit as st


# --- Define each page as a function ---
def home_page():
    st.title("🏠 Home")
    st.markdown("Welcome! Use the buttons below to navigate through the app.")

def jams_and_juice():
    st.title("🍹 Jams & Juice")
    st.markdown("Pick a drink and discover a blended playlist!")

def rewards():
    st.title("🎁 Rewards")
    st.markdown("Check out your rewards and special offers!")

def about():
    st.title("ℹ️ About")
    st.markdown("Learn more about this app and its mission.")

def contact():
    st.title("📬 Contact")
    st.markdown("Get in touch with us!")

# --- Navigation logic ---
pages = {
    "Home": home_page,
    "Jams & Juice": jams_and_juice,
    "Rewards": rewards,
    "About": about,
    "Contact": contact
}

# Track selected page
if "page" not in st.session_state:
    st.session_state.page = "Home"

# Sidebar navigation (optional) or buttons on home page
if st.session_state.page == "Home":
    st.markdown("### Navigate to a page:")
    for page_name in pages.keys():
        if page_name != "Home":  # skip Home itself
            if st.button(page_name):
                st.session_state.page = page_name

# Render the selected page
pages[st.session_state.page]()

# Add a "Back to Home" button on other pages
if st.session_state.page != "Home":
    if st.button("⬅️ Back to Home"):
        st.session_state.page = "Home"