import matplotlib.pyplot as plt

xlist = [21,0,763,474,335,6,54,48,29,0]
ylist = ['bazz','gazz','hazz','mazz','chazz','dazz','cazz','lazz','razz','nazz']

plt.xlabel('This is X')
plt.ylabel("This is Y")

plt.title('This is my Plot')

plt.plot(xlist,ylist)

plt.show()