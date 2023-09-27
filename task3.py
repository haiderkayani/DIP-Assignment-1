import cv2

image = cv2.imread("peacock.jpg")

new_length = 256
new_width = 256

image_resize = cv2.resize(image,(new_length, new_width))

grayscale_image = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)


#Using built-in function for binary thresholding to convert to binary image
threshold = 128
_, binary_image = cv2.threshold(grayscale_image, threshold, 255, cv2.THRESH_BINARY)

#Displaying the image
cv2.imshow("binary image", binary_image )
cv2.waitKey(0)