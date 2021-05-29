import streamlit as st
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace
# from deepface import DeepFace
import streamlit as st
import test

header  = st.beta_container()
inp = st.beta_container()
pred = st.beta_container()

with header:
    st.title('Emotion Detection and Song Recommendation')
    st.text('Aim : To detect the emotion of the person and predict a song')

with inp:
    st.title("Taking the face of the user as input")
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
    page = st.sidebar.selectbox("Input or Predict", ("Input", "Predict"))

    if page == "Input":
        test.take_input()
#else:
    #show_explore_page()

with pred:
    st.title("Prediction")
    img = cv2.imread('photo.jpg')

    plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

    predictions = DeepFace.analyze(img)

    st.text("Your emotion is {}".format(predictions['dominant_emotion']))  


    if(predictions['dominant_emotion'] == 'happy'):
        my_html = '<iframe src="https://open.spotify.com/embed/playlist/37i9dQZF1DWWQRwui0ExPn" width="300" height="380" frameborder="0" allowtransparency="true" allow="encrypted-media"></iframe>'

        st.markdown(my_html, unsafe_allow_html=True)

    