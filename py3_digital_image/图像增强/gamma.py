import cv2
import numpy as np

img = cv2.imread('./picture/pic1.JPG')

def adjust_gamma(image, gamma=1.0):
    invGamma = 1.0 / gamma
    table = []
    for i in range(256):
        table.append(((i / 255.0) ** invGamma) * 255)
    table = np.array(table).astype("uint8")
    print(table)
    return cv2.LUT(image, table)


# gamma大于0和小于1的时候图像会比原图更暗
# gamma大于1的时候，图像会比原图更亮
img_gamma = adjust_gamma(img, 4.5)
# print(img_gamma)
cv2.imshow("img", img)
cv2.imshow("img_gamma", img_gamma)
cv2.waitKey(0)
cv2.destroyAllWindows()