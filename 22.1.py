import cv2
import numpy as np

a=cv2.imread("Assignment22/hw2/a.tif")
b=cv2.imread("Assignment22/hw2/b.tif")

a=cv2.cvtColor(a,cv2.COLOR_RGB2GRAY)
b=cv2.cvtColor(b,cv2.COLOR_RGB2GRAY)

rows, cols=a.shape

img_result=cv2.multiply(a-255,b)


cv2.imwrite('result.tif', img_result)
cv2.imshow('Picture',img_result)
cv2.waitKey()