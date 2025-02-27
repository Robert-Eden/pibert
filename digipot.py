import smbus
import time

# Function to convert binary string to byte array
def binary_string_to_byte_array(binary_string):
    byte_array = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        byte_array.append(int(byte, 2))
    return byte_array

# Function to enable write operation on the AD5272
def enable_write_operation(bus, device_address):
    command_byte = 0x1C  # Command to enable write operation (0x1C is the command for enabling write)
    bus.write_byte(device_address, command_byte)
    print(f"Sent command to enable write operation: {bin(command_byte)}")

# Function to set the wiper position
def set_wiper_position(bus, device_address, position):
    command_byte = 0x04  # Command to write to the wiper register
    bus.write_byte_data(device_address, command_byte, position)
    print(f"Sent command to set wiper position: {bin(command_byte)}, position: {bin(position)}")

def main():
    # Initialize I2C bus
    bus = smbus.SMBus(1)  # Use I2C bus 1

    # I2C address of the AD5272 device
    device_address = 0x2F  # Replace with your device's I2C address

    # Enable write operation on the chip
    enable_write_operation(bus, device_address)

    for _ in range(2):
        # Set the wiper to one extreme (0x00)
        set_wiper_position(bus, device_address, 0x00)
        time.sleep(1)  # Wait 1 second

        # Set the wiper to the other extreme (0xFF)
        set_wiper_position(bus, device_address, 0xFF)
        time.sleep(1)  # Wait 1 second

    print("Operation completed successfully!")

if __name__ == "__main__":
    main()