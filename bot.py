import pyautogui
import time
import vision


TILESIZE = 62 #res1640

TILESIZE = 50 #res1440

TILESIZE = 48#res1280

TILESIZE = 50#res1280

class Zones:
    NEXUS = 0
    REALM = 1

class Keybinds:
    NEXUS = 'r'
    INTERACT = 'c'
    UP = 'w'
    DOWN = 's'
    LEFT = 'a'
    RIGHT = 'd'
    NONE = '9'

class Bot: 

    # properties
    state = None
    Health = 0
    Mana = 0
    Zone = None
    statusEffects = []
    speed = 10
    location = (0,0)
   
    # init method or constructor  
    def __init__(self): 
        self.state = None
        self.Zone = Zones.NEXUS
        self.speed = 10
        #self.location = (660,594)#res 1640
        #self.location = (570,524)#Res 1440x900
        #self.location = (504,466)#Res 1280x800
        self.location = (302,372)#Res min
   
    # Sample Method  
    def enter_dungeon(self): 
        pyautogui.press(Keybinds.INTERACT)


    def move_to(self,templateName):
        loc = vision.find_template(templateName)
        if (loc == 0):
            print("vision not found")
            return
        x = loc[0]
        y = loc[1]
        keyX = Keybinds.RIGHT
        keyY = Keybinds.DOWN
        if (x < self.location[0]):
            keyX = Keybinds.LEFT
        if (y < self.location[1]):
            keyY = Keybinds.UP
        pyautogui.keyDown(keyX)
        pyautogui.keyDown(keyY)
        xDone = False
        yDone = False
        lastLoc = (0,0)
        t = time.time()
        while True:
            print (1/(time.time()-t))
            t = time.time()
            loc = vision.find_template(templateName)     
           # print(loc)
            if (loc == 0):
                print("vision lost")
                pyautogui.keyUp(keyX)
                pyautogui.keyUp(keyY)
                break
            x = loc[0]
            y = loc[1]
            if (not xDone and x <= self.location[0]+TILESIZE/2 and keyX == Keybinds.RIGHT):
               # print("xmove stopped")
                pyautogui.keyUp(keyX)
                xDone = True
            if (not xDone and x >= self.location[0]-TILESIZE/2 and keyX == Keybinds.LEFT):
                #print("xmove stopped")
                pyautogui.keyUp(keyX)
                xDone = True
            if (not yDone and y <= self.location[1]+TILESIZE/2 and keyY == Keybinds.DOWN):
                #print("ymove stopped")
                pyautogui.keyUp(keyY)
                yDone = True
            if (not yDone and y >= self.location[1]-TILESIZE/2 and keyY == Keybinds.UP):
                #print("ymove stopped")
                pyautogui.keyUp(keyY)
                yDone = True
            if (xDone and yDone):
                break
            lastLoc = loc
    
    def move_to_old(self,tile):
        x = tile[0]
        y = tile[1]
        keyX = Keybinds.RIGHT
        keyY = Keybinds.UP
        if (x < 0):
            keyX = Keybinds.LEFT
        if (y < 0):
            keyY = Keybinds.DOWN
        tps = 4 + 5.6 * (self.speed / 75)
        timeToX = abs(x)/tps
        timeToY = abs(y)/tps
        if (timeToY < 0.02 and timeToY > -0.02):
            keyY = Keybinds.NONE
        if (timeToY < 0.02 and timeToY > -0.02):
            keyX = Keybinds.NONE
        if (timeToX > timeToY):
            timeToX = timeToX - timeToY
            pyautogui.keyDown(keyX)
            pyautogui.keyDown(keyY)
            time.sleep(timeToY)
            pyautogui.keyUp(keyY)
            time.sleep(timeToX)
            pyautogui.keyUp(keyX)
        else:
            timeToY = timeToY - timeToX
            pyautogui.keyDown(keyX)
            pyautogui.keyDown(keyY)
            time.sleep(timeToX)
            pyautogui.keyUp(keyX)
            time.sleep(timeToY)
            pyautogui.keyUp(keyY)



            
