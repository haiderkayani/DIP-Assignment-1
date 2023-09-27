import cv2

#Loading the image
image = cv2.imread("peacock.jpg")

#Setting new length and width
new_length = 256
new_width = 256

#Resizing image using in-built functions
image_resize = cv2.resize(image,(new_length, new_width))

#Using in built function for second task
grayscale_image = cv2.cvtColor(image_resize, cv2.COLOR_BGR2GRAY)

#Image display
cv2.imshow("grayscale image", grayscale_image)

cv2.waitKey(0)