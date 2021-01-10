from PIL import ImageGrab
import cv2
import numpy as np
import pyscreenshot as pyss
from mss import mss

top = 0
left = 0
width = 870
height = 630

#Res 1440x900
width = 725
height = 455

#res 1280x800
width = 640
height = 400

#res 800x600
width = 400
height = 300

def capture_window(top,left,width,height):
    #im = ImageGrab.grab(bbox = (300,300,700,700))
    with mss() as sct:
        monitor = {"top":top, "left": left, "width": width, "height": height}
        # grab the data
        sct_img = sct.grab(monitor)
        #sct_img = sct.grab(sct.monitors[1])
        return np.array(sct_img)
    #im = pyss.grab()
    #return np.array(im,dtype = 'uint8')
    #return im


def template_match(original,target,rectangle = False):

    method = cv2.TM_CCOEFF_NORMED
    threshold = 0.9
    result = cv2.matchTemplate(target, original, method)

    # Step 2: Get the size of the template. This is the same size as the match.
    trows,tcols = target.shape[:2]

    #Find all spots where there might be a match
    loc = np.where(result >= threshold)

    if (len(loc[0]) == 0):
        #There is no matches above the threshold, so return the original and false
        return original,False,0
    else:
        #Matches found, (sometimes)draw rectangle and return first location in list
        if (rectangle):
            for pt in zip(*loc[::-1]):
                cv2.rectangle(original, pt, (pt[0] + tcols, pt[1] + trows), (0,0,255), 2)
        return original,True,(loc[0][0]+trows/2,loc[1][0]+tcols/2)

def find_template(name):
    filename = "Templates/" + name + ".png"
    target = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
    img = capture_window(top,left,width,height)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img,found,loc = template_match(img,target,rectangle = True)
    if found:
        #print("found it")
        locH = (loc[0] + top*2) 
        locW = (loc[1] + left*2)
        #Loc is in H,W coords w/o offset, need to add offset and flip
        return(locW,locH)
    #img = cv2.resize(img, (600, 400))
    #cv2.imshow('image',img)
    #cv2. waitKey(0)
    #if cv2.waitKey(1) == ord('q'):
    #    cv2.destroyAllWindows()
    return 0
    
