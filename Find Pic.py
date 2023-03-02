import cv2
import numpy as np

# Loading the Stegano
Entry_pic = cv2.imread('Stego_Pic.png')
w_S, h_S, c_S = Entry_pic.shape

Num_pixels = 128 * 128 * 8

# Finding the Selected pixels
np.random.seed(35)
Sel_pixels = np.random.choice(w_S * h_S * c_S, size=Num_pixels, replace=False)

# Reshaping the Stegano
Entry_pic = Entry_pic.reshape(1, 1, w_S * h_S * c_S)

# Creating the int nums from pixels
str = ''
Hidden_pic = []
for i in Sel_pixels:
    if len(str) == 8:
        Hidden_pic.append(int(str, 2))
        str = ''
    str = str + '0' if Entry_pic[0, 0, i] % 2 == 0 else str + '1'
Hidden_pic.append(int(str, 2))

# creating a matrix of data found from pixels
Hidden_pic = np.matrix(Hidden_pic, dtype= np.uint8)
Hidden_pic = Hidden_pic.reshape((128, 128))

# Saving and showing the hideden picture
cv2.imwrite('Pic Found.png', Hidden_pic)
cv2.imshow('Hidden Pic', Hidden_pic) # Just for test
cv2.waitKey(0) # Just for