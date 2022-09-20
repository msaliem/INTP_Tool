
import threading
import time
import os
import schedule
from destroyWin import destroy
from sentMail import mailDataOfSTB
from pathlib import Path
from jsonData import zapTable
import json

def getJsonData(projectName):
     try:
        filePath=Path(r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\zapData.json')
     except:
         print('JSON file not found')
     try:
        file1=open(filePath,'r+')
     except:
        print('issue in opening the file')
        return
     print('commining in getJsonData function')
     try:
        file_Data = json.load(file1)
     except:
         print('Not working file load')
     dic=file_Data[projectName][-1]
     new_data={}
     for DateKey in dic:
          new_data=dic[DateKey]
          break
     referenceDataDictionary={}
     referenceData={}
     referencekey=str(projectName)+'Reference'
     if referencekey in file_Data.keys():
        for key in file_Data[referencekey][-1]:
            referenceDataDictionary=file_Data[referencekey][-1][key]
            break   
     else:
         defaultValues=[0,0,0]
         for key in new_data:
             referenceDataDictionary[key]=referenceData
             for tp in new_data[key]:
                 referenceDataDictionary[key][tp]=defaultValues 

     print(referenceDataDictionary)        
     
     for useCase in new_data:
         zapTable(new_data[useCase],referenceDataDictionary[useCase],useCase,projectName) 
     
     return

def schedulingMain(main_frame):
    
    def hotFolderPickup(lock):
        
        try:
            
            myDir = Path(r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\File_pickup')
            fliname=None
            filePaths=None
            for file in myDir.iterdir():
                #print(file)
                if file.name.startswith("Boot") or file.name.startswith("Zap") or file.name.startswith("Performance"):
                    callto=file.name.split('_')[0]
                    filename=file.name
                    filePaths=file
                    try:
                        file=open(filePaths,encoding="cp437", errors='ignore')
                        data=file.read()
                        file.close()
                        destroy(callto,data,filename)
                        print("comming back")
                        try:
                           os.remove(filePaths)
                           print('Zap file deleted')
                           
                           time.sleep(3)
                           
                        except:
                            print('Zap file is not getting deleted')
                            time.sleep(3)    

                    except:
                        return
                
                else:
                    break   
                 

        except IOError:
               return


    
       
        
                     


    lock=threading.Lock()
  
    
    while True:
        #hotFolderPickup(lock)
        schedule.run_pending()
        #schedule.every(20).seconds.do(mailDataOfSTB)
        schedule.every().day.at("13:26").do(mailDataOfSTB)
        hotFolderPickup(lock)

        time.sleep(2)



   
    

    


