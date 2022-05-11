import cv2
import numpy as np
from matplotlib import pyplot as plt
# image = cv2.imread("pdsu.jpg")
# imagf = cv2.imread("fanshetu.png")

def zh_ch(string):
    return string.encode('gbk').decode(errors='ignore')

def Pan_zoom_rotate(image):   # 平移  缩放
    cv2.imshow("Original", image)
    M = np.float32([[1, 0, 30], [0, 1, 50]])
    image2 = cv2.warpAffine(image, M, (image.shape[1], image.shape[0]))
    cv2.imshow("Origin", image2)
    image3=cv2.resize(image,(250,300))
    cv2.imshow("SuoFang",image3)

    #  旋转操作
    h,w=image.shape[:2]
    print(h,w)
    center=(h/2,w/2)
    print(center)
    M=cv2.getRotationMatrix2D(center,45,0.75)
    rotated=cv2.warpAffine(image,M,(h,w))
    cv2.imshow("imge_45`",rotated)

    cv2.waitKey(0)
    #cv2.destroyWindow()
    cv2.destroyAllWindows()

def Affine_P(imagf):  #仿射 透视
    cv2.imshow("yuan", imagf)
    rows,cols,ch=imagf.shape
    #指定点
    pts1 = np.float32([[50,50],[200,50],[50,200]])
    pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

    M = cv2.getAffineTransform(pts1,pts2)
    dst=cv2.warpAffine(imagf,M,(cols,rows))
    cv2.imshow("getAffineTransform", dst)

    cv2.waitKey(0)
    #cv2.destroyWindow()
    cv2.destroyAllWindows()


def Perspective(image):   # 透视变换
    width,height =image.shape[:2]
    pts1 = np.float32([[211,36],[684,200],[87,357],[540,540]])#图像四边形顶点坐标
    pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])#新的图片大小
    matrix = cv2.getPerspectiveTransform(pts1,pts2)#计算透视映射矩阵
    img_output = cv2.warpPerspective(image,matrix,(width,height))#透视变换
    cv2.imshow("input", image)
    cv2.imshow("output",img_output)
    cv2.waitKey(0)
    # cv2.destroyWindow()
    cv2.destroyAllWindows()

def SuanShu(image): #算数运算
    # 转换颜色通道
    b, g, r = cv2.split(image)
    image = cv2.merge([r, g, b])

    img_level = cv2.flip(image, 1)  # 水平翻转
    img_vertical = cv2.flip(image, 0)
    img_vertical_level = cv2.flip(image, -1)

    plt.figure(1)
    plt.subplot(221), plt.imshow(image), plt.title("input")
    plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(img_level), plt.title("img_l")
    plt.xticks([]), plt.yticks([])
    plt.subplot(223), plt.imshow(img_vertical), plt.title("img_v")
    plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(img_vertical_level), plt.title("img_v_l")
    plt.xticks([]), plt.yticks([])
    plt.show()

def Fourier(img):      #傅里叶 和 逆DFT

    # 傅里叶
    dft = cv2.dft(np.float32(img), flags=cv2.DFT_COMPLEX_OUTPUT)
    dft_shift = np.fft.fftshift(dft)
    magnitude_spectrum = 20 * np.log(cv2.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1]))


    # 逆DFT
    rows, cols = img.shape
    crow, ccol = int(rows / 2), int(cols / 2)

    # create a mask first, center square is 1, remaining all zeros
    mask = np.zeros((rows, cols, 2), np.uint8)
    mask[crow - 30:crow + 30, ccol - 30:ccol + 30] = 1

    # apply mask and inverse DFT
    fshift = dft_shift * mask
    f_ishift = np.fft.ifftshift(fshift)
    img_back = cv2.idft(f_ishift)
    img_back = cv2.magnitude(img_back[:, :, 0], img_back[:, :, 1])

    plt.subplot(221), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(222), plt.imshow(magnitude_spectrum, cmap='gray')
    plt.title('dft_shift'), plt.xticks([]), plt.yticks([])

    plt.subplot(223), plt.imshow(img, cmap='gray')
    plt.title('Input Image'), plt.xticks([]), plt.yticks([])
    plt.subplot(224), plt.imshow(img_back, cmap='gray')
    plt.title('Magnitude Spectrum'), plt.xticks([]), plt.yticks([])
    plt.show()

if __name__ == '__main__':
    while True:
        # 按下键盘任意键 执行下一步
        # 图片路径
        try:
            Pan_zoom_rotate(cv2.imread("pdsu.jpg"))  # 平移  缩放
            Affine_P(cv2.imread("fanshetu.png"))  # 仿射 透视
            Perspective(cv2.imread("book.png"))  # 透视变换
            SuanShu(cv2.imread("pdsu.jpg"))      #算数运算
            Fourier(cv2.imread("pdsu.jpg", 0))  # 傅里叶  和 逆DFT

        except:
            print("程序错误...")

