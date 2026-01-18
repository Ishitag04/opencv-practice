import cv2

video_path = "../Phase4/myVideo.avi"

cap = cv2.VideoCapture(video_path)

if not cap.isOpened():
    print("Error: Cannot open the video file.")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Playing AVI Video", frame)

    # Press q to quit
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
