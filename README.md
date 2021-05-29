## Music Heals the Soul - HackOn Hackathon 2021
<img src = "background.png">
Theme : Mental Wellness

### Introduction

Music Heals the Soul is a Smart Application that predicts songs froom Spotify of a particular Genre based on the real time emotions of the user.

### What problems does it solve?

Often, people are depressed about something and dont find it easy to communicate their problems with others. This may lead to severe depression and suicidal thoughts.

Music is often a key under estimated factor that can help calm their mind and cheer them up.

In this project, we have created a live emotion detection algorithm that can predict the emotions of the person in real time and recommend songs to cheer them up!

### Inspiration

The coronavirus pandemic has taken a toll on our mental health. And one of the few things that makes us feel good, and disconnects us from reality is *music*. Music has kept most of us sane during these testing times. 
One of the greatest qualities of music is the range of emotion in the songs. Each song has been written by the songwriters, who pen their emotions into beautiful songs, and this application hopes to help people relax and listen to songs based on their emotion and mental state at that time.

### Technologies 
- Casscade Classifiers and Webcam input from OpenCV
- A Lightweight Face Recognition and Facial Attribute Analysis Framework Deepface for Emotion Recognition
- Spotify API to fetch songs and playlists base d on emotions
- App deployed using Streamlit Python Library

### How DeepFace Work?
Deepface is a hybrid face recognition package. It currently wraps the state-of-the-art face recognition models: VGG-Face , Google FaceNet, OpenFace, Facebook DeepFace, DeepID, ArcFace and Dlib. The default configuration verifies faces with VGG-Face model. You can set the base model while verification as illustared below.
FaceNet, VGG-Face, ArcFace and Dlib overperforms than OpenFace, DeepFace and DeepID based on experiments. Supportively, FaceNet got 99.65%; ArcFace got 99.40%; Dlib got 99.38%; VGG-Face got 98.78%; OpenFace got 93.80% accuracy scores on LFW data set whereas human beings could have just 97.53%.
### How to Run the application:
Make sure you have all the dependencies mentioned in requirements.txt
- Go to the terminal and run the command `streamlit run app.py`

### Video Demo

### Next Steps
- [ ] Add Movie Recommendation with IMDB
- [ ] Deployment of the application
- [ ] Speech Seniment Analysis

### Team Members
1. Vedanth Baliga
2. Aaditya Goel
3. Prateek Rao 



