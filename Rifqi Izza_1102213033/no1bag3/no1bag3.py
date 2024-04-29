import cv2
import numpy 

emma_jpg = cv2.imread('emma.jpg')
flipVertical = cv2.flip(emma_jpg, 0)
flipHorizontal = cv2.flip(emma_jpg, 1)
flipHorizontal = cv2.flip(emma_jpg, 2)

cv2.imshow('Original image', emma_jpg)
cv2.imshow('Flipped vertical image', flipVertical)
cv2.imshow('Flipped horizontal image', flipHorizontal)

 
 
cv2.waitKey(0)
cv2.destroyAllWindows()