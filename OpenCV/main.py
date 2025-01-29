import cv2
from recognition import SimpleFaceRec

sfr = SimpleFaceRec()
sfr.load_images("TrainImages")

cap = cv2.VideoCapture(0)
while True:
    ret, frame = cap.read()
    if not ret:
        break
    locations, names = sfr.detect_faces(frame)
    for (top, right, bottom, left), name in zip(locations, names):
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 3)
        cv2.putText(
            frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2
        )
        cv2.imshow("Face Recognition", frame)
    if cv2.waitKey(1) == 27:
        break
cap.release()
cv2.destroyAllWindows()
