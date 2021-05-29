import streamlit as st
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
import spotipy

from spotipy.oauth2 import SpotifyClientCredentials
import streamlit as st
import test
import random

client_id = '8be5f0367b7a4b54b730b33faa7c1b2c'
client_secret = '0bc78da67fa44fe985c2586aa74d7e1d'

client_credentials_manager = SpotifyClientCredentials(client_id, client_secret)
sp = spotipy.Spotify(client_credentials_manager =client_credentials_manager)

header  = st.beta_container()
inp = st.beta_container()
pred = st.beta_container()

with header:
    st.image('background.png')
    st.title('Emotion Detection and Song Recommendation')
    st.markdown('**Aim : To detect the emotion of the person and predict a song**')

with inp:
    st.title("Image Capture")
    st.markdown("**Capturing an image of your face**")
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    test.take_input()

with pred:
    st.title("Let's see what songs you should listen to !!")
    img = cv2.imread('photo.jpg')

    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

    predictions = DeepFace.analyze(img)

    #st.text("Your emotion is {}".format(predictions['dominant_emotion']))  

    if(predictions['dominant_emotion'] != 'happy'):

        st.markdown("**You don't look too cheerful....Here are some songs to lift your mood up!!**")
        playlist_id = '37i9dQZF1DX9XIFQuFvzM4'

        def get_track_ids(playlist_id):
            music_id_list = []
            playlist = sp.playlist(playlist_id)

            for item in playlist['tracks']['items']:
                music_track = item['track']
                music_id_list.append(music_track['id'])
            return music_id_list

        track_ids = get_track_ids(playlist_id)

        for i in range(5):

            random.shuffle(track_ids)

            my_html = '<iframe src="https://open.spotify.com/embed/track/{}" width="300" height="100" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'.format(track_ids[0])

            st.markdown(my_html, unsafe_allow_html=True)


