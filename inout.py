import cv2
import numpy as np
import datetime

# Initialize the camera
cap = cv2.VideoCapture(0)

# Capture the first frame
ret, frame1 = cap.read()
if not ret:
    print("Error: Couldn't capture the frame")
    cap.release()
    cv2.destroyAllWindows()
    exit()

frame1 = cv2.flip(frame1, 1)
gray_inp_img = cv2.cvtColor(cv2.blur(frame1, (4, 4)), cv2.COLOR_BGR2GRAY)

# Define initial points to track
old_pts = np.array([[350, 350], [350, 400]], dtype=np.float32).reshape(-1, 1, 2)

backup = old_pts.copy()
backup_img = gray_inp_img.copy()

# Initialize an output window for text
outp = np.zeros((480, 640, 3), dtype=np.uint8)

ytest_pos = 40

while True:
    # Capture the next frame
    ret, new_inp_img = cap.read()
    if not ret:
        print("Error: Couldn't capture the frame")
        break
    
    new_inp_img = cv2.flip(new_inp_img, 1)
    new_gray = cv2.cvtColor(cv2.blur(new_inp_img, (4, 4)), cv2.COLOR_BGR2GRAY)

    # Calculate the optical flow
    new_pts, status, err = cv2.calcOpticalFlowPyrLK(gray_inp_img, new_gray, old_pts, None, maxLevel=1, criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 15, 0.08))

    if new_pts is not None:
        # Ensure the new points are within the frame
        new_pts[:,:,0] = np.clip(new_pts[:,:,0], 0, new_inp_img.shape[1] - 1)
        new_pts[:,:,1] = np.clip(new_pts[:,:,1], 0, new_inp_img.shape[0] - 1)

        # Draw the tracking line
        x, y = new_pts[0].ravel()
        a, b = new_pts[1].ravel()
        cv2.line(new_inp_img, (int(x), int(y)), (int(a), int(b)), (0, 0, 255), 15)

        # Check if the points cross the horizontal boundaries and log the event
        if y > 400 or b > 400:
            if x > 550 or a > 550:
                new_pts = backup.copy()
                ytest_pos += 40
                cv2.putText(outp, "gone at {}".format(datetime.datetime.now().strftime("%H:%M")), (10, ytest_pos), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0))
        elif x < 200 or a < 200:
            if x < 50 or a < 50:
                new_pts = backup.copy()
                ytest_pos += 40
                cv2.putText(outp, "came at {}".format(datetime.datetime.now().strftime("%H:%M")), (10, ytest_pos), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255))

        # Display the frames
        cv2.imshow("Frame", new_inp_img)
        cv2.imshow("Log", outp)

        # Update the previous frame and points
        gray_inp_img = new_gray.copy()
        old_pts = new_pts.reshape(-1, 1, 2)

    # Break the loop if 'ESC' is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the camera and close the windows
cap.release()
cv2.destroyAllWindows()