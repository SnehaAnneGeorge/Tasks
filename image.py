import cv2
import numpy as np

image_path = 'thug duck.jpeg'
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

edges = cv2.Canny(original_image, threshold1=100, threshold2=200)

cv2.imshow('Original Image', original_image)
cv2.imshow('Canny Edge Detection', edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
