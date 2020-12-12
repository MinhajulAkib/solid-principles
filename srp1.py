#user registration module where the user data should be stored with in sqlite db and 
# if there is an error we need to log that error and also once the user has 
# been registered we would like to send a email.

import sqlite3
from sqlite3 import Error

class User:
    def RegisterUser(self,uname,passwd,email):
        con=sqlite3.connect('sqldb.db')
        sql="insert into Users values ('{0}','{1}','{2}')".format(uname,passwd,email)
        con.execute(sql)
        con.commit()
        print(f"User Registrattion with {uname} and {passwd}")

import syslog
class Logger:
    def WriteLogToSystem(self,message):
        syslog.syslog(syslog.LOG_ERR,message)



import json
import smtplib,ssl 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart      

class Email:
    def SendEmail(self,to_email,message_content,subject='User Registered'):
        with open('credentials.jsos') as f:
            data= json.load(f)
        smtp_server="smtp.gmail.com" 
        port=465
        sender_email=data["fromuser"]   
        password=data["password"]
        context=ssl.create_default_context()
        message=MIMEMultipart("alternative")


        message["From"] = sender_email
        message["To"] =to_email
        message["Subject=subject"]
        message_content=f'hello,<br/>message from helloworld:</b> <br/>
        {message_content} <br/> all the best <br/> best wishes,<br/>hellloworld support team'


        part=MIMEText(message_content,"html")
        message.attach(part)
        with smtplib.SMTP_SSL(smtp_server,port,context=xontext) as server:
            server.login(sender_email,password)
            server.sendmail(sender_email,message.as_string())

        print(f"mail send to{to_email}")    

class Registrations:
    def RegisterUser(self,uname.pwd,email):
        try:
            User().RegisterUser(uname,pwd,email)
            Email().SendEmail(email,'you have successfully registered')
        except Exception:
            Logger().WriteLogToSystem("error while registerUser")

r=Registrations()
r.RegisterUser('akib','minhaj','minhajakib@gmail.com')                