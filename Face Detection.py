import cv2

# Print the OpenCV version
print(cv2.__version__)

# Load the face classifier
face_classifier = cv2.CascadeClassifier("C:\\Users\\user\\Desktop\\Edgematrix\\xml files\\haarcascade_frontalface_default.xml")

# Initialize video capture
video_capture = cv2.VideoCapture("C:\\Users\\user\\Desktop\\Edgematrix\\py files\\facedetection.mp4")

# Function to detect bounding box around faces
def detect_bounding_box(vid):
    gray_image = cv2.cvtColor(vid, cv2.COLOR_BGR2GRAY)
    faces = face_classifier.detectMultiScale(gray_image, 1.1, 5, minSize=(40, 40))
    for (x, y, w, h) in faces:
        cv2.rectangle(vid, (x, y), (x + w, y + h), (0, 255, 0), 4)
    return faces

# Main loop for video capture and face detection
while True:
    result, video_frame = video_capture.read()
    if result is False:
        break
    faces = detect_bounding_box(video_frame)
    cv2.imshow("My Face Detection Project", video_frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video capture and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
