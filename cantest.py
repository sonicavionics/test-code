import time
import board
import busio
import digitalio

import adafruit_mcp2515
from adafruit_mcp2515.canio import Message

# --- SPI Setup ---
# Adjust these pins as needed for your board
spi = busio.SPI(board.GP22, board.GP19, board.GP20)

cs_pin = digitalio.DigitalInOut(board.GP17)
cs_pin.direction = digitalio.Direction.OUTPUT

# Create MCP2515 object at 250 kbps
mcp = adafruit_mcp2515.MCP2515(spi_bus=spi, cs_pin=cs_pin, baudrate=250_000, silent=True)

print("CAN Receiver is ready...")

# Start listening for any CAN messages (no filtering here)

listener = mcp.listen(matches=None, timeout=1.0)

while True:
    # Attempt to receive a message
    message = listener.receive()
    if message is not None:
        # We got a message!
        print("Received message!")
        print("   ID:    0x{:X}".format(message.id))
        print("   Data:  ", message.data)
    else:
        # No message this loop
        time.sleep(0.1)
