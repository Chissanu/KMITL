import cv2
import numpy as np

img = cv2.imread("Lab5\\fingerprint.png", cv2.IMREAD_GRAYSCALE)

width = img.shape[1]
height = img.shape[0]

def threshhold(val):
    for i in range(height):
        for j in range(width):
            if img[i][j] > val:
                img[i][j] = 255
            else:
                img[i][j] = 0

threshhold(127)
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()

"""
Explanation:
Left is to zero because if the pixel value is higher than threshold it would be set to white
and the coin is black so it means that the pixel value is close to white so it will get convert
to black while the invert will convert the white to black instead and the coin will get inverted as well.
"""