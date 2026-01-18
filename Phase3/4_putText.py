import cv2

image = cv2.imread("../Phase1/OpenCV_image.png")

if image is None:
    print("Image not loaded")
else:
    cv2.imshow("Original", image)
    org = (100,100)
    # fontFace = 100
    fontScale = 1.0
    color = (0,255,0)
    cv2.putText(image, "OpenCV", org, cv2.FONT_HERSHEY_SIMPLEX, fontScale, color, 2)
    cv2.imshow("After", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()