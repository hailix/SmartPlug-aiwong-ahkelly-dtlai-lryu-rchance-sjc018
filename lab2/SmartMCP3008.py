import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI
class SmartMCP3008:
    def __init__(self):
        self.p = 2
    def read(MCP3008,pin_num):
        values = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(0,0)).read_adc(pin_num)
        return values


