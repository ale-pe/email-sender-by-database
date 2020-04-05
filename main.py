emailsender = input("Email (Gmail Only) ?") #Gmail Only
emailpassword = input("Password Account Email ?")
emailsubject = input("Email subject ?")



import sqlite3
import smtplib
from email.message import EmailMessage
import os.path
from os import path
if str(path.exists('data.txt')) == "False":
    print("No data.txt file found in the folder")
    exit()
if str(path.exists('base.db')) == "False":
    connection = sqlite3.connect('base.db')
    cursor = connection.cursor()
    connection.commit()
    cursor.execute('CREATE TABLE base (name TEXT, email TEXT)')
    connection.commit()

connection = sqlite3.connect('base.db')
cursor = connection.cursor()
connection.commit()


with open('data.txt', 'r') as file:
    data = file.read()


cursor.execute('SELECT name, email FROM base')
ids_and_urls = cursor.fetchall()
for row in ids_and_urls:
    print ("ID: {}".format( row[0] ))
    print ("URL: {}".format( row[1] ))

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    msg = EmailMessage()
    msg["From"] = emailsender
    msg["Subject"] = emailsubject
    msg["To"] = row[1]
    msg.set_content("Hello "+row[0]+",\n"+data)
    s.login(emailsender, emailpassword)
    s.send_message(msg)

