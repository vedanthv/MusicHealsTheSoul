# Importing the librarires
import streamlit as st
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import streamlit as st
import test
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random


client_id = '8be5f0367b7a4b54b730b33faa7c1b2c'
client_secret = '0bc78da67fa44fe985c2586aa74d7e1d'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager =client_credentials_manager)

# Creating the containers
header  = st.beta_container()
inp = st.beta_container()
pred = st.beta_container()

with header:
    st.title('Emotion Detection and Song Recommendation')
    st.text('Aim : To detect the emotion of the person and predict a song')

# Captures user's face as input
with inp:
    st.title("Taking the user's face as input")
    st.markdown("**Press 'C' to capture the image**")
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    test.take_input()

# Predicting the dominant emotion
with pred:
    st.title("Prediction")
    img = cv2.imread('photo.jpg')

    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

    predictions = DeepFace.analyze(img)

    emotion = predictions['dominant_emotion']

    st.markdown("<b>You don't look very happy!</b> ")  

# Recommending songs based on the dominant emotion
    if(predictions['dominant_emotion'] != 'happy'):

        playlist_id = '42EL4koTAevxJ4R8IT8OHJ'
        #func to extract all track ids
        def get_track_ids(playlist_id):
            music_id_list = []
            playlist = sp.playlist(playlist_id)
            # creating a list of track ids of all the songs in the playlist
            for item in playlist['tracks']['items']:
                music_track = item['track']
                music_id_list.append(music_track['id'])
            return music_id_list
        
        track_ids = get_track_ids(playlist_id)

        # looping over the entire track_ids list and returning 5 random songs
        for i in range(5):
            random.shuffle(track_ids)
            embed = '<iframe src="https://open.spotify.com/embed/track/{}" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'.format(track_ids[0])

            st.markdown(embed, unsafe_allow_html=True)

