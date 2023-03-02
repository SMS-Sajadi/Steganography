import cv2
import numpy as np

# Loading the target pic and resizeing
Entry_pic = cv2.imread('Target_pic.jpg')
Entry_pic = cv2.resize(Entry_pic, (128, 128))

Num_pixels = 128 * 128 * 8

# Grayscaling the pic and reshaping
Gray_Entry = cv2.cvtColor(Entry_pic, cv2.COLOR_BGR2GRAY)
Gray_Entry = Gray_Entry.reshape(1, Num_pixels // 8)

# Saving the data in binary
bit_list = []
for i in range(128 * 128):
    str = f'{Gray_Entry[0, i]:08b}'
    for j in str:   
        bit_list.append(j)

# Loading the base pic and reshaping it
Stegano = cv2.imread('Base_pic.jpg')
w_S, h_S, c_S = Stegano.shape
Stegano = Stegano.reshape(1, 1, w_S * h_S * c_S)

# Select random pixels to hide data in
np.random.seed(35)
Sel_pixels = np.random.choice(w_S * h_S * c_S, size= Num_pixels, replace= False)

# Hide data in selected pixels
for i, j in zip(bit_list, Sel_pixels):
    if (Stegano[0, 0, j] % 2 == 0 and i == '0') or (Stegano[0, 0, j] % 2 != 0 and i == '1'):
        continue
    if (Stegano[0, 0, j] % 2 == 0 and i == '1') or (Stegano[0, 0, j] % 2 != 0 and i == '0') :
       Stegano[0, 0, j] = Stegano[0, 0, j] - 1 if Stegano[0, 0, j] == 255 else Stegano[0, 0, j] + 1

Stegano = Stegano.reshape(w_S, h_S, c_S)
cv2.imwrite('Stego_Pic.png', Stegano)

cv2.imshow('Stegano', Stegano) # Just for test
cv2.waitKey(0) # Just for test