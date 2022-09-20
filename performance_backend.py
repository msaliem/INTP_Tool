import re
import sys
import numpy
import json
from pathlib import Path
from msgBox import errorMsgPattern,successfulMsgCalculationDone,errorMsgJVMCalculationDone
import tkinter
from jsonData import write_json
from datetime import date
from jsonData import write_jsonForPerformance

out=[]
out1=[]
secondsDifference=0


def performnceCalculation(cpuData,totalCpuUtil,freeMemory,summaryOfData,jvmConsume,jvmFree,summaryOfDataMemory,summaryOfDatajvmConsume,summaryOfDatajvmFree,filename):
    
    row=[]
    del freeMemory[:]
    del summaryOfData[:]
    del totalCpuUtil[:]
    del jvmConsume[:]
    del jvmFree[:]
    del summaryOfDataMemory[:]
    del summaryOfDatajvmConsume[:]
    del summaryOfDatajvmFree[:]
    everySample=0
    totalBoxRunningTime=0
    def fun(pattern,jvmPattern,string):
        
        temp=[]
        secondsDifference=0
        line1=""
        for line in string.split("\n"):

            if jvmPattern in line:
               num=line.split(',')
               jvmC=float(int(num[8])/(1024*1024))
               jvmF=float(56.0-jvmC)
               jvmConsume.append(round(jvmC,2))
               jvmFree.append(round(jvmF,2))

               
            
            if pattern in line: 
               try:
                  num=line.split(',')
                  time=line.split(',')[0].split(':')
                  print()
                  if 'CPU utilization' in num:
                      continue
               #print(num[9])
                  if len(line1)>0:
                     num1=line1.split(',')
                     secondsDifference=int(num1[0].split('epoch_timestamp:')[1])

                  
                  totalBoxRunningTime=int(num[0].split('epoch_timestamp:')[1])
                  everySample=int(totalBoxRunningTime-secondsDifference)
                  
                 

                  freeMemory.append(round(float(int(num[2]))/(1024*1024),2))
                  totalCpuUtil.append(round(float(num[9]),2))
                  line1=line
               except:
                  errorMsgPattern()
                  return
                  
                  
    #print row
        
        if len(totalCpuUtil)==0:
           return(-1,-1)
        
        return(everySample,totalBoxRunningTime)
        
    """ 
    F1=open(filename,encoding="cp437", errors='ignore')
    cpuData=F1.read()
    F1.close()
    """
    everySample,totalBoxRunningTime=(fun("epoch_timestamp","GC#",cpuData))
    try:
      projectName=filename.split('_')[1].split('.')[0]
    except:
      projectName=filename.split('_')[1] 
   
    if len(totalCpuUtil)==0:
       errorMsgPattern()
       return 
    if len(jvmConsume)==0:
       errorMsgJVMCalculationDone()

    
    
    jsonDictionary={}
    #print(out[0])
    print("\nBox has rebooted "+str(len(out)-2)+" Times")
    print("-----------------------------------\n")

    del summaryOfData[:]
    if len(totalCpuUtil)>0:
       summaryOfData.append(max(totalCpuUtil))
       summaryOfData.append(min(totalCpuUtil))
       summaryOfData.append(round(float(sum(totalCpuUtil)/len(totalCpuUtil)),2))

    
    if len(freeMemory)>0:
       summaryOfDataMemory.append(max(freeMemory))
       summaryOfDataMemory.append(min(freeMemory))
       summaryOfDataMemory.append(round(float(sum(freeMemory)/len(freeMemory)),2))

    
    if len(jvmConsume)>0:
       summaryOfDatajvmConsume.append(max(jvmConsume))
       summaryOfDatajvmConsume.append(min(jvmConsume)) 
       summaryOfDatajvmConsume.append(round(float(sum(jvmConsume)/len(jvmConsume)),2))



    
    if len(jvmFree)>0:
       summaryOfDatajvmFree.append(max(jvmFree))
       summaryOfDatajvmFree.append(min(jvmFree)) 
       summaryOfDatajvmFree.append(round(float(sum(jvmFree)/len(jvmFree)),2))
    
    #Printing the calculated data into the performance file
    
   
    print("\n\n Total Number of Sample are: "+str(len(totalCpuUtil)))
    print("-----------------------------------\n")

    print("CPU utilization             %cpu")
    print("-----------------------------------")
    print("Minimum                 ",round(summaryOfData[0],2))
    print("-----------------------------------")
    print("Maximum                 ",round(summaryOfData[1],2))
    print("-----------------------------------")
    print("Average                 ",round(summaryOfData[2],2))
    print("-----------------------------------")
    jsonDictionary['CPU Consumption']=[round(summaryOfData[0],2),round(summaryOfData[1],2),round(summaryOfData[2],2)]

    print("\n\n\n System Memory Utilization\n\n")

    print("\n\n Total Number of Sample are: "+str(len(totalCpuUtil)))
    print("-----------------------------------\n")

    print("System Memory utilization           freeMem")
    print("-----------------------------------------")
    print("Minimum                           ",round(summaryOfDataMemory[0],2),"MB")
    print("------------------------------------------")
    print("Maximum                           ",round(summaryOfDataMemory[1],2),"MB")
    print("------------------------------------------")
    print("Average                           ",round(summaryOfDataMemory[2],2),"MB")
    print("-------------------------------------------\n")

    jsonDictionary['Free System Memory']=[round(summaryOfDataMemory[0],2),round(summaryOfDataMemory[1],2),round(summaryOfDataMemory[2],2)]

    print("\n\n\n JVM heap calculation\n\n")
    if len(jvmConsume)>0:
       print("\n\n Total Number of Sample are: "+str(len(jvmConsume)))
       print("-----------------------------------\n")

       print("JVM consume heap Memory        Consume memory")
       print("-------------------------------------------------")
       print("Minimum                       ",round(summaryOfDatajvmConsume[0],2),"MB")
       print("-------------------------------------------")
       print("Maximum                       ",round(summaryOfDatajvmConsume[1],2),"MB")
       print("---------------------------------------------")
       print("Average                       ",round(summaryOfDatajvmConsume[2],2),"MB")
       print("----------------------------------------------\n")



       print("\n\n Total Number of Sample are: "+str(len(jvmConsume)))
       print("-----------------------------------\n")

       print("JVM free heap Memory            free memory")
       print("-------------------------------------------------")
       print("Minimum                       ",round(summaryOfDatajvmFree[0],2),"MB")
       print("-------------------------------------------")
       print("Maximum                       ",round(summaryOfDatajvmFree[1],2),"MB")
       print("---------------------------------------------")
       print("Average                       ",round(summaryOfDatajvmFree[2],2),"MB")
       print("----------------------------------------------\n")
       jsonDictionary['Free JVM memory']=[round(summaryOfDatajvmFree[0],2),round(summaryOfDatajvmFree[1],2),round(summaryOfDatajvmFree[2],2)]
    
       
    jsondateDictionary={}
    jsondateDictionary[str(date.today())]=jsonDictionary
  #  print(jsondateDictionary)
    if len(jsonDictionary)>0:
       write_jsonForPerformance(jsondateDictionary,projectName)
       print('Json Done')
    return (everySample,projectName)
      
                  
    


       
