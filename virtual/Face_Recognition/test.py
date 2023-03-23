import face_recognition
from pyttsx3 import speak

import cv2
import numpy as np




video_capture = cv2.VideoCapture(0)
nabeel_image = face_recognition.load_image_file("virtual\\Face_Recognition\\Resources\\1.jpg")
nabeel_face_encoding = face_recognition.face_encodings(nabeel_image)[0]
aman_image = face_recognition.load_image_file("virtual\\Face_Recognition\\Resources\\2.jpg")
aman_face_encoding = face_recognition.face_encodings(aman_image)[0]
known_face_encodings = [
    nabeel_face_encoding,
    aman_face_encoding
]
known_face_names = [
    "Nabeel Ali Khan",
    "Aman Ali Khan"
]
face_locations = []
face_encodings = []
face_names = []
process_this_frame = True
while True:
    ret, frame = video_capture.read()
    if process_this_frame:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            face_names.append(name)
    process_this_frame = not process_this_frame
    # Display the results
    for (top, right, bottom, left), name in zip(face_locations, face_names):
        # Scale back up face locations since the frame we detected in was scaled to 1/4 size
        top *= 4
        right *= 4
        bottom *= 4
        left *= 4
        with open("virtual\\Face_Recognition\\db.txt",'w+')as f:
            f.write(f"{name}\n")
        
        if name==known_face_names[0]:
                print("Face Recognized")
                print(name)
                speak("Face Recognized")
                exit()
                        
        else:
                print("Face Recognition Failed!")
                speak("Face Recognition Failed")
    # if cv2.waitKey(1) & 0xFF == ord('q'):
    #     break
    # Display the resulting image
    # cv2.imshow('Video', frame)
    # Hit 'q' on the keyboard to quit!
print(name)
# Release handle to the webcam
# video_capture.release()
# cv2.destroyAllWindows()