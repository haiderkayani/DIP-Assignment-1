import cv2

image = cv2.imread("peacock.jpg") #loading image

new_height = 256 #setting new pixel length for width and height
new_width = 256

image_resize = cv2.resize(image, (new_height, new_width)) #using in-built function to resize original image and storing in new variable

cv2.imshow("resized image", image_resize) #displaying image
cv2.waitKey(0)
cv2.destroyAllWindows()