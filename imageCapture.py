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
while count <= 1000:
    print(f"Capturing image {count}")
    ret, img = cam.read()
    
    if not ret:
        print("Failed to capture image.")
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = haar_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=4)
    
    for (x, y, w, h) in faces:
        face_img = gray[y:y + h, x:x + w]
        resized = cv2.resize(face_img, (width, height))
        
        # Save the captured image
        cv2.imwrite(f"{path}/image_{count}.jpg", resized)
        count += 1
    
    cv2.imshow("Face", img)
    
    # Exit if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
