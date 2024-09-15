import cv2
import numpy as np
import os

img_type_flag  = 1
filename = "traffic.jpeg"
img = cv2.imread(filename,img_type_flag)

if img is None:
    print("Error: Could not open or find the image.")
else:
    print(img)
    cv2.imshow("image",img)
cv2.waitKey(0)
cv2.destroyAllWindows()