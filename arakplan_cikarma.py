import cv2
import numpy as np
from matplotlib import pyplot as plt


class BackgroundSubtraction:
    
    def __init__(self, img):
        self.img = img

    def convert_to_gray_and_hsv(self):
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.hsv = cv2.cvtColor(self.img, cv2.COLOR_BGR2HSV)

    
    def edge_detection(self):
        self.edges = cv2.Canny(self.gray, threshold1=100, threshold2=200)
        
    def morphological_closing(self):
        kernel_close = np.ones((9, 9), np.uint8)
        iterasyon = 3
        self.closing = cv2.morphologyEx(self.edges, cv2.MORPH_CLOSE, kernel_close, iterasyon)

    def find_contours(self):
        contours, _ = cv2.findContours(self.closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        temp = []
        for i in range(len(contours)):
            if(i == 0 or i == 3 or i == 4 or i == 9):
                continue
            temp.append(contours[i])
    
        self.contours_sift = tuple(temp)
        
    def in_range(self):

        lower_red = np.array([19, 39, 0])
        upper_red = np.array([180, 255, 255])
        mask_range = cv2.inRange(self.hsv, lower_red, upper_red)
        self.contours_range, _ = cv2.findContours(mask_range, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    
    def draw_contours(self):
        self.contour_range_mask = np.zeros_like(self.gray)
        cv2.drawContours(self.contour_range_mask, [self.contours_range[0]], -1, 255, thickness=cv2.FILLED)
    
        self.contour_mask = np.zeros_like(self.gray)
        cv2.drawContours(self.contour_mask, self.contours_sift, -1, 255, thickness=cv2.FILLED)

    def bitwise_or(self):
        self.result = cv2.bitwise_or(self.contour_mask, self.contour_range_mask)
        return self.result

if __name__ == '__main__':
    img = cv2.imread('input.jpg')
    process = BackgroundSubtraction(img)
    process.convert_to_gray_and_hsv()
    process.edge_detection()
    process.morphological_closing()
    process.find_contours()
    process.in_range()
    process.draw_contours()
    result = process.bitwise_or()
    
    cv2.imwrite("output.jpg", result)
    
    cv2.imshow("Sonuc", result)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

