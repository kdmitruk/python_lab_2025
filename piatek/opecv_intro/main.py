import cv2
from viewer import Viewer

def ex1():
    img = cv2.imread("tekstura_grzybka.png")
    cv2.imshow("", img)
    cv2.waitKey(0)

def ex2():
    capture = cv2.VideoCapture(0)
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        cv2.imshow('', frame)
        if cv2.waitKey(1) == ord('q'):
            break

def ex3():
    cv2.namedWindow('window')
    capture = cv2.VideoCapture(0)
    cv2.createTrackbar('slider', 'window', 256, 256 * 2 - 1, lambda x:None)
    while True:
        ret, frame = capture.read()
        if not ret:
            break
        cv2.imshow('window', cv2.add(frame,cv2.getTrackbarPos('slider', 'window') - 256))
        if cv2.waitKey(1) == ord('q'):
            break

if __name__ == '__main__':
    viewer = Viewer(0,1)
    viewer.run()