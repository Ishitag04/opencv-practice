import cv2

image = cv2.imread("../Phase1/OpenCV_image.png")

if image is None:
    print("Image could not be loaded")
else:
    flipped_image_horizontal = cv2.flip(image, 1)
    flipped_image_vertical = cv2.flip(image , 0)
    flipped_image_both = cv2.flip(image, -1)

    cv2.imshow("Original", image)
    cv2.imshow("Horizontal", flipped_image_horizontal)
    cv2.imshow("Verical", flipped_image_vertical)
    cv2.imshow("Both", flipped_image_both)

    cv2.waitKey(0)
    cv2.destroyAllWindows()