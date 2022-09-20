import sys
from Zap_main import zapTime
from BootTime_main import BootTime 
from performance_main import CPU_util

      




def destroy(callto,Data,filename):
    
   
    print("destroy.......")
    if callto=="Boot": 
       return BootTime(Data,filename)
       
    elif callto=="Zap":
         return zapTime(Data,filename)
         

    elif callto=="Performance":
         return CPU_util(Data,filename)
   
      
