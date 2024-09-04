import matplotlib 
from matplotlib import pyplot as plt

x = [1, 2, 3, 4, 5]
y = [10, 4, 30, 16, 50]
x2 = [1, 2, 3, 4, 5]
y2 = [8, 12, 25, 18, 45]  # Different values for the second line

plt.plot(x, y, 'r', label='Line 1')   # Red line
plt.plot(x2, y2, 'g', label='Line 2')  # Green line
plt.plot(x, y, 'ro')    # Red dots
plt.plot(x2, y2, 'go')  # Green dots

plt.title("Graph")
plt.xlabel("Order")
plt.ylabel("Count")
plt.legend()  # Adding a legend to differentiate the lines
plt.show()
 