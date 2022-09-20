
import tkinter
import re
import sys
from msgBox import errorMsgPatternDataNotFound
from PIL import ImageGrab
import time

def summary(frame1,summaryOfData,summaryOfDataMemory,summaryOfDatajvmFree,jvmDataLength,CpuMemLength,everySample,totalBoxRunningTime):
    
    if len(summaryOfData)==0:
        errorMsgPatternDataNotFound()
        return

    for i in frame1.winfo_children():
        i.destroy()
    
    
    #printButton1=tkinter.Button(frame1, text="click here", font=("Arial", 16), fg="black", bg=DarkGrey,command=lambda:onclick(result)).place(x=500, y=20)
    

    col='#f0edff'
    DarkGrey='#800080'
    buttonColor='#1500b9'
    #printButton=tkinter.Button(frame1, text=, font=("Arial", 16), fg="black", bg=DarkGrey,command=lambda:PrintIterationData(result,inpu)).place(x=850, y=380)
    headingArray=['CPU utilization','Free System memory','Free heap memory']
    tag=['%CPU','MB','MB']
    default=['NA','NA','NA']
    if len(summaryOfData)==0:
        summaryOfData=default
        summaryOfDataMemory=default
    
    if len(summaryOfDatajvmFree)==0:
        summaryOfDatajvmFree=copy.copy(default)
    n=20
    for i in range(0,3):
        e = tkinter.Label(frame1, text=headingArray[i], width=30,  fg="white", bg=DarkGrey, font=('Arial',16,'bold')).place(x=200, y=n, width=500)
        e = tkinter.Label(frame1, text=tag[i], width=50,  fg="white", bg=DarkGrey, font=('Arial',16,'bold')).place(x=650, y=n, width=200)
        e = tkinter.Label(frame1, text="Minimum", width=50, fg="black", bg=col, font=('Arial',16,'bold')).place(x=200, y=n+40, width=500)
        e = tkinter.Label(frame1, text="Maximum", width=50,  fg="black", bg=col, font=('Arial',16,'bold')).place(x=200, y=n+80, width=500)
        e = tkinter.Label(frame1, text="Average", width=50, fg="black", bg=col, font=('Arial',16,'bold')).place(x=200, y=n+120, width=500)
        n+=160

    
   
    n=60
    for i in range(len(summaryOfData)):
        e = tkinter.Label(frame1, text=summaryOfData[i], width=50, fg="black", bg=col, font=('Arial',16,'bold')).place(x=650, y=n, width=200)
        n+=40
    n+=40
   
    for i in range(len(summaryOfDataMemory)):
        e = tkinter.Label(frame1, text=summaryOfDataMemory[i], width=50, fg="black", bg=col, font=('Arial',16,'bold')).place(x=650, y=n, width=200)
        n+=40
    n+=40
    for i in range(len(summaryOfDatajvmFree)):
        e = tkinter.Label(frame1, text=summaryOfDatajvmFree[i], width=50, fg="black", bg=col, font=('Arial',16,'bold')).place(x=650, y=n, width=200)
        n+=40

    labelname=tkinter.Label(frame1, text="* Total running time of the box in seconds: "+str(totalBoxRunningTime)+", Each sample taken after every "+str(everySample)+"sec", font=("Arial",16,'bold'), fg="black", width="70",anchor="w").place(x=200, y=n)
    labelname=tkinter.Label(frame1, text="* Total number of samples for CPU and System Memory: "+str(CpuMemLength), font=("Arial",16,'bold'), fg="black", width="50",anchor="w").place(x=200, y=n+40)
    labelname=tkinter.Label(frame1, text="* Total number of samples for heap size: "+str(jvmDataLength), font=("Arial",16,'bold'), fg="black", width="40",anchor="w").place(x=200, y=n+80)
    time.sleep(5)
    def getter():
        x0 = frame1.winfo_rootx()
        y0 = frame1.winfo_rooty()
        x1 = x0 + frame1.winfo_width()
        y1 = y0 + frame1.winfo_height()
        
        ImageGrab.grab().crop((x0, y0, x1, y1)).save(r"C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\SummaryOfCPUMemoryJVM.jpg")

    getter()
    return 
    





























