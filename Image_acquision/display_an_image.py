"""
Display an image in Python OpenCV
Tested on:
Python3 on Ubuntu 22.03
19/07/2022
Anwar Isied
"""

import numpy as np
import cv2 as cv
img = cv.imread('Photos/anwar.jpg')
cv.imshow('image', img)
k = cv.waitKey(0) & 0xFF
# wait for ESC key to exit
if k == 27:
   cv.destroyAllWindows()
#Save image
elif k == ord('s'): 
   cv.imwrite('Photos/savedImage.jpg',img)
   cv.destroyAllWindows()