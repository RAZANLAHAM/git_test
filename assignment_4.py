import cv2

# Q1
path = "imgprocessing_test.png"
image = cv2.imread(path)
cv2.imshow("image", image)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("gray",gray)
cv2.imwrite("gray.png",gray)

cv2.waitKey(0)
cv2.destroyAllWindows()


