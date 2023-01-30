import streamlit as st


# Add a header
st.title("Welcome to My Music Genre Classifier")

# Add a subheader
st.subheader("Explore the amazing content on our page")

# Add some text
st.text("Our web page is helps musicians to determine the genre of their music")
st.text(" ")
st.header("It could determine a few genres which is :")
st.text("- Blues")
st.text("- Classical")
st.text("- Country")
st.text("- Disco")
st.text("- Hip-Hop")
st.text("- Jazz")
st.text("- Metal")
st.text("- Pop")
st.text("- Raggae")
st.text("- Rock")
st.text(" ")

# Add an image
st.header("How do i use the web page ?")
st.text("1) Click on the 'Upload Music' tab on the left of the screen.")
st.text("2) After the page has fully loaded, upload by dragging the music file into the upload tab or press 'Browse files' to get the file.")
st.text("3) After uploading, press the 'Predict Now !' button.")
st.text("4) The webpage will display the genre of the song and similar song to the genre.")
