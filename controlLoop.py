import pyautogui
import time
import cv2

import bot
from bot import Bot
import vision

bot = Bot()

time.sleep(2)

top = 200
left = 200
width = 1200
height = 600

#info about the screen
resolution = (2880,1800)
pyagSize = pyautogui.size()
resToPyag = (pyagSize[0]/resolution[0],pyagSize[1]/resolution[1])

tileSize = 62
playerLoc = (1242,686)

#Takes in a location in screen resolution coords
#returns the location in pyautogui coords
def res_to_pyag(loc):
    locH = (loc[0] + top*2) * resToPyag[0]
    locW = (loc[1] + left*2) * resToPyag[1]
    return((locW,locH))

#Returns the coordinates of an image on the screen, or 0 if not found

#Given a location in (x,y) res coords, figure out tile coords
def find_tile_of_location(loc):
    xOffset = loc[0] - playerLoc[0]
    yOffset = playerLoc[1] - loc[1]
    xTiles = xOffset/tileSize
    yTiles = yOffset/tileSize
    return((xTiles,yTiles))


time.sleep(2)

pyautogui.keyDown('w')
while True:
    loc = vision.find_template("Realm")
    if (loc != 0):
        print("found it, now moving towards realm")
        pyautogui.keyUp('w')
        time.sleep(2)
        bot.move_to("Realm")
        time.sleep(2)
        bot.enter_dungeon()






