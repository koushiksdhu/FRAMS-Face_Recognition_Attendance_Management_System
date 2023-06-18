import face_recognition
import cv2
import numpy as np
import csv
import os
from datetime import datetime
import time
import winsound

cwd = os.getcwd()
face_cascade = cv2.CascadeClassifier(cwd+"\\FRAMS\\haarcascade_frontalface_default.xml")

camCount = 5

def cam():
    for i in range(0, camCount):
        video_capture = cv2.VideoCapture(i)
        if video_capture.isOpened():
            print(f"Camera {i} Detected")
            return video_capture
        else:
            video_capture.release()
            if i == camCount - 1:
                print("No WebCam Detected.")
            
video_capture = cam()

folder_path = cwd+"\\FRAMS\\Faces"
filenames = os.listdir(folder_path)

data_encoding = []
data_names = []

for filename in filenames:
    file_path = os.path.join(folder_path, filename)
    image = filename[:-4]+"_image"
    encoding = filename[:-4]+"_encoding"
    globals()[image] = face_recognition.load_image_file(file_path)
    globals()[encoding] = face_recognition.face_encodings(globals()[image])[0]
    data_encoding.append(globals()[encoding])
    data_names.append(filename[:-4])    

students = data_names.copy()

face_locations = []
face_encodings = []
face_names = []
s = True

text_duration = 5

current_date = datetime.now().strftime("%Y-%m-%d")

f = open(cwd+"\\FRAMS\\Attendance\\"+current_date+'.csv', 'w+', newline = '')
lnwriter = csv.writer(f)
lnwriter.writerow(["Name", "Timestamp"])


while True:
    _,frame = video_capture.read()
    small_frame = cv2.resize(frame,(0, 0), fx = 0.25, fy = 0.25)
    rgb_small_frame = small_frame[:, :, ::-1]
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        
    if s:
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
        face_names = []
                
        for face_encoding in face_encodings:
            matches = face_recognition.compare_faces(data_encoding, face_encoding)
            name = ""
            face_distance = face_recognition.face_distance(data_encoding, face_encoding)
            best_match_index = np.argmin(face_distance)
            if matches[best_match_index]:
                name = data_names[best_match_index]
                
            face_names.append(name)
            if name in data_names:
                if name in students:
                    students.remove(name)
                    print(students)
                    lnwriter.writerow([name, datetime.now().strftime("%H:%M:%S")])
                    winsound.Beep(800, 2000)
                    for (x, y, w, h) in faces:
                        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                        cv2.putText(frame, name+" Present", (80, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                            
                        
                           
    cv2.imshow("Face Recognition Attendance System", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()
f.close()






