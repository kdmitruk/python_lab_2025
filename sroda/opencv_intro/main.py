import cv2

def ex1():
    img = cv2.imread("grzybek.png")
    cv2.imshow("okno", img)
    cv2.waitKey(0)

def ex2():
    cam = cv2.VideoCapture(0)
    if cam is not None and cam.isOpened():
        while True:
            ok, frame = cam.read()
            if not ok:
                break
            cv2.imshow("okno", frame)
            key = cv2.waitKey(1)
            if key & 0xFF == ord('q'):
                break

def main():
    ex2()


if __name__ == '__main__':
    main()