import cv2
import numpy as np

img = cv2.imread("Cognitive\Lab6\coin.png")
# img = cv2.cvtColor(src=img, code=cv2.COLOR_BGR2GRAY) 

scale_percent = 60 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
  
# resize image
resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)

# GaussianBlue
guss = cv2.GaussianBlur(resized, (11, 11), 0)
guss = cv2.cvtColor(src=guss, code=cv2.COLOR_BGR2GRAY) 
image_canny = cv2.Canny(resized, 190, 450)
contour, hierarchy = cv2.findContours(image_canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
resized = cv2.drawContours(resized, contour, -1, (255, 0, 0), 2)

print(f"The count of coins is {len(contour)}")

cv2.imshow('Blur', guss)
cv2.imshow("Canny", image_canny)
cv2.imshow("contoured", resized)

# print(hierarchy)
cv2.waitKey()
cv2.destroyAllWindows()