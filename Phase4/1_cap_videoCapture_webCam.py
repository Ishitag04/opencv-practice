import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    #ret => True/False 
    #frame => image

    if not ret:
        print("Could not read frame")
        break

    cv2.imshow("Webcam feed", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):   # if 'q' is pressed then this loop will break
        print("Quitting...")
        break

cap.release()   #Close the camera
cv2.destroyAllWindows()     #Destroys all the open OpenCV Windows
