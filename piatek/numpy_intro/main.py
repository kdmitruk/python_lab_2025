import math

import numpy as np
import matplotlib.pyplot as plt

SIZE = (100, 100)
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

def ex7(img):
    img = img.copy()
    y=20
    x=30
    h=40
    w=50
    img[y:y+h, x:x+w] = 255
    return img

def ex8(img):
    img = img.copy()
    img = 255 - img
    return img

def ex9():
    line = np.linspace(0, 255, SIZE[0], dtype=np.uint8)
    img = np.tile(line, (SIZE[1], 1))
    return img

def ex10():
    freq = 5
    x = np.linspace(0, math.pi * 2 * freq, 100)
    y = np.sin(x)
    plt.figure()
    plt.plot(x, y)
    plt.show()

def ex11():
    freq = 5
    x = np.linspace(0, np.pi * 2 * freq, 100)
    xx, yy = np.meshgrid(x, x)
    xx = np.sin(xx)
    return xx

def ex12():
    freq = 5
    x = np.linspace(0, np.pi * 2 * freq, 100)
    xx, yy = np.meshgrid(x, x)
    yy = np.sin(yy)
    return yy

def ex13():
    freq = 5
    x = np.linspace(0, np.pi * 2 * freq, 100)
    xx, yy = np.meshgrid(x, x)
    xx = np.sin(xx)
    yy = np.sin(yy)
    return (xx+yy)*255+127

if __name__ == '__main__':
    img,_ = ex4(False)
    _,axes = plt.subplots(1,2)
    # axes[1].imshow(ex5(img,100,1.2), **IMSHOW_ARGS)
    #img_with_rect = ex7(img)
    axes[0].imshow(ex13(), **IMSHOW_ARGS)
    #axes[1].imshow(ex8(img_with_rect), **IMSHOW_ARGS)
    plt.show()