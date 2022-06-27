import cv2 as cv

img = cv.imread("mama.jpg")

if(len(img.shape)<3):
    cv.imshow("Black and White.")
    cv.waitKey(0)
    cv.destroyAllWindows()
if(len(img.shape)==3):
    cv.imshow("dubu", img)
    cv.waitKey(0)
    cv.destroyAllWindows()

    print("ACCESS PIXEL:")
    x = int(input("X: "))
    y = int(input("Y: ")) 
    print("PIXEL VALUE: ",img[x,y],"\n")

    print("MODIFY PIXAL VALUES")
    green = input("green (0-255): ")
    red = input("red (0-255): ")
    blue = input("blue (0-255): ")
    print("\nBEFORE: ", img[x, y])
    img.itemset((x, y, 0), blue)
    img.itemset((x, y, 1), green)
    img.itemset((x, y, 2), red)
    print("AFTER: ", img[x, y])

    InDime = img.shape
    fixDime = (255, 255, 0)
    if(InDime[0]>=fixDime[0] and InDime[1]>=fixDime[1]):
        print("The image is within boundary.")
    else:
        print("The image is out of boundary.")

    if(img.size>98989899):
        print("The set pixel is lower than image total pixel count.")
    else:
        print("The set pixel is higher than image total pixel count.")

    print("Image Datatype: ", img.dtype,"\n")