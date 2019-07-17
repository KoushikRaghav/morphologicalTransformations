import cv2
import numpy as np
image = cv2.imread('shapes_and_colors.png')
kernel = np.ones((5,5),np.uint8)
dialation = cv2.dilate(image,kernel,iterations = 1)
cv2.imshow("shapes",dialation)
cv2.waitKey(0)
cv2.destroyAllWindows()
