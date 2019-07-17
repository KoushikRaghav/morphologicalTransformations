import cv2
import numpy as np
image = cv2.imread('red_eyes2.jpg')
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(image,kernel,iterations = 1)
dialation = cv2.dilate(erosion,kernel,iterations = 1)
opening = cv2.morphologyEx(dialation, cv2.MORPH_OPEN, kernel)
cv2.imshow("shapes",opening)
cv2.waitKey(0)
cv2.destroyAllWindows()

