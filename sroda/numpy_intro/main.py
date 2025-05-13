import math

import numpy as np
import matplotlib.pyplot as plt
import matplotlib

maxes = {"vmin": 0, "vmax": 255}

def ex1():
    array2 = np.array([1,2,3,4],dtype=np.uint8)
    array = np.array([[1,2,3,4,5],[1,2,3,4,5]])
    print(array,array.shape,array.dtype)

def ex2():
    img = np.zeros((100, 100), dtype=np.uint8)
    img[50, 50] = 255
    plt.imshow(img)
    plt.show()

def ex3():
    img = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
    plt.imshow(img, cmap="gray")
    plt.show()

def ex4():
    img1 = np.random.normal(loc=0,scale=50,size=(100,100))
    #fig,(ax1,ax2) = plt.subplots(1,2)
    img = np.random.randint(0, 256, (512, 512), dtype=np.uint8)
    #ax1.imshow(img1)
    #ax2.imshow(img)
    #plt.imshow(img, cmap="gray")
    #plt.show()
    return (img,img1)

def ex5(img, bri, con):
    fig,(ax1,ax2) = plt.subplots(1,2)
    img2 = np.clip(img.astype(np.float32)*con + bri, 0, 255).astype(np.uint8)

    ax1.imshow(img, **maxes)
    ax2.imshow(img2, **maxes)
    #matplotlib.colors.Normalize(vmin=0, vmax=255)
    plt.show()

def ex6(img, x, y, w, h):
    result = img.copy()
    result[y:y+h, x:x+w] = 255
    plt.imshow(result)
    plt.show()
    return result

def ex8(img):
    img = img.copy()
    img = 255 - img
    plt.imshow(img)
    plt.show()

def ex9():
    line = np.linspace(0,255,100,dtype=np.uint8)
    # print(line)
    img = np.tile(line,(100,1))
    plt.imshow(img)
    plt.show()
    return img

def ex7(img):
    img = img.copy()
    threshold = 150
    img[img > threshold] = 255
    img[img < 50] = 0
    plt.imshow(img)
    plt.show()
    return img

def ex10(freq):
    x = np.linspace(0,2*np.pi*freq,100)
    y = np.sin(x)
    plt.figure()
    plt.plot(x,y)
    plt.show()

def ex11(freq):
    x = np.linspace(0,2*np.pi*freq,100)
    xx,_ = np.meshgrid(x,x)
    img = np.sin(xx)
    plt.imshow(img)
    plt.show()

def ex12(freq):
    x = np.linspace(0,2*np.pi*freq,100)
    _,xx = np.meshgrid(x,x)
    img = np.sin(xx)
    plt.imshow(img)
    plt.show()

def ex13(freq):
    x = np.linspace(0,2*np.pi*freq,512)
    xx,yy = np.meshgrid(x,x)

    img = np.sin(xx) + np.sin(yy)
    # plt.imshow(img, cmap="gray")
    # plt.show()
    return img

def ex14(img, mask):
    img = img.astype(np.float32) * mask.astype(np.float32)
    plt.imshow(img)
    plt.show()


if __name__ == '__main__':
    #ex1()
    # ex2()
    (img1, img2) = ex4()
    #ex5(img1, 0, 1.2)

    # img3 = ex6(img1,60,50,20,45)

    # ex5(img1,-120,1.2)
    # ex8(img3)
    #img = ex9()
    #ex7(img)
    #ex10(5)
    #ex11(5)
    #ex12(5)
    #ex13(32)
    ex14(img1, ex13(5))