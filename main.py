import threading
import subprocess

def run_jetson_uart():
    subprocess.run(["python3", "Jetson_UART.py"])

def run_oled_emotion():
    subprocess.run(["python3", "OLED_emotion.py"])

# Create threads
thread1 = threading.Thread(target=run_jetson_uart)
thread2 = threading.Thread(target=run_oled_emotion)

# Start threads
thread1.start()
thread2.start()

# Wait for both threads to complete
thread1.join()
thread2.join()
