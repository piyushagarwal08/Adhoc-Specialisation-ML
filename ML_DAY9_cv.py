#!/usr/bin/python3
import sys
import cv2


### version
print(cv2.__version__)

# image name as first argument
data = sys.argv[1]

## image read
img = cv2.imread(data,1) 		#loading data of image
print(img)

print(img.shape)
#height width color

# applying mathematical functions to change the color values by working on ndarray
# complete mathematical patterns
cv2.imshow('image1',img)
cv2.imshow('image2',img//2)
cv2.imshow('image3',img-255)
cv2.imshow('image4',img+10)
cv2.imshow('image5',img+255)
cv2.imshow('image5',img+255)

# Saving image
cv2.imwrite('image-name.jpeg',img[0:400,0:300]/10)


cv2.waitKey(0)
