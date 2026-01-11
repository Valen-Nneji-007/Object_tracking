import cv2 as cv
import numpy as np

cap = cv.VideoCapture("traffic.mp4")

_, frame = cap.read()
cv.imshow("Frame", frame)
cv.waitKey(0)