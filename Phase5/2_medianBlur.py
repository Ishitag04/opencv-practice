import cv2

image = cv2.imread("../Phase5/medianBlur_ExImg.png")

if image is None:
    print("Image not found! Check the path.")
    exit()

blurred = cv2.medianBlur(image, 5)

cv2.imshow("Original", image)
cv2.imshow("Blurred", blurred)

cv2.waitKey(0)
cv2.destroyAllWindows()