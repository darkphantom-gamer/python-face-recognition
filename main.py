import face_recognition
import cv2
import numpy as np
import openpyxl
from datetime import datetime
import time

# Initialize video capture
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Load and encode images
try:
    God = face_recognition.load_image_file(r"x:/AI/pic.jpg")
    God_encoding = face_recognition.face_encodings(God)[0]

    tesla = face_recognition.load_image_file(r"Path to imageng")
    tesla_encoding = face_recognition.face_encodings(tesla)[0]
    
    elon = face_recognition.load_image_file(r"Path to imageg")
    elon_encoding = face_recognition.face_encodings(elon)[0]
    
    hunbaba = face_recognition.load_image_file(r"Path to image.jpg")
    hunbaba_encoding = face_recognition.face_encodings(hunbaba)[0]
    
except Exception as e:
    print(f"Error loading images: {e}")
    exit()

# Known encodings and namesimport face_recognition
import cv2
import numpy as np
import openpyxl
from datetime import datetime
import time

# Initialize video capture
video_capture = cv2.VideoCapture(0)
if not video_capture.isOpened():
    print("Error: Could not access the camera.")
    exit()

# Load and encode images
try:
    Person1 = face_recognition.load_image_file(r"Path to image")  # Change this to the path of the image
    Person1_encoding = face_recognition.face_encodings(Person1)[0] 

    Person2 = face_recognition.load_image_file(r"Path to image") # Change this to the path of the image
    Person2_encoding = face_recognition.face_encodings(Person2)[0]
    
    Person3 = face_recognition.load_image_file(r"Path to imageg")
    Person3_encoding = face_recognition.face_encodings(Person3)[0]
    
    Person4 = face_recognition.load_image_file(r"Path to image")
    Person4_encoding = face_recognition.face_encodings(Person2)[0]
    
except Exception as e:
    print(f"Error loading images: {e}")
    exit()

# Known encodings and names
known_face_encoding = [Person1_encoding, Person2_encoding, Person3_encoding, Person4_encoding] #change the number of encodings according to the number of people 
known_face_name = ["Person1", "Person2", "Person3", "Person4"] #change the number of names according to the number of people

# Initialize attendance tracking
students = set(known_face_name)

# Prepare Excel file
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
excel_file_path = current_date + '.xlsx'
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Attendance"
sheet.append(["Name", "Time"])

# Timeout mechanism
start_time = time.time()
max_runtime = 3600  # Maximum runtime in seconds (e.g., 1 hour)

try:
    # Main video processing loop
    while True:
        # Check for timeout
        if time.time() - start_time > max_runtime:
            print("Timeout reached. Exiting.")
            break

        # Capture video frame
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Failed to capture frame. Exiting loop.")
            break

        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Detect faces and compare
        face_locations = face_recognition.face_locations(rgb_small_frame, model='hog')
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Scale back up face locations to the original frame size
            top *= 4
            right *= 4
            bottom *= 4 
            left *= 4

            # Compare face with known encodings
            face_distances = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distances)

            name = "Unknown"
            if face_distances[best_match_index] < 0.6:  # Threshold for recognition
                name = known_face_name[best_match_index]

                # Mark attendance
                if name in students:
                    students.remove(name)  # Prevent duplicate entries
                    current_time = datetime.now().strftime("%H:%M:%S")
                    sheet.append([name, current_time])
                    print(f"Attendance marked for {name} at {current_time}")

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Draw a label with a name above the face
            font = cv2.FONT_HERSHEY_DUPLEX
            text_size = cv2.getTextSize(name, font, 0.5, 1)[0]
            text_x = left + (right - left - text_size[0]) // 2
            text_y = top - 10  # Position text above the head
            cv2.putText(frame, name, (text_x, text_y), font, 0.5, (0, 255, 0), 1)

        # Display the frame
        cv2.imshow("Attendance System", frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Save Excel file and release resources
    workbook.save(excel_file_path)
    video_capture.release()
    cv2.destroyAllWindows()
    print("Resources released. Attendance system stopped.")

known_face_encoding = [God_encoding,tesla_encoding,elon_encoding,hunbaba_encoding]
known_face_name = ["Creator", "tesla", "Elon Musk", "Hunbaba"]

# Initialize attendance tracking
students = set(known_face_name)

# Prepare Excel file
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
excel_file_path = current_date + '.xlsx'
workbook = openpyxl.Workbook()
sheet = workbook.active
sheet.title = "Attendance"
sheet.append(["Name", "Time"])

# Timeout mechanism
start_time = time.time()
max_runtime = 3600  # Maximum runtime in seconds (e.g., 1 hour)

try:
    # Main video processing loop
    while True:
        # Check for timeout
        if time.time() - start_time > max_runtime:
            print("Timeout reached. Exiting.")
            break

        # Capture video frame
        ret, frame = video_capture.read()
        if not ret:
            print("Error: Failed to capture frame. Exiting loop.")
            break

        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Detect faces and compare
        face_locations = face_recognition.face_locations(rgb_small_frame, model='hog')
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
            # Scale back up face locations to the original frame size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Compare face with known encodings
            face_distances = face_recognition.face_distance(known_face_encoding, face_encoding)
            best_match_index = np.argmin(face_distances)

            name = "Unknown"
            if face_distances[best_match_index] < 0.6:  # Threshold for recognition
                name = known_face_name[best_match_index]

                # Mark attendance
                if name in students:
                    students.remove(name)  # Prevent duplicate entries
                    current_time = datetime.now().strftime("%H:%M:%S")
                    sheet.append([name, current_time])
                    print(f"Attendance marked for {name} at {current_time}")

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

            # Draw a label with a name above the face
            font = cv2.FONT_HERSHEY_DUPLEX
            text_size = cv2.getTextSize(name, font, 0.5, 1)[0]
            text_x = left + (right - left - text_size[0]) // 2
            text_y = top - 10  # Position text above the head
            cv2.putText(frame, name, (text_x, text_y), font, 0.5, (0, 255, 0), 1)

        # Display the frame
        cv2.imshow("Attendance System", frame)

        # Exit on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Save Excel file and release resources
    workbook.save(excel_file_path)
    video_capture.release()
    cv2.destroyAllWindows()
    print("Resources released. Attendance system stopped.")
