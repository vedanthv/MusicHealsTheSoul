import cv2

def take_input():
    video = cv2.VideoCapture(0) 

    while True:
        check, frame = video.read()
        cv2.imshow('cap', frame)
        key = cv2.waitKey(1)
        if key == ord('C'):
            break

    showPic = cv2.imwrite("photo.jpg",frame)
    print(showPic)

    video.release()
    cv2.destroyAllWindows()
