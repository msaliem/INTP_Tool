import tkinter
import tkinter.filedialog as filedialog
import re
import sys


def PrintIterationData(bootupDataforEverystep, bootUpSteps):
    window =tkinter.Tk()
    window.title("All iteration Data")
    window.geometry("2000x700")
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
    numberOfFrame = int((len(bootupDataforEverystep)/14)+1)
    startPoint = 0

    for i in range(0, numberOfFrame):
        # creating new frame for each iteration
        frame1 =tkinter.LabelFrame(second_frame, font=(
            'Arial', 15, 'bold'), padx=130, pady=0, width=2000, height=400, bg="white")

        frame1.pack()

   
        e =tkinter.Label(frame1, text="Starting and Ending points",  fg="white", bg="purple", font=('Arial', 16, 'bold')).place(x=0, y=80, width=300)
        

        X_axis = 270
        Y_axis = 120
        X_axisForbootUpSteps = 0
        Y_axisForbootUpSteps = 120
        for k in range(0, len(bootUpSteps)):
            if k < len(bootUpSteps)-1:
               e =tkinter.Label(frame1, text=bootUpSteps[k], fg="black", bg="gray85", font=('Arial', 16), anchor="w").place(x=X_axisForbootUpSteps, y=Y_axisForbootUpSteps, width=350)
               
            else:
                e =tkinter.Label(frame1, text=bootUpSteps[k], fg="black", bg="gray85", font=('Arial', 16, 'bold'), anchor="w").place(x=X_axisForbootUpSteps, y=Y_axisForbootUpSteps, width=350)
               

            Y_axisForbootUpSteps += 40
        X_axisForBootUpData = X_axis;
        for k in range(startPoint, len(bootupDataforEverystep)):
            X_axisForBootUpData += 100
            Y_axisForBootUpData = Y_axis
            e =tkinter.Label(frame1, text="iter "+str(k+1), width=0, fg="white", bg="purple", font=('Arial',16,'bold')).place(x=X_axisForBootUpData, y=80, width=100)
            for j in range(0,len(bootupDataforEverystep[0])):
          
                if j<len(bootupDataforEverystep[0])-1: 
                   e =tkinter.Label(frame1, text=bootupDataforEverystep[k][j], width=10,fg="black",bg="gray85" , font=('Arial',16)).place(x=X_axisForBootUpData, y=Y_axisForBootUpData, width=100)
                   Y_axisForBootUpData+=40
               
                else:
                   e =tkinter.Label(frame1, text=bootupDataforEverystep[k][j], width=10,fg="black", bg="gray85" , font=('Arial',16,'bold')).place(x=X_axisForBootUpData, y=Y_axisForBootUpData, width=100)
               
                   Y_axisForBootUpData+=40
            if (k+1)%14==0:
               startPoint=k+1
               break

   


    window.mainloop()

