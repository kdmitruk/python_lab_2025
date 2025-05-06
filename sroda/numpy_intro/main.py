import numpy as np


def ex1():
    array2 = np.array([1,2,3,4],dtype=np.uint8)
    array = np.array([[1,2,3,4,5],[1,2,3,4,5]])
    print(array,array.shape,array.dtype)

if __name__ == '__main__':
    ex1()