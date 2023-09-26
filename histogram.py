import cv2
import matplotlib.pyplot as plt
path = "imgprocessing_test.png"
image = cv2.imread(path, 0)
# hist_test = cv2.calcHist(image, [0], None, [256], ranges=[0,256])
hist_test = cv2.calcHist(image, [0], None, [256], ranges=[0, 256])
plt.plot(hist_test)
plt.show()
image_2 = cv2.equalizeHist(image)
plt.plot(image_2)
plt.show()
cv2.imshow("fig", image_2)
cv2.imshow("fig_2", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
