import matplotlib.pyplot as plt
# data since using matplotlib lib
x= [1,4,5,7,8]
y = [2,6,3,6,8]
plt.scatter(x,y)
plt.show()
plt.plot(x,y)
plt.show() # when I want to show any pic I have use this func
# putting title to the fig :
# the concept is every fig will have a name in run time
plt.figure("one")
plt.step(x,y)
plt.show()
plt.figure("two")
plt.scatter(x,y)
plt.show()
# the two figures will drae in the same plot(togother)
plt.step(x,y)
plt.plot(x,y)
plt.show()
