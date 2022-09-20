from email import message
import smtplib
import imghdr
from email.message import EmailMessage

from email.mime.multipart import MIMEMultipart #pip install email-to
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
from pathlib import Path
import shutil
def fun():
    print('Workin in function to read data')
def mailDataOfSTB():
   
    try:
       
        myDir = Path(r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images')
        myDir1=Path(r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\\')
        fliname=None
        filePaths=None
        
        for file in myDir.iterdir():
            myDir = Path(r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images')
            res=[x[1] for x in os.walk(myDir)]

        result1=res[0]
        picPath=[]
        for i in range(len(result1)):
            if result1[i].endswith('Reference'):
               continue
            else:
                
               path1=Path(r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\\'+result1[i])
               picPath.append(path1)
               

        mailArray=['neha.vishan@irdeto.com']
        
         
        
        for i in range(len(picPath)):
            counter=1
            msg = EmailMessage()
            msg['Subject'] = 'STB performance details'
           # msg['From'] = 'mohd.saliem@irdeto.com'
            msg['From'] = 'mohd.saliem@irdeto.com'
            #msg['To'] = ['iammohdsaliem@gmail.com']
            msg['To'] = mailArray

            text_part = msg.iter_parts()
            text_part
            msg.add_alternative("""\
                            <!DOCTYPE html>
                            <html>
                            <body>
                            <p style="font-size:15px">Hi All,</p><br>
                            <p style="font-size:15px">Please find all the attach file for STB peformance details</p><br>
                            
                            <img src="cid:image1" alt='Summary of bootup data' /><br>

                            
                            <img src="cid:image2" alt='Boot time graph' /><br>

                            
                            <img src="cid:image3" /><br>

                            
                            <img src="cid:image4" /><br>

                            
                            <img src="cid:image5" /><br>

                            
                            <img src="cid:image6" /><br>

                           
                            <img src="cid:image7" /><br>

                            
                            <img src="cid:image8" /><br>

                            
                            <img src="cid:image9" /><br>

                            
                            <img src="cid:image10" /><br>

                            
                            
                            <img src="cid:image11" /><br>
                            
                            <img src="cid:image12" /><br>
                            
                            
                            <img src="cid:image13" /><br>
                            
                            <img src="cid:image14" /><br>

                            <h3>Note:- Please Note that this is just testing mail</h6><br>
                            <p>Thanks and regards,</p>
                            <p>Mohd Saliem</p>
                            </body>
                            </html>
                            """, subtype='HTML')
            
            for file in picPath[i].iterdir():
                filePath=file
                try:
               
                   img=open(filePath,"rb")
                   msgImage = MIMEImage(img.read())
              
                   img.close()
                   msg.add_attachment(msgImage,filename=file.name)
                   # Define the image's ID as referenced above
                   msgImage.add_header('Content-ID', '<image'+str(counter)+'>')
                   msg.attach(msgImage)
               
                   counter += 1
                except:
                   print(picPath[i])
                   print("File Not found")
                   continue

        
            try:
               server = smtplib.SMTP('smtp.outlook.com', 587)
               server.starttls()
               print('Connection done')
               server.login('mohd.saliem@irdeto.com', 'User4@123')
               print('login done')
               server.send_message(msg)
               print('Msg send......')
               server.quit()
               print("mail done.............")
            except:
               print('Connection failed')
            try:
               shutil.rmtree(picPath[i])
               print("Directory Deleted")
            except:
                print(picPath[i])
                print("Exception occur in deletion")
    except:
        print("connection not established")
        return
   


