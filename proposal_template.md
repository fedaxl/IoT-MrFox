# IoT Based Fox Monitoring System using Raspberry PI 3B+
#### Student Name: Federica Fiorenza   Student ID: 20091413

This project presents an idea to design a Smart Outdoor Monitor System to detect the presence of a recurring visitor in the garden, a Fox, using motion sensors and a PI Noir camera and transmits also outdoor weather conditions to all the subscribers.
Analytics will be build on top of the data collected (pictures and timestamp) to understand the habits and pattern of our visitor (Mr. Fox). It's not excluded that this project can be expanded to detected unwanted visitor and send an immediate notification via mobile and activate red led lights on RPI and sound. 

The images will be stored in a cloud service and then published into a website and processed with TensorFlow (open-source software library for machine learning).
Ideally, if any Fox gets detected on camera, the subscriber will receive a POST notification and main user will be able to control the Raspberry PI using a Telegram Bot.  

## Tools, Technologies and Equipment

Raspberry PI 3B+ 
Waterproof RPI Case
PI Noir camera
Motion Sensor
SenseHat (currently researching if this can add value to the project)
PowerBank for power supply (when outdoor)
Telegram BOT API (for activating remotely the RPI)
Amazon Cloud Drive for storage (https://ifttt.com/applets/fFCWiGxS-save-photos-to-amazon-cloud-drive?term=publish%20to%20instagram%20from%20cloud%20service)
(with possibility to publish photos on Instagram)
or Google Cloud Services
Google API for Live streaming: https://developers.google.com/youtube/v3/live/docs/liveStreams
YouTube service
TensorFlow for AI image learning (recognizing a fox - or a person in phase 2 of this project)
Website built in ReactJS 
Programming languages: Python, JavaScript, HTML, CSS, JSON with REST API) 
node-RED 
MQTT
ThingSpeak
IFTTT
RapidAPI 

## Project Repository
https://github.com/fedaxl/IoT-MrFox.git (currently private)


