from matplotlib import pyplot as plt
x=[1,2,3,4,5,6,7,8,9]
y=[10,2,3,6,4,9,7,4,2]
x2=[1,2,3,4,5,6,7,8,9]
y2=[2,4,7,9,5,3,8,10,2]

plt.subplot(2,1,1)
plt.title("Subplot 1")
plt.plot(x,y,'r')


plt.subplot(2,1,2)
plt.plot(x2,y2,'g')
plt.show()