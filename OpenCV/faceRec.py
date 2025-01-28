import cv2

# Load the cascade 
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Read the input image
image = cv2.imread("images.jpeg")

# Convert into grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# detect faces in the image
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

print(faces)

# Draw rectangle around the faces
for(x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Display the output
cv2.imshow("img", image)

# Wait for a key press to exit
cv2.waitKey(0)

# Close the window
cv2.destroyAllWindows()