import tkinter
import tkinter.filedialog as filedialog
import re
import sys
from performanceCPUMemJVM import performanceCal
from msgBox import errorMsgInputFile,errorMsgInputFile

def CPU_util(Data,filename):
  
    
    

    

    print('Performance......')
    performanceCal(Data,filename)
    """
   #upload file
    filename=""  
    def UploadAction(event=None):
    
        filename = filedialog.askopenfilename()
        printFileName=filename.split("/")[-1]
        if len(printFileName)==0:
            errorMsgInputFile()
            
        e=tkinter.Label(frame, text=printFileName,fg="purple", font=("Arial",14),bg="white",width="50",anchor='w').place(x=400, y=25)
        button=tkinter.Button(frame, text="Submit", font=("Arial", 16), fg="white", bg='#1500b9', command=lambda:performanceCal(frame,frame1,filename)).place(x=370, y=100)
        
        
    
    
    choosefile=tkinter.Label(frame, text="Choose file",fg="purple", font=("Arial",16), bg="white").place(x=30, y=20)
    

   

    #creating button
    opentbn =tkinter.Button(frame, text="Open",font=("Arial",16), width="10", command=UploadAction).place(x=230, y=20)    


    button=tkinter.Button(frame, text="Submit", font=("Arial", 16), fg="white", bg='#1500b9', command=errorMsgInputFile).place(x=370, y=100)
    """






