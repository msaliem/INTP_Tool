from email import message
import smtplib
import imghdr
from email.message import EmailMessage

from email.mime.multipart import MIMEMultipart #pip install email-to
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def fun():
    print('Workin in function to read data')
def mailDataOfSTB():
   
    try:
        print("Before the array.......")
        picPath=[r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\Boot_Data.jpg',r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\totalBootupData.jpg',
        r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\Across TP_HD-HD.jpg',
        r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\Across TP_HD-HDGraph.jpg',
        r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\Across TP_HD-SD.jpg',
        r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\Across TP_HD-SDGraph.jpg',
        r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\Across TP_SD-HD.jpg',
        r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\Across TP_SD-HDGraph.jpg',
        r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\Across TP_SD-SD.jpg',
        r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\Across TP_SD-SDGraph.jpg',
        r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\SummaryOfCPUMemoryJVM.jpg',r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\CPU.jpg',r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\Memory.jpg',r'C:\Users\mohd.saliem\Documents\PythonDev\HotFolder\Images\JVM.jpg']
        print("Working")
        picName=['Boot_Data.jpg','totalBootupData.jpg','Across TP_HD-HD.jpg','Across TP_HD-HDGraph.jpg','Across TP_HD-SD.jpg','Across TP_HD-SDGraph.jpg','Across TP_SD-HD.jpg','Across TP_SD-HDGraph.jpg','Across TP_SD-SD.jpg','Across TP_SD-SDGraph.jpg','SummaryOfCPUMemoryJVM.jpg','CPU.jpg','Memory.jpg','JVM.jpg']
        mailArray=['mohdsaleem12786@gmail.com']
        
        msg = EmailMessage()
        msg['Subject'] = 'STB performance details'
        #msg['From'] = 'mohd.saliem@irdeto.com'
        msg['From'] = 'iammohdsaliem@gmail.com'
        #msg['To'] = ['iammohdsaliem@gmail.com']
        msg['To'] = ['mohdsaleem12786@gmail.com','mohd.saliem@irdeto.com']
        text_part1 = msg.iter_parts()
        text_part1
        msg.add_alternative("""\
                            <!DOCTYPE html>
                            <html>
                            <body>
                            {%-fun()%}
                            <p style="font-size:15px">Hi All,</p><br>
                            <p style="font-size:15px">Please find all the attach file for STB peformance details</p><br>
                             """, subtype='HTML')
        text_part = msg.iter_parts()
        text_part
        msg.add_alternative("""\
                            <!DOCTYPE html>
                            <html>
                            <body>
                            {%-fun()%}
                            <p style="font-size:15px">Hi All,</p><br>
                            <p style="font-size:15px">Please find all the attach file for STB peformance details</p><br>
                            
                            
                            <p style="font-size:18px">Summary of boot time data</p>
                            <img src="cid:image1" alt='Summary of bootup data' /><br>

                            <p style="font-size:18px">Total bootup Time graph</p><br>
                            <img src="cid:image2" alt='Boot time graph' /><br>

                            <p style="font-size:18px">Zap time Summary </p><br>
                            <img src="cid:image3" /><br>

                            <p style="font-size:18px">Graph for total time for channel change</p><br>
                            <img src="cid:image4" /><br>

                            
                            <img src="cid:image5" /><br>

                            
                            <img src="cid:image6" /><br>

                           
                            <img src="cid:image7" /><br>

                            
                            <img src="cid:image8" /><br>

                            
                            <img src="cid:image9" /><br>

                            
                            <img src="cid:image10" /><br>

                            
                            <p style="font-size:18px">Summary of performance Data</p><br>
                            <img src="cid:image11" /><br>
                            <p style="font-size:18px">CPU performance graph</p><br>
                            <img src="cid:image12" /><br>
                            
                            <p style="font-size:18px">System Memory Graph</p>
                            <img src="cid:image13" /><br>
                            <p style="font-size:18px">JVM  graph</p><br>
                            <img src="cid:image14" /><br>

                            <h3>Note:- Please Note that this is just testing mail</h6><br>
                            <p>Thanks and regards,</p>
                            <p>Mohd Saliem</p>
                            </body>
                            </html>
                            """, subtype='HTML')
        counter=1
        for i in range(len(picPath)):
            try:
               img=open(picPath[i],"rb")
               msgImage = MIMEImage(img.read())
              
               img.close()
               msg.add_attachment(msgImage,filename=picName[i])
               # Define the image's ID as referenced above
               msgImage.add_header('Content-ID', '<image'+str(counter)+'>')
               msg.attach(msgImage)
               
               counter += 1
            except:
                print("File Not found")
                continue

        
        """ for i in range(len(picPath)):
            try:
                fp = open(picPath[i], 'rb')                                                    
                img_data=fp.read()
                img_subType=imghdr.what(fp.name)
                msg.add_attachment(img_data,maintype='image',subtype=img_subType,filename=picName[i])
                fp.close()
            except:
                print("file not found...")
                continue """
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login('iammohdsaliem@gmail.com', 'Mohd@098')
        server.send_message(msg)
        server.quit()
        print("mail done.............")
    except:
        print("connection not established")
        return
   


