import cv2

def main():
    net = cv2.dnn.readNet("coco/model.pbtxt","coco/weights.pb")
    img = cv2.imread("obraz.png")
    blob = cv2.dnn.blobFromImage(img,1.0/127.5,size=(300,300),mean=(127.5,127.5,127.5),swapRB=True,crop=False)
    net.setInput(blob)
    result = net.forward()
    with open("coco/labels.txt") as file:
        labels = [label.strip() for label in file.readlines()]
    for entry in result[0,0,:,:]:
        print(labels[int(entry[1])],entry[2], entry[3:])

if __name__ == '__main__':
    main()