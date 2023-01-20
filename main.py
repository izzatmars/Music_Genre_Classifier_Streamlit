import streamlit as st


# Add a header
st.title("Welcome to My Music Genre Classifier")

# Add a subheader
st.subheader("Explore the amazing content on our page")

# Add some text
st.text("Our web page is helps musicians to determine the genre of their music")

# Add a button
if st.button("Explore Now"):
    st.write("Enjoy exploring our web page!")

# Add an image
st.header("Collaborators")
image_url = "MF logo.jpg"

st.image(image_url, width=100)
st.write("Midnight Fusic")
