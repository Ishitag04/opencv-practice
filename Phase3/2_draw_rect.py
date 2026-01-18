import cv2

image = cv2.imread("../Phase1/OpenCV_image.png")

if image is None:
    print("Image not loaded")
else:
    cv2.imshow("Original", image)
    pt1 = (50,50)
    pt2 = (150,150)
    color = (200,200,200)
    thickness = 4
    cv2.rectangle(image, pt2, pt1, color, thickness)
    cv2.imshow("After", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()