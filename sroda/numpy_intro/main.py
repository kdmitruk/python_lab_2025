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

if __name__ == '__main__':
    ex1()
    # ex2()
    ex3()