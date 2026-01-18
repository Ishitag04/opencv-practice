import cv2

name = input("Enter the path of the file to open : ")

image = cv2.imread(name)

if image is None:
    print("Cannot load the image")
else:
    print("Image loaded successfully")
    cv2.imshow("Original", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    n = input("Enter :\n1. To draw a line\n2. To draw a rectangle\n3. To draw a circle\n4. To add a text\n")
    if n=="1":
        x1, y1 = map(int, input("Enter the value of pt1 (x1, y1) : ").split())
        x2, y2 = map(int, input("Enter the value of pt1 (x2, y2) : ").split())
        pt1 = (x1,y1)
        pt2 = (x2,y2)
        cv2.line(image, pt1, pt2, (0,255,0), 4)
        cv2.imshow("After line",image)
    elif n=="2":
        x1, y1 = map(int, input("Enter the value of pt1 (x1, y1) : ").split())
        x2, y2 = map(int, input("Enter the value of pt1 (x2, y2) : ").split())
        pt1 = (x1,y1)
        pt2 = (x2,y2)
        cv2.rectangle(image, pt1, pt2, (0,255,0), 4)
        cv2.imshow("After rectangle",image)
    elif n=="3":
        x, y = map(int, input("Enter the value of center (x, y) : ").split())
        r = int(input("Enter the value of radius : "))
        center = (x,y)
        cv2.circle(image, center, r, (0,255,0), 4)
        cv2.imshow("After circle",image)
    elif n=="4":
        text = input("Enter the text to show on the image : ")
        x,y = map(int, input("Enter the value of pt(x,y) from where you want to start the text : ").split())
        org = (x,y)
        cv2.putText(image, text, org, cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,0), 4)
        cv2.imshow("After text", image)
    else:
        print("Invalid option")

    if n in ["1", "2", "3", "4"]:
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        x = input("Do you want to save the edited image(1-Yes and 0-No) : ")
        if(x=="1"):
            updated = cv2.imwrite("../Phase3/Assignment_updated_img.png", image)
            if updated:
                print("Image saved successfully")
            else:
                print("Cannot save the same")
        
print("Assignment complete...")