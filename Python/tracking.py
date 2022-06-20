# import the necessary packages
from collections import deque
from imutils.video import VideoStream
from pynput.keyboard import Key, Controller
import numpy as np
import argparse
import cv2
import imutils
import time

# ! Digamosle a la maquina que existe un objeto amarillo
# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser() 
ap.add_argument("-v", "--video",
	help="path to the (optional) video file")
args = vars(ap.parse_args())
# valores permitidos para nuestro objeto en HSV
yellowLower = (12, 120, 110)
yellowUpper = (37, 255, 255)
# if a video path was not supplied, grab the reference
# to the webcam
if not args.get("video", False):
	vs = VideoStream(src=0).start()
# otherwise, grab a reference to the video file
else:
	vs = cv2.VideoCapture(args["video"])
# allow the camera or video file to warm up
time.sleep(2.0)
# keep looping

while True:
	# grab the current frame
	frame = vs.read()
	# handle the frame from VideoCapture or VideoStream

	frame = frame[1] if args.get("video", False) else frame
	# if we are viewing a video and we did not grab a frame,
	# then we have reached the end of the video

	if frame is None:
		break

	# resize the frame, blur it, and convert it to the HSV
	# color space
	frame = imutils.resize(frame, width=600)
	blurred = cv2.GaussianBlur(frame, (11, 11), 0)
	hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)
	keyboard = Controller()

	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
	mask = cv2.inRange(hsv, yellowLower, yellowUpper)
	mask = cv2.erode(mask, None, iterations=2)
	mask = cv2.dilate(mask, None, iterations=2)

    # find contours in the mask and initialize the current
	# (x, y) center of the banana
	cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)
	cnts = imutils.grab_contours(cnts)
	center = None
	dale = False

	# only proceed if at least one contour was found
	if len(cnts) > 0:
		# find the largest contour in the mask, then use
		# it to compute the minimum enclosing circle and
		# centroid
		c = max(cnts, key=cv2.contourArea)

		# Debemos determinar un area lo suficientemente grande
		if (cv2.contourArea(c) > 1500):

			if (cv2.contourArea(c) > 8000):
				
				dale = True

			(boundRect) = cv2.boundingRect(c)

			# draw a square around
			M = cv2.moments(c)
			center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
			# draw a rectangle around the object
			color = (0, 255, 0)
			cv2.rectangle(frame, (int(boundRect[0]), int(boundRect[1])),
			(int(boundRect[0]+boundRect[2]), int(boundRect[1]+boundRect[3])), color, 2)
			cv2.circle(frame, center, 5, (0, 0, 255), -1)

	# show the frame to our screen
	frame = cv2.flip(frame, 1)
	cv2.imshow("Frame", frame)
	key = cv2.waitKey(1) & 0xFF
	# if the 'q' key is pressed, stop the loop
	if key == ord("q"):
		break

	# if the banana moves up, press the letter 'j'

	# print(center)
	brincar = 'j'

	if center is not None:
		
		if center[1] <= 300:

			keyboard.press(brincar)

		else:

			keyboard.release(brincar)

	acelerar = 'u'

	if (dale):

		keyboard.press(acelerar)

	else:
		
		keyboard.release(acelerar)

	derecha = 'd'
	izquierda = 'a'

	if center is not None:

		if center[0] <= 230:

			keyboard.press(derecha)
			keyboard.release(izquierda)

		elif center[0] >= 370:

			keyboard.press(izquierda)
			keyboard.release(derecha)

		else:

			keyboard.release(derecha)
			keyboard.release(izquierda)
	
	else:
		
		keyboard.release(derecha)
		keyboard.release(izquierda)


# if we are not using a video file, stop the camera video stream

if not args.get("video", False):
	vs.stop()
# otherwise, release the camera
else:
	vs.release()
# close all windows
cv2.destroyAllWindows()