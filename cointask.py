import cv2
import numpy as np

image = cv2.imread("coins.png") #loading image

height = image.shape[0] #getting height and width of image
width = image.shape[1]

binary_image = np.zeros((height, width), dtype="uint8") #creating empty binary image with same dimensions as original image

for i in range(height): #iterating over each pixel in image
    for j in range(width):
        red = int(image[i][j][2]) #extracting rgb value of current pixel in loop
        green = int(image[i][j][1])
        blue = int(image[i][j][0])
        
        intensity = (0.14*red+0.57*green+ 0.29*blue) #converting rgb to binary using weighted sum
        
        if intensity<141: #thresholding intensity value to help create binary image
            intensity = 255   
        else:
            intensity = 0     
            
        binary_image[i][j] = intensity #assigning intensity to corresponding pixel in binary image
        

cv2.imshow("Coin segmentation", binary_image) #displaying image
coin_count, _ = cv2.connectedComponents(binary_image) #using connected components to count distinct coins in binary image
coin_count -= 1 #subtracting 1 from the total count to exclude background

print(f"Number of coins: {coin_count}")

cv2.waitKey(0)
cv2.destroyAllWindows()
