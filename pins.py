import RPi.GPIO as GPIO
import time

# Pin numbers (BCM mode)
PIN_MAP = {
    '1': 20,
    '2': 21
}

GPIO.setmode(GPIO.BCM)
for pin in PIN_MAP.values():
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, GPIO.LOW)

try:
    while True:
        cmd = input("Enter 1 or 2: ").strip()
        if cmd in PIN_MAP:
            # Set all pins low first
            for pin in PIN_MAP.values():
                GPIO.output(pin, GPIO.LOW)
            # Set selected pin high
            GPIO.output(PIN_MAP[cmd], GPIO.HIGH)
            print(f"Pin {PIN_MAP[cmd]} set HIGH")
        else:
            print("Invalid input. Please enter 1 or 2.")
except KeyboardInterrupt:
    print("Exiting...")
finally:
    GPIO.cleanup()