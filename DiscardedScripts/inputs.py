import pyautogui

def clickLocation(location):
    print(location)
    pyautogui.moveTo(location[0], location[1])
    pyautogui.click()

