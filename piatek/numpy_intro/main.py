import numpy as np
import matplotlib.pyplot as plt

SIZE = (5, 5)
IMSHOW_ARGS = {"vmin": 0, "vmax": 255, "cmap": 'gray'}

def ex1():
    array_1d = np.array([1,2,3,4,5], dtype=np.uint8)
    array_2d = np.array([[1,2,3],[4,5,6]])

    print(f'array_1d: {array_1d}, shape: {array_1d.shape}, dtype: {array_1d.dtype}')
    print(f'array_2d: {array_2d}, shape: {array_2d.shape}, dtype: {array_2d.dtype}')

def ex2():
    img = np.zeros(SIZE, dtype=np.uint8)
    img[35, 77] = 255
    plt.imshow(img, cmap='gray')
    plt.show()

def ex3():
    img = np.random.randint(0, 256, size=SIZE)
    plt.imshow(img, cmap='gray')
    plt.show()

def ex4(show = False):
    img_normal = np.random.normal(loc = 127, scale=1, size = SIZE)
    img_uniform =  np.random.randint(0, 256, size=SIZE,dtype=np.uint8)
    if show:
        _,(ax_normal, ax_uniform) = plt.subplots(1, 2)
        ax_normal.imshow(img_normal)
        ax_uniform.imshow(img_uniform)
        plt.show()
    return img_uniform, img_normal

def ex5(img,brightness,contrast):
    img = np.clip(img.copy().astype(np.float32)*contrast + brightness,0,255).astype(np.uint8)
    return img


if __name__ == '__main__':
    img,_ = ex4(False)
    _,axes = plt.subplots(1,2)
    axes[0].imshow(img, **IMSHOW_ARGS)
    axes[1].imshow(ex5(img,100,1.2), **IMSHOW_ARGS)
    plt.show()