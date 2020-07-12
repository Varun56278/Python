import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')
x=[1,2,3]
y=[5,7,6]

x2=[6,9,5]
y2=[8,6,7]
plt.plot(x,y,'g',label='Line One',  linewidth = 4)
plt.plot(x2,y2,'c',label='Line Two', linewidth = 4)
plt.title('Sachin')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.legend()
plt.grid(True, color='k')
plt.show()













import matplotlib.pyplot as plt
plt.plot([1,2,3],[4,5,7])
plt.plot([1,4,3],[8,5,2])
plt.title('Sachin')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.show()
