import cv2
import face_recognition
import os
import numpy as np


def predict_from_folder(known_faces_dir, test_image_path , threshold = 0.5):

    known_encodings = []
    known_names = []


    for file in os.listdir(known_faces_dir):
        img_path = os.path.join(known_faces_dir , file)
        image = face_recognition.load_image_file(img_path)

        encodings = face_recognition.face_encodings(image)
        known_encodings.append(encodings[0])
        known_names.append(os.path.splitext(file)[0])

    print("Known faces loaded")

    test_image = face_recognition.load_image_file(test_image_path)
    test_encodings = face_recognition.face_encodings(test_image)

    if len(test_encodings) == 0:
        print("No face foundin the test image")
        return
    test_encoding = test_encodings[0]

    distances = face_recognition.face_distance(known_encodings, test_encoding)
    best_match_index = np.argmin(distances)
    best_distance = distances[best_match_index]

    if best_distance < threshold:
        predicted_name = known_names[best_match_index]
    else:
        predicted_name = "Unknown"


    test_bgr = cv2.cvtColor(test_image, cv2.COLOR_RGB2BGR)
    cv2.putText(
        test_bgr,
        f"Prediction: {predicted_name}",
        (20,40),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0,255,0),
        2
    )


    cv2.imshow("Prediction Result", test_bgr)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


predict_from_folder(
    known_faces_dir="D:\Py Django\DataScience\Faces",
    test_image_path="D:\Py Django\DataScience\Faces\Archana.jpeg"
)