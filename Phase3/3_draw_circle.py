import cv2

image = cv2.imread("../Phase1/OpenCv_image.png")

if image is None:
    print("Image not loaded")
else:
    center = (100,100)
    radius = 50
    color = (111,111,111)
    thickness = 4
    cv2.imshow("Original", image)
    cv2.circle(image, center, radius, color, thickness)
    cv2.imshow("After", image)

    cv2.waitKey(0)
    cv2.destroyAllWindows()