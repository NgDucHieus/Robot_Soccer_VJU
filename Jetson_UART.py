import pygame
import serial
import time

# from luma.core.interface.serial import i2c
# from luma.oled.device import ssd1306
# from luma.core.render import canvas
# import time
# serialOled = i2c(port=1, address=0x3C)  # Update the address if different
# device = ssd1306(serialOled)

# with canvas(device) as draw:
#     draw.text((0, 0), "Vietnam Japan University", fill="white")
# time.sleep(3)

# Initialize pygame
pygame.init()

# Set up the joystick
pygame.joystick.init()
if pygame.joystick.get_count() > 0:
    joystick = pygame.joystick.Joystick(0)
    joystick.init()
else:
    print("No joystick found.")
    exit()

# Set up the serial connection (adjust '/dev/ttyTHS1' to your specific port)
ser = serial.Serial('/dev/ttyACM0', 115200)
time.sleep(2)  # Wait for the serial connection to initialize

# Function to send a command to the Arduino
def send_command(command):
    ser.write(command.encode())
    print(f"Sent: {command}")

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if pygame.joystick.get_count() > 0:
        # Using D-pad (hat) to control motor 1 and motor 2
        hat = joystick.get_hat(0)
        if hat[1] == 1:  # Up
            send_command('U')  # Command to move motors 1 and 2 forward
        elif hat[1] == -1:  # Down
            send_command('D')  # Command to move motors 1 and 2 backward
        elif hat[0] == -1:  # Left
            send_command('L')  # Command to move motors 3 and 4 forward
        elif hat[0] == 1:  # Right
            send_command('R')  # Command to move motors 3 and 4 backward
        else:
            send_command('S')  # Command to stop all motors

   



        # Using button X for relay
        if joystick.get_button(3):  # Button X is typically button 3
            send_command('X')  # Command to toggle relay

        # Using button A for motor 5 forward
        if joystick.get_button(6):  # Button A is typically button 0
            send_command('M')  # Command to move motor 5 forward

        # Using button B for motor 5 backward
        if joystick.get_button(7):  # Button B is typically button 1
            send_command('N')  # Command to move motor 5 backward

        if joystick.get_button(8):  # Button A is typically button 0
            send_command('B')  # Command to move motor 5 forward

        # Using button B for motor 5 backward
        if joystick.get_button(9):  # Button B is typically button 1
            send_command('A')  # Command to move motor 5 backward


    # Delay to prevent spamming the serial connection
    time.sleep(0.1)

pygame.quit()
ser.close()