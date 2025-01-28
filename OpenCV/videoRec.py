import cv2 as cv

# Load the cascade
cap = cv.VideoCapture(0)
while True:
    # Capture frame-by-frame
    ret, frame = cap.read()
    # Display the resulting frame
    cv.imshow("Frame", frame)
    # Wait for a key press to exit
    key=cv.waitKey(1)
    # Close the window
    if key == 27:
        break
# When everything done, release the capture
cap.release()
# Destroy the window
cv.destroyAllWindows()