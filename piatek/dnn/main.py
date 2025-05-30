import cv2
import numpy as np

def main():
    net = cv2.dnn.readNet("model.pbtxt", "weights.pb")

    file = open("labels.txt", "r")
    labels = file.read().split("\n")

    cap = cv2.VideoCapture(0)
    while True:
        ret, img = cap.read()
        if not ret:
            break
        #img = cv2.imread("bear.jpg")
        h, w = img.shape[:2]

        blob = cv2.dnn.blobFromImage(img, scalefactor=1.0/127.5, size=(300, 300), crop=False, mean=(127.5, 127.5, 127.5), swapRB=True)

        net.setInput(blob)
        detection = net.forward()

        confidence = 0.6

        for roi in detection[0, 0, :, :]:
            current_confidence = roi[2]
            if current_confidence > confidence:
                label = labels[int(roi[1]-1)]
                box = roi[3:7] * np.array([w, h, w, h])
                box = box.astype(np.uint16)
                print(label, box)
                text = f"{label}: {current_confidence*100:.2f}%"
                cv2.rectangle(img, (box[0], box[1]), (box[2], box[3]),(0, 255, 0), 2)
                cv2.putText(img, text, (box[0], box[1]), cv2.FONT_HERSHEY_SIMPLEX, fontScale=1, color=(0, 255, 0))

        cv2.imshow("", img)
        cv2.waitKey(1)

if __name__ == '__main__':
    main()
