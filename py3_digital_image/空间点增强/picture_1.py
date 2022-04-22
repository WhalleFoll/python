# 编程实现中值降噪、直方图统计、直方图均衡化和局部自适应直方图均衡化，并输出相关结果

# # 直方图统计
# import numpy as np
# import  cv2 as cv
# from matplotlib import  pyplot as plt
#
# img = cv.imread('./picture/lena.jpg',0)
# histr = cv.calcHist([img],[0],None,[256],[0,256])
# plt.subplot(121),plt.imshow(img,'gray')
# plt.title('originall'),plt.xticks([]),plt.yticks([])
# plt.subplot(122)
# plt.title('hist')
# plt.plot(histr,color='gray')
# plt.xlim([0,256])
# plt.show()

# 直方图均衡化
# 案例
# import  cv2
# from matplotlib import  pyplot as plt
#
# img = cv2.imread('./picture/test.jpg',0)
# hist = cv2.calcHist([img],[0],None,[256],[0,256])
# # hist是一个256*1的数组，每一个值代表了与此灰度值对应的像素点的
#
# plt.hist(img.ravel(),256);
# plt.show()



# # 中值降噪
# import  cv2
# import numpy as np
#
# img = cv2.imread('./picture/test.jpg')
# cv2.imshow('src', img)
# def addSaltNoise(img,snr):
#     # 指定信噪比
#     SNR = snr
#     # 获取总共像素个数
#     size = img.size
#     # 因为信噪比是 SNR ，所以噪声占据百分之10，所以需要对这百分之10加噪声
#     noiseSize = int(size * (1 - SNR))
#     # 对这些点加噪声
#     for k in range(0, noiseSize):
#         # 随机获取 某个点
#         xi = int(np.random.uniform(0, img.shape[1]))
#         xj = int(np.random.uniform(0, img.shape[0]))
#         # 增加噪声
#         if img.ndim == 2:
#             img[xj, xi] = 255
#         elif img.ndim == 3:
#             img[xj, xi] = 0
#     return img
#
# img2 = addSaltNoise(img,0.99)
#
# # 进行中值滤波
# dstimg = cv2.medianBlur(img2, 3)
#
# cv2.imshow('zaoshen', img2)
# cv2.imshow('output', dstimg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



# # 直方图均衡化 局部自适应直方图均衡化
# import cv2 as cv
#
# src = cv.imread("./picture/tsukuba.jpg")
#
#
# # 1. 全局直方图均衡化
# def globalEqualHist(image):
#     # 如果想要对图片做均衡化，必须将图片转换为灰度图像
#     gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     dst = cv.equalizeHist(gray)  # 在说明文档中有相关的注释与例子
#     # equalizeHist(src, dst=None)函数只能处理单通道的数据,src为输入图像对象矩阵，必须为单通道的uint8类型的矩阵数据
#     # dst: 输出图像矩阵(src的shape一样)
#     cv.imshow("Global equalizeHist", dst)
#     # print(len(image.shape))  # 彩色图像的shape长度为3
#     # print(len(gray.shape))  # 灰度图像的shape长度为2
#     # print(gray.shape)   # 灰度图像只有高、宽
#
#
# def localEqualHist(image):
#     gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#     clahe = cv.createCLAHE(clipLimit=5, tileGridSize=(7,7))
#     dst = clahe.apply(gray)
#     cv.imshow("clahe image", dst)
#
# globalEqualHist(src)
# # localEqualHist(src)
# cv.imshow("original image", src)
# cv.waitKey(0)
# cv.destroyAllWindows()





# 直方图比较
# def create_rgb_hist(image):
#     h, w, c = image.shape
#     rgbHist = np.zeros([16*16*16, 1], np.float32)
#     bsize = 256/16
#     # enumerate() 函数可以永健一个可遍历的数据对象（如列表、元组或字符串）组合为一个索引序列，同时列出数据以及对应的下标，一般用在for循环中。
#     # range()函数用于创建一个整数列表
#     for row in range(h):
#         for col in range(w):
#             b = image[row, col, 0]
#             g = image[row, col, 1]
#             r = image[row, col, 2]
#             index = np.int((b/bsize)/16*16 + (g/bsize)*16 + (r/bsize))
#             rgbHist[np.int(index), 0] = rgbHist[np.int(index), 0] + 1
#
#     return rgbHist
#
#
# def hist_compare(image1, image2):
#     hist1 = create_rgb_hist(image1)
#     hist2 = create_rgb_hist(image2)
#     match1 = cv.compareHist(hist1, hist2, cv.HISTCMP_BHATTACHARYYA)
#     match2 = cv.compareHist(hist1, hist2, cv.HISTCMP_CORREL)
#     match3 = cv.compareHist(hist1, hist2, cv.HISTCMP_CHISQR)
#     print("巴氏距离: %s, 相关性: %s, 卡方: %s"%(match1, match2, match3))
#     cv.imshow("image1", image1)
#     cv.imshow("image2", image2)
#
#
# image1 = cv.imread("./images/raindropGirl.jpg")
# image2 = cv.imread("./images/raindropGirl01.jpg")
#
# hist_compare(image1, image2)
# cv.waitKey(0)
# cv.destroyAllWindows()



# 下面我们来使用双边滤波 cv2.bilateralFilter 来实现图像的磨皮美白方法
import cv2
img = cv2.imread('./picture/man.png', 1)
cv2.imshow('img', img)
dat = cv2.bilateralFilter(img, 30,35,35)
cv2.imshow('dat',dat)
cv2.waitKey(0)

