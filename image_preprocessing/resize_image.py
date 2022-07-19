
"""
Resize an image in Python OpenCV
To resize an image, OpenCV provides cv2.resize() function
Tested on:
Python3 on Ubuntu 22.03
19/07/2022
Anwar Isied
"""
import cv2

#Resize image or frame, 0..100
def resize_image(img,scale=50):
    width = int(img.shape[1] * scale / 100)
    height = int(img.shape[0] * scale / 100)

    dimensions=(width,height)

    return cv2.resize(img,dimensions,interpolation=cv2.INTER_AREA)

img = cv2.imread('Photos/space.jpg')
rescaled_image=resize_image(img,10)

cv2.imshow('Space',rescaled_image)
k = cv2.waitKey(0) & 0xFF
# wait for ESC key to exit
if k == 27:
   cv2.destroyAllWindows()
