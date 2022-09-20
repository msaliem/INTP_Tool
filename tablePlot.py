from matplotlib.figure import Figure
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from msgBox import errorMsgPatternDataNotFound
import time
from pathlib import Path


def bootTable(new_data,referenceData,projectName):
    colName=['Max','MaxRef','Min','MinRef','Avg','AVGRef']
    rowColor=['#EDF7EF','#EDF7EF','#EDF7EF','#EDF7EF','#EDF7EF','#E0DE51']
    colColor=['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080']
    cellColoring=[['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#FAFA57','#FCAA46','#FAFA57','#FCAA46','#FAFA57','#FCAA46']]
    rowData=[]
    row=[]
    for i in new_data:
        row.append(i)
        x=[]
        for k in range(len(new_data[i])):
            x.append(new_data[i][k])
            if int(referenceData[i][k])>0:
               x.append(referenceData[i][k])
            else:
                x.append('NA')
        rowData.append(x)
    
    plt.subplots_adjust(left=0.2, top=0.9)
    plt.axis('tight')
    plt.axis('off')
    try:
       ytable=plt.table(cellText=rowData, rowLabels=row,rowColours=rowColor, colLabels=colName,colColours=colColor,cellColours=cellColoring, loc='center',cellLoc='left')
       ytable.set_fontsize(22)
       ytable.scale(1, 3)    
       plt.title('Min Max Avg with reference for '+str(projectName))
    except:
       print('error in try')
       return

    path=r"C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images"
    path+='\\'+str(projectName)+'\\'+str(projectName)+'MinMaxAvg_OfBootData.jpg'
    plt.savefig(path,bbox_inches='tight', dpi=130)
    plt.cla()
    return


def zapTable(new_data,referenceData,useCase,projectName):
    
    colName=['Max','MaxRef','Min','MinRef','Avg','AvgRef']
    colColor=['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080']
    rowColor=['#EDF7EF','#EDF7EF','#EDF7EF','#EDF7EF','#EDF7EF','#EDF7EF','#EDF7EF','#EDF7EF','#EDF7EF','#EDF7EF','#EDF7EF','#EDF7EF','#E0DE51']
    cellColoring=[['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#FAFA57','#FCAA46','#FAFA57','#FCAA46','#FAFA57','#FCAA46']]
    rowData=[]
    row=[]
    for i in new_data:
        row.append(i)
        x=[]
        for k in range(len(new_data[i])):
            x.append(new_data[i][k])
            if referenceData[i][k]>0:
               x.append(referenceData[i][k])
            else:
                x.append('NA')
        rowData.append(x)
        
    print("Plotting the Table data...........................................................")  
    time.sleep(3)
    plt.subplots_adjust(left=0.2, top=0.9)
    plt.axis('tight')
    plt.axis('off')
    try:
       ytable=plt.table(cellText=rowData, rowLabels=row, rowColours=rowColor, colLabels=colName, colColours=colColor,cellColours=cellColoring, loc='center')
       
       ytable.set_fontsize(16)
       ytable.scale(1, 1.5) 
       plt.title('MaxMinAvg with reference for useCase'+str(useCase))
    except:
       print('error in try')
       time.sleep(3)
       return

    path=r"C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images"
    path+='\\'+str(projectName)+'\\'+str(projectName)+'_'+str(useCase)+'_zapDatatable.jpg'
    try:
        plt.savefig(path,bbox_inches='tight', dpi=130) 
        
    except:
        print('issue in saving the figure')
    plt.cla()
    return
    
def performanceTable(new_data,referenceData,projectName):
    colName=['Max','MaxRef','Min','MinRef','Avg','AvgRef']
    colColor=['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080']
    rowColor=['#EDF7EF','#EDF7EF','#EDF7EF']
    cellColoring=[['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080'],['#D3D3D3','#808080','#D3D3D3','#808080','#D3D3D3','#808080']]
    rowData=[]
    row=[]
    print(new_data)
    for i in new_data:
        row.append(i)
        x=[]
        for k in range(len(new_data[i])):
            x.append(new_data[i][k])
            if referenceData[i][k]>0:
               x.append(referenceData[i][k])
            else:
                x.append('NA')
        rowData.append(x)
    
    plt.subplots_adjust(left=0.2, top=0.8)
    plt.axis('tight')
    plt.axis('off')
    try:
       ytable=plt.table(cellText=rowData, rowLabels=row, rowColours=rowColor, colLabels=colName, colColours=colColor,cellColours=cellColoring, loc='center')
       
       ytable.set_fontsize(25)
       ytable.scale(1, 4)    
       plt.title('Max Min Avg for CPU, Sys memory,  JVM memory'+str(projectName))
    except:
       print('error in try')
    
    path=r"C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images"
    path+='\\'+str(projectName)+'\\'+str(projectName)+'_MinMaxAvg_OfPerfromace.jpg'
    plt.savefig(path,bbox_inches='tight', dpi=140)
    plt.cla()
    return