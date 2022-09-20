from time import time
import tkinter
import threading
from tkinter import ttk
import tkinter.filedialog as filedialog
import re
import time
from msgBox import errorMsgOpenFile,errorMsgInputFile

from BootTime_backend import calculateBootTimeForEachstep
from BootTime_All_IterationData import PrintIterationData
from BootTime_MaxMinAvg import printData
from graph import plot

buttonColor='#1500b9'
def BootTime(Data,filename):

    
    #define arrys to store the data
    minMaxAvgOfBootData=[]
    bootupDataforEverystep=[]
    totalBootUpTime=[]
    bootUpSteps=["Boot to kernel init                                                    ","Kernel init to HAL Initialization                                       ","Time taken for HAL init                                                 ","HAL Initialization done to VM start                                    ","VM Start to first video frame                                         ","Total bootup time                                                     "]   
    bootSteps=["Boot to kernel init","Kernel init to HAL Initialization","Time taken for HAL init","HAL Initialization done to VM start","VM Start to first video frame","Total bootup time"]
    Airtel=["Debu to done","done to Hello URT","Hello URT to  IMW directories"," IMW directories: to first video frame","Total bootup time"]

  #  print(Data)
    try:
       checkForCorrectFile=calculateBootTimeForEachstep(Data,bootupDataforEverystep,minMaxAvgOfBootData,totalBootUpTime,bootSteps,filename)
    except:
        print('Issue in calling the function')
    
    def threadBoot(lock):
        lock.acquire()
        print('Working')
        print(len(totalBootUpTime))
        plot(totalBootUpTime,filename.split('_')[1])
        print("returnning back")
        time.sleep(2)
        lock.release()

    lock=threading.Lock()
    x=threading.Thread(target=threadBoot,args=(lock,))
    x.setDaemon(True)
    x.start()
    x.join()
    print("Mohammad...................")
    return
    
    
    
    

    
    
    """ button=tkinter.Button(frame, text="Print Graph", font=("Arial", 16), fg="white", bg=buttonColor, command=lambda:plot(frame1,totalBootUpTime)).place(x=470, y=130)
    
    
    button=tkinter.Button(frame, text="SummaryOfData", font=("Arial", 16), fg="white", bg=buttonColor, command=lambda:printData(frame1,bootupDataforEverystep,bootUpSteps,minMaxAvgOfBootData,totalBootUpTime)).place(x=600, y=130) """   



    #printAllIterationButton=tkinter.Button(window, text="All iterations data", font=("Arial", 14), fg="white", bg="#856ff8", command=submitPopup).place(x=570, y=240)


    #table
    #Statement=tkinter.Label(window, text="Title", font=("Arial",10), bg="white").place(x=100, y=270)
    





