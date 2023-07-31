import psutil
import time
import signal


def signal_handler(sig, frame):
    print("\nStopping the script...")
    exit(0)


# Set up the signal handler for 'Ctrl + C'
signal.signal(signal.SIGINT, signal_handler)

# import keyboard


# current network data
last_sent = psutil.net_io_counters().bytes_sent
last_received = psutil.net_io_counters().bytes_recv
last_total = last_sent + last_received

# updated network data

while True:
    bytes_sent = psutil.net_io_counters().bytes_sent
    bytes_received = psutil.net_io_counters().bytes_recv
    total_bytes = bytes_sent + bytes_received

    sent = bytes_sent - last_sent
    received = bytes_received - last_received
    total = total_bytes - last_total

    # converting to megabytes
    mb_sent = sent / 1024 / 1024
    mb_received = received / 1024 / 1024
    mb_total = total_bytes / 1024 / 1024

    print(
        f"{mb_sent:.2f} MB data sent,{mb_received:.2f} MB data received,{mb_total:.2f} MB total data"
    )

    last_sent = sent
    last_received = received
    last_total = total

    time.sleep(1)
