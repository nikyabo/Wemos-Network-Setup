def connect():
    import network
    ssid = "Endeavor"
    password ="dzapanta1"
    station = network.WLAN(network.STA_IF)
    if station.isconnected() == True:
        print("Already connected")
        print("Acidity Loaded")
        return
    station.active(True)
    station.connect(ssid, password)
    while station.isconnected() == False:
        pass
    print("Connection successful")
def disconnect():
  import network
  station = network.WLAN(network.STA_IF)
  station.disconnect()
  station.active(False)
  print(station.ifconfig())





