import cv2

image = cv2.imread('OpenCV/download.jpeg')
print(image)
grayScaleImage = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
print(grayScaleImage)
cv2.imshow("Gray Image", grayScaleImage)
cv2.waitKey(0)