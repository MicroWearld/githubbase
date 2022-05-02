from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
img = np.array(Image.open('123.jpg').convrt('L'))
row,cols=imag.shape
for i in range(rows):
    for j in range(cols):
        if(img[i,j]>128):
            img[i,j]= 1
        else:
            img[i,j]=0
plt.figure("lena")
plt.imshow(img,camp='gray')
plt.axis('off')
plt.show()
