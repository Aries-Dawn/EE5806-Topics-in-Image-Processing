import cv2 
import numpy as np 
from matplotlib import pyplot as plt 

img = cv2.imread('hongkong.jpg', cv2.IMREAD_GRAYSCALE) 
cv2.imshow('Hong Kong', img)


hist = cv2.calcHist([img],[0],None,[256],[0,256]) 
# plt.hist(img.ravel(),256,[0,256]) 
# plt.title('Histogram for gray scale picture') 
# plt.show() 

while True: 
	k = cv2.waitKey(0) & 0xFF 
	if k == 27: break 	# ESC key to exit 
cv2.destroyAllWindows()

##################################

# import matplotlib.pyplot as plt
# import matplotlib.image as mpimg
# import numpy as np
# import cv2

# # Read and Display the image using plt and mpimg
# img=mpimg.imread('hongkong.jpg')
# imgplot = plt.imshow(img)

# # Compute the histogram using cv2.calcHist()
# hist = cv2.calcHist([img],[0],None,[256],[0,256])

# # Display the histogram using plt.hist() 
# # plt.hist(img.ravel(),256,[0,256]) 
# # plt.title('Histogram for gray scale picture') 
# plt.show() 




