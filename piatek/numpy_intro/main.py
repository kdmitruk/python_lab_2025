import numpy as np
import matplotlib.pyplot as plt

def ex1():
    array_1d = np.array([1,2,3,4,5], dtype=np.uint8)
    array_2d = np.array([[1,2,3],[4,5,6]])

    print(f'array_1d: {array_1d}, shape: {array_1d.shape}, dtype: {array_1d.dtype}')
    print(f'array_2d: {array_2d}, shape: {array_2d.shape}, dtype: {array_2d.dtype}')

def ex2():
    img = np.zeros((100, 100), dtype=np.uint8)
    img[35, 77] = 255
    plt.imshow(img, cmap='gray')
    plt.show()

def ex3():
    img = np.random.randint(0, 256, size=(100, 100))
    plt.imshow(img, cmap='gray')
    plt.show()

if __name__ == '__main__':
    ex3()