import sys
import time
import SmartDHT22
import SmartMCP3008
import SmartSound

MCP=SmartMCP3008.SmartMCP3008()
DHT = SmartDHT22.SmartDHT22(18)
SS = SmartSound.SmartSound()
while True:
    print "MCP",MCP.read(0)
    print "celsius",DHT.get_temp_celsius()
    print "fahrenheit",DHT.get_temp_fahrenheit()
    print "humidity",DHT.get_humidity()
    print "gate",SS.get_gate()
    print "envlope",SS.get_envelope()
    print "audio", SS.get_audio()

    time.sleep(0.3)




