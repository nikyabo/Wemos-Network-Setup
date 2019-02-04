import gc
gc.collect()
import os
print("Entering Network ======")
import networklink_ph as nl
nl.connect()
print("Entering main Code ======")
import PH_sensor as mqtt
mqtt.main()



