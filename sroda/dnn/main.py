import cv2
import numpy as np


def main():
    net = cv2.dnn.readNet("coco/model.pbtxt","coco/weights.pb")
    # img = cv2.imread("obraz.png")
    camera = cv2.VideoCapture(2)
    while True:
        _,frame = camera.read()
        blob = cv2.dnn.blobFromImage(frame,1.0/127.5,size=(300,300),mean=(127.5,127.5,127.5),swapRB=True,crop=False)
        net.setInput(blob)
        detections = net.forward()
        conf_threshold=0.66
        with open("coco/labels.txt") as file:
            class_names = [label.strip() for label in file.readlines()]
        h, w = frame.shape[:2]
        for i in range(detections.shape[2]):
            confidence = float(detections[0, 0, i, 2])
            if confidence > conf_threshold:
                class_id = int(detections[0, 0, i, 1])
                box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                (x1, y1, x2, y2) = box.astype('int')
                label = f"{class_names[class_id-1]}: {confidence*100:.1f}%"
                cv2.rectangle(frame, (x1, y1), (x2, y2), (0,255,0), 2)
                cv2.putText(frame, label, (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)
        cv2.imshow("img",frame)
        if cv2.waitKey(1) == ord('q'):
            break;

if __name__ == '__main__':
    main()