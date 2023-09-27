import cv2
import numpy as np

image = cv2.imread("coins.png") #loading image

height = image.shape[0]
width = image.shape[1]

# cv2.imshow("coin", image)

# grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #converting original image to grayscale

grayscale_image = np.zeros((height, width), dtype="uint8")

for i in range(height):
    for j in range(width):
        red = int(image[i][j][2])
        green = int(image[i][j][1])
        blue = int(image[i][j][0])
        
        
        intensity = (0.14*red+0.57*green+ 0.29*blue)
        
        
        if intensity<141:
            intensity = 255
            
        else:
            intensity = 0     
            
        grayscale_image[i][j] = intensity  
        

cv2.imshow("gray", grayscale_image)
coin_count, _ = cv2.connectedComponents(grayscale_image)
cv2.imwrite("black.png", grayscale_image)
# threshold, binary_image = cv2.threshold(grayscale_image, 160, 255, cv2.THRESH_BINARY)
# segmented_image = cv2.bitwise_and(image, image, mask=binary_image)

# coin_count, _ = cv2.connectedComponents(binary_image)

coin_count -= 1   # Red

print(coin_count)

# print(f"Number of coins: {coin_count}")
# cv2.imshow("Coin segmentation", segmented_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
