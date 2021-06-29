import cv2
import numpy as np


images1=[]
images2=[]
images3=[]
images4=[]

for i in range(1,6):
    img1=cv2.imread(f'Assignment22/hw2/black hole/1/{i}.jpg')
    img1=cv2.cvtColor(img1,cv2.COLOR_RGB2GRAY)
    images1.append(img1)


img_result1=np.zeros(images1[0].shape, dtype='uint8')


for image in images1:
    img_result1+=image//len(images1)


for i in range(1,6):
    img2=cv2.imread(f'Assignment22/hw2/black hole/2/{i}.jpg')
    img2=cv2.cvtColor(img2,cv2.COLOR_RGB2GRAY)
    images2.append(img2)


img_result2=np.zeros(images2[0].shape, dtype='uint8')


for image in images2:
    img_result2+=image//len(images2)


for i in range(1,6):
    img3=cv2.imread(f'Assignment22/hw2/black hole/3/{i}.jpg')
    img3=cv2.cvtColor(img3,cv2.COLOR_RGB2GRAY)
    images3.append(img3)


img_result3=np.zeros(images3[0].shape, dtype='uint8')


for image in images3:
    img_result3+=image//len(images3)


for i in range(1,6):
    img4=cv2.imread(f'Assignment22/hw2/black hole/4/{i}.jpg')
    img4=cv2.cvtColor(img4,cv2.COLOR_RGB2GRAY)
    images4.append(img4)


img_result4=np.zeros(images4[0].shape, dtype='uint8')


for image in images4:
    img_result4+=image//len(images4)

img_v1=cv2.vconcat([img_result1,img_result3])
img_v2=cv2.vconcat([img_result2,img_result4])
img_final=cv2.hconcat([img_v1,img_v2])

cv2.imwrite('finalpic.tif', img_final)
cv2.imshow('Picture',img_final)
cv2.waitKey()