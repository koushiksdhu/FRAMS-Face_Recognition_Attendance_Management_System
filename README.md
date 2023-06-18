# Face Recognition Attendance Management System

The Face Recognition Attendance Management System is a Python-based application that utilizes computer vision techniques, including OpenCV (cv2), Haar cascade classifiers, and the face_recognition dataset module. The system enables real-time face detection and recognition from a video stream and automatically marks attendance in an Excel sheet, including the date and timestamp.

## Installation

To use the Face Recognition Attendance Management System, follow the steps below:

1. Clone the repository to your local machine:

   ```
   git clone https://github.com/your-username/face-attendance-management.git
   ```

2. Make sure you have Python 3.x installed on your system.

3. Install the required packages by running the following command:

   ```
   pip install face_recognition
   pip install opencv-python
   ```

   This will install the necessary dependencies, including OpenCV, Haar cascade classifiers, and the face_recognition dataset module.

## Usage

1. Prepare the dataset by creating a folder named "Faces" within the project directory. Inside the "Faces" folder, name the image file according to the respective person's name or unique identifier.

2. Run the following command to start the system and detect faces in a video stream:

   ```
   python main.py
   ```

   The system will open the default video camera and start detecting faces in real-time. It will compare the detected faces against the dataset and mark attendance in an Excel sheet.

3. The attendance records will be saved in an Excel file named "current_date.xlsx" in the project directory. Each entry will include the date and timestamp when the face was recognized.

## Contributing

Contributions to this project are welcome. If you encounter any issues or have suggestions for improvements, please create a GitHub issue and/or submit a pull request with your proposed changes.

## Acknowledgements

The Face Recognition Attendance Management System was developed using the following resources:

- OpenCV (cv2) - https://opencv.org/
- Haar cascade classifiers - https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
- face_recognition dataset module - https://github.com/ageitgey/face_recognition
