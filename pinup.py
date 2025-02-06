import RPi.GPIO as GPIO
import time
import keyboard

try:
    # Set the GPIO mode
    print("Setting GPIO mode to BCM")
    GPIO.setmode(GPIO.BCM)

    # Define the GPIO pin number
    pin = 18
    print(f"Using GPIO pin {pin}")

    # Set up the GPIO pin as an output
    print(f"Setting up GPIO pin {pin} as an output")
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

    print("Press 't' to toggle the pin. Press 'q' to exit.")
    while True:
        if keyboard.is_pressed('t'):
            # Toggle the pin and print the new state
            new_state = toggle_pin(pin)
            print(f"Pin {pin} is now {'HIGH' if new_state else 'LOW'}")
            # Wait for a short period to avoid multiple toggles on a single key press
            time.sleep(0.5)
        elif keyboard.is_pressed('q'):
            print("Exiting program.")
            break
except KeyboardInterrupt:
    # Clean up GPIO settings before exiting
    GPIO.cleanup()
    print("Program terminated")
except Exception as e:
    # Print any other exceptions
    print(f"An error occurred: {e}")
    GPIO.cleanup()
finally:
    GPIO.cleanup()