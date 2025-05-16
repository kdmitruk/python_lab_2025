import cv2

class Viewer:
    def __init__(self, initial_value, max_value):
        cv2.namedWindow('window')
        self.capture = cv2.VideoCapture(0)
        cv2.createTrackbar('slider', 'window', initial_value, max_value, lambda x:None)

    def get_trackbar_pos(self):
        return cv2.getTrackbarPos('slider', 'window')

    def process_frame(self,frame,trackbar_pos):
        return frame

    def run(self):
        while True:
            ret, frame = self.capture.read()
            if not ret:
                break
            trackbar_pos = self.get_trackbar_pos()
            frame = self.process_frame(frame,trackbar_pos)
            cv2.imshow('window', frame)
            if cv2.waitKey(1) == ord('q'):
                break

class BrightnessViewer(Viewer):
    def __init__(self):
        super().__init__(256, 256 * 2 - 1)

    def get_trackbar_pos(self):
        return super().get_trackbar_pos() - 256

    def process_frame(self, frame, trackbar_pos):
        return cv2.add(frame, trackbar_pos)