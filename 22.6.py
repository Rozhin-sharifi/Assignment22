import cv2
import numpy as np


a=cv2.imread("Assignment22/hw2/Mona_Lisa.jpg")
b=cv2.imread("Assignment22/hw2/f.tif")

a=cv2.cvtColor(a,cv2.COLOR_RGB2GRAY)
b=cv2.cvtColor(b,cv2.COLOR_RGB2GRAY)

b=cv2.flip(b,1)


b=cv2.resize(b,[512,775])
print(b.shape)

img_result=a/b


cv2.imwrite('finalpic.tif',img_result)
cv2.imshow('Picture',img_result)
cv2.waitKey()
