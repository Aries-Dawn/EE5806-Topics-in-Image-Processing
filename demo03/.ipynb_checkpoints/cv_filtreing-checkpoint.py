import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while(1):

    # Take each frame
    _, frame = cap.read()

    # Resize the frame by half in both height and width
    # frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5) 


    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('Original',frame)
    cv2.imshow('Result',res)

    # Apply simple average fitler to the tracking frame
    kernel = np.ones((15,15),np.float32)/225
    smoothed = cv2.filter2D(res,-1,kernel)
    cv2.imshow('Average Blurring',smoothed)

    # Apply Gaussian fitler to the tracking frame
    blur = cv2.GaussianBlur(res,(15,15),0)
    cv2.imshow('Gaussian Blurring',blur)
    
    # Apply Meidan fitler to the tracking frame
    median = cv2.medianBlur(res,15)
    cv2.imshow('Median Blur',median)

    # Apply Bilateral fitler to the tracking frame
    bilateral = cv2.bilateralFilter(res,15,75,75)
    cv2.imshow('bilateral Blur',bilateral)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cv2.destroyAllWindows()