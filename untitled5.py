# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 02:33:34 2020

@author: lenovo
"""


from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from  matplotlib.animation import FuncAnimation

plt.style.use('seaborn')
 
  


index = count()

def animate(i):
 x=[] 
y1 =[]
y2 =[]
data = pd.read_csv('data.csv')
x = data['x_value'] 
y1 = data['total_1'] 
y2 = data['total_2'] 
fig, (ax1, ax2) = plt.subplots(nrows=2, ncols=1)
ax1.cla()
ax2.cla()
ax1.plot(x,y1, label='st signal')

ax2.plot(x,y2, label='21st signal')


ax1.legend(loc='upper left')
ax2.legend(loc='upper left')
plt.tight_layout()
ax1.set_title('Median Salary (USD) by Age')
ax1.set_xlabel('Age')
ax1.set_ylabel('Median Salary')

ax2.set_title('Median Salary (USD) by Age')
ax2.set_xlabel('Age')
ax2.set_ylabel('Median Salary')
     
ani = FuncAnimation(plt.gcf(), animate, interval=10)

plt.tight_layout()
plt.show()


 