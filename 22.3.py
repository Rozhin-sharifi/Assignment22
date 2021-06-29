import cv2
import numpy as np

a=cv2.imread("Assignment22/hw2/board-test.bmp")
b=cv2.imread("Assignment22/hw2/board-origin.bmp")

a=cv2.cvtColor(a,cv2.COLOR_RGB2GRAY)
b=cv2.cvtColor(b,cv2.COLOR_RGB2GRAY)

rows, cols=a.shape
img_result=np.zeros((rows,cols), dtype='uint8')


# for i in range(rows):
#     for j in range(cols):
#         if a[i,j]>=b[i,j]:
#             img_result[i,j]=a[i,j]-b[i,j]
#         else:
#             img_result[i,j]=0
# img_result=255-img_result

img_result=cv2.subtract(a,b)


cv2.imwrite('result.tif', img_result)
cv2.imshow('Picture',img_result)
cv2.waitKey()