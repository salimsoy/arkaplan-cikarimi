import cv2
import numpy as np

class BackgroundSubtractionWithLab:
    def __init__(self, img):
        self.img = img
    
    def convert_to_lab_and_gray(self):
        self.lab_img = cv2.cvtColor(self.img, cv2.COLOR_BGR2LAB)
        self.gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
    
    def in_range_lab(self):
        lower = np.array([0, 80, 144], dtype=np.uint8)
        upper = np.array([255, 255, 255], dtype=np.uint8)
        self.mask = cv2.inRange(self.lab_img, lower, upper)
    
    def morphological_closing(self):
        kernel_close = np.ones((9, 9), np.uint8)
        iterasyon = 3
        self.closing = cv2.morphologyEx(self.mask, cv2.MORPH_CLOSE, kernel_close, iterasyon)
    
    def find_contours(self):
        self.contours, _ = cv2.findContours(self.closing, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
        temp = []
        for i in range(len(self.contours)):
            if(i == 2 or i == 3 or i == 8):
                continue
            temp.append(self.contours[i])
    
        self.contours_sift = tuple(temp)

    def draw_contours(self):
        self.contour_mask = np.zeros_like(self.gray)
        cv2.drawContours(self.contour_mask, self.contours_sift, -1, 255, thickness=cv2.FILLED)


if __name__ == '__main__':
    img = cv2.imread('input.jpg')
    proces = BackgroundSubtractionWithLab(img)
    proces.convert_to_lab_and_gray()
    proces.in_range_lab()
    proces.morphological_closing()
    proces.find_contours()
    proces.draw_contours()
    
    cv2.imwrite("output_LAB.jpg", proces.contour_mask)
    
    cv2.imshow("maske", proces.mask)
    cv2.imshow("closing", proces.closing)
    cv2.imshow("sonuc", proces.contour_mask)
    cv2.waitKey(0)
    cv2.destroyAllWindows()