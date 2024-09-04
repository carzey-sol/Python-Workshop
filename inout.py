import cv2
import numpy as np
import datetime

# Initialize the camera
cap = cv2.VideoCapture(0)

# Capture the initial frame and process it
ret, inp_img = cap.read()
if not ret:
    print("Failed to capture initial frame")
    cap.release()
    cv2.destroyAllWindows()
    exit()

inp_img = cv2.flip(inp_img, 1)
gray_inp_img = cv2.cvtColor(cv2.blur(inp_img, (4, 4)), cv2.COLOR_BGR2GRAY)

# Define initial points to track
old_pts = np.array([[350, 180], [350, 350]], dtype=np.float32).reshape(-1, 1, 2)
backup = old_pts.copy()
backup_img = gray_inp_img.copy()

# Initialize an output window for text
outp = np.zeros((480, 640, 3), dtype=np.uint8)
ytest_pos = 40

while True:
    # Capture a new frame and process it
    ret, new_inp_img = cap.read()
    if not ret:
        print("Failed to capture frame")
        break

    new_inp_img = cv2.flip(new_inp_img, 1)
    new_gray = cv2.cvtColor(cv2.blur(new_inp_img, (4, 4)), cv2.COLOR_BGR2GRAY)

    # Calculate optical flow
    new_pts, status, err = cv2.calcOpticalFlowPyrLK(
        gray_inp_img, new_gray, old_pts, None,
        maxLevel=1,
        criteria=(cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 15, 0.08)
    )

    # Ensure points stay within specified boundaries
    new_pts[:, :, 0] = np.clip(new_pts[:, :, 0], 20, 600)
    new_pts[:, :, 1] = np.clip(new_pts[:, :, 1], 150, 350)

    # Draw a line between the tracked points
    x, y = new_pts[0].ravel()
    a, b = new_pts[1].ravel()
    cv2.line(new_inp_img, (int(x), int(y)), (int(a), int(b)), (0, 0, 255), 15)

    # Display the new frame with the line
    cv2.imshow("output", new_inp_img)

    # Check if points cross specified horizontal boundaries and log the event
    if new_pts[0, 0, 0] > 400 or new_pts[1, 0, 0] > 400:
        if new_pts[0, 0, 0] > 550 or new_pts[1, 0, 0] > 550:
            new_pts = backup.copy()
            ytest_pos += 40
            cv2.putText(outp, "came at {}".format(datetime.datetime.now().strftime("%H:%M")),
                        (10, ytest_pos), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0))

    elif new_pts[0, 0, 0] < 200 or new_pts[1, 0, 0] < 200:
        if new_pts[0, 0, 0] < 50 or new_pts[1, 0, 0] < 50:
            new_pts = backup.copy()
            ytest_pos += 40
            cv2.putText(outp, "gone at {}".format(datetime.datetime.now().strftime("%H:%M")),
                        (10, ytest_pos), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255))

    # Display the final text output
    cv2.imshow('final', outp)

    # Update the previous frame and points
    gray_inp_img = new_gray.copy()
    old_pts = new_pts.reshape(-1, 1, 2)

    # Break the loop if 'Esc' key is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()