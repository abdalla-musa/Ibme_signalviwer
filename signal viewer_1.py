# -*- coding: utf-8 -*-
"""
Created on Mon Dec 21 00:02:46 2020

@author: lenovo
"""

import matplotlib.pyplot as plt
import pandas as pd
plt.style.use('seaborn')
data= pd.read_csv('samples.csv')
x = data['seconds'] 
y1 = data['uv'] 
plt.ion()
j=1
i=1
q=len(x)
w=[]
f=[]
while True:
   plt.cla()
   for i in range(q): 
    # plt.gca().cla() # optionally clear axes
    plt.cla()
    w.append((x[i]))
    f.append((y1[i]))
    plt.plot(w,f)
    line,= plt.plot(w,f)
    plt.draw() 
    plt.pause(0.1)
    
    plt.legend(handles = [line], 
               labels  = ['1st signal']) 
    plt.title('It is demo')
    plt.tight_layout()
   plt.show()
   
   


