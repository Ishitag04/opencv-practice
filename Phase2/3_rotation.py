import cv2

image = cv2.imread("../Phase1/OpenCV_image.png")

if image is None:
    print("Image not loaded")
else:
    w,h = image.shape[:2]
    # w,h = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY).shape

    # M = cv2.getRotationMatrix2D((w//2, h//2), -90, 1.0)

    center = (w//2, h//2)
    M = cv2.getRotationMatrix2D(center, 90, 1.0)

    rotated_image = cv2.warpAffine(image, M, (w,h))

    cv2.imshow("Original", image)
    cv2.imshow("Rotated", rotated_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()