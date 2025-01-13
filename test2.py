import time
import board
import adafruit_bmp3xx
import busio
i2c = busio.I2C(board.A3, board.A2)
bmp = adafruit_bmp3xx.BMP3XX_I2C(i2c)