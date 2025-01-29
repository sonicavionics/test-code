from time import sleep
import board
import busio
from digitalio import DigitalInOut
from adafruit_mcp2515.canio import Message
from adafruit_mcp2515 import MCP2515 as CAN

# Setup SPI and MCP2515 CS (Chip Select) pin
cs = DigitalInOut(board.GP17)
cs.switch_to_output()
spi = busio.SPI(board.GP22, board.GP19, board.GP20)

can_bus = CAN(spi, cs, loopback=False, silent=True)
