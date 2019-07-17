import cv2
import numpy as np
img = cv2.imread('red_eyes2.jpg')
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
dialation = cv2.dilate(erosion,kernel,iterations = 1)
closing = cv2.morphologyEx(dialation, cv2.MORPH_CLOSE, kernel)
cv2.imshow("shapes",closing)
cv2.waitKey(0)
cv2.destroyAllWindows()
