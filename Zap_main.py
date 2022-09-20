import threading
import time
from tkinter import *
import tkinter
import tkinter.filedialog as filedialog
import re
import sys
from zap_backend import zapTimeCal
from graph import plotZapData
from Zap_minMaxAvg import maxMinAvg
import csv

from msgBox import errorMsgOpenFile, errorMsgInputFile,errorMsgInputFile

#btn=StringVar()
timeElapseWithDefaultStep=[]
timeElapseforCA=[]
deltaTimeWithDefaultStep=[]
deltaTimeWithCA=[]
Totalzaptime=[]
minMaxAvgforDefaultStep=[]
minMaxAvgforCA=[]
MWsequence=[]
defaultStepsDetail=["Start                 ->      Video Stop","Video Stop        ->      PMT request","PMT request      ->     PMT retrieved","PMT retrieved    ->     Video Start","Video Start        ->      First frame","Total zap time"]
CA_SequnceStepsDetail=["PMT retrieved   ->      CA Start","CA Start            ->      ECM filter","ECM filter         ->       ECM received","ECM received   ->      Key Set","Key Set           ->       First frame"]
MW_SequnceStepsDetail=["Start                 ->      Video Start    ","Start                 ->      Key Set        ","Zapping time                     "]


buttonColor='#1500b9'

def csvRead(fileName):
    dic={}
    try:
       with open(fileName,'r') as f:
            Data=csv.reader(f)

            next(Data)

            for i in Data:
                dic[i[0]]=[i[1],i[2]]
            f.close()
    except:
        return dic

    return dic
def zapTime(Data,filenameForZap):
    

    

    

    fileName=r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\zap_Usecase.csv'
    


    dic=csvRead(fileName)
    projectName=filenameForZap.split('_')[2]
    
    
    
    """
    #upload file
    filename=""
    def UploadAction():
        
        if channel.get() ==0 or Manual.get()==0:
           errorMsgOpenFile()
           return
        
        filename = filedialog.askopenfilename()
        File=filename.split("/")[-1]

        if len(File)==0:
            errorMsgInputFile()
            File='                                                                                                  '

        e=tkinter.Label(frame, text=File,fg="purple", font=("Arial",14),bg="white").place(x=400, y=40)
       
        button=tkinter.Button(frame, text="Submit", font=("Arial", 16), fg="white", bg=buttonColor, command=lambda:zapTimeCal(timeFromEach,timeFromEach1,deltaTime,deltaTime1,filename,frame,frame1,minMaxAvgforDefaultStep,minMaxAvgforCA,MWsequence)).place(x=390, y=90)
        return 
   # return filename
    
    #creating label
    #labelname=tkinter.Label(frame, text="Log Generator", font=("Arial",20,'bold'), fg="white",bg="purple",width="65").place(x=50, y=20)
    
    project=tkinter.Label(frame, text="Manual zaping",fg="purple", font=("Arial",16), bg="white").place(x=30, y=10)

    project=tkinter.Label(frame, text="Get the Data for",fg="purple", font=("Arial",16), bg="white").place(x=30, y=60)

    #Radio Buttons
    Manual=tkinter.IntVar()
    ChannelUp=tkinter.Radiobutton(frame, text="Yes", variable=Manual, value=1, font="bold").place(x=230, y=12)
    ChannelDown=tkinter.Radiobutton(frame, text="No", variable=Manual, value=2,font="bold").place(x=400, y=12)
    Channel=tkinter.IntVar()
    ChannelUp=tkinter.Radiobutton(frame, text="Channel Up", variable=Channel, value=1, font="bold").place(x=230, y=62)
    ChannelDown=tkinter.Radiobutton(frame, text="Channel Down", variable=Channel, value=2,font="bold").place(x=400, y=62)

    
    print("Working")
    #creating button
    ufile=tkinter.Label(frame, text="Choose file",fg="purple", font=("Arial",16), bg="white").place(x=30, y=40)
    button=tkinter.Button(frame, text="Submit", font=("Arial", 16), fg="white", bg=buttonColor, command=errorMsgInputFile).place(x=390, y=90)
    opentbn =tkinter.Button(frame, text="Open",font=("Arial",16), width="10", command=UploadAction).place(x=230, y=40)
    """  
    def threadZap(lock):
        lock.acquire()
        eachLogFile=Data.split('original LCN= 1111')
       # print(Data)
        i=0
        for row in dic:
            
            if len(eachLogFile)==1:
               print(dic[row])
               boolVar=zapTimeCal(timeElapseWithDefaultStep,timeElapseforCA,deltaTimeWithDefaultStep,deltaTimeWithCA,Data,minMaxAvgforDefaultStep,minMaxAvgforCA,MWsequence,defaultStepsDetail,CA_SequnceStepsDetail,MW_SequnceStepsDetail,Totalzaptime,dic[row],filenameForZap,row)
            else:
                boolVar=zapTimeCal(timeElapseWithDefaultStep,timeElapseforCA,deltaTimeWithDefaultStep,deltaTimeWithCA,eachLogFile[i],minMaxAvgforDefaultStep,minMaxAvgforCA,MWsequence,defaultStepsDetail,CA_SequnceStepsDetail,MW_SequnceStepsDetail,Totalzaptime,dic[row],filenameForZap,row)   
            if boolVar==False:
                i+=1
                continue
           # maxMinAvg(defaultStepsDetail,CA_SequnceStepsDetail,MW_SequnceStepsDetail,minMaxAvgforDefaultStep,minMaxAvgforCA,MWsequence,timeElapseWithDefaultStep,timeElapseforCA,deltaTimeWithDefaultStep,deltaTimeWithCA,row)
            print('Hi Mohammad........................................')
            plotZapData(Totalzaptime,projectName,row) 
           
            del timeElapseWithDefaultStep[:]
            del timeElapseforCA[:]
            del deltaTimeWithDefaultStep[:] 
            del deltaTimeWithCA[:]
            del Totalzaptime[:]
            del minMaxAvgforDefaultStep[:]
            del minMaxAvgforCA[:]
            del MWsequence[:]
            
            i+=1
            #print(eachLogFile[i])
          
        lock.release()
    lock=threading.Lock()
    x=threading.Thread(target=threadZap,args=(lock,))
    x.start()   
    x.join()
     
  






#printAllIterationButton=tkinter.Button(window, text="All iterations data", font=("Arial", 14), fg="white", bg="#856ff8", command=submitPopup).place(x=570, y=240)
#table
#Statement=tkinter.Label(window, text="Title", font=("Arial",10), bg="white").place(x=100, y=270)






