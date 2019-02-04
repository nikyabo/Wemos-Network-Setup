# Wemos-Network-Setup
Network Monitoring System for Measuring the Multiparameter of Seawater Quality with Database using Django REST Framework Manual. A guide to set up your Wemos networking capabilities.

BEFORE EVERYTHING ELSE YOU NEED TO FLASH YOUR WEMOS TO MICRO PYTHON OS. GUIDE IS IN THIS LINK:
https://micropython-on-wemos-d1-mini.readthedocs.io/en/latest/setup.html

and Install Upycraft here:
https://randomnerdtutorials.com/install-upycraft-ide-windows-pc-instructions/

#### Welcome to Wemos Network Setup Guide by Nik Yabo ####

How do I setup the Wemos for connectivity?
- By setting up Wemos you need to make sure it is connected to a common access point. An access point in this context would mean WiFi connectivity. 

How do I use Wemos
How do I connect my Wemos to my Wifi? 
- Hover over networklink.py and change the variables

SSID = "YOUR NETWORK NAME"
password = "YOUR NETWORK PASSWORD"

if your network has no password just leave it blank. (" ")

After all that. The next thing to do is to configure IP Address of your broker. You need to first find your Broker's IP through CMD using ## ipconfig ## or ifconfig if in linux. 

then under the PH_sensor.py in your WEMOS 
c = MQTTClient(b"client1",b"192.168.43.235")

Change the IP Aaddress to your Broker's IP Address.

After you do this to all of your WEMOS Devices you should be able to see the values reflected upon your listener powershells started through in the executable file.

