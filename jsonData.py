import json
from pathlib import Path
from datetime import date
from tablePlot import zapTable,bootTable,performanceTable
from graph import plot
import time
import os
def createDirectory(path):
    try:
        os.makedirs(path)    
        print("Directory " , path ,  " Created ")
    except FileExistsError:
        print("Directory " , path ,  " already exists")
    return

def write_jsonForZap(new_data,projectName,useCase):
    try:
       path=r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images'
       path+='\\'+str(projectName)
       if createDirectory(path):
          print('directory created') 
       filePath=Path(r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\zapData.json')
    except:
        print('JSON file not found')
    try:
       file1=open(filePath,'r+')
    except:
       print('issue in opening the file')
       return

    try:  
        file_Data = json.load(file1)
    except:
        print('File is not loading')
        file_Data={}
    try:
       dateData={}
       jsonUsecase={}
       jsonUsecase[useCase]=new_data
       
       if projectName in file_Data.keys():
          
          if str(date.today()) in file_Data[projectName][-1]:
              print('Sam')
              file_Data[projectName][-1][str(date.today())][useCase]=new_data
          else:
              file_Data[projectName][-1][str(date.today())].append(jsonUsecase)

          #file_Data[projectName].append(dateData)
       else:
          print('Sam')
          dateData[str(date.today())]=jsonUsecase
          file_Data[projectName]=[dateData]  
          
    except:
        
        print('Issue in if statement')
        return
        
    file1.seek(0)
    if len(file_Data[projectName])>30:
        del file_Data[projectName][0]

        
    try:
       json.dump(file_Data, file1, indent = 4)
    except:
        print('Issue in dumping')

    if not projectName.endswith('Reference'):    
        referencekey=projectName+'Reference'   
        referenceData={} 
        try: 
          referenceDataDictionary=file_Data[referencekey][-1]
          for key in referenceDataDictionary:
              referenceData=referenceDataDictionary[key][useCase]
              break
        except:
            defaultValues=[0.00,0.00,0.00]
            for key in new_data:
                referenceData[key]=defaultValues
        """ referenceDataDictionary=file_Data[referencekey][-1]
        for key in referenceDataDictionary:
            referenceData=referenceDataDictionary[key][useCase]
            break """
        print("in JSON Dumping")
        zapTable(new_data,referenceData,useCase,projectName)
    file1.close()
    return


def write_jsonForBoot(new_data,projectName):
    try:
        path=r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images'
        path+='\\'+str(projectName)
        if createDirectory(path):
           print('directory created')
        filePath=Path(r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\bootData.json')    
        #First we load existing data into a dict.
        try:
           file1=open(filePath,"r+")
        except:
            print("Wrong file choosen")
        try:  
           file_Data = json.load(file1)
        except:
            print('File is not loading')
            file_Data={}
        print(projectName)
    
        try:
           if projectName in file_Data.keys():
              print('Sam')
              file_Data[projectName].append(new_data)
           else:
              file_Data[projectName]=[new_data]  
        except:
            print('Issue in if statement')
            return
        
        file1.seek(0)
        if len(file_Data[projectName])>30:
            del file_Data[projectName][0]
        try:
           json.dump(file_Data, file1, indent = 4)
        except:
            print('Issue in dumping')

        if not projectName.endswith('Reference'):    
           referencekey=projectName+'Reference'   
           referenceData={} 
           try: 
              referenceDataDictionary=file_Data[referencekey][-1]
              for key in referenceDataDictionary:
                  referenceData=referenceDataDictionary[key]
                  break
           except:
                defaultValues=[0.00,0.00,0.00]
                for key in new_data[str(date.today())]:
                    referenceData[key]=defaultValues
                    
           print(referenceData)
           
           bootTable(new_data[str(date.today())],referenceData,projectName)
        file1.close()   
           
    except:
        print('File Not found')


def write_jsonForPerformance(new_data,projectName):
    try:
        path=r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images'
        path+='\\'+str(projectName)
        if createDirectory(path):
           print('directory created') 
        filePath=Path(r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\performanceData.json')    
        try:
           file1=open(filePath,"r+")
        except:
            print("Wrong file choosen")
        try:  
           file_Data = json.load(file1)
        except:
            print('File is not loading')
            file_Data={}
        print(projectName)
    
        try:
           if projectName in file_Data.keys():
              file_Data[projectName].append(new_data)
           else:
              file_Data[projectName]=[new_data]  
        except:
            print('Issue in if statement')
            return
        
        file1.seek(0)
        if len(file_Data[projectName])>30:
            del file_Data[projectName][0]
        try:
           json.dump(file_Data, file1, indent = 4)
        except:
            print('Issue in dumping')

        if not projectName.endswith('Reference'):    
           referencekey=projectName+'Reference'   
           referenceData={}
           try: 
              referenceDataDictionary=file_Data[referencekey][-1]
              for key in referenceDataDictionary:
                  referenceData=referenceDataDictionary[key]
                  break
           except:
                defaultValues=[0.00,0.00,0.00]
                for key in new_data[str(date.today())]:
                    referenceData[key]=defaultValues
           #print(referenceData)
           
           performanceTable(new_data[str(date.today())],referenceData,projectName)
        file1.close()
    except:
        print('File Not found')



def write_json(new_data,projectName,testFor):
    print("before the open file")
    try:
        if testFor == "Boot":
           filePath=Path(r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\bootData.json')
        elif testFor == "Zap":
             filePath=Path(r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\zapData.json')
        elif testFor =="Performance":
            filePath=Path(r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\performanceData.json')
        else:
            print("wrong test excution")
            return

        
        

        
            #return
        #First we load existing data into a dict.
        print(new_data)
        try:  
           file_Data = json.load(file1)
        except:
            print('File is not loading')
            file_Data={}
        print(projectName)
    
        try:
           if projectName in file_Data.keys():
              print('Sam')
              file_Data[projectName].append(new_data)
           else:
              file_Data[projectName]=[new_data]  
        except:
            print('Issue in if statement')
            return
        
        file1.seek(0)
        if len(file_Data[projectName])>30:
            del file_Data[projectName][0]
        try:
           json.dump(file_Data, file1, indent = 4)
        except:
            print('Issue in dumping')
        
        
    except:

        print("Json file not found")
    return