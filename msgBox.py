from tkinter import*
import tkinter.messagebox


def errorMsgPattern():
    messagebox.showerror("Invalid file","You might have choosen an invalid file, please choose the valide file")

def errorMsgOpenFile():
    messagebox.showerror("Input missing Error","Please select the above input options first")

def errorMsgInputFile():
    messagebox.showerror("Input file missing Error","Please first select the correct input file")

def errorMsgPatternManual():
    messagebox.showerror("Pattern missing error","You have choosen Manual zaping but the text file contain admin tool zaping data")

def errorMsgPatternAutoZaping():
    messagebox.showerror("Pattern missing error","You have choosen Auto zaping but the text file contain Manual zaping data")

def errorMsgPatternDataNotFound():
    messagebox.showerror("Data not found","Either you have choosen a wrong file or you might not choosen any file")

def successfulMsgCalculationDone():
    messagebox.showinfo("Calculation Done","Data Successfully calculated")

def errorMsgJVMCalculationDone():
    messagebox.showerror("GC details logs missing","jvm heap logs missing")

def errorMsgCpuMemMissing():
    messagebox.showerror("Memtool missing","CPU and  system memory data is missing, please add the memtool to get the data")








