import streamlit as st

st.title("📬 Submit Your Business")

with st.form("business_form"):
    name = st.text_input("Business Name*", max_chars=100)
    description = st.text_area("Short Description*", max_chars=300)
    category = st.selectbox("Category*", ["Cafe", "Restaurant", "Bookstore", "Shop", "Service", "Other"])
    website = st.text_input("Website (optional)")
    image_url = st.text_input("Image URL (optional)")
    email = st.text_input("Contact Email*")
    spotlight = st.checkbox("Consider us for a Spotlight Feature")

    submitted = st.form_submit_button("Submit")

    if submitted:
        if not name or not description or not email:
            st.error("Please fill in all required fields.")
        else:
            # Prepare the row data
            #row = [
                #datetime.now().isoformat(),
                #name,
                #description,
                #category,
                #website,
                #image_url,
                #email,
                #"yes" if spotlight else "no"
            #]
            #try:
                #sheet.append_row(row)
                st.success("Thank you! Your business has been submitted successfully.")
            #except Exception as e:
             #   st.error(f"Oops! Something went wrong: {e}")