import cv2 as cv

# Load the cascade
face_cascade = cv.CascadeClassifier(cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
# Load the webcam
cap = cv.VideoCapture(0)
while True:
    # Read the frame
    ret, frame = cap.read()
    # Detect faces in the frame 
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    # Draw the rectangle around each face
    for(x, y, w, h) in faces:
        # Draw rectangle around the faces
        cv.rectangle(frame, (x, y), (x+w, y+h), (255, 255, 255), 2)

    # Display
    cv.imshow("Frame", frame)
    # Exit
    key=cv.waitKey(1)
    # Close the window
    if key == 27:
        break
# When everything done, release the capture
cap.release()
# Destroy the window
cv.destroyAllWindows()