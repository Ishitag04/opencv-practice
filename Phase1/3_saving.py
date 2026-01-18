import cv2

image = cv2.imread("OpenCV_image.png")

if image is not None:
    success = cv2.imwrite("Output_Python.png", image)
    # print(success)
    # print(type(success))
    if success:
        print("Image saved successfully as 'Output_Python.png'")
    else:
        print("Failed to save an image")
else:
    print("Error : Could not load the image")