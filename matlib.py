# how to read,show an image using matplotlib library
# image processing field
import matplotlib.pyplot as plt
print(dir(plt))
plt.figure(figsize=(10,10)) # to print tho image in certine size
for i in range(20) :
  img_0 = plt.imread("img.jpg") # to show the image as a data (matrix)
  print(type(img_0))
  plt.subplot(5,4,i+1) # to add two images at the same time (nrows ncolums order)
  plt.title("test image") # to put a title on the img
  plt.axis("off") # to remove the x-y plan
  plt.imshow(img_0) # to show the image

# image 2 :
img_1 = plt.imread("cv.JPG")
print(type(img_1))
# plt.subplot(551)
plt.title("cv img")
plt.axis("off")
plt.imshow(img_1)
print(img_1.shape) # to determine the volume of the img (length,width,channels)

plt.show()
