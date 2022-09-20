
import tkinter
import re
import sys
import time
from PIL import ImageGrab
from BootTime_All_IterationData import PrintIterationData
from graph import plot
from msgBox import errorMsgPatternDataNotFound



def printData(frame1,bootupDataforEverystep,bootUpSteps,minMaxAvgOfBootData,totalBootUpTime):
   
    
    if len(totalBootUpTime)==0:
        errorMsgPatternDataNotFound()
        return

    for i in frame1.winfo_children():
        i.destroy()
    col='#f0edff'
    
    
    e = tkinter.Label(frame1, text="Starting and Ending points", width=50,  fg="white", bg="purple", font=('Arial',16,'bold'),anchor="w").place(x=100, y=80, width=400)
    e = tkinter.Label(frame1, text="Max", width=50, fg="white", bg="purple", font=('Arial',16,'bold')).place(x=530, y=80, width=100)
    e = tkinter.Label(frame1, text="Min", width=50,  fg="white", bg="purple", font=('Arial',16,'bold')).place(x=630, y=80, width=100)
    e = tkinter.Label(frame1, text="Avg", width=50, fg="white", bg="purple", font=('Arial',16,'bold')).place(x=730, y=80, width=100)
    X_axisForBootUpData=530
    Y_axisForBootUpData=120
    X_axisForbootUpSteps=100
    Y_axisForbootUpSteps=120
    for i in range(0,len(bootUpSteps)):
         if i<len(bootUpSteps)-1:
             e = tkinter.Label(frame1, text=bootUpSteps[i], fg="black",bg=col ,font=('Arial',16),anchor="w").place(x=X_axisForbootUpSteps, y=Y_axisForbootUpSteps, width=400) 
         else:
             e = tkinter.Label(frame1, text=bootUpSteps[i], fg="black", bg=col ,font=('Arial',16,'bold'),anchor="w").place(x=X_axisForbootUpSteps, y=Y_axisForbootUpSteps, width=400)
        
           
         Y_axisForbootUpSteps+=40
    for j in range(0,len(minMaxAvgOfBootData[0])):
            if j<len(minMaxAvgOfBootData[0])-1: 
               e = tkinter.Label(frame1, text=minMaxAvgOfBootData[0][j], width=10,fg="black",bg=col , font=('Arial',16)).place(x=X_axisForBootUpData, y=Y_axisForBootUpData, width=100)
           
               e = tkinter.Label(frame1, text=minMaxAvgOfBootData[1][j], width=10,fg="black",bg=col , font=('Arial',16)).place(x=X_axisForBootUpData+100, y=Y_axisForBootUpData, width=100)
           
               e = tkinter.Label(frame1, text=minMaxAvgOfBootData[2][j], width=10,fg="black",bg=col , font=('Arial',16)).place(x=X_axisForBootUpData+200, y=Y_axisForBootUpData, width=100)
           
           
               Y_axisForBootUpData+=40
            else:
               e = tkinter.Label(frame1, text=minMaxAvgOfBootData[0][j], width=10,fg="black", bg=col , font=('Arial',16,'bold')).place(x=X_axisForBootUpData, y=Y_axisForBootUpData, width=100)
           
               e = tkinter.Label(frame1, text=minMaxAvgOfBootData[1][j], width=10,fg="black", bg=col , font=('Arial',16,'bold')).place(x=X_axisForBootUpData+100, y=Y_axisForBootUpData, width=100)
           
               e = tkinter.Label(frame1, text=minMaxAvgOfBootData[2][j], width=10,fg="black", bg=col , font=('Arial',16,'bold')).place(x=X_axisForBootUpData+200, y=Y_axisForBootUpData, width=100)
           
           
               Y_axisForBootUpData+=40


            
           
               

      
    

    labelname=tkinter.Label(frame1, text="* Total number of iteration : "+str(len(totalBootUpTime)), font=("Arial",16,'bold'), fg="black", width="30",anchor="w").place(x=100, y=400)
    labelname=tkinter.Label(frame1, text="* Time calculated in seconds", font=("Arial",16,'bold'), fg="black", width="30",anchor="w").place(x=100, y=440)
    

    printButton=tkinter.Button(frame1, text="All iteration Data", font=("Arial", 16), fg="white", bg="#1500b9",command=lambda:PrintIterationData(bootupDataforEverystep,bootUpSteps)).place(x=650, y=440)       
    
    
    time.sleep(10)
    def getter():
        x0 = frame1.winfo_rootx()
        y0 = frame1.winfo_rooty()
        x1 = x0 + frame1.winfo_width()
        y1 = y0 + frame1.winfo_height()
        
        ImageGrab.grab().crop((x0, y0, x1, y1)).save(r"C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\Boot_Data.jpg")

    getter()
       
    return





























