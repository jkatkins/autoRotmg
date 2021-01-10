import subprocess
import pyautogui
import time
import imageMatch
import cv2

original = cv2.imread("ScreenTest.png")
target = cv2.imread("Templates/Play.png")

resImage = imageMatch.findImg(original,target)


cv2.imshow('image',resImage)

cv2.waitKey(0)
