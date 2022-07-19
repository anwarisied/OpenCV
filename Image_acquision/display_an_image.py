"""
Display an image in Python OpenCV
Tested on:
Python3 on Ubuntu 22.03
19/07/2022
Anwar Isied
"""

import numpy as np
import cv2
img = cv2.imread('Photos/anwar.jpg')
cv2.imshow('image', img)
k = cv2.waitKey(0) & 0xFF
# wait for ESC key to exit
if k == 27:
   cv2.destroyAllWindows()
#Save image
elif k == ord('s'): 
   cv2.imwrite('Photos/savedImage.jpg',img)
   cv2.destroyAllWindows()