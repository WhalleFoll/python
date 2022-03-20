from  skimage import  data
from  matplotlib import  pyplot as plt
import numpy as np
image=data.coffee()
plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
print(image.shape)
print(image)
print(type(image))
def picture_Caiy(ratio=1):
    images = np.zeros((int(image.shape[0] / ratio),
                       int(image.shape[1] / ratio), image.shape[2]), dtype='int32')
    for i in range(images.shape[0]):
        for j in range(images.shape[1]):
            for k in range(images.shape[2]):
                delta = image[i * ratio:(i + 1) * ratio, j * ratio:(j + 1) * ratio, k]
                images[i, j, k] = np.mean(delta)
    return images

image2 = picture_Caiy(10)
image3 = picture_Caiy(20)
image4 = picture_Caiy(40)

plt.subplot(2,2,1)
plt.imshow(image)
plt.title('原图')

plt.subplot(2,2,2)
plt.imshow(image2)
plt.title('采样x10')

plt.subplot(2,2,3)
plt.imshow(image3)
plt.title('采样x20')

plt.subplot(2,2,4)
plt.imshow(image4)
plt.title('采样x40')
plt.show()
