import tkinter
from PIL import ImageTk, Image
import re
import threading
from destroyWin import destroy
from BootTime_help import bootHelp,zapHelp,performanceHelp
from scheduling import schedulingMain
import threading
import time
import schedule

    
     



window = tkinter.Tk()


window.title("STB performance tool")
window.geometry("1200x900")
# window.attributes('-fullscreen',True)
# set window color
window.configure(bg="gray")
window.resizable(0,0)
path = "irdetopic.jpg"

#Creates a Tkinter-compatible photo image, which can be used everywhere Tkinter expects an image object.
img = ImageTk.PhotoImage(Image.open(path))


main_frame = tkinter.Frame(window, width=0, height=0)
main_frame.pack(fill="both", expand=1)

# Create A Canvas
my_canvas = tkinter.Canvas(main_frame)
my_canvas.pack(side="left", fill="both", expand=1)

# Create ANOTHER Frame INSIDE the Canvas
second_frame = tkinter.Frame(my_canvas)

# Add that New frame To a Window In The Canvas
my_canvas.create_window((5, 14), window=second_frame)
# Container
# create a toplevel menu
#The Label widget is a standard Tkinter widget used to display a text or image on the screen.
panel = tkinter.Label(my_canvas, image = img)

#The Pack geometry manager packs widgets in rows or columns.
panel.pack(side = "top", fill = "both", expand = "yes")
menubar = tkinter.Menu(window)

menubar.config(bg = "GREEN",fg='white',activebackground='red',activeforeground='purple',activeborderwidth=0,font=("Verdana", 12))


try:
        thread=threading.Thread(target=schedulingMain, args=(main_frame,))
        thread.start()
        print("Saleem.........")
        #schedulingMain(main_frame)
        
except:
     print("Not running Again")



menubar.add_command(label="Boot Time",command=lambda: destroy(main_frame, 1))
menubar.add_command(label="Zap time", command=lambda: destroy(main_frame, 2))
menubar.add_command(label="Performance Measuring",command=lambda: destroy(main_frame, 3))

help_ = tkinter.Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Help', menu = help_)
help_.add_command(label ='Boot Time', command = bootHelp)
help_.add_separator()
help_.add_command(label ='Zap time', command = zapHelp)
help_.add_separator()
help_.add_command(label ='Performance Measuring', command = performanceHelp)

window.mainloop()  


       





