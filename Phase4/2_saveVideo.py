import cv2

cap = cv2.VideoCapture(0)

frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# ret, frame = cap.read()
# if not ret:
#     print("Camera not working")
#     exit()

# h,w = frame.shape[:2]

codec = cv2.VideoWriter_fourcc(*'XVID')

recorder = cv2.VideoWriter("../Phase4/myVideo.avi", codec, 20, (frame_width, frame_height))

while True:
    ret, frame = cap.read()

    if not ret:
        print("Could not find the frame")
        break

    recorder.write(frame)
    cv2.imshow("Frame", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Quitting...")
        break

recorder.release()
cap.release()
cv2.destroyAllWindows()

print("Video saved successfully!")