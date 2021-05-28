import streamlit as st
import cv2
import matplotlib.pyplot as plt
# from deepface import DeepFace
header  = st.beta_container()
input = st.beta_container()
pred = st.beta_container()

# Write something in a container

with header:
    st.title('Emotion Detection and Song Recommendation')
    st.text('Aim : To detect the emotion of the person and predict a song')

with input:
    st.title("Taking the face of the user as input")
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
# 1.creating a video object
video = cv2.VideoCapture(0) 
# 2. Variable
a = 0
# 3. While loop
while True:
    a = a + 1
    # 4.Create a frame object
    check, frame = video.read()
    # Converting to grayscale
    # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # 5.show the frame!
    cv2.imshow("Capturing",frame)
    # 6.for playing 
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
# 7. image saving
showPic = cv2.imwrite("photo.jpg",frame)
print(showPic)
# 8. shutdown the camera
video.release()
cv2.destroyAllWindows()


# with pred():
#     st.title("Prediction")
#     img = cv2.imread('photo.jpg')

#     plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))

#     predictions = DeepFace.analyze(img)

#     st.body("Your emotion is",predictions)  


