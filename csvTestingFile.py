import csv


fileName=r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\zap_Usecase.csv'
dic={}
f=open(fileName,'r')
Data=csv.reader(f)

fields=next(Data)

for i in Data:
    dic[i[0]]=[i[1],i[2]]



f.close()

for i in dic:
    print(dic[i])













    import re
import sys
import numpy

from msgBox import errorMsgPattern,successfulMsgCalculationDone

import tkinter

from msgBox import errorMsgOpenFile, errorMsgInputFile,errorMsgPatternManual,errorMsgPatternAutoZaping

buttonColor='#1500b9'
def calculateMinMaxAvg(timeElapse,deltaTimeWithDefaultStep,minMaxAvgArr):
    del minMaxAvgArr[:]
    
    for i in range(0,len(deltaTimeWithDefaultStep[0])):
         mx=0
         mn=50000
         sumOfData=0
         row=[]
         try:
             for j in range(0,len(deltaTimeWithDefaultStep)):
                 mx=max(mx,deltaTimeWithDefaultStep[j][i])
                 mn=min(mn,deltaTimeWithDefaultStep[j][i])
                 sumOfData+=deltaTimeWithDefaultStep[j][i]
             
             row.append(mx)
             row.append(mn)
             row.append(int(sumOfData/len(deltaTimeWithDefaultStep)))
             minMaxAvgArr.append(row)
         except:
            minMaxAvgArr.append(['NA','NA','NA'])
    
    mx=0
    mn=50000
    sumofdata=0
    row1=[]
    del row1[:]
    try:
        for i in range(len(timeElapse)):
          
            mx=max(mx,timeElapse[i][-2])
            mn=min(mn,timeElapse[i][-2])
         
            sumofdata+=timeElapse[i][-2]
       
        #print(sumOfData         
        row1.append(mx)
        row1.append(mn)
        row1.append(int(sumofdata/len(timeElapse)))
        print(row1)
        minMaxAvgArr.append(row1)
    except:
        minMaxAvgArr.append(['NA','NA','NA'])
   
    
   
def zapTimeCal(timeElapseWithDefaultStep,timeElapseforCA,deltaTimeWithDefaultStep,deltaTimeWithCA,Data,minMaxAvgforDefaultStep,minMaxAvgforCA,MWsequence,defaultStepsDetail,CA_SequnceStepsDetail,MW_SequnceStepsDetail,Totalzaptime,channnel_num):
    del timeElapseWithDefaultStep[:]
    del timeElapseforCA[:]
    del deltaTimeWithDefaultStep[:]
    del deltaTimeWithCA[:]
   
    dic={}
   
    def patternSearchingAndStoringInOutArray(indexTocalculateDefaultTime,indexToCalculateCA,pattern,string,channnel_num):
        row=[]
        boolSource=False
        boolDesti=False
        
        for line in string.splitlines():
            if 'lcn= '+str(channnel_num[0]) in line or 'LCN= '+str(channnel_num[0]) in line:
                boolSource=True
               
            if 'lcn= '+str(channnel_num[1]) in line or 'LCN= '+str(channnel_num[1]) in line:
                boolDesti=True
                print(line)

              
            if boolSource==True and boolDesti==False:
              
               for i in range(len(pattern)):
                   if pattern[i] in line: 
                      try:
                         #print(line)
                        
                         line1=line.split(' ')[0]
                        
                         minute=int(line1.split(':')[0])*60*1000
                         
                         ms=float(line1.split(':')[1])*1000
                         ms=int(ms)
                         ms+=minute
                         dic[pattern[i]]=ms
                         #print(ms)
                      except:
                          print("Error in pattern searching")
                          dic.clear()
                          break
                         
                   
                    
    
            if pattern[0] in line and boolSource==True and boolDesti==True:
                
                boolSource=False
                boolDesti=False 
                #print(line)               
                res=[]
                res1=[]
                defaultValue=['NA','NA','NA','NA','NA']
                boolDefault=False
                for i in range(1,len(indexTocalculateDefaultTime)):
                    try:
                       res1.append(dic[indexTocalculateDefaultTime[i]]-dic[pattern[0]])
                       res.append(dic[indexTocalculateDefaultTime[i]]-dic[indexTocalculateDefaultTime[i-1]])
                    except:
                        boolDefault=True
                        break
                        
                print(res)
                if boolDefault==False:
                   timeElapseWithDefaultStep.append(res1)
                   deltaTimeWithDefaultStep.append(res)
                


                resCca=[]
                resCca1=[]
                boolCca=False
                for i in range(1,len(indexToCalculateCA)):
                    try:
                        resCca1.append(dic[indexToCalculateCA[i]]-dic[pattern[0]])
                        resCca.append(dic[indexToCalculateCA[i]]-dic[indexToCalculateCA[i-1]])
                    except:
                        boolCca=True
                        break
                print(resCca)
                if boolCca:
                    timeElapseforCA.append(defaultValue)
                    deltaTimeWithCA.append(defaultValue)
                else:
                   timeElapseforCA.append(resCca1)
                   deltaTimeWithCA.append(resCca) 

                
                dic.clear()

        return(timeElapseWithDefaultStep,deltaTimeWithDefaultStep,timeElapseforCA,deltaTimeWithCA)
                

    """ 
    File=open(filename,encoding="cp437", errors='ignore')
    zapData=File.read()

    File.close()


    
    string=""
    temp1=[]
    del temp1[:]
    pattern1="<CHANNEL_UP> Pressed device"
    pattern2="<CHANNEL_DOWN> Pressed device"
    if Manual==2:
       print("Sam****************************************************************************\n")
       checkPattern=re.search("live zap dvb://",zapData)
       if checkPattern==None:
          print("Not found")
          
       temp1=zapData.split("live zap dvb://")
       print("length is ",len(temp1))
       for i in range(len(temp1)):
           if Get_theDat_for==1 and i%2==0:
              string+=temp1[i]
           elif Get_theDat_for==2 and i%2==1:
              string+=temp1[i]

    if Manual==1:
       if Get_theDat_for==1 and Manual==1:
          print("Nad****************************************************************************\n")
          checkPattern=re.search(pattern1,zapData)
          if checkPattern==None:
             print("Not found  ",checkPattern)
             
          x=zapData.split(pattern1) #break the string with this keyword
          
          temp=[]
          for i in range(len(x)):
              temp.append(x[i].split(pattern2)[0]) #this will break the string further

       
          for i in range(len(temp)):
              if i%2==0 and temp[i].find("select: service=IMWChannel[")!= -1:   #take only the <CHANNEL_UP> Pressed device 
                 string+=str(temp[i]+"\n*********************************************************************************\n")
                #print(temp[i],"\n*********************************************************************************\n")
       else:
            print("Mar****************************************************************************\n")
            checkPattern=re.search(pattern2,zapData)
            if checkPattern==None:
               print("Not found")
               
            x=zapData.split(pattern2) #break the string with this keyword
            
               
            temp=[]
            for i in range(len(x)):
                temp.append(x[i].split(pattern1)[0]) #this will break the string further

       
            for i in range(len(temp)):
                if i%2==0 and temp[i].find("select: service=IMWChannel[")!= -1:   #take only the <CHANNEL_UP> Pressed device 
                   string+=str(temp[i]+"\n*********************************************************************************\n")
                   #print(temp[i],"\n*********************************************************************************\n")
        """
    defaultPattern=["select: service=IMWChannel[","AV_VideoStop","startPMTMonitoring for service locator","PMT monitoring event (","call UniversalClient_DVB_NotifyPMT with","UniversalClientSPI_Stream_OpenFilter","received first ecm","AV_VideoPlay(","[HALCALL]:000 - DSC_open(","AV_VideoFirstFrameDisplayedCallback"]
    
    
    #defaultPattern1=["select: service=IMWChannel[","AV_VideoStop","startPMTMonitoring for service locator","WAIT_PMT: Received PMT monitoring event (","AV_VideoPlay","AV_VideoFirstFrameDisplayedCallback"]
    indexTocalculateDefaultTime=["select: service=IMWChannel[","AV_VideoStop","startPMTMonitoring for service locator","PMT monitoring event (","AV_VideoPlay(","AV_VideoFirstFrameDisplayedCallback"]
    indexToCalculateCA=["PMT monitoring event (","call UniversalClient_DVB_NotifyPMT with","UniversalClientSPI_Stream_OpenFilter","received first ecm","[HALCALL]:000 - DSC_open(","AV_VideoFirstFrameDisplayedCallback"]
    
    (timeElapseWithDefaultStep,deltaTimeWithDefaultStep,timeElapseforCA,deltaTimeWithCA)=patternSearchingAndStoringInOutArray(indexTocalculateDefaultTime,indexToCalculateCA,defaultPattern,Data,channnel_num)

    if len(timeElapseWithDefaultStep)==0:
        print("Noting is there")
        return       

    
    """
    for i in range(len(out)):
        print(out)
    """
    
  
    """
    if len(out)>0 and checkPattern==None and Manual==1:
       errorMsgPatternManual()
       return
    elif len(out)>0 and checkPattern==None and Manual==2:
         errorMsgPatternAutoZaping()
         return
    if len(out)==0 and checkPattern==None:
        errorMsgPattern()
        return
    """
    """ for i in range(0,len(out[0])):
        res=[] 
        res1=[]   # it will contain the result for the each pattern
        sum=0
        for j in range(1,len(indexTocalculateDefaultTime)):
            sum+=out[indexTocalculateDefaultTime[j]][i]-out[indexTocalculateDefaultTime[j-1]][i]
            x=out[indexTocalculateDefaultTime[j]][i]-out[0][i]
            res1.append(x)
            res.append(out[indexTocalculateDefaultTime[j]][i]-out[indexTocalculateDefaultTime[j-1]][i]) # calculating the difference between each pattern
   
        timeElapseWithDefaultStep.append(res1)
        deltaTimeWithDefaultStep.append(res)  # append the each row data into the result matrix


    for i in range(0,len(out[0])):
        res=[] 
        res1=[]   # it will contain the result for the each pattern
        sum=0
        for j in range(1,len(indexToCalculateCA)):
        
            x=out[indexToCalculateCA[j]][i]-out[0][i]
            res1.append(x)
            res.append(out[indexToCalculateCA[j]][i]-out[indexToCalculateCA[j-1]][i]) # calculating the difference between each pattern
     
        timeElapseforCA.append(res1)
        deltaTimeWithCA.append(res)  # append the each row data into the result matrix"""



    
    del Totalzaptime[:]
    for i in range(len(timeElapseWithDefaultStep)):
         Totalzaptime.append(timeElapseWithDefaultStep[i][-1])
    #print(Totalzaptime) 

   
    print("\n\n\n-----------------------\n")

    """
    print("This Data is been taken minMaxAvgforDefaultStep number of ",len(result)," iteration"
    print("_____________________________________________________\n")
    print(" Numbers are represented in milliseconds\n")
    print("\n")
    minMaxAvgforDefaultStep=[]  # Total is a 2D array with 3 rows and columns(number of pattern)

    minimum=[]  #will contain the minimum value each pattern from the result matrix
    maximum=[]  #will contain the maximum value each pattern from the result matrix
    average=[]  #will contain the average value each pattern from the result matrix


    for i in range(0,len(result[0])-1):
        avg=int(0)
        maxi=int(0)
        mini=int(50000)
        # finding minimum, maximum, and average from the result matrix
        for j in range(0,len(result)):
            avg+=int(result[j][i])       
            maxi=max(maxi,int(result[j][i]))
            mini=min(mini,int(result[j][i]))
        maximum.append(maxi)
        minimum.append(mini)
        avg/=len(result)
        average.append(avg)

      # variables to calculate the sum of each pattern in their respect one
    maxArraySum=0   
    minArraySum=0
    avgArraySum=0

    for i in range(len(maximum)):
        maxArraySum+=maximum[i]
        minArraySum+=minimum[i]
        avgArraySum+=average[i]

    #storing the sum in their respective array
    maximum.append(maxArraySum)
    minimum.append(minArraySum)
    average.append(avgArraySum)



    minMaxAvgforDefaultStep.append(maximum)
    minMaxAvgforDefaultStep.append(minimum)
    minMaxAvgforDefaultStep.append(average)

    for i in range(len(result)):
        print(result[i]

    print("\n")
    #print(defaultStepsDetail 
    print("Maximum,Minimum and Average data of each iteration\n\n")
    print("                                                                       Maximum      Minimum        Average\n")
    for j in range(0,len(minMaxAvgforDefaultStep[0])): 
        print(minMaxAvgforDefaultStep[0][j],"      ",minMaxAvgforDefaultStep[1][j],"        ",minMaxAvgforDefaultStep[2][j]
        print("-----------------------------------------------------------------------------------------------------------"

       
    """
    
    
    
    del minMaxAvgforDefaultStep[:]
    del minMaxAvgforCA[:]
    del MWsequence[:]
    
    calculateMinMaxAvg(timeElapseWithDefaultStep,deltaTimeWithDefaultStep,minMaxAvgforDefaultStep)
    calculateMinMaxAvg(timeElapseforCA,deltaTimeWithCA,minMaxAvgforCA)
    
    MWsequence.append(minMaxAvgforDefaultStep[-1])
    MWsequence.append(minMaxAvgforCA[-1])

    Totalzaptime=[]
    for i in range(len(timeElapseWithDefaultStep)):
        Totalzaptime.append(timeElapseWithDefaultStep[i][-1])
    totalZapTimeMx=0
    totalZapTimeMn=0
    totalZapSum=0   

    row=[]

    # calculating the data for MW sequnce
    for i in range(len(minMaxAvgforDefaultStep)-1):
         totalZapTimeMx+=minMaxAvgforDefaultStep[i][0]
         totalZapTimeMn+=minMaxAvgforDefaultStep[i][1]
         totalZapSum+=minMaxAvgforDefaultStep[i][2]
    row.append(totalZapTimeMx)
    row.append(totalZapTimeMn)
    row.append(totalZapSum)
    MWsequence.append(row)
    
    original_stdout = sys.stdout # Save a reference to the original standard output
    file1=open("zapResult.txt","w")   #open file
    sys.stdout=file1
    print("\n \n Total data of Min max and average\n")
    print("Step                             ; max   ; min   ; Avg \n")
    
    for i in range(len(minMaxAvgforDefaultStep)-1):
        print(defaultStepsDetail[i],"; ",minMaxAvgforDefaultStep[i][0],"; ",minMaxAvgforDefaultStep[i][1],"; ",minMaxAvgforDefaultStep[i][2])
        print("\n-----------------------------------------------------------------------------------\n")

    for i in range(len(minMaxAvgforCA)-1):
        print(CA_SequnceStepsDetail[i],"; ",minMaxAvgforCA[i][0],"; ",minMaxAvgforCA[i][1],"; ",minMaxAvgforCA[i][2])
        print("-----------------------------------------------------------------------------------\n")
    
    print("\n MW start sequence\n")
    for i in range(len(MWsequence)):
         print(MW_SequnceStepsDetail[i],"; ",MWsequence[i][0],"; ",MWsequence[i][1],"; ",MWsequence[i][2])
    
    print("\n\n_______________________________________________\n")
    print("Data of each iterarion starting from 1-----")
    print("\n__________________________________________________\n\n\n")

    for i in range(0,len(timeElapseWithDefaultStep)):
        print("\n***************************************")
        print("* ITERATION",i+1,"                        *")
        print("***************************************\n")
        print("Step                             ; Elapse   ; Delta \n")
        for j in range(0,len(timeElapseWithDefaultStep[0])):
            print(defaultStepsDetail[j],"; ",timeElapseWithDefaultStep[i][j],"   ;  ",deltaTimeWithDefaultStep[i][j])
            print("-----------------------------------------------------------------------------------|")
        print(defaultStepsDetail[-1],"    ",timeElapseWithDefaultStep[i][-1])
#    print("\niteration",i+1,"Done ____________________________\n")



    """ print("\n\n_______________________________________________\n")
    print("Data of each iterarion starting from 1-----")
    print("\n__________________________________________________\n\n\n")

    for i in range(0,len(timeElapseforCA)):
        print("\n***************************************")
        print("* ITERATION",i+1,"                        *")
        print("***************************************\n")
        print("Step                             ; Elapse   ; Delta\n ")
        for j in range(0,len(timeElapseforCA[0])):
            print(CA_SequnceStepsDetail[j],"; ",timeElapseforCA[i][j],"   ;  ",deltaTimeWithCA[i][j])
            print("-----------------------------------------------------------------------------------|")
    
    print("\n\n_______________________________________________\n")
    print("Data of each iterarion starting from 1-----")
    print("\n__________________________________________________\n\n\n") """

    sys.stdout.close()
    file1.close()
    sys.stdout=original_stdout
    return
    
    
   
    
    


        
        




       
