from tkinter import *
import tkinter
import tkinter.filedialog as filedialog
import re
import sys

def bootHelp():
    window=tkinter.Tk()
    window.title("Log Tool")
    window.geometry("1220x720")
    window.configure(bg="white")
   # l = tkinter.Label(window, text="Please check the log file pattern are not matching",font=("Arial",20,'bold'), fg="white", bg="purple", width="50").place(x=70, y=30)
    #l.grid(row=0, column=0)

    #b = tkinter.Button(window, text="Okay", command=window.destroy,font=("Arial", 16), fg="white", bg="purple").place(x=470, y=100)

    
# Create ANOTHER Frame INSIDE the Canvas
    #second_frame =tkinter.Frame(my_canvas)

# Add that New frame To a Window In The Canvas
    #my_canvas.create_window((0, 0), window=second_frame)
    
    string1="Boot Time Calculation\n"
    tkinter.Label(window, text=str(string1),font=("Arial",15,'bold'), bg="white", fg="purple").place(x=550, y=10)
    string="This tool will take log file of multiple boot iterations and process it and display the result in required format. \n Please follow below points to get the correct data \n 1. Open the custom -> vendor -> startup -> init.c\n   * Search for the main(\n   *Add the print statement before and after the HAL init function like in below format---\n    print(HAL initialization start from here)\n    MAIN_EXEC(hal_init())\n    print(HAL Initialization done)\n 2. Open the startIdwayj and add loggers---\n    -idwLogDrivers AV_EVT -idwLogLevel INFO \ \n"
    y1=70
    for line in string.split("\n"):
        tkinter.Label(window, text=str(line),font=("Arial",15), fg="black", bg="white",width="200",anchor='w').place(x=20, y=y1)
        y1=y1+50
    
    button=tkinter.Button(window, text="Back", font=("Arial", 16), fg="white",bg="purple",width="20",command=window.destroy).place(x=900, y=y1)
    window.mainloop()


def zapHelp():
    window=tkinter.Tk()
    window.title("Log Tool")
    window.geometry("1220x720")
    window.configure(bg="white")
   # l = tkinter.Label(window, text="Please check the log file pattern are not matching",font=("Arial",20,'bold'), fg="white", bg="purple", width="50").place(x=70, y=30)
    #l.grid(row=0, column=0)

    #b = tkinter.Button(window, text="Okay", command=window.destroy,font=("Arial", 16), fg="white", bg="purple").place(x=470, y=100)

    
# Create ANOTHER Frame INSIDE the Canvas
    #second_frame =tkinter.Frame(my_canvas)

# Add that New frame To a Window In The Canvas
    #my_canvas.create_window((0, 0), window=second_frame)
    
    string1="Zap Time Calculation\n"
    tkinter.Label(window, text=str(string1),font=("Arial",15,'bold'), bg="white", fg="purple").place(x=550, y=10)
    #data_string = StringVar()  
    data_string="This tool also takes the input log file and calculate the zap data and present the result on UI.\n Follow the below steps to get the correct data for zap time\n Enable CCA logs.\n 1. Grep -nri IRDTO_CA_ZAP_TIMING, in Phoebe_2 code\n 2. Make all the changes from DEBUG to INFO\n 3. Regenerate CCA libs and replace it in your custom\n 4. Open log4j.properties File add the following loggers\n log4j.logger.imw.serviceselection.servicecontext.calls=DEBUG\n log4j.logger.imw.ca.core.engine=INFO\n log4j.logger.imw.live.player=INFO\n 5. Open the startIdwayJ file\n -idwLogDrivers UIN,AV_EVT,HALCALL_AV,HALCALL_DSC,HALCALL_CCA,CCA_SPI_STREAM,\n IRDTO_CA_ZAP_TIMING -idwLogLevel INFO \ \n "
    y1=70
    for line in data_string.split("\n"):
        l=Label(window, text=str(line),font=("Arial",15), fg="black", bg="white",width="200",anchor='w').place(x=20, y=y1)



        #Label(window, text=str(line),font=("Arial",15), fg="black", bg="white",width="200",anchor='w').place(x=20, y=y1).pack()
        y1=y1+50
    
    button=tkinter.Button(window, text="Back", font=("Arial", 16), fg="white",bg="purple",width="20",command=window.destroy).place(x=900, y=y1-100)
    window.mainloop()

def performanceHelp():
    window=tkinter.Tk()
    window.title("Log Tool")
    window.geometry("1220x720")
    window.configure(bg="white")
   # l = tkinter.Label(window, text="Please check the log file pattern are not matching",font=("Arial",20,'bold'), fg="white", bg="purple", width="50").place(x=70, y=30)
    #l.grid(row=0, column=0)

    #b = tkinter.Button(window, text="Okay", command=window.destroy,font=("Arial", 16), fg="white", bg="purple").place(x=470, y=100)

    
# Create ANOTHER Frame INSIDE the Canvas
    #second_frame =tkinter.Frame(my_canvas)

# Add that New frame To a Window In The Canvas
    #my_canvas.create_window((0, 0), window=second_frame)
    
    string1="Performance Calculation\n"
    tkinter.Label(window, text=str(string1),font=("Arial",15,'bold'), bg="white", fg="purple").place(x=550, y=10)
    string="This tool will take log file of any long run test and process it and display the results for CPU utilization, System Memory utilization,\n JVM heap in required format.\n Follow the below stpes to get the correct data for the CPU, System Memory Utilization and for the JVM heap\n 1. Add the memtool in idway folder\n 2. Open the startIdwayj file add the below line\n ./memtool.out S1:360 & \n 3. Open start startIdwayj add -verbose:gcdetail \ \n"
    y1=70
    for line in string.split("\n"):
        tkinter.Label(window, text=str(line),font=("Arial",15), fg="black", bg="white",width="200",anchor='w').place(x=20, y=y1)
        y1=y1+50
    
    button=tkinter.Button(window, text="Back", font=("Arial", 16), fg="white",bg="purple",width="20",command=window.destroy).place(x=900, y=y1)
    window.mainloop()