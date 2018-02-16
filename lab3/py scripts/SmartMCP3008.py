import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI
class SmartMCP3008:
    def __init__(self):
        self.mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(0,0))
    def read(self,pin_num):
        values =self.mcp.read_adc(pin_num)
        return values


