import cv2
import time
import winsound

face_cascade = cv2.CascadeClassifier("../Phase8_Last/haarcascade_frontalface_default.xml")
eye_cascade = cv2.CascadeClassifier("../Phase8_Last/haarcascade_eye.xml")
smile_cascade = cv2.CascadeClassifier("../Phase8_Last/haarcascade_smile.xml")


cap = cv2.VideoCapture(0)

eyes_closed_start = None
alarm_played = False
closed_frames = 0

while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 5)

    for (x,y,w,h) in faces:

        cv2.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), 2)

        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 5)

        if len(eyes) > 0:
            cv2.putText(frame, "Eyes Detected", (x, y-30), cv2.FONT_HERSHEY_SIMPLEX, 0.6,(0,0,255) , 2)
            eyes_closed_start = None
            alarm_played = False
            closed_frames = 0

        if len(eyes) == 0:
            closed_frames += 1

            if closed_frames == 1:
                eyes_closed_start = time.time()
            elapsed = time.time() - eyes_closed_start

            cv2.putText(frame, "Blink", (x, y-60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0,255,255), 2)
            cv2.putText(frame, f"Eyes Closed: {int(elapsed)} sec",(x, y - 35), cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 255, 255), 2)

            print("Elapsed:", elapsed)

            if elapsed >= 0.5 and not alarm_played:
                winsound.Beep(1500, 1000)
                alarm_played = True
        
    cv2.imshow("Smart Face Detector", frame)

    if (cv2.waitKey(1) & 0xFF == ord('q')):
        break

cap.release()
cv2.destroyAllWindows()