import smbus
import time

# Function to convert binary string to byte array
def binary_string_to_byte_array(binary_string):
    byte_array = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        byte_array.append(int(byte, 2))
    return byte_array

def main():
    # Initialize I2C bus
    bus = smbus.SMBus(1)  # Use I2C bus 1

    # I2C address of the peripheral device
    device_address = 0x2F  # Replace with your device's I2C address

    # Ask the user for a binary message
    binary_message = input("Enter the binary message to send (1's and 0's): ")

    # Convert the binary message to a byte array
    byte_array = binary_string_to_byte_array(binary_message)

    # Send the byte array to the peripheral device
    for byte in byte_array:
        bus.write_byte(device_address, byte)
        time.sleep(0.1)  # Small delay between bytes

    print("Message sent successfully!")

if __name__ == "__main__":
    main()