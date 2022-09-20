import tkinter
import tkinter.filedialog as filedialog
import re
import sys
from BootTime_MaxMinAvg import printData
from msgBox import successfulMsgCalculationDone, errorMsgPattern, errorMsgInputFile
from pathlib import Path
from json.decoder import JSONDecodeError
import json
from jsonData import write_jsonForBoot
from datetime import date
from graph import plot




def calculateBootTimeForEachstep(string, bootupDataforEverystep, minMaxAvgOfBootData, totalBootUpTime, bootUpSteps,filename):

    
    
    
    del minMaxAvgOfBootData[:]
    del totalBootUpTime[:]
    
    row1 = []

    def fun(pattern, string):
        checkCorrectFile=False
        row = []
        del bootupDataforEverystep[:]
        for line in string.split("\n"):
            if pattern[0] in line:
               checkCorrectFile=True

            for i in range(len(pattern)):
                if pattern[i] in line:
                    try:
                       # print(line)
                       hour = line.split(']')[0].split(' ')[1].split(':')[0].split()  # this will give us hour
                       minutes = line.split(']')[0].split(':')[1].split()            # this will give us minute
                       milliSeconds = line.split(']')[0].split(':')[2].split('.')
                       string = ""

                       ms = int(string.join(milliSeconds))

                       minute = int(string.join(minutes))
                       hours = int(string.join(hour))

                       if hours == 0:
                          hours = int(24)
                      # print(line,"    ",ms)
                       # convert hour and minutes into the miliseconds and add them both miliseconds i.e ms
                       ms += (hours*60*60*1000+int(minute)*60*1000)
                       # print(ms)
                       # row[] is a 1D array which contain the time of each pattern occurence in a file
                      
                       row.append(ms)
                       # print(len(row)," ",ms)
                    except:
                        return False
            #To handle the inconsistent bootup logs 
            if  pattern[5] in line:
                if checkCorrectFile==True:
                    ind = len(row)-6
                    del row[0:ind]
                    out=[]
                    sum1 = 0
                    for j in range(1, len(row)):
                       sum1 += row[j]-row[j-1]
                       out.append(round(float(row[j]-row[j-1])/1000,3))
               
                    out.append(round(float(sum1/1000),3))
                   
                    bootupDataforEverystep.append(out)       
                    row=row1
                else:
                    return checkCorrectFile

            
            
                

        return checkCorrectFile

    defaultPattern=[]  # run time input will be store in input array


    GriffinAndSphinxPattern=["Hit CIS","Starting kernel","HAL initialization start from here","HAL Initialization done","Starting VM 4.2.028","AV_VideoFirstFrameDisplayedCallback"] #this array contain the default pattern

    NavyaLoaderPattern=["Find CIS","Initializing cgroup subsys cpu","HAL initialization start from here","HAL Initialization done","Starting VM 4.2.028","AV_VideoFirstFrameDisplayedCallback"] #this array contain the default pattern
    Airtel=["] debu","] done","Hello UART","IMW directories:","AV_VideoFirstFrameDisplayedCallback"]
    """
    try:
       F1=open(File,encoding="cp437", errors='ignore')
       string=F1.read()
       F1.close()
    except:
       errorMsgInputFile()
       return 
    if Project==1:
        defaultPattern=Airtel
    elif Project==2:
        defaultPattern=NavyaLoaderPattern
    else:
    """
    
    projectName=filename.split('_')[1]
    
    if projectName.startswith('Airtel'):    
       defaultPattern=GriffinAndSphinxPattern
    elif projectName.startswith('Navya'):
        defaultPattern=NavyaLoaderPattern
    elif projectName.startswith('Griffin&Sphinx'):
        defaultPattern=GriffinAndSphinxPattern
    
        
    if fun(defaultPattern,string)==False:
        return False
        
    jsonDictionary={}    
    res1=[]
    print(bootupDataforEverystep)
    print("\n")
    for i in range(len(bootupDataforEverystep)):
        print(bootupDataforEverystep[i])
   
    print("This Data is been taken minMaxAvgOfBootData number of ",len(bootupDataforEverystep)," iteration")
    print("_____________________________________________________\n")
    print(" Numbers are represented in milliseconds\n")
    print("\n")
    # minMaxAvgOfBootData=[]  # Total is a 2D array with 3 rows and columns(number of pattern)
    
    minimum=[]  #will contain the minimum value each pattern from the bootupDataforEverystep matrix
    maximum=[]  #will contain the maximum value each pattern from the bootupDataforEverystep matrix
    average=[]  #will contain the average value each pattern from the bootupDataforEverystep matrix

    for i in range(len(bootupDataforEverystep)):
        
         totalBootUpTime.append(bootupDataforEverystep[i][len(bootupDataforEverystep[0])-1])

         
    for i in range(0,len(bootupDataforEverystep[0])-1):
        avg=float(0)
        maxi=float(0)
        mini=float(50.000)
        
   # finding minimum, maximum, and average from the bootupDataforEverystep matrix
        for j in range(0,len(bootupDataforEverystep)):
            avg+=float(bootupDataforEverystep[j][i])       
            maxi=max(maxi,bootupDataforEverystep[j][i])
            mini=min(mini,bootupDataforEverystep[j][i])
            
        maximum.append(round(maxi,3))
        minimum.append(round(mini,3))
        avg=round(float((avg/len(bootupDataforEverystep))),3)
        average.append(avg)

# variables to calculate the sum of each pattern in their respect one
    maxArraySum=max(totalBootUpTime)   
    minArraySum=min(totalBootUpTime)
    avgArraySum=float(sum(totalBootUpTime)/(len(totalBootUpTime)))

# storing the sum in their respective array
    maximum.append(round(maxArraySum,3))
    minimum.append(round(minArraySum,3))
    average.append(round(avgArraySum,3))



    minMaxAvgOfBootData.append(maximum)
    minMaxAvgOfBootData.append(minimum)
    minMaxAvgOfBootData.append(average)
    
    
    
    
    print("Total time copeid successfully\n")
    
    try:
       print("Min max and average")
       
       print("\n")
 
       print("Maximum,Minimum and Average data of each iteration\n\n")
       print("                                                                       Maximum      Minimum        Average\n")
    
       for j in range(0,len(minMaxAvgOfBootData[0])): 
           print(bootUpSteps[j],minMaxAvgOfBootData[0][j],"      ",minMaxAvgOfBootData[1][j],"        ",minMaxAvgOfBootData[2][j])
           print("-----------------------------------------------------------------------------------------------------------")
           jsonDictionary[bootUpSteps[j]]=[minMaxAvgOfBootData[0][j],minMaxAvgOfBootData[1][j],minMaxAvgOfBootData[2][j]]
           print("\n_______________________________________________")
           print("Data of each iterarion starting from 1-----")
           print("\n__________________________________________________")
        
        

       for i in range(0,len(bootupDataforEverystep)):
           print("\n***************************************")
           print("* ITERATION",i+1,"                        *")
           print("***************************************")
           for j in range(0,len(bootupDataforEverystep[0])):
               print(bootUpSteps[j],bootupDataforEverystep[i][j])
               print("-----------------------------------------------------------------------------------|")   
               
       jsondateDictionary={}
       jsondateDictionary[str(date.today())]=jsonDictionary
      # print(jsonDictionary)
       if len(jsonDictionary)>0:
           print('json calling')
           write_jsonForBoot(jsondateDictionary,projectName) 
           print('json done')
           #plot(frame1,totalBootUpTime,projectName)
    except:
        return False
