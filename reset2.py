from machine import Pin

def deinit_all_pins():
    for pin_num in range(41):  # Adjust range based on your board's pin count
        try:
            pin = Pin(pin_num)
            pin.init(Pin.IN)  # Reset pin to input (default safe state)
        except ValueError:
            # Ignore pins that don't exist on the board
            pass

# Call the function to reset all pins
deinit_all_pins()
