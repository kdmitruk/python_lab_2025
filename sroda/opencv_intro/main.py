import cv2


class Viewer:
    def __init__(self, slider_name, current_value, end_value):
        self.slider_name = slider_name
        self.start_value = current_value
        self.end_value = end_value
        self.cam = cv2.VideoCapture(0)
        if self.cam is not None and self.cam.isOpened():
            cv2.namedWindow("okno")
            cv2.createTrackbar(slider_name, "okno", current_value, end_value, lambda x:x)

    def get_slider_value(self):
        return cv2.getTrackbarPos(self.slider_name, "okno")

    def process_frame(self, frame, value):
        return frame

    def run(self):
        value = 0
        while True:
            ok, frame = self.cam.read()
            if not ok:
                break
            cv2.flip(frame, 1, frame)
            value = self.get_slider_value()
            # frame = cv2.add(frame, value)
            frame = self.process_frame(frame,value)
            cv2.imshow("okno", frame)
            if cv2.waitKey(1) == ord('q'):
                break

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
    viewer = Viewer("slider",0,255)
    viewer.run()


if __name__ == '__main__':
    main()