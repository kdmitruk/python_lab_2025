import cv2

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

if __name__ == '__main__':
    ex2()