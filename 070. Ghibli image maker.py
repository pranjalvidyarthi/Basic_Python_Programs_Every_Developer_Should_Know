# Ghibli image converter

import cv2
import numpy as np

def cartoonize_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (800, 600))

    # Convert to grayscale 
    gray = cv2.cvtColor(img,  cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray , 5)

    # Detect edges
    edges = cv2.adaptiveThreshold(gray ,  255, cv2.ADAPTIVE_THRESH_MEAN_C,  cv2.THRESH_BINARY , 9, 10)

    # applying bilateral filter to smooth colors 
    color  = cv2.bilateralFilter(img,  9  , 250 ,  250)

    # Combine edges and color
    cartoon = cv2.bitwise_and(color , color , mask=edges)
    cv2.imshow("Cartoonized Image" , cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
cartoonize_image("pranjalvidyarthi.jpg")