import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BCM)

# Define the GPIO pin number
pin = 18

# Set up the GPIO pin as an output
GPIO.setup(pin, GPIO.OUT)

# Function to toggle the pin
def toggle_pin(pin):
    # Read the current state of the pin
    current_state = GPIO.input(pin)
    # Toggle the state
    new_state = not current_state
    # Set the new state
    GPIO.output(pin, new_state)
    return new_state

try:
    print("Starting the toggle loop. Press Ctrl+C to exit.")
    while True:
        # Toggle the pin and print the new state
        new_state = toggle_pin(pin)
        print(f"Pin {pin} is now {'HIGH' if new_state else 'LOW'}")
        # Wait for 1 second
        time.sleep(1)
except KeyboardInterrupt:
    # Clean up GPIO settings before exiting
    GPIO.cleanup()
    print("Program terminated")
except Exception as e:
    # Print any other exceptions
    print(f"An error occurred: {e}")
    GPIO.cleanup()
