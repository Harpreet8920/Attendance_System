import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime


class AttendanceSystem:
    def __init__(self):
        self.video_capture = cv2.VideoCapture(0)
        self.known_face_encodings = []
        self.known_face_names = []
        self.load_known_faces()
        self.student = self.known_face_names.copy()
        self.current_date = datetime.now().strftime("%Y-%m-%d")
        self.csv_file = open(f"{self.current_date}.csv", "w+", newline="")
        self.csv_writer = csv.writer(self.csv_file)

    def load_known_faces(self):
        harry_image = face_recognition.load_image_file("faces/harry.jpg")
        harry_encoding = face_recognition.face_encodings(harry_image)[0]
        self.known_face_encodings.append(harry_encoding)
        self.known_face_names.append("Harry")

        kalash_image = face_recognition.load_image_file("faces/kalash.jpg")
        kalash_encoding = face_recognition.face_encodings(kalash_image)[0]
        self.known_face_encodings.append(kalash_encoding)
        self.known_face_names.append("Kalash")

    def process_frame(self, frame):
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(
            rgb_small_frame, face_locations
        )

        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(
                self.known_face_encodings, face_encoding
            )
            face_distance = face_recognition.face_distance(
                self.known_face_encodings, face_encoding
            )
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = self.known_face_names[best_match_index]

            if name in self.known_face_names:
                cv2.putText(
                    frame,
                    name + " Present",
                    (10, 100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1.5,
                    (255, 0, 0),
                    3,
                    2,
                )
                if name in self.student:
                    self.student.remove(name)
                    current_time = datetime.now().strftime("%H-%M-%S")
                    self.csv_writer.writerow([name, current_time])

    def run(self):
        while True:
            ret, frame = self.video_capture.read()
            if not ret:
                break
            self.process_frame(frame)
            cv2.imshow("Attendance", frame)
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break

        self.video_capture.release()
        cv2.destroyAllWindows()
        self.csv_file.close()


if __name__ == "__main__":
    attendance_system = AttendanceSystem()
    attendance_system.run()
