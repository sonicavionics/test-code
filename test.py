import board
import busio
import digitalio

# Create the SPI bus
spi = busio.SPI(board.GP20, board.GP19, board.GP18)

# Create a chip-select pin
cs = digitalio.DigitalInOut(board.GP17)
cs.direction = digitalio.Direction.OUTPUT
cs.value = True  # Deselect by default

# Prepare a buffer for reads (for example, 4 bytes)
read_buffer = bytearray(4)

# Lock the SPI and configure settings
while not spi.try_lock():
    pass
try:
    # Configure your SPI parameters: 
    # baudrate, polarity=0 or 1, phase=0 or 1
    spi.configure(baudrate=1_000_000, phase=0, polarity=0)
    
    # ----- Writing to SPI -----
    cs.value = False  # Assert CS (low)
    spi.write(b"\x9F")  # Example: send the 'Read ID' command
    cs.value = True   # De-assert CS (high)

    # ----- Reading from SPI -----
    cs.value = False  # Assert CS
    spi.readinto(read_buffer)  # read 4 bytes into read_buffer
    cs.value = True   # De-assert CS

finally:
    spi.unlock()

print("Read buffer:", read_buffer)
