import tkinter
import sys
import threading
import time
from graph import lineGraph,lineGraphMemory,lineGraphHeap
from performance_SummaryOfData import summary
from performance_backend import performnceCalculation
sys.path.append('C:/Users/mohd.saliem/Documents/development/python/project')
from graph import lineGraph,lineGraphMemory



    

totalCpuUtil=[]
freeMemory=[]
summaryOfData=[]
jvmConsume=[]
jvmFree=[]
summaryOfDataMemory=[]
summaryOfDatajvmFree=[]
summaryOfDatajvmConsume=[]

def performanceCal(Data,filename):
   

    del totalCpuUtil[:]
    del freeMemory[:]
    del summaryOfData[:]
    del jvmConsume[:]
    del jvmFree[:]
    del summaryOfDataMemory[:]
    del summaryOfDatajvmFree[:]
    del summaryOfDatajvmConsume[:]
    print('cpumemjvm')
    everySample,projectName=performnceCalculation(Data,totalCpuUtil,freeMemory,summaryOfData,jvmConsume,jvmFree,summaryOfDataMemory,summaryOfDatajvmConsume,summaryOfDatajvmFree,filename)

    print(len(totalCpuUtil))
    def performanceThread(lock):
        lock.acquire()
        lineGraph(totalCpuUtil,everySample,projectName)
        time.sleep(2)
        lineGraphMemory(freeMemory,everySample,projectName) 
        time.sleep(2)
        lineGraphHeap(jvmFree,jvmConsume,projectName)
        time.sleep(2)
        lock.release()

    lock=threading.Lock()
    thread=threading.Thread(target=performanceThread,args=(lock,))
    thread.start()
    thread.join()    
    return
    