from time import sleep
import board
import busio
from digitalio import DigitalInOut
from adafruit_mcp2515.canio import Message, RemoteTransmissionRequest
from adafruit_mcp2515 import MCP2515 as CAN

# Setup SPI and MCP2515 CS (Chip Select) pin
cs = DigitalInOut(board.GP17)
cs.switch_to_output()
spi = busio.SPI(board.GP22, board.GP19, board.GP20)

# Initialize MCP2515 CAN Bus in active listening mode
can_bus = CAN(spi, cs, loopback=False, silent=False)  # Active mode for real CAN bus

print("CAN Listener Started... Waiting for messages")

while True:
    with can_bus.listen(timeout=10) as listener:
        message_count = listener.in_waiting()

        if message_count > 0:
            print(f"{message_count} message(s) received")
    with can_bus.listen(timeout=10) as listener:

        for _ in range(message_count):
            msg = listener.receive()

            print("Message from:", hex(msg.id))

            if isinstance(msg, Message):
                print("Message data:", msg.data.decode(errors='ignore'))  # Decode if it's text
            elif isinstance(msg, RemoteTransmissionRequest):
                print("RTR Request - Expected Length:", msg.length)

    sleep(1)  # Small delay to avoid excessive CPU usage
