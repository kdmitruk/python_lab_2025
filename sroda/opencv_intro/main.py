import cv2

def ex1():
    img = cv2.imread("grzybek.png")
    cv2.imshow("okno", img)
    cv2.waitKey(0)

def ex2():
    cam = cv2.VideoCapture(0)
    if cam is not None and cam.isOpened():
        cv2.namedWindow("okno")
        brightness = 0
        slider = cv2.createTrackbar("jasnosc", "okno", 256, 256*2-1, lambda x:x)
        while True:
            ok, frame = cam.read()
            if not ok:
                break
            cv2.flip(frame, 1, frame)
            brightness = cv2.getTrackbarPos("jasnosc", "okno") - 256
            frame = cv2.add(frame, brightness)
            cv2.imshow("okno", frame)
            if cv2.waitKey(1) == ord('q'):
                break


def main():
    ex2()


if __name__ == '__main__':
    main()