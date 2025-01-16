```
git init
git remote add origin https://github.com/sonicavionics/test-code.git
git fetch origin
rm code.py sd/placeholder.txt settings.toml
git checkout -t origin/main
screen /dev/tty.usbmodem101 115200  
```

[Circuit python image](https://circuitpython.org/board/raspberry_pi_pico/)

[Adafruit_CircuitPython_MCP2515](https://github.com/adafruit/Adafruit_CircuitPython_MCP2515/tree/main)


    ls /dev/tty.usb*

    screen /dev/tty.usbmodem1101 115200

Reattach:

    screen -D -R                                                                           
