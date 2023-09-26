import cv2
import numpy as np
import  pandas as np

path = "resized.png"
img = cv2.imread(path)                             # loading an image
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)       # convert the img 2 gray scale
num, thrshold2 = cv2.threshold(gray, 128, 255, cv2.THRESH_BINARY)
cv2.imshow("gray ", gray)
cv2.imshow("threshold", thrshold2)
cv2.waitKey(0)
cv2.destroyAllWindows()