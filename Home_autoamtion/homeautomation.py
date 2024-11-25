import serial
import time

# Replace 'COMX' with your Bluetooth COM port (e.g., COM3 for Windows or /dev/ttyUSBx for Linux/Mac)
bluetooth = serial.Serial("COMX", 9600) 
time.sleep(2)  # Wait for connection

def send_command(command):
    bluetooth.write(command.encode())  # Send command as bytes
    print(f"Command {command} sent.")

print("Home Automation via Bluetooth")
print("1: Turn ON Device 1")
print("2: Turn ON Device 2")
print("3: Turn ON Device 3")
print("4: Turn ON Device 4")
print("5: Turn OFF Device 1")
print("6: Turn OFF Device 2")
print("7: Turn OFF Device 3")
print("8: Turn OFF Device 4")
print("q: Quit")

while True:
    user_input = input("Enter command: ")
    if user_input == 'q':
        print("Exiting...")
        break
    elif user_input in ['1', '2', '3', '4', '5', '6', '7', '8']:
        send_command(user_input)
    else:
        print("Invalid command. Try again.")

bluetooth.close()
