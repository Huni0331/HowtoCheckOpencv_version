import cv2
# import numpy as np


print('Opencv version {0}'.format(cv2.__version__))

img = cv2.imread('/Users/jeongbyeonghun/Downloads/cat.jpg')
cv2.imshow('window', img)
cv2.waitKey()