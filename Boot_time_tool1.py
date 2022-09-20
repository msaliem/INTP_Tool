import Tkinter
import ttk
import tkFileDialog as filedialog
import re
import sys
from submit import submitbtn
from popup import popup_result,popup_log
#from examplePlot import histogram
from allIterationData import PrintIterationData

window=Tkinter.Tk()
window.title("Boot time analysis tool")
window.geometry("1280x900") 
#set window color
window.configure(bg="gray") 
#btn=StringVar()
total=[]
result=[]
inpu=["Boot start to starting kernel","Starting kernel to HAL Initialization start","HAL Initialization start to HAL Initialization done","HAL Initialization done to VM start","VM Start to first frame","Total bootup time"]
inpu1=["Boot start to kernel","Kernel to HAL init","HAL Init to HAL done","HAL Init done to VM","VM to firstFrame","Total bootup time"]

totalBootUpTime=[]

#Container
container=Tkinter.LabelFrame(window,padx=10,pady=10,width=1150,height=200, bg="white", fg="purple", highlightthickness=3, highlightbackground="gray85")
container.pack()

frame=Tkinter.LabelFrame(container,text="  User Input Information  ",font=('Arial',12,'bold'),padx=10,pady=0,width=1150,height=200, bg="white", fg="purple")
frame.pack()

frame1=Tkinter.LabelFrame(container,text="  Calculated Data  ",font=('Arial',12,'bold'),padx=10,pady=20,width=1150,height=400, bg="white", fg="purple")
frame1.pack()
def printData():
    #canvas.create_rectangle(45,0,660,900,fill='red')
    if len(result)==0:
       popup_result()
       return
    printButton=Tkinter.Button(frame1, text="PrintAllData", font=("Arial", 16), fg="white", bg="purple",command=lambda:PrintIterationData(result,inpu)).place(x=850, y=380)
    labelname=Tkinter.Label(frame1, text="Total number of iteration are "+str(len(result)), font=("Arial",14,'bold'), fg="black", bg="gray85", width="80").place(x=0, y=20)
    e = Tkinter.Label(frame1, text="Starting and Ending points", width=50,  fg="white", bg="purple", font=('Arial',16,'bold')).place(x=50, y=80, width=600)
    e = Tkinter.Label(frame1, text="Max (ms)", width=50, fg="white", bg="purple", font=('Arial',16,'bold')).place(x=700, y=80, width=100)
    e = Tkinter.Label(frame1, text="Min", width=50,  fg="white", bg="purple", font=('Arial',16,'bold')).place(x=800, y=80, width=100)
    e = Tkinter.Label(frame1, text="Avg", width=50, fg="white", bg="purple", font=('Arial',16,'bold')).place(x=900, y=80, width=100)
    m=700
    n=120
    xaxiForinpu=50
    yaxiForinpu=120
    for i in range(0,len(inpu)):
         if i<len(inpu)-1:
             e = Tkinter.Label(frame1, text=inpu[i], fg="black",bg="gray85" ,font=('Arial',16)).place(x=xaxiForinpu, y=yaxiForinpu, width=600) 
         else:
             e = Tkinter.Label(frame1, text=inpu[i], fg="black", bg="gray85" ,font=('Arial',16,'bold')).place(x=xaxiForinpu, y=yaxiForinpu, width=600)
        
           
         yaxiForinpu+=40
    for j in range(0,len(total[0])):
            if j<len(total[0])-1: 
               e = Tkinter.Label(frame1, text=total[0][j], width=10,fg="black",bg="gray85" , font=('Arial',16)).place(x=m, y=n, width=100)
           
               e = Tkinter.Label(frame1, text=total[1][j], width=10,fg="black",bg="gray85" , font=('Arial',16)).place(x=m+100, y=n, width=100)
           
               e = Tkinter.Label(frame1, text=total[2][j], width=10,fg="black",bg="gray85" , font=('Arial',16)).place(x=m+200, y=n, width=100)
           
           
               n+=40
            else:
               e = Tkinter.Label(frame1, text=total[0][j], width=10,fg="black", bg="gray85" , font=('Arial',16,'bold')).place(x=m, y=n, width=100)
           
               e = Tkinter.Label(frame1, text=total[1][j], width=10,fg="black", bg="gray85" , font=('Arial',16,'bold')).place(x=m+100, y=n, width=100)
           
               e = Tkinter.Label(frame1, text=total[2][j], width=10,fg="black", bg="gray85" , font=('Arial',16,'bold')).place(x=m+200, y=n, width=100)
           
           
               n+=40


            
           
               print inpu[j]," ",total[0][j],"      ",total[1][j],"        ",total[2][j]
               print "-----------------------------------------------------------------------------------------------------------"

      
   
    print "\n\n_______________________________________________\n"
    print "Data of each iterarion starting from 1-----"
    print "\n__________________________________________________\n\n\n"

    for i in range(0,len(result)):
        print "\n***************************************"
        print "* ITERATION",i+1,"                        *"
        print "***************************************\n"
        for j in range(0,len(result[0])):
            print inpu[j],result[i][j]
            print "-----------------------------------------------------------------------------------|"    

#upload file
filename=""
def UploadAction(event=None):
    
    filename = filedialog.askopenfilename()
    File=filename.split("/")[-1]
    e=Tkinter.Label(frame, text=File,fg="purple", font=("Arial",14),bg="white").place(x=400, y=25)
    button=Tkinter.Button(frame, text="Submit", font=("Arial", 16), fg="white", bg="purple", command=lambda:submitbtn(filename,result,total,totalBootUpTime)).place(x=370, y=135)
   # return filename
    
#creating label
#labelname=Tkinter.Label(frame, text="Log Generator", font=("Arial",20,'bold'), fg="white",bg="purple",width="65").place(x=50, y=20)
ufile=Tkinter.Label(frame, text="Choose file",fg="purple", font=("Arial",16), bg="white").place(x=30, y=20)
project=Tkinter.Label(frame, text="Select Project",fg="purple", font=("Arial",16), bg="white").place(x=30, y=80)

# List
n = Tkinter.StringVar()
projectname = ttk.Combobox(window,text="Plese select Project", width = "16", textvariable = n)
projectname['values'] = (' Airtel', 
                          ' TataSky',
                          ' Sphinx & Griffin')

projectname.place(x=280, y=110)
projectname.current()

#creating button
opentbn =Tkinter.Button(frame, text="Open",font=("Arial",16), width="10", command=UploadAction).place(x=230, y=20)  
printButton=Tkinter.Button(frame, text="PrintApproximatData", font=("Arial", 16), fg="white", bg="purple", command=printData).place(x=490, y=141)
printButton=Tkinter.Button(frame, text="PrintGraph", font=("Arial", 16), fg="white", bg="purple", command=lambda:histogram(totalBootUpTime)).place(x=730, y=142)

window.mainloop()
