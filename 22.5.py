import cv2
import numpy as np


images=[]

for i in range(1,15):
    img=cv2.imread(f'Assignment22/hw2/highway/h{i}.jpg')
    img=cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
    images.append(img)


img_result=np.zeros(images[0].shape, dtype='uint8')


for image in images:
    img_result+=image//len(images)



cv2.imwrite('finalpic.tif',  img_result)
cv2.imshow('Picture',  img_result)
cv2.waitKey()