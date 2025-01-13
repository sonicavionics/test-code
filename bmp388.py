import time
import board
import adafruit_bmp3xx
import busio

i2c = busio.I2C(board.A3, board.A2)
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c, address=0x76)

while True:
    print("Pressure: {:6.1f}".format(bmp.pressure))
    print("Temperature: {:5.2f}".format(bmp.temperature))
    time.sleep(1)