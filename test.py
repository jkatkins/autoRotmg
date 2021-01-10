import time
import pyautogui




while True:
    time.sleep(0.5)
    print(pyautogui.position()[0]*2,pyautogui.position()[1]*2)

