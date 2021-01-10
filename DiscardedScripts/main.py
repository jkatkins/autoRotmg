#https://pyautogui.readthedocs.io/en/latest/

import subprocess
import pyautogui
import time

subprocess.Popen(["/usr/bin/open", "-W", "-n", "-a", "/Applications/RotMG Exalt Launcher.app"])

screenWidtscreenHeight = pyautogui.size() # Get the size of the primary monitor.

currentMouseX, currentMouseY = pyautogui.position() # Get the XY position of themouse.

playX = 1000
playY = 625

#while True:
#    print(pyautogui.position())

time.sleep(7)

pyautogui.click(playX,playY) #TODO remove hardcoding for this, use CV to find play button
