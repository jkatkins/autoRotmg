import pyautogui
import time
import cv2
import numpy as np
import subprocess
import psutil

import vision

#Figure out how to convert from resolution coordinates to pyautogui coordinates
resolution = (2880,1800)
pagSize = pyautogui.size()
resToPag = (pagSize[0]/resolution[0],pagSize[1]/resolution[1])

t = time.time()
target = cv2.imread("Templates/Play.png",cv2.IMREAD_GRAYSCALE)
top = 200
left = 200
width = 1200
height = 600

def clickLocation(location):
    pyautogui.moveTo(location[0], location[1])
    pyautogui.click()

def findStart():
    while True:
        img = vision.capture_window(top,left,width,height)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        img,found,loc = vision.template_match(img,target)
        if found:
            #If the start button was found, press, wait 3 sec, close launcer
            locH = (loc[0] + top*2) * resToPag[0]
            locW = (loc[1] + left*2) * resToPag[1]
            print(pyautogui.position())
            clickLocation((locW,locH))
            time.sleep(3)
            subprocess.call(['osascript', '-e', 'tell application "RotMG Exalt Launcher.app" to quit'])
            break
        #img = cv2.resize(img, (600, 400))
        #cv2.imshow('image',img)
        #print(1/(time.time()-t))
        t = time.time()
    #if cv2.waitKey(1) == ord('q'):
    #    cv2.destroyAllWindows()
    #    break



#open the launcher, the call the find start
p = subprocess.Popen(["/usr/bin/open", "-W", "-n", "-a", "/Applications/RotMG Exalt Launcher.app"])

findStart()
