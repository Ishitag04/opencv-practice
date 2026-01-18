import cv2

image = cv2.imread("OpenCV_image.png")
# print(type(image))
# print(image)
# print(image.ndim)
# print(image.shape)


if image is None:
    print("Error: Image not found")
else:
    print("Image loaded successfully")