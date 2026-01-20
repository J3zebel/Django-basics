import cv2
import face_recognition
import os
import numpy as np

known_faces_dir = "D:\Py Django\DataScience\Faces"

known_faces_encoding = []
known_face_names = []

for filename in os.listdir(known_faces_dir):
    image_path = os.path.join(known_faces_dir, filename)
    image = face_recognition.load_image_file(image_path)

    encoding = face_recognition.face_encodings(image)[0]

    known_faces_encoding.append(encoding)
    known_face_names.append(os.path.splitext(filename)[0])

print("Known faces loaded")

video_capture = cv2.VideoCapture(0)

print("Camera started. Press h to quit.")

while True:
    ret,frame = video_capture.read()
    if not ret:
        break

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)


    for (top,right,bottom,left), face_encodings in zip(face_locations, face_encodings):
        matches = face_recognition.compare_faces(known_faces_encoding,face_encodings)
        name = "Unknown"

        face_distances = face_recognition.face_distance(known_faces_encoding,face_encodings)
        best_match_index = np.argmin(face_distances)


        if matches[best_match_index]:
            name = known_face_names[best_match_index]

        cv2.rectangle(frame, (left,top),(right,bottom),(0,255,0),2)


        cv2.putText(
            frame,
            name,
            (left,top-10),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.9,
            (0,255,0),
            2
        )

        cv2.imshow("Face Recognition", frame)

        if cv2.waitKey(1) & 0xFF == ord("h"):
            break

video_capture.release()
cv2.destroyAllWindows()