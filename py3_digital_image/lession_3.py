# 学校某个景色照片为处理图像，利用OpenCV、python工具和所学内容，
# 进行图像算术变换、逻辑变换、几何变换和傅里叶变换和反变换编程实现。上传变换结果和程序源码！
import  cv2
from matplotlib import pyplot as plt

image = cv2.imread("pdsu.jpg")

#转换颜色通道
b,g,r=cv2.split(image)
image=cv2.merge([r,g,b])

img_level=cv2.flip(image,1)    #水平翻转
img_vertical=cv2.flip(image,0)
img_vertical_level=cv2.flip(image,-1)

plt.figure(1)
plt.subplot(221),plt.imshow(image),plt.title("input")
plt.xticks([]),plt.yticks([])
plt.subplot(222),plt.imshow(img_level),plt.title("img_l")
plt.xticks([]),plt.yticks([])
plt.subplot(223),plt.imshow(img_vertical),plt.title("img_v")
plt.xticks([]),plt.yticks([])
plt.subplot(224),plt.imshow(img_vertical_level),plt.title("img_v_l")
plt.xticks([]),plt.yticks([])

plt.show()


