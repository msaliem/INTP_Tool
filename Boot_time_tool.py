import Tkinter
import ttk
import tkFileDialog as filedialog
import re
import sys
from submit import submitbtn
#from popup import popup_result,popup_log
from examplePlot import histogram
from allIterationData import PrintIterationData
from MaxMinAvg import printData
from graph import plot
from popup import onclick,submitPopup

window=Tkinter.Tk()
window.title("Tool")
window.geometry("1200x900") 
#window.attributes('-fullscreen',True)
#set window color
window.configure(bg="gray")


# create a toplevel menu  
menubar = Tkinter.Menu(window)  
menubar.add_command(label="Boot Time")  
menubar.add_command(label="Zapt time")
menubar.add_command(label="CPU utilization")
menubar.add_command(label="Memory utilization")  
  
# display the menu  
window.config(menu=menubar) 


#btn=StringVar()
total=[]
result=[]
inpu=["Boot to kernel init","Kernel init to HAL Initialization","Time taken for HAL init","HAL Initialization done to VM start","VM Start to first video frame","Total bootup time"]
inpu1=["Boot start to kernel","Kernel to HAL init","HAL Init to HAL done","HAL Init done to VM","VM to firstFrame","Total bootup time"]

totalBootUpTime=[]


# Create A Main Frame
main_frame = Tkinter.Frame(window,width=50,height=50)
main_frame.pack(fill="both", expand=1)

# Create A Canvas
my_canvas = Tkinter.Canvas(main_frame)
my_canvas.pack(side="left", fill="both", expand=1)

# Add A Scrollbar To The Canvas
my_scrollbar = Tkinter.Scrollbar(main_frame, orient="vertical", command=my_canvas.yview)
my_scrollbar.pack(side="right", fill="y")

# Configure The Canvas
my_canvas.configure(yscrollcommand=my_scrollbar.set)
my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion = my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
second_frame = Tkinter.Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((5,10), window=second_frame)
#Container
container=Tkinter.LabelFrame(second_frame,padx=30,pady=20,width=1280,height=200, bg="white", fg="purple", highlightthickness=3, highlightbackground="gray85")
container.pack()

frame=Tkinter.LabelFrame(container,text="  User Input Information  ",font=('Arial',12,'bold'),padx=10,pady=10,width=1150,height=200, bg="white", fg="purple")
frame.pack()

frame1=Tkinter.LabelFrame(container,text="  Calculated Data  ",font=('Arial',12,'bold'),padx=13,pady=20,width=1150,height=430, bg="white", fg="purple")
frame1.pack()

frame2=Tkinter.LabelFrame(container,text="  Bar graph  ",font=('Arial',12,'bold'),padx=10,pady=20,width=1150,height=400, bg="white", fg="purple")
frame2.pack()




#upload file
filename=""
def UploadAction(event=None):
    
    filename = filedialog.askopenfilename()
    File=filename.split("/")[-1]
    e=Tkinter.Label(frame, text=File,fg="purple", font=("Arial",14),bg="white").place(x=400, y=25)
    button=Tkinter.Button(frame, text="Submit", font=("Arial", 16), fg="white", bg="purple", command=lambda:submitbtn(filename,result,total,totalBootUpTime,inpu,frame1,frame2)).place(x=370, y=135)
   # return filename
    
#creating label
#labelname=Tkinter.Label(frame, text="Log Generator", font=("Arial",20,'bold'), fg="white",bg="purple",width="65").place(x=50, y=20)
ufile=Tkinter.Label(frame, text="Choose file",fg="purple", font=("Arial",16), bg="white").place(x=30, y=20)
project=Tkinter.Label(frame, text="Select Project",fg="purple", font=("Arial",16), bg="white").place(x=30, y=80)

# List
n = Tkinter.StringVar()
projectname = ttk.Combobox(frame,text="Plese select Project", width = "16", textvariable = n)
projectname['values'] = (' Airtel', 
                          ' TataSky',
                          ' Sphinx & Griffin')

projectname.place(x=230, y=80)
projectname.current()

#creating button
opentbn =Tkinter.Button(frame, text="Open",font=("Arial",16), width="10", command=UploadAction).place(x=230, y=20)    


button=Tkinter.Button(frame, text="Submit", font=("Arial", 16), fg="white", bg="purple", command=submitPopup).place(x=370, y=135)



#printAllIterationButton=Tkinter.Button(window, text="All iterations data", font=("Arial", 14), fg="white", bg="#856ff8", command=submitPopup).place(x=570, y=240)


#table
#Statement=Tkinter.Label(window, text="Title", font=("Arial",10), bg="white").place(x=100, y=270)





window.mainloop()
