import board
import busio
import digitalio
import adafruit_mcp2515

CS_PIN = 28
cs = digitalio.DigitalInOut(board.GP17)
cs.direction = digitalio.Direction.OUTPUT
# SCK, MOSI, MISO
spi = busio.SPI(board.GP22, board.GP19, board.GP20)
mcp = adafruit_mcp2515.MCP2515(spi, cs)