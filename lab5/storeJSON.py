import sys
import time
import SmartDHT22
import SmartMCP3008
import SmartSound
import json

MCP=SmartMCP3008.SmartMCP3008()
DHT = SmartDHT22.SmartDHT22(18)
SS = SmartSound.SmartSound()
i=1
my_dict={}

while (i<=60):
    
    timestamp=i
    light = MCP.read(0)
    celsius = DHT.get_temp_celsius()
    fahrenheit = DHT.get_temp_fahrenheit()
    humidity = DHT.get_humidity()
    envelope = SS.get_envelope()
    
    # dummy json
    # timestamp=i
    # light=1
    # celsius=1
    # fahrenheit=1
    # humidity=1
    # envelope=1
    my_dict[i] = {'timestamp':timestamp,'light':light,'celsius':celsius,'fahrenheit':fahrenheit,'humidity':humidity,'envelope':envelope}
    print ("i: ", i)
    print ("light", light)
    print ("tempC",celsius)
    print ("humidity", humidity)
    print ("envelope", envelope)
    i=i+1
    time.sleep(60)
    


data=json.dumps(my_dict)
print(type(data))
print(data)

with open("testjson.json","w") as f:
    f.write(data)

print("donezo")


