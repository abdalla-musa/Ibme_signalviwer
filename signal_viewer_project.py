# -*- coding: utf-8 -*-
"""
Created on Wed Dec 23 02:36:23 2020

@author: Enj.Ammar
"""
  
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextDocumentLayout, QWidget, QInputDialog, QLineEdit, QFileDialog
import sys
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from itertools import count
import random
import numpy as np
from numpy.fft import fft,fftfreq,ifft
import pandas as pd
import os
import struct
import sys
import time
import scipy
from scipy import signal
 

 
running = 1
w=[]
f=[]

index = count()


class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__()
        self.initUI()


    def b1_clicked(self):
        print("start")
        if next(index)%2  == 0:
            self.b1.setText("close")
        else:
            plt.close()
            self.b1.setText("open")



    def b2_clicked(self):
        print("fft")
        fig, ax1 = plt.subplots()
        
       # a=fft(w)
        b=ifft(f)
    
        ax1.plot(b,label='this is fourier transform')
        plt.legend(loc='upper left')
        plt.tight_layout()
        plt.show()  
        


    def b3_clicked(self):
        print("browse function")
        filename = QFileDialog.getOpenFileName()
        path = filename[0]
        print(path)
        self.open_dialog_box(path)


        with open(path, "r") as f:
            print(f.readline())
        
    
    def b4_clicked(self):
        print("stop function")
        self.stop()
    
    def b5_clicked(self):
        print("resume fuction")
        self.resume()
    
        
        
    
    def b6_clicked(self):
        print("zoom function")
        self.close()
        
    def open_dialog_box(self,path):
        
        plt.style.use('seaborn')
        data= pd.read_csv(path)
        x = data['seconds'] 
        y1 = data['uv'] 
        plt.ion()
        j=1
        i=1
        q=len(x)
        
        plt.cla()
        while running ==1: 
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
                i=i+1
                
                self.b4.clicked.connect(self.stop)
                self.b5.clicked.connect(self.resume)
                    
                
                
                
    
    

        
    
    def stop(self):
        global running
        running=0
        
    def resume(self):
        global running
        running=1

                
        
        
        
        
    

    
        
          
            
            
            
            
    def initUI(self):
        self.setGeometry(200, 200, 300, 300)
        self.setWindowTitle("signal viewer")


        self.b1 = QtWidgets.QPushButton(self)
        self.b1.move(0,10)
        self.b1.setText("start the signal")
        self.b1.clicked.connect(self.b1_clicked)


        self.b2 = QtWidgets.QPushButton(self)
        self.b2.move(0,60)
        self.b2.setText("fourier transform")
        self.b2.clicked.connect(self.b2_clicked)


        self.b3 = QtWidgets.QPushButton(self)
        self.b3.move(180,35)
        self.b3.setText("Browse")
        self.b3.clicked.connect(self.b3_clicked)
        
        
        self.b4 = QtWidgets.QPushButton(self)
        self.b4.move(0,90)
        self.b4.setText("Stop")
        self.b4.clicked.connect(self.b4_clicked)
        
        
        self.b5 = QtWidgets.QPushButton(self)
        self.b5.move(0,120)
        self.b5.setText("Resume")
        self.b5.clicked.connect(self.b5_clicked)
        
        self.b6 = QtWidgets.QPushButton(self)
        self.b6.move(0,150)
        self.b6.setText("Exit")
        self.b6.clicked.connect(self.b6_clicked)
        
        



def window():
    app = QApplication(sys.argv)
    win = MyWindow()
    win.show()
    sys.exit(app.exec_())

window()


