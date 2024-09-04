import cv2
import os

# Setup the dataset directory and target name
dataset = "mukesh"
name = "photo"
path = os.path.join(dataset, name)

# Create the directory if it does not exist
os.makedirs(path, exist_ok=True)

# Define the dimensions and Haar cascade for face detection
(width, height) = (130, 100)
alg = "haarcascade_frontalface_default.xml"
haar_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + alg)

# Start the webcam
cam = cv2.VideoCapture(0)

count = 1
while count <= 20:
    print(f"Capturing image {count}")  # Fixed f-string usage
    ret, img = cam.read()
    
    if not ret:
        print("Failed to capture image.")
        break

    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray_img, 1.3, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
        face_only = gray_img[y:y+h, x:x+w]
        resize_img = cv2.resize(face_only, (width, height))
        cv2.imwrite(f"{path}/{name}_{count}.jpg", resize_img)  # Fixed file naming

        count += 1

    cv2.imshow("Face Detection", img)

    # Press 'ESC' to break out of the loop early
    key = cv2.waitKey(10)
    if key == 27:
        break

print("Image Capture Complete")
cam.release()
cv2.destroyAllWindows()
