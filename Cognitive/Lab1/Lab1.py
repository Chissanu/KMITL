# -*- coding: utf-8 -*-
"""
Created on Wed Jan 18 13:37:30 2023

@author: chiss
"""

import cv2
import numpy as np
img = cv2.imread("imgs/sunset_image.png")
overlay = img.copy()

# img[0:290, 386:772] = (255,0,0)

#772 x 580
  
# A filled rectangle
cv2.rectangle(overlay, (386,0), (772, 290), (95, 0, 0), -1)
cv2.rectangle(overlay, (0,290), (386, 580), (0, 95, 0), -1)
cv2.rectangle(overlay, (386,290), (772, 580), (0, 0, 95), -1)
alpha = 0.6

final = cv2.addWeighted(overlay, alpha, img, 1 - alpha, 0)
  
cv2.imshow("Chalita", final)
cv2.waitKey(0)

# cv2.imshow('image', img)

cv2.waitKey(0)