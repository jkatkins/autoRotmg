from Quartz import CGWindowListCopyWindowInfo, kCGNullWindowID, kCGWindowListOptionAll
import matplotlib.pyplot as plt
from PIL import Image
import os
import cv2
from uuid import uuid4

gen_filename = lambda : str(uuid4())[-10:] + '.jpg'

def capture_window(window_name):
    window_list = CGWindowListCopyWindowInfo(kCGWindowListOptionAll, kCGNullWindowID)
    for window in window_list:
        try:
            if window_name.lower() in window['kCGWindowName'].lower():
                filename = gen_filename()
                os.system('screencapture -l %s %s' %(window['kCGWindowNumber'], filename))
                #img = Image.open(filename)
                #plt.imshow(img)
                #plt.xticks([])
                #plt.yticks([])
                img = cv2.imread(filename)
                #img = cv2.resize(img, (960, 540))
                os.remove(filename)
                return img
                #cv2.imshow('image',img)
                #cv2.waitKey(0)
        except:
            pass
    return None
    #else:
        #print("error")
       # raise Exception('Window %s not found.'%window_name)

