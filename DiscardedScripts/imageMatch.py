import cv2
import numpy as np

method = cv2.TM_CCOEFF_NORMED
threshold = 0.9


def findImg(original,target,rectangle = False):

    
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
            return original,True,(loc[0][0],loc[1][0])
   
