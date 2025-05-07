import time
from collections import defaultdict
from datetime import datetime
import os

LOG_FILE = 'requests.log'
THRESHOLD = 30  # requests in 5 seconds
INTERVAL = 5

# Ensure the log file exists
if not os.path.exists(LOG_FILE):
    with open(LOG_FILE, 'w') as f:
        pass  # Create the file if it doesn't exist

def monitor():
    print("👁️ Starting DDoS detector...")
    seen = set()

    while True:
        ip_counter = defaultdict(int)
        now = time.time()

        with open(LOG_FILE, 'r') as f:
            lines = f.readlines()

        for line in lines:
            ip, timestamp_str = line.strip().split(',')
            timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S').timestamp()

            if now - timestamp <= INTERVAL:
                ip_counter[ip] += 1

        for ip, count in ip_counter.items():
            if count > THRESHOLD and ip not in seen:
                seen.add(ip)
                print(f" DDoS DETECTED from {ip} — {count} requests in {INTERVAL} seconds")
                print(f"Blocking IP: {ip} (simulated)")

        time.sleep(INTERVAL)

monitor()
