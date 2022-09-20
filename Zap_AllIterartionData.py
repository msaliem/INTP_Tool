import tkinter
import tkinter.filedialog as filedialog
import re
import sys


def PrintIterationData(defaultStepsDetail,CA_SequnceStepsDetail,MW_SequnceStepsDetail,timeElapseWithDefaultStep,timeElapseforCA,deltaTimeWithDefaultStep,deltaTimeWithCA):
    window =tkinter.Tk()
    window.title("All iteration Data")
    window.geometry("2000x700")
    DarkGrey='#800080'
    col='#f0edff'
# Create A Main Frame
    main_frame =tkinter.Frame(window, width=50, height=50)
    main_frame.pack(fill="both", expand=1)

# Create A Canvas
    my_canvas =tkinter.Canvas(main_frame)
    my_canvas.pack(side="left", fill="both", expand=1)


# Add A Scrollbar To The Canvas

    my_scrollbar =tkinter.Scrollbar(
        main_frame, orient="vertical", command=my_canvas.yview)
    my_scrollbar.pack(side="right", fill="y")


# Configure The Canvas
    my_canvas.configure(yscrollcommand=my_scrollbar.set)
    my_canvas.bind('<Configure>', lambda e: my_canvas.configure(
        scrollregion=my_canvas.bbox("all")))

# Create ANOTHER Frame INSIDE the Canvas
    second_frame =tkinter.Frame(my_canvas)

# Add that New frame To a Window In The Canvas
    my_canvas.create_window((0, 0), window=second_frame)
    if len(timeElapseWithDefaultStep)%12==0:
        numberOfFrame = int((len(timeElapseWithDefaultStep)/12))
    else:
        numberOfFrame = int((len(timeElapseWithDefaultStep)/12+1))
    startPoint = 0

    for j in range(0, numberOfFrame):

        frame1 =tkinter.LabelFrame(second_frame, font=(
            'Arial', 15, 'bold'), padx=130, pady=0, width=2000, height=600, bg="white")

        frame1.pack()
        e =tkinter.Label(frame1, text="Starting and Ending points",  fg="white",
                          bg=DarkGrey, font=('Arial', 16, 'bold'),anchor='w').place(x=0, y=60, width=370)
    #my_canvas.create_window((0,i), window=frame1, anchor="nw")

   
        n=100
        m=400
        xaxiForinpu=0
        yaxiForinpu=100
        for i in range(0,len(defaultStepsDetail)-1):
         
            e = tkinter.Label(frame1, text=defaultStepsDetail[i], fg="black",bg=col ,font=('Arial',16),anchor='w').place(x=xaxiForinpu, y=yaxiForinpu, width=370) 
            yaxiForinpu+=35

        e = tkinter.Label(frame1, text="CA sequence", width=50,  fg="white", bg=DarkGrey, font=('Arial',16,'bold'),anchor='w').place(x=0, y=yaxiForinpu, width=370)
        yaxiForinpu+=35
        for i in range(0,len(CA_SequnceStepsDetail)):
             e = tkinter.Label(frame1, text=CA_SequnceStepsDetail[i], fg="black",bg=col ,font=('Arial',16),anchor='w').place(x=xaxiForinpu, y=yaxiForinpu, width=370)
             yaxiForinpu+=35

        e = tkinter.Label(frame1, text="Total Zap Time", fg="black",bg=col ,font=('Arial',16,'bold'),anchor='w').place(x=xaxiForinpu, y=yaxiForinpu, width=370)
        

       
                  
           
         
        for i in range(startPoint,len(timeElapseWithDefaultStep)):
           

            e = tkinter.Label(frame1, text="Sample "+str(i+1), fg="white",bg=DarkGrey ,font=('Arial',16,'bold'),anchor='w').place(x=m, y=20, width=110)

            e = tkinter.Label(frame1, text="Delta", fg="black",bg='#95dc73' ,font=('Arial',16,'bold')).place(x=m, y=60, width=100)

            e = tkinter.Label(frame1, text="", width=10,fg="black",bg=col , font=('Arial',16)).place(x=m, y=n, width=100)
            for j in range(0,len(deltaTimeWithDefaultStep[0])):
               # e = tkinter.Label(frame1, text=timeElapseWithDefaultStep[i][j], width=10,fg="black",bg=col , font=('Arial',16)).place(x=m, y=n, width=100)
                e = tkinter.Label(frame1, text=deltaTimeWithDefaultStep[i][j], width=10,fg="black",bg=col , font=('Arial',16)).place(x=m, y=n, width=100)
                n+=35
            e = tkinter.Label(frame1, text="Delta", fg="black",bg='#95dc73' ,font=('Arial',16,'bold'),anchor='w').place(x=m, y=n, width=100)  
            n+=35
            
            for j in range(0,len(deltaTimeWithCA[0])):
               # e = tkinter.Label(frame1, text=timeElapseforCA[i][j], width=10,fg="black",bg=col , font=('Arial',16)).place(x=m, y=n, width=100)
                e = tkinter.Label(frame1, text=deltaTimeWithCA[i][j], width=10,fg="black",bg=col , font=('Arial',16)).place(x=m, y=n, width=100)
                n+=35
            e = tkinter.Label(frame1, text=timeElapseWithDefaultStep[i][-1], width=10,fg="black",bg='#ffa600' , font=('Arial',16,'bold')).place(x=m, y=n, width=100)
            n=100
            m+=120
           
            if (i+1)%12==0:
               startPoint=i+1
               break

   
  
   

    window.mainloop()

