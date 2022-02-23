import smtplib
import numpy as np
from email.message import EmailMessage
from PyPDF2 import PdfFileReader

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import numpy as np

file=open('msg.txt',mode='r')
msg=file.read()#takes message in text
file.close()

temp=np.loadtxt('receivers.txt',dtype='str',delimiter=",")#takes all words in receivers.txt and converts to a matrix depending on "," symbol
receivers=temp[:]

for info in receivers:
    mailaccounts=info[0]
    names=info[1]
    print(mailaccounts)

    message=MIMEMultipart()#used MIME (Multipurpose Internet Mail Extensions) , you can send pdf , word , excel , sound files with MIME
    message['Subject']='white your subject here'
    message['From']='put your mail address here'
    message['to']=mailaccounts
    message.attach(MIMEText("Dear "+names+" ;\n"+msg, "plain"))

    with open('PDF_files/'+names+'.pdf', "rb") as f:
        attach = MIMEApplication(f.read(), _subtype="pdf")
    attach.add_header('Content-Disposition', 'attachment', filename=str(names))
    message.attach(attach)


    mail=smtplib.SMTP("smtp.gmail.com",587)
    mail.ehlo()#Introducing ourselves to gmail
    mail.starttls()# encrypt our gmail username and password

    mail.login("put your mail address here","put your mail password here")
    mail.send_message(message)

#for make this code work you need to go this link and activate your mail sender account to 3rd party programs to send mails from email.

#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbXNrSnpJREVPc0lsdGR1a2ZjMkhWMExOTUpXQXxBQ3Jtc0trczVPNG0xeGsyczVTVExjT0tielRIMmlfVWh4YnZuTzNuWHl4cnI3YmdqYURwcHpvTjhIVDZTdFJINFg3RUlzTnd4SHpjTnN0XzNyY0tvcTlSNEZGR1ZGeEtITHc2dGJBZVFyR0tOTzI3c1cxZ1dIYw&q=https%3A%2F%2Fwww.google.com%2Fsettings%2Fsecurity%2Flesssecureapps































































"""
import smtplib
import numpy as np
from email.message import EmailMessage

file=open('C:/Users/ipproo/PycharmProjects/Sending_mail_with_PDF/msg.txt',mode='r')
msg=file.read()
file.close()


subject='ahhh'
content=f'Subject:{subject}\n\n{msg}'
receiver="fatihcan55666@gmail.com"

mail=smtplib.SMTP("smtp.gmail.com",587)
mail.ehlo()#Introducing ourselves to gmail
mail.starttls()# encrypt our gmail username and password

mail.login("yaybabyyay66@gmail.com","fatihatice07")
mail.sendmail("yaybabyyay66@gmail.com",receiver,content)

#for make this code work you need to go this link and activate your mail account to 3rd party programs send mails from email.
#https://www.youtube.com/redirect?event=video_description&redir_token=QUFFLUhqbXNrSnpJREVPc0lsdGR1a2ZjMkhWMExOTUpXQXxBQ3Jtc0trczVPNG0xeGsyczVTVExjT0tielRIMmlfVWh4YnZuTzNuWHl4cnI3YmdqYURwcHpvTjhIVDZTdFJINFg3RUlzTnd4SHpjTnN0XzNyY0tvcTlSNEZGR1ZGeEtITHc2dGJBZVFyR0tOTzI3c1cxZ1dIYw&q=https%3A%2F%2Fwww.google.com%2Fsettings%2Fsecurity%2Flesssecureapps
"""




























