import machine
from micropython import const
from machine import ADC
import array 
import time
import network
from machine import WDT
from umqtt.simple import MQTTClient

adc0=ADC(0)
phVolume = 0.0
phValue = 0.0
sensorValue = 0
sensorValue = 0
int(sensorValue)
float(phValue)
float(phVolume)
avgValue = 0
abs(avgValue)
temp = 0

buffer = array.array('i',[])
c = MQTTClient(b"client1",b"192.168.43.235")
c.connect()
 

def toomuchacid():
  print("WARNING! Too acidic")
  c.publish("acidity:","Water parameter too acidic")
  
def four_to_nine_range_display(phLevel):
  print("PH Level =",phLevel)  
  c.publish("acidity:","PH Level: {}".format(phLevel))
  

def main():
  print("nisulod nako")
  while True:
    for i in range(10):
      adc0.read()
      time.sleep(1)
      buffer.append(adc0.read())
      print("PH Sensor Reading in millivolts:",buffer[i])
    
    for x in range(9):
      for y in range(1,10):
        if (buffer[x] > buffer[y]):
          temp = buffer[x]
          buffer[x] = buffer[y]
          buffer[y] = temp

    avgValue = 0;

    for a in range(2,8):
      avgValue += buffer[a]
      print(avgValue)
    
    phVolume = (avgValue * 5.0 / 1024) /6
    phValue = -5.70 * phVolume + 21.35
    print("Volume:",phVolume)
    print("Value:",phValue)
   
    if(phValue>14):
      toomuchacid()
    else:
      four_to_nine_range_display(phValue)
    time.sleep(1) 

    



  
main()


