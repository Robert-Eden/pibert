
import serial
import re
import threading
import RPi.GPIO as GPIO
import time


def read_sheave(sheave, pc, stop_event):
    while not stop_event.is_set():
        try:
            if sheave.in_waiting > 0:
                message = sheave.readline().decode('utf-8', errors='replace').strip()
                # print(f"Sheave message: {message}")
                match = re.search(r"\$CC.(\d+\.\d)", message)
                if match:
                    pos = match.group(1)
                    # print(f"Position: {pos}")
                    pc.write(f"Position: {pos}\n".encode('utf-8'))
        except Exception as e:
            if not stop_event.is_set():
                # print(f"Sheave error: {e}")
                pass

def read_pc(pc, stop_event):
    while not stop_event.is_set():
        try:
            if pc.in_waiting > 0:
                message = pc.readline().decode('utf-8', errors='replace').strip()
                if message == "out":
                    # print("Paying out")
                    GPIO.output(17, GPIO.HIGH)
                    GPIO.output(27, GPIO.LOW)
                elif message == "in":
                    # print("Reeling in")
                    GPIO.output(27, GPIO.HIGH)
                    GPIO.output(17, GPIO.LOW)
                elif message == "stop":
                    # print("Halting Winch")
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(27, GPIO.LOW)
                else:
                    # print(f"Unknown command: {message}")
                    GPIO.output(17, GPIO.LOW)
                    GPIO.output(27, GPIO.LOW)
        except Exception as e:
            if not stop_event.is_set():
                # print(f"PC error: {e}")
                pass

def main():
    print("Starting Winch Control...")

    # GPIO setup
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.OUT)
    GPIO.setup(27, GPIO.OUT)
    GPIO.output(17, GPIO.LOW)
    GPIO.output(27, GPIO.LOW)
    print("GPIO pins initialized. Winch is stopped and ready for commands.")

    pc = serial.Serial('/dev/ttyS0', baudrate=9600, timeout=1)
    sheave = serial.Serial('/dev/ttyUSB0', baudrate=9600, timeout=1)
    print("Listening for RS232 messages from both sheave and PC...")
    stop_event = threading.Event()

    try:
        sheave_thread = threading.Thread(target=read_sheave, args=(sheave, pc, stop_event), daemon=True)
        pc_thread = threading.Thread(target=read_pc, args=(pc, stop_event), daemon=True)
        sheave_thread.start()
        pc_thread.start()
        while True:
            pass  # Keep main thread alive
    except KeyboardInterrupt:
        print("Exiting...")
        stop_event.set()
        sheave_thread.join()
        pc_thread.join()
    finally:
        GPIO.cleanup()
        pc.close()
        sheave.close()

if __name__ == "__main__":
    main()