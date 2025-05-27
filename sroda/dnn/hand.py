import cv2
import numpy as np
import os
import time

# Ścieżki do plików modelu
PROTO_FILE = "hand/model.prototxt"
WEIGHTS_FILE = "hand/weights.caffemodel"

# Liczba punktów i połączenia (kciuk, palce)
N_POINTS = 22
HAND_PAIRS = [
    (0, 1), (1, 2), (2, 3), (3, 4),      # kciuk
    (0, 5), (5, 6), (6, 7), (7, 8),      # wskazujący
    (0, 9), (9, 10), (10, 11), (11, 12), # środkowy
    (0, 13), (13, 14), (14, 15), (15, 16),# serdeczny
    (0, 17), (17, 18), (18, 19), (19, 20) # mały
]

# Parametry detekcji
THRESHOLD = 0.1
IN_WIDTH, IN_HEIGHT = 368, 368

def check_model_files():
    """Sprawdza, czy pliki modelu istnieją."""
    missing = [f for f in (PROTO_FILE, WEIGHTS_FILE) if not os.path.isfile(f)]
    if missing:
        raise FileNotFoundError(f"Nie znaleziono plików modelu: {missing}")

def load_network():
    """Ładuje sieć z plików Caffe."""
    return cv2.dnn.readNetFromCaffe(PROTO_FILE, WEIGHTS_FILE)

def process_frame(frame, net):
    """Wykrywa punkty dłoni na pojedynczej klatce."""
    h, w = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(frame, scalefactor=1.0/255,
                                 size=(IN_WIDTH, IN_HEIGHT),
                                 mean=(0,0,0),
                                 swapRB=True, crop=False)
    net.setInput(blob)
    output = net.forward()  # [1, N_POINTS, H, W]

    H, W = output.shape[2], output.shape[3]
    points = [None] * N_POINTS

    # Wyszukiwanie lokalnych maksimów w każdej mapie prawdopodobieństwa
    for i in range(N_POINTS):
        prob_map = output[0, i, :, :]
        _, conf, _, loc = cv2.minMaxLoc(prob_map)
        x = int((w * loc[0]) / W)
        y = int((h * loc[1]) / H)
        if conf > THRESHOLD:
            points[i] = (x, y)

    # Rysowanie punktów i linii
    for i, p in enumerate(points):
        if p is not None:
            cv2.circle(frame, p, 4, (0, 255, 0), thickness=-1)

    for pair in HAND_PAIRS:
        a, b = pair
        if points[a] and points[b]:
            cv2.line(frame, points[a], points[b], (255, 0, 255), 2)

    return frame

def main():
    check_model_files()
    net = load_network()

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Nie można otworzyć kamery")
        return

    # Przygotowanie miernika FPS
    prev_time = time.time()
    fps = 0

    cv2.namedWindow("Hand Pose", cv2.WINDOW_NORMAL)

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Koniec strumienia wideo")
            break

        frame = process_frame(frame, net)

        # Obliczanie i wyświetlanie FPS
        curr_time = time.time()
        fps = 1.0 / (curr_time - prev_time)
        prev_time = curr_time
        cv2.putText(frame, f"FPS: {fps:.1f}", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)

        cv2.imshow("Hand Pose", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
