
import tkinter
from pathlib import Path
import re
import sys
from PIL import ImageGrab
import time
#from popup import popup_result,popup_log

from Zap_AllIterartionData import PrintIterationData


def maxMinAvg(frame1,defaultStepsDetail,CA_SequnceStepsDetail,MW_SequnceStepsDetail,minMaxAvgforDefaultStep,minMaxAvgforCA,MWsequence,timeElapseWithDefaultStep,timeElapseforCA,deltaTimeWithDefaultStep,deltaTimeWithCA,tpDetail):
     
    for i in frame1.winfo_children():
        i.destroy()
    if len(timeElapseWithDefaultStep)==0:
        return
    
    labelname=tkinter.Label(frame1, text="* Total number of samples: "+str(len(timeElapseWithDefaultStep)), font=("Arial",14,'bold'), fg="black",anchor='w').place(x=0, y=650)

    labelname=tkinter.Label(frame1, text="* Time calculated in seconds", font=("Arial",14,'bold'), fg="black",anchor='w').place(x=0, y=685)
    
    
    color=['#87f1ff','#6af0e8','#64ecc7','#77e69f','#95dc73']
    color1=['#003f5c','#665191','#ffa600']
    col='#f0edff'
    DarkGrey='#800080'
    buttonColor='#1500b9'

    tkinter.Label(frame1,text='Channel change '+str(tpDetail),font=("Arial",16,'bold'),fg="white",width=100,bg=DarkGrey).place(x=180, y=20, width=500)
    printButton=tkinter.Button(frame1, text="Iterations Data", font=("Arial", 16), fg="white", bg=buttonColor,command=lambda:PrintIterationData(defaultStepsDetail,CA_SequnceStepsDetail,MW_SequnceStepsDetail,timeElapseWithDefaultStep,timeElapseforCA,deltaTimeWithDefaultStep,deltaTimeWithCA)).place(x=950, y=670)
    
    #printButton=tkinter.Button(frame1, text=, font=("Arial", 16), fg="white", bg=DarkGrey,command=lambda:PrintIterationData(result,defaultStepsDetail)).place(x=850, y=380)
    e = tkinter.Label(frame1, text="Starting and Ending points", width=50,  fg="white", bg=DarkGrey, font=('Arial',16,'bold')).place(x=180, y=70, width=370)
    e = tkinter.Label(frame1, text="Max", width=50, fg="white", bg=DarkGrey, font=('Arial',16,'bold')).place(x=610, y=70, width=100)
    e = tkinter.Label(frame1, text="Min", width=50,  fg="white", bg=DarkGrey, font=('Arial',16,'bold')).place(x=710, y=70, width=100)
    e = tkinter.Label(frame1, text="Avg", width=50, fg="white", bg=DarkGrey, font=('Arial',16,'bold')).place(x=810, y=70, width=100)
    m=610
    n=100
    xaxiForinpu=180
    yaxiForinpu=100
    for i in range(0,len(defaultStepsDetail)-1):
         
        e = tkinter.Label(frame1, text=defaultStepsDetail[i], fg="black",bg=col ,font=('Arial',16),anchor="w").place(x=xaxiForinpu, y=yaxiForinpu, width=370) 
        yaxiForinpu+=35

    e = tkinter.Label(frame1, text="CA sequence", width=50,  fg="white", bg=DarkGrey, font=('Arial',16,'bold'),anchor="w").place(x=180, y=yaxiForinpu, width=370)
    yaxiForinpu+=35
    for i in range(0,len(CA_SequnceStepsDetail)):
         e = tkinter.Label(frame1, text=CA_SequnceStepsDetail[i], fg="black",bg=col ,font=('Arial',16),anchor="w").place(x=xaxiForinpu, y=yaxiForinpu, width=370)
         yaxiForinpu+=35

 
    e = tkinter.Label(frame1, text="Middleware sequence", width=50,  fg="white", bg=DarkGrey, font=('Arial',16,'bold'),anchor="w").place(x=180, y=yaxiForinpu, width=370)    
    yaxiForinpu+=35  

    for i in range(0,len(MW_SequnceStepsDetail)):
         if i<len(MW_SequnceStepsDetail)-1:
            e = tkinter.Label(frame1, text=MW_SequnceStepsDetail[i], fg="black",bg=col ,font=('Arial',16),anchor="w").place(x=xaxiForinpu, y=yaxiForinpu, width=370)
         else:
            e = tkinter.Label(frame1, text=MW_SequnceStepsDetail[i], fg="black",bg=col ,font=('Arial',16,'bold'),anchor="w").place(x=xaxiForinpu, y=yaxiForinpu, width=370)
         yaxiForinpu+=35      
           
         
    for j in range(0,len(minMaxAvgforDefaultStep)-1):
            
        e = tkinter.Label(frame1, text=minMaxAvgforDefaultStep[j][0], width=10,fg="black",bg=col , font=('Arial',16)).place(x=m, y=n, width=100)
           
        e = tkinter.Label(frame1, text=minMaxAvgforDefaultStep[j][1], width=10,fg="black",bg=col , font=('Arial',16)).place(x=m+100, y=n, width=100)
           
        e = tkinter.Label(frame1, text=minMaxAvgforDefaultStep[j][2], width=10,fg="black",bg=col , font=('Arial',16)).place(x=m+200, y=n, width=100)
           
           
        n+=35
    e = tkinter.Label(frame1, text="Max", width=50,  fg="white", bg=DarkGrey, font=('Arial',16,'bold')).place(x=m, y=n, width=100)
    e = tkinter.Label(frame1, text="Min", width=50,  fg="white", bg=DarkGrey, font=('Arial',16,'bold')).place(x=m+100, y=n, width=100)
    e = tkinter.Label(frame1, text="Avg", width=50,  fg="white", bg=DarkGrey, font=('Arial',16,'bold')).place(x=m+200, y=n, width=100)
    n+=35
   
    for j in range(0,len(minMaxAvgforCA)-1):
            
        e = tkinter.Label(frame1, text=minMaxAvgforCA[j][0], width=10,fg="black",bg=col , font=('Arial',16)).place(x=m, y=n, width=100)
           
        e = tkinter.Label(frame1, text=minMaxAvgforCA[j][1], width=10,fg="black",bg=col , font=('Arial',16)).place(x=m+100, y=n, width=100)
           
        e = tkinter.Label(frame1, text=minMaxAvgforCA[j][2], width=10,fg="black",bg=col , font=('Arial',16)).place(x=m+200, y=n, width=100)

        n+=35
    e = tkinter.Label(frame1, text="Max", width=50,  fg="white", bg=DarkGrey, font=('Arial',16,'bold')).place(x=m, y=n, width=100)
    e = tkinter.Label(frame1, text="Min", width=50,  fg="white", bg=DarkGrey, font=('Arial',16,'bold')).place(x=m+100, y=n, width=100)
    e = tkinter.Label(frame1, text="Avg", width=50,  fg="white", bg=DarkGrey, font=('Arial',16,'bold')).place(x=m+200, y=n, width=100)
    n+=35
    
    for j in range(0,len(MWsequence)):
        if j<len(MWsequence)-1:    
           e = tkinter.Label(frame1, text=MWsequence[j][0], width=10,fg="black",bg=col , font=('Arial',16)).place(x=m, y=n, width=100)
           
           e = tkinter.Label(frame1, text=MWsequence[j][1], width=10,fg="black",bg=col , font=('Arial',16)).place(x=m+100, y=n, width=100)
           
           e = tkinter.Label(frame1, text=MWsequence[j][2], width=10,fg="black",bg=col , font=('Arial',16)).place(x=m+200, y=n, width=100)
        else:
           e = tkinter.Label(frame1, text=MWsequence[j][0], width=10,fg="black",bg=col , font=('Arial',16,'bold')).place(x=m, y=n, width=100)
           
           e = tkinter.Label(frame1, text=MWsequence[j][1], width=10,fg="black",bg=col , font=('Arial',16,'bold')).place(x=m+100, y=n, width=100)
           
           e = tkinter.Label(frame1, text=MWsequence[j][2], width=10,fg="black",bg=col , font=('Arial',16,'bold')).place(x=m+200, y=n, width=100)   
           
        n+=35
         
    return 

            
           
              

      
   
     






























