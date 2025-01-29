import face_recognition
import cv2
import os
import glob
import numpy as np


class SimpleFaceRec:
    def __init__(self):
        self.known_faces_encodings = []
        self.known_faces_name = []
        self.resize_factor = 0.25

    def load_images(self, path):
        for img_path in glob.glob(f"{path}/*.*"):
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            face_encoding = face_recognition.face_encodings(rgb_img)
            if face_encoding:
                self.known_faces_encodings.append(face_encoding[0])
                self.known_faces_name.append(
                    os.path.splitext(os.path.basename(img_path))[0]
                )
                print(f"Loaded {len(self.known_faces_encodings)} faces from '{path}'.")

    def detect_faces(self, frame):
        if not self.known_faces_encodings:
            return [], []

        small_faces = cv2.resize(
            frame, (0, 0), fx=self.resize_factor, fy=self.resize_factor
        )

        rgb_frame = cv2.cvtColor(small_faces, cv2.COLOR_BGR2RGB)
        locations = face_recognition.face_locations(rgb_frame)
        encodings = face_recognition.face_encodings(rgb_frame, locations)
        names = []
        for encoding in encodings:
            matches = face_recognition.compare_faces(
                self.known_faces_encodings, encoding
            )
            name = "Unknown"
            if any(matches):
                first_match_index = np.argmin(
                    face_recognition.face_distance(self.known_faces_encodings, encoding)
                )
                name = self.known_faces_name[first_match_index]
            names.append(name)

        return (np.array(locations) / self.resize_factor).astype(int), names
