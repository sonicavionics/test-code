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

# Initialize MCP2515 CAN Bus (No loopback, Not Silent)
can_bus = CAN(spi, cs, loopback=False, silent=False)

while True:
    # Create a CAN message with ID 0x123 and "hello world" data
    message = Message(id=0x123, data=b"hellobro", extended=False)

    # Send the message
    is_send_successful = can_bus.send(message)
    print("Send success:", is_send_successful)

    sleep(1)  # Wait before sending the next message
