import cv2

image = cv2.imread("../Phase1/OpenCv_image.png")

if image is None:
    print("Image not loaded")
else:
    cv2.imshow("Original", image)
    pt1 = (50,100)
    pt2 = (100,100)
    color = (255,0,0)
    thickness = 4
    cv2.line(image, pt1, pt2, color, thickness)
    cv2.imshow("After", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
