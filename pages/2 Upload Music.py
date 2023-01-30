import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
import streamlit as st
import spotipy
from Metadata import getmetadata
import requests

loaded_model = pickle.load(
    open('trained_pipe_updated.pkl', 'rb'))

# Access token needs to get updated after every 1 hour of usage
access_token = "BQDHnCqxGTdiXkh_jo1IAOJi_Zf3Vqpd84AhA53_Pe8mT8nbuodSGGTsBFU-4anrbbtK6X-ts1aBFj7cWtKLGLkykU9Kv23hz4SYKSBkRvkvuMmTsZwkOLx08n5ttsjcZ9-OEEm4JJlUW7NpNC0tUM7hzcWU6l27CsqL52eeYL2OzcJY4nIzROYCjRqNexW9PGY"


# creating a function for prediction


def genre_prediction(input_data):

    d1 = np.array(input_data)
    data1 = d1.reshape(1, -1)
    model = loaded_model.predict(data1)
    # st.write(model)

#       Genres
#       0: 'blues',
#       1: 'classical',
#       2: 'country',
#       3: 'disco',
#       4: 'hiphop',
#       5: 'jazz',
#       6: 'metal',
#       7: 'pop',
#       8: 'reggae',
#       9: 'rock'

    if model == 0:
        genre_model = "Blues"
    elif model == 1:
        genre_model = "Classical"
    elif model == 2:
        genre_model = "Country"
    elif model == 3:
        genre_model = "Disco"
    elif model == 4:
        genre_model = "Hip-hop"
    elif model == 5:
        genre_model = "Jazz"
    elif model == 6:
        genre_model = "Metal"
    elif model == 7:
        genre_model = "Pop"
    elif model == 8:
        genre_model = "Raggae"
    elif model == 9:
        genre_model = "Rock"

    return genre_model


def check_access_token(access_token):
    url = "https://api.spotify.com/v1/me"
    headers = {
        "Authorization": f"Bearer {access_token}"
    }
    response = requests.get(url, headers=headers)

    # Check if the access token is valid
    if response.status_code != 200:
        error = response.json()["error"]
        if error["status"] == 401:
            st.error(
                "The access token is invalid. Please update the token and try again.")
            return False
    return True


def main():

    # Page Title
    st.title("Determine The Genre of Your Music")

    try:
        # getting input from user
        file = st.file_uploader("Upload Your Music Here", type=["wav"])

    except Exception as e:
        st.warning("Upload .wav file only")

    if file is not None:
        st.audio(file)
        uploaded_audio = getmetadata(file)

    # Code for prediction
    genre = ''

    # Creating a button for prediction
    if st.button('Predict Now !'):
        with st.spinner("Predicting genre and searching tracks on Spotify..."):
            genre = genre_prediction(uploaded_audio)
            st.success(genre)
# ______________________________________________________________________________________________________________________
        # DISPLAY FROM SPOTIFY
        if check_access_token(access_token):
            try:

                # Create a Spotify client
                spotify = spotipy.Spotify(auth=access_token)

                # Try making a request to the Spotify API
                # spotify.current_playback()

                # Determine the genre of the song (replace with your own code)
                genre_image = genre

                # Search for songs in the specified genre
                results = spotify.search(q=genre_image, type="track")

                # Extract the first track from the search results
                tracks = results["tracks"]["items"]

                # Iterate over the tracks and display the cover art and song name for each one
                for track in tracks:
                    cover_art_url = track["album"]["images"][0]["url"]
                    song_name = track["name"]
                    st.image(cover_art_url, width=100)
                    st.write(song_name)

            except spotipy.client.SpotifyException as e:
                st.error(
                    "An error occurred while calling the Spotify API: " + str(e))
# ______________________________________________________________________________________________________________________
    # st.success(genre)


if __name__ == '__main__':
    main()
