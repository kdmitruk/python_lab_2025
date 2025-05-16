import cv2

def ex1():
    img = cv2.imread("tekstura_grzybka.png")
    cv2.imshow("", img)
    cv2.waitKey(0)

if __name__ == '__main__':
    ex1()