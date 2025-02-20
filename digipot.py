# spitest.py
# A brief demonstration of the Raspberry Pi SPI interface, using the Sparkfun
# Pi Wedge breakout board and a SparkFun Serial 7 Segment display:
# https://www.sparkfun.com/products/11629

import time
import spidev

# We only have SPI bus 0 available to us on the Pi
bus = 0

# Device is the chip select pin. Set to 0 or 1, depending on the connections
device = 0

# Enable SPI
spi = spidev.SpiDev()

# Open a connection to a specific bus and device (chip select pin)
spi.open(bus, device)

# Set SPI speed and mode
spi.max_speed_hz = 50000000
spi.mode = 0

# Define the 16-bit data to send
data1 = bytearray([0b00000100, 0b00000000])  # 0000010000000000
data2 = bytearray([0b00000111, 0b11111111])  # 0000011111111111

try:
    while True:
        # Send the first byte array over SPI
        spi.writebytes(data1)
        print("Sent data: 0000010000000000")
        time.sleep(2)

        # Send the second byte array over SPI
        spi.writebytes(data2)
        print("Sent data: 0000011111111111")
        time.sleep(2)
except KeyboardInterrupt:
    print("Program terminated")
finally:
    # Clean up and close the SPI connection
    spi.close()

