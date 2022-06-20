import cv2

yellow = {"r": 255, "g": 255, "b": 0}

def show_webcam():

    capture = cv2.VideoCapture(0)

    while (True):
        ret, frame = capture.read()
        frame = cv2.flip(frame, 1)
        cv2.imshow('frame',frame)
        #Usar write para GUARDAR el video
        if (cv2.waitKey(1) == ord('s')):
            break

    capture.release()
    cv2.destroyAllWindows()

def process_webcam():
    print("Processing webcam...")

show_webcam()