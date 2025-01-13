import board
import busio
import time


# Initialize I2C with SCL, SDA
i2c = busio.I2C(board.A3, board.A2)

# Check if I2C is locked (ensure it's ready)
while not i2c.try_lock():
    pass

# Scan for I2C devices
devices = i2c.scan()

# Print the list of I2C devices connected or "Nothing found"
if devices:
    print("I2C devices found:", [hex(device) for device in devices])
else:
    print("Nothing found")

# Unlock the I2C bus after use
i2c.unlock()

