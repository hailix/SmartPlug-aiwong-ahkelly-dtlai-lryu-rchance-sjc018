import sys
import time
import SmartDHT22
import SmartMCP3008

DHT = SmartDHT22.SmartDHT22(4)
MCP = SmartMCP3008.SmartMCP3008()

while True:
    print "1",MCP.read(2)
    print "2",DHT.get_temp_celsius()
    print "3",DHT.get_temp_fahrenheit()
    print "4",DHT.get_humidity()

    time.sleep(60)




