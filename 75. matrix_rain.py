# matrix_rain.py
import random
import time
import os

chars = "01"
width = os.get_terminal_size().columns

try:
    while True:
        line = ''.join(random.choice(chars) for _ in range(width))
        print("\033[92m" + line)  # Green color
        time.sleep(0.05)
except KeyboardInterrupt:
    pass
