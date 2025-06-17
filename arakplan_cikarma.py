import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('input.jpg')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, threshold1=100, threshold2=200)

kernel_close = np.ones((9, 9), np.uint8)
iterasyon = 3

closing = cv2.morphologyEx(edges, cv2.MORPH_CLOSE, kernel_close, iterasyon)

contours, _ = cv2.findContours(closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

temp = []
for i in range(len(contours)):
    if(i == 0 or i == 3 or i == 4 or i == 9):
        continue
    temp.append(contours[i])
    
contours_sift = tuple(temp)
    
result = np.zeros_like(gray)

cv2.drawContours(result, contours_sift, -1, 255, thickness=cv2.FILLED)


cv2.imwrite("output.jpg", result)

cv2.imshow("Sonuc", result)
cv2.imshow("Orijinal", img)
cv2.imshow("gri", gray)
cv2.imshow("canny", edges)
cv2.imshow("close", closing)
cv2.waitKey(0)
cv2.destroyAllWindows()