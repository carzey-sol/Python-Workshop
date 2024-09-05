import cv2

# Initialize the video capture object
cap = cv2.VideoCapture(0)  # 0 is the default camera

# Read the first frame
ret, frame1 = cap.read()
if not ret:
    print("Failed to grab the first frame")
    exit()

# Convert the frame to grayscale
gray1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
# Blur the frame to reduce noise
gray1 = cv2.GaussianBlur(gray1, (21, 21), 0)

while True:
    # Read the next frame
    ret, frame2 = cap.read()
    if not ret:
        print("Failed to grab the next frame")
        break
    
    # Convert the frame to grayscale
    gray2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    # Blur the frame to reduce noise
    gray2 = cv2.GaussianBlur(gray2, (21, 21), 0)

    # Calculate the difference between the two frames
    diff = cv2.absdiff(gray1, gray2)

    # Threshold the difference to get the moving parts
    _, thresh = cv2.threshold(diff, 30, 255, cv2.THRESH_BINARY)

    # Find contours
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    # If contours are found, it means there is motion
    if len(contours) > 0:
        print("Moving Object Detected")
    else:
        print("Normal")
    
    # Display the frames
    cv2.imshow("frame", frame2)
 

    # Assign the current frame to the previous frame for the next iteration
    gray1 = gray2

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all openCV windows
cap.release()
cv2.destroyAllWindows()
