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
            frame = self.process_frame(frame,value)
            cv2.imshow("okno", frame)
            if cv2.waitKey(1) == ord('q'):
                break

class BrightnessViewer(Viewer):
    def __init__(self):
        super().__init__("jasność", 256, 256*2-1)

    def get_slider_value(self):
        return super().get_slider_value() - 256

    def process_frame(self, frame, value):
        return cv2.add(frame, value)

class GaussianViewer(Viewer):
    def __init__(self):
        super().__init__("gauss",0,50)

    def get_slider_value(self):
        return super().get_slider_value()*2+1

    def process_frame(self, frame, value):
        slider_value = self.get_slider_value()
        return cv2.GaussianBlur(frame,(slider_value,slider_value),0)

class MedianViewer(Viewer):
    def __init__(self):
        super().__init__("median",0,50)

    def get_slider_value(self):
        return super().get_slider_value()*2+1

    def process_frame(self, frame, value):
        return cv2.medianBlur(frame,self.get_slider_value())

class HSVViewer(Viewer):
    def __init__(self):
        super().__init__("H", 0, 180)

    def process_frame(self, frame, value):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hue = frame[:,:,0]
        frame[:,:,0] = (hue + super().get_slider_value()) % 180
        return cv2.cvtColor(frame, cv2.COLOR_HSV2BGR)

def ex1():
    img = cv2.imread("grzybek.png")
    cv2.imshow("okno", img)
    cv2.waitKey(0)

def ex2():
    cam = cv2.VideoCapture(0)
    if cam is not None and cam.isOpened():
        cv2.namedWindow("okno")
        brightness = 0
        slider = cv2.createTrackbar("jasność", "okno", 256, 256*2-1, lambda x:x)
        while True:
            ok, frame = cam.read()
            if not ok:
                break
            cv2.flip(frame, 1, frame)
            brightness = cv2.getTrackbarPos("jasność", "okno") - 256
            frame = cv2.add(frame, brightness)
            cv2.imshow("okno", frame)
            if cv2.waitKey(1) == ord('q'):
                break


def main():
    # viewer = Viewer("slider",0,255)
    # viewer = BrightnessViewer()
    # viewer = MedianViewer()
    viewer = HSVViewer()
    viewer.run()


if __name__ == '__main__':
    main()