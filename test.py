import cv2

# Open the camera
cap = cv2.VideoCapture(0)

# Check if the camera is opened
if not cap.isOpened():
    print("Camera not accessible")
else:
    print("Camera is accessible")

    # Read and display frames in a loop
    while True:
        # Capture frame-by-frame
        ret, frame = cap.read()

        # If frame is read correctly, ret is True
        if not ret:
            print("Failed to grab frame")
            break

        # Display the resulting frame
        cv2.imshow('Camera Feed', frame)

        # Press 'q' to quit the window
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the camera and close the window
    cap.release()
    cv2.destroyAllWindows()
