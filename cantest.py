import time
import board
import busio
import digitalio
import adafruit_mcp2515
from adafruit_mcp2515.canio import Message

# Setup SPI and MCP25625

spi = busio.SPI(board.GP22, board.GP19, board.GP20)
cs = digitalio.DigitalInOut(board.GP17)
cs.switch_to_output()

mcp = adafruit_mcp2515.MCP2515(spi, cs, baudrate=500_000)

while True:
    try:
        mcp.send(Message(id=0x321, data=b'Hello'))
        print("Sent: Hello")
    except RuntimeError:
        print("Send failed")
    time.sleep(1)
