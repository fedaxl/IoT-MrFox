#!/usr/bin/python3
from gpiozero import MotionSensor
from picamera import PiCamera 
import requests
import time
import datetime
import storeFileFB

#import objectDetection
#import tensorflow as tf
#import cv2
#import numpy as np
#import sys

import firebase_admin
from firebase_admin import credentials, firestore, storage, db
import os

import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart


# Setup PIR sensor
pir = MotionSensor(4)

# Setup Pi Camera
camera = PiCamera()
camera.rotation = 180
camera.start_preview()
frame = 1 

# ThingSpeak get temperature data
link = "https://api.thingspeak.com/channels/1263705/fields/1/last?api_key=LX24RSBOHE6C83AB"
f = requests.get(link)
temp =  f.text

# Send an email with an attachment using SMTP

def send_mail(eFrom, to, subject, text, attachment):
    # SMTP Server details: update to your credentials or use class server
    smtpServer='smtp.mailtrap.io'
    smtpUser='e22a037b32e00d'
    smtpPassword='d4e9ca3601b15c'
    port=587

    # open attachment and read in as MIME image
    fp = open(attachment, 'rb')
    msgImage = MIMEImage(fp.read())
    fp.close()

    #construct MIME Multipart email message
    msg = MIMEMultipart()
    msg.attach(MIMEText(text))
    msgImage['Content-Disposition'] = 'attachment; filename="image.jpg"'
    msg.attach(msgImage)
    msg['Subject'] = subject

    # Authenticate with SMTP server and send
    s = smtplib.SMTP(smtpServer, port)
    s.login(smtpUser, smtpPassword)
    s.sendmail(eFrom, to, msg.as_string())
    s.quit()



while True:
    pir.wait_for_motion()

    fileLoc = f'/home/pi/mrfox/img/frame{frame}.jpg' # set location of image file and current time
    currentTime = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    camera.capture(fileLoc) # capture image and store in fileLoc
    text= f'Hi,\n the attached image was taken today at {currentTime}\n and for your record, the temperature is {temp}'
    send_mail('federica.fiorenza@gmail.com', '20091413@mail.wit.ie', 'Motion Detected',text, fileLoc)
    print(f'frame {frame} taken at {currentTime}') # print frame number to console
    storeFileFB.store_file(fileLoc)
    storeFileFB.push_db(fileLoc, currentTime)
    frame += 1

    pir.wait_for_no_motion()
    camera.stop_preview()
    time.sleep(5)


