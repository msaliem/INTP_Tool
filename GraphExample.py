import random
import matplotlib
import tkinter as Tk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def plotGraph(frame1,Totalzaptime):
    matplotlib.use('TkAgg')

    root = Tk.Tk()
    root.wm_title("Embedding in TK")
    fig = plt.Figure()
    canvas = FigureCanvasTkAgg(fig, root)
    canvas.get_tk_widget().pack(side=Tk.TOP, fill=Tk.BOTH, expand=1)

    ax=fig.add_subplot(111)
    fig.subplots_adjust(bottom=0.25)

    y_values = np.arange(len(Totalzaptime))
    x_values =Totalzaptime

    
    ax.bar( y_values,Totalzaptime)

    ax_time = fig.add_axes([0.12, 0.1, 0.78, 0.03])
    s_time = Slider(ax_time, 'Time', 0, len(Totalzaptime), valinit=0)


    def update(val):
        pos = s_time.val
        ax.axis([pos, pos+10, 0, y_values])
        fig.canvas.draw_idle()
    s_time.on_changed(update)

    Tk.mainloop()