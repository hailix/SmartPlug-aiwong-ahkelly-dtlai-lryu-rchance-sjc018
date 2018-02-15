import Adafruit_MCP3008
import Adafruit_GPIO.SPI as SPI
import SmartMCP3008

GATE_THRESHOLD = 500

class SmartSound:
    def __init__(self):
        sMCP = SmartMCP3008.SmartMCP3008()
        self.mcp = sMCP
    def get_gate(self):
        gate = self.mcp.read(2)
        if (gate <= GATE_THRESHOLD):
            return 0
        else:
            return 1
    def get_envelope(self):
        envelope = self.mcp.read(3)
        return envelope
    def get_audio(self):
        audioval = self.mcp.read(4)
        return audioval

    

