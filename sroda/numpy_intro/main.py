import numpy as np
import matplotlib.pyplot as plt

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
    fig,(ax1,ax2) = plt.subplots(1,2)
    img = np.random.randint(0, 256, (100, 100), dtype=np.uint8)
    ax1.imshow(img1)
    ax2.imshow(img)
    #plt.imshow(img, cmap="gray")
    plt.show()
    return (img,img1)

if __name__ == '__main__':
    ex1()
    # ex2()
    ex4()