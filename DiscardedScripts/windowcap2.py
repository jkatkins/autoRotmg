from PIL import ImageGrab
import cv2
import numpy as np
import pyscreenshot as pyss
from mss import mss

def capture_window(windowname):
    #im = ImageGrab.grab(bbox = (300,300,700,700))
    with mss() as sct:
        monitor = {"top":300, "left": 200, "width": 1200, "height": 600}
        # grab the data
        sct_img = sct.grab(monitor)
        #sct_img = sct.grab(sct.monitors[1])
        return np.array(sct_img)
    #im = pyss.grab()
    #return np.array(im,dtype = 'uint8')
    #return im
    
