import cv2

name = input("Enter the name of the file to be converted to grayscale :")

image = cv2.imread(name)

if image is not None:

    cv2.imshow("Colored image",image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if gray is not None:
        n = int(input("Press\n1. To see gray scale image\n2. To save the image\n"))
        if n==1:
            cv2.imshow("GrayScaled image", gray)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print("Assignment Complete...")
        elif n==2:
            m = input("Enter the name with which you want to save the file : ")
            save = cv2.imwrite(m, gray)
            if save:
                print(f"{m} saved successfully")
                print("Assignment Complete...")
            else:
                print("Image could not be saved successfully")
        else:
            print("Not a valid option")

    else:
        print("Cannot be conveted to Gray Scale")

else:

    print("Could not load the image")









# import cv2

# image = cv2.imread("OpenCV_image.png")

# if image is not None:
#     cv2.imshow("Real Colored image", image)
#     cv2.waitKey(0)
#     cv2.destroyAllWindows()

#     gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#     if gray is not None:
#         cv2.imshow("Grayscaled Image", gray)
#         cv2.waitKey(0)
#         cv2.destroyAllWindows()

#         cv2.imwrite("OpenCV_GrayScale.png", gray)
#         print("Assignment Complete...")
#     else:
#         print("Colud not convert to grayScale")

# else:
#     print("Colud not load the image")


