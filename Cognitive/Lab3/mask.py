import cv2
import numpy as np

img = cv2.imread("Lab3\cat03.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
mask = np.zeros(gray.shape[:2], dtype = "uint8")

circle = np.zeros((300, 300, 3), dtype = "uint8")
r = 150
for i in range(6):
    cv2.circle(img=circle, center = (150,150), radius = r, color =(220,220,220), thickness=1)
    r -= 25

cv2.imshow('Circle', circle)

cv2.imshow('Grey Image', gray)

cv2.circle(img=mask, center = (gray.shape[0] // 2,gray.shape[1] // 2), radius = 150, color =(220), thickness=-1)
masked = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Masked image', masked)
cv2.waitKey(0)