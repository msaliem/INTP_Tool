
from matplotlib.figure import Figure
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from msgBox import errorMsgPatternDataNotFound
import time
from pathlib import Path
#matplotlib.use('TkAgg')
#Grap to plot total boot time





def plot(totalBootUpTime,projectName):
    if len(totalBootUpTime)==0:
        errorMsgPatternDataNotFound()
        return
    print("Plot function boot is callled")
    
    fig = Figure(figsize =(16, 6), dpi=140)
  
    
  
    # adding the subplot
    Plot= fig.add_subplot(111)
    # Setting Plot and Axis variables as subplots()

    
  
# Adjust the bottom size according to the
# requirement of the user
    fig.subplots_adjust(bottom=0.15)
    

# Set the x and y axis to some dummy data
    numberOfSample = np.arange(len(totalBootUpTime))

# plot the numberOfSample and totalBootUpTime using bar function
    Plot.bar(numberOfSample, totalBootUpTime)
  
# Choose the Slider color
    slider_color = 'White'
    Plot.tick_params(axis='x', labelsize=18)
    Plot.tick_params(axis='y', labelsize=18)
    Plot.set_title('Boot up data for all iteration',fontsize=20)
    Plot.set_xlabel('Total number of sample are '+str(len(totalBootUpTime)),fontweight="bold", fontsize=20)
    # Y Axis lable 
    Plot.set_ylabel('Total time in milisecodns',fontweight="bold", fontsize=20)
    
    path=r"C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images"
    path+='\\'+str(projectName)+'\\'+str(projectName)+'_Graph_Boot.jpg'
    path=Path(path)
    fig.savefig(path)

    return
    

def plotZapData(ZapData,projectName,useCase):
    if len(ZapData)==0:
        errorMsgPatternDataNotFound()
        return
    print("Plot function Zap is callled")
   
    # Defining the size of the figure    
    fig = Figure(figsize =(16, 6), dpi=140)

    # Setting Plot and Axis variables as subplots()
    # adding the subplot
    Plot= fig.add_subplot(111)
 
# Adjust the bottom size according to the
# requirement of the user
    fig.subplots_adjust(bottom=0.15)
    

# Set the X and Y axis to some dummy data
    numberOfSample = np.arange(len(ZapData))
    
# plot the numberOfSample ZapData and  using matplot bar function
    Plot.bar(numberOfSample, ZapData)
    Plot.tick_params(axis='x', labelsize=18)
    Plot.tick_params(axis='y', labelsize=18)
# Choose the Slider color
    # X axis label
    Plot.set_title(str(useCase),fontweight="bold", fontsize=20)
    Plot.set_xlabel('Total number of sample are '+str(len(ZapData)),fontweight="bold", fontsize=20)
    # Y axis label
    Plot.set_ylabel('Total time in secodns',fontweight="bold", fontsize=20)

# creating the Tkinter canvas
    # containing the Matplotlib figure 
    """ canvas = FigureCanvasTkAgg(fig,master=frame1)  
    canvas.draw()
  
    # placing the canvas on the Tkinter window
    canvas.get_tk_widget().pack()
  
    # creating the Matplotlib toolbar
    toolbar = NavigationToolbar2Tk(canvas,frame1)
    toolbar.update()
  
    # placing the toolbar on the Tkinter window
    canvas.get_tk_widget().pack() """
    path=r"C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images"
    path+='\\'+str(projectName)+'\\'+str(projectName)+' '+str(useCase)+'_Graph_Zap.jpg'
    path=Path(path)
    fig.savefig(path)
    return
  
   


    
    
def lineGraph(CpuConsumption,everySample,projectName):
    if len(CpuConsumption)==0:
        errorMsgPatternDataNotFound()
        return
    
    print("Plot CPU is callled")
    
    fig = Figure(figsize =(16, 6), dpi=140)
    Plot = fig.add_subplot(111)
    fig.subplots_adjust(bottom=0.15)
    # list of squares

    numberOfSample = np.arange(len(CpuConsumption))
  
    # adding the subplot
   
     
    # plotting the graph
    Plot.plot(numberOfSample,CpuConsumption,marker='.',markersize=3)

    
    Plot.tick_params(axis='x', labelsize=18)
    Plot.tick_params(axis='y', labelsize=18)
    Plot.set_title('% CPU Utilization',fontsize=20)
    Plot.set_xlabel('Total number of sample: '+str(len(CpuConsumption))+", one sample after every "+str(everySample)+"sec",fontweight="bold", fontsize=20)
    Plot.set_ylabel('Total CPU usage %',fontweight="bold", fontsize=20)
    Plot.grid()
    path=r"C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images"
    path+='\\'+str(projectName)+'\\'+str(projectName)+'_Graph_PerformanceCPU.jpg'
    path=Path(path)
    fig.savefig(path)
    print('CPU Image Done')
    
   

   

    


def lineGraphMemory(MemoryConsumption,everySample,projectName):
   
    if len(MemoryConsumption)==0:
        errorMsgPatternDataNotFound()
        return
    print("Plot System Memory function is callled")
    
    fig = Figure(figsize =(16, 6), dpi=140)
    Plot = fig.add_subplot(111)
    fig.subplots_adjust(bottom=0.15)
    # list of squares
    numberOfSample = np.arange(len(MemoryConsumption))
  
    
    # plotting the graph
    Plot.plot(numberOfSample,MemoryConsumption,marker='.',markersize='3')
   
    Plot.tick_params(axis='x', labelsize=18)
    Plot.tick_params(axis='y', labelsize=18)
    Plot.set_title('Free System Memory',fontsize=20)
    Plot.set_xlabel('Total number of sample are '+str(len(MemoryConsumption))+", one sample after every "+str(everySample)+"sec",fontweight="bold", fontsize=20)
    Plot.set_ylabel('Total Free memory in MB',fontweight="bold", fontsize=20)

    # Shows the graph in grid form
    Plot.grid()

    path=r"C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images"
    path+='\\'+str(projectName)+'\\'+str(projectName)+'_Graph_PerformanceMemory.jpg'
    path=Path(path)
    fig.savefig(path)   
    print('memory Image Done')
    return
    
   
     


def lineGraphHeap(jvmFree,jvmCons,projectName):
   
    if len(jvmFree)==0:
        errorMsgPatternDataNotFound()
        return
    print("Plot function is callled")
    
    fig = Figure(figsize =(16, 6), dpi=140)
    Plot = fig.add_subplot(111)
    fig.subplots_adjust(bottom=0.15)
    # list of squares
    numberOfSample = np.arange(len(jvmFree))
  
    # adding the subplot
    #slider_color = 'White'
    # plotting the graph
    Plot.plot(numberOfSample,jvmCons,color='blue',markersize='3',label='Consume Memory')
    Plot.plot(numberOfSample,jvmFree,color='green',markersize='3',label='Free Memory')
    Plot.tick_params(axis='x', labelsize=16)
    Plot.tick_params(axis='y', labelsize=16)
   # plot.set_yticklabels(axis="y", rotation=0, fontsize=20)
    #Plot.ticklabel_format(useOffset=False)
    Plot.set_title('Heap Memory',fontsize=20)
    Plot.set_xlabel('Total number of sample are '+str(len(jvmFree)),fontweight="bold", fontsize=20)
    Plot.set_ylabel('Total memory in MB',fontweight="bold", fontsize=20)
    Plot.grid()
    Plot.legend(prop={"size":16})
    path=r"C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images"
    path+='\\'+str(projectName)+'\\'+str(projectName)+'_Graph_PerformanceJVM.jpg'
    path=Path(path)
    fig.savefig(path)   
    print('Heap Image Done')
    return
    

   





