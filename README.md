# morphologicalTransformations

* Operations based on the image shape

* Normally performed on binary images

## Two Inputs

* Original Image

* Structuring Element / Kernel(decides the nature of the operation)

## Types

    * Erosion
    * Dilation
    * Opening
    * Closing
    * Gradient
    * Tophat
    * Blackhat
    
### Erosion

* Removes thickness of the image(white region decreases)

      erosion = cv2.erode(img,kernel,iterations = 1)

### Dilation

* Opposite to erosion

* Increases white region

* Removes white objects but SHRINKS

      dilation = cv2.dilate(img,kernel,iterations = 1)

### Opening

* Another name of erosion followed by dilation

      opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
      
### Closing

* Reverse of opening

* Useful in closing small holes

      closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
      
### Gradient

* Difference between dilation and erosion

      gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
      
### Top Hat

*  Difference between input image and opening 

       tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, kernel)
      
### Black Hat

* Difference between the closing and input image

       blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, kernel)
