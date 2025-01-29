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
mcp = adafruit_mcp2515.MCP2515(
    spi_bus=spi,
    cs_pin=cs_pin,
    baudrate=250_000
)

print("CAN Sender is ready...")

while True:
    # Construct a simple CAN message with ID=0x123 and data='Hello'
    message = Message(
        id=0x123,
        data=b'Hello',    # Up to 8 bytes of data
        extended=False    # False = standard (11-bit) ID
    )

    try:
        mcp.send(message)
        print("Sent: 'Hello'")
    except RuntimeError as e:
        print("Failed to send message:", e)

    time.sleep(1)
