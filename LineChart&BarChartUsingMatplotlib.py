#Note for installing Matplotlib Library Run this command in terminal: pip install matplotlib

import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,8,6,4,2]
plt.plot(x,y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Chart')
plt.show()

x=['A','B','C','D','E']
y=[10,8,6,4,2]
plt.bar(x,y)
plt.xlabel('Categories')
plt.ylabel('Values')
plt.title('Bar Chart')
plt.show()

                            #Output Error