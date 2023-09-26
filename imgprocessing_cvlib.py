import cv2


# cv2.imread("filepath",flag) --> flag : specifies the way how the img should be read
# IMREAD():READ THE IMG COLOUR AS IT IS || IMREAD_COLOURS(1) ||
# IMREAD_GRAYSCALE(0)
# IMREAD_UNCHANGED(-1)

#  load the image --> imread()
path = "imgprocessing_test.png"
image = cv2.imread(path,-1)
image_1 = cv2.imread("img.jpg",0)

# get the dim (height,width,chann)
dim = image.shape
print(dim)

#  Display the image --> imshow() method
cv2.imshow("image proccessing " , image)
cv2.imshow("img_1", image_1)

print(type(image))
# print(image)    nmpy array

# resizing
imageResized = cv2.resize(image,(400,200)) # width comes first
cv2.imshow("image resized",imageResized)
dimResized = imageResized.shape
print(dimResized)  # (height,width)

# cropping
imgCropped = image[0:200 , 0:400]        #height comes first
cv2.imshow("cropped img ",imgCropped)
print("size after cropp ",imgCropped.shape)

# to save the cropped & resized imgs --> imwrite("imgname.ecxu",image var)
cv2.imwrite("resized.png",imageResized)
cv2.imwrite("cropped.png",imgCropped)

# to convert between many systems(RGB , GRAY ,BGR ...)
grayimg = cv2.cvtColor(image,cv2.COLOR_Luv2RGB)                           # -->IMPORTANT
cv2.imshow("gray",grayimg)

#  wait for the user to press key
cv2.waitKey(0)

# close all windows
cv2.destroyAllWindows()
