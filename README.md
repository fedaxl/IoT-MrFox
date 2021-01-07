# IoT Based Fox Monitoring System using Raspberry PI 3B+
#### Student Name: Federica Fiorenza   Student ID: 20091413

This project presents an idea to design a Smart Outdoor Monitor System to detect the presence of a recurring visitor in the garden, a Fox, using motion sensors and a PI Noir camera and transmits also outdoor weather conditions to all the subscribers.

In future developments, analytics will be build on top of the data collected (pictures and timestamp) to understand the habits and pattern of our visitor (Mr. Fox). It's not excluded that this project can be expanded to detected unwanted visitor and send an immediate notification via mobile and activate red led lights on RPI and sound. 
Currently the project has been rebuild using node-red console in order to use Tensorflow for image recognition. The model in use is Coco SSD, which is trained to recognize several objects, including a person, a cat, a dog to name few, but it's not trained to recognize a fox. 

The images will be stored in a cloud service and then published into a website and processed with TensorFlow (open-source software library for machine learning).
Ideally, if any Fox gets detected on camera, the subscriber will receive an email notification.  

## Tools, Technologies and Equipment

* Raspberry PI 3B+ 
* Waterproof RPI Case
* PIR sensor module (Parallax Inc 555-28027)
* female-to-female jumper wires x 3
* PI Noir camera
* Mini Black Hat Hack3r (assembled) + ribbon
* SenseHat
* PowerBank for power supply (outdoor)
* Power Supply for Raspberry Pi 3 5.1V 2.5A 

* Firebase DB
* TensorFlow for image recognition
* node-red
* Mailtrap
* ThingSpeak
* Met Eireann API

* Website built in HTML,CSS,JS
* Programming languages: Python, JavaScript, HTML, CSS, node.js, JSON) 
* 000webhost provider (to host the website)

![](https://i.ibb.co/SJStpR2/overall.png)

## Project Repository
https://github.com/fedaxl/IoT-MrFox.git

## Project Website
Click on Project to view the Demo page
https://mrfox26445.000webhostapp.com/

![](https://i.ibb.co/vQ4hchp/website.png)

## Development - Phase 1 TensorFlow
In the first phase of this project I was able to recreate and complete the following feature in the project: have ThingsSpeak read data from the SenseHat, detect motion with the PIR sensor, take a photo with the pi noir camera and store it to Firebase (RealTime Database and Database Storage) and get all the subscriber notfied by email (from SMTP server Mailtrap) when this is happening.
Due to several attempts to install Tensorflow correctly in the Pi and after successfully complete this part, due to an increasing of memory error when attempting to use Tensorflow (Coco SSD model was saved locally in the Pi), the need to look for alternative was real. 

![](https://i.ibb.co/KKGXsrb/project.png)

## Development - Phase 2 Node-Red
In order to use Tensorflow to recognize images, I diverted to node-red [https://nodered.org/docs/getting-started/raspberrypi]. 

To install Node-RED on a Raspberry Pi you can run the following command:
>bash <(curl -sL https://raw.githubusercontent.com/node-red/linux-installers/master/deb/update-nodejs-and-nodered)

The script will run for about 20 min, it will remove any previous version, check Node.js and install teh new version of Node-Red using npm
The install script for the Pi also sets it up to run as a service. This means it can run in the background and be enabled to automatically start on boot.

The following commands are provided to work with the service:

* node-red-start - this starts the Node-RED service and displays its log output. Pressing Ctrl-C or closing the window does not stop the service; it keeps running in the background
* node-red-stop - this stops the Node-RED service
* node-red-restart - this stops and restarts the Node-RED service
* node-red-log - this displays the log output of the service

<dl>
 <dt>http://hostnamehere:1880</dt>
 <dd>node-red console will run locally on port 1880</dd>
</dl>

From the node-red console it's then possible to create a flow and add different module, in my case I've been using the following command to install TensorFlow Coco SSD model:
* TensorFlow[https://flows.nodered.org/node/node-red-contrib-tensorflow]:  npm install node-red-contrib-tensorflow  

For additional guidance, check: https://github.com/kazuhitoyokoi/node-red-contrib-tensorflow

![](https://i.ibb.co/sb2vsRW/node-red.png)

## Considerations
If I had to start this project again, I'd probably consider to integrate the project from the beginning with node-red. 
There are couple of modules, such Firebase Storage, that in console are throwing several errors but I believe once integrating with SDK it should be easier.
I was able to test Firebase in Node-Red console installing a module for Realtime Database, although the plugin contained a bug (JSON credentials project id did not match the format of the database name)
With TensorFlow I was able to test correctly image recognitions, although I did not run a test with a real fox (as the model was not trained for that), I was able to complete all test correctly when showing a picture of a dog or other objects.


