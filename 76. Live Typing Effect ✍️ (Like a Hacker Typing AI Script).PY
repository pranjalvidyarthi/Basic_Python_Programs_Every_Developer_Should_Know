# Live Typing Effect ✍️ (Like a Hacker Typing AI Script)
import time, sys

text = "Initializing Quantum AI Neural Protocol...\nConnecting to node: localhost:9001\nLogin: root\nAccess granted ✅\n \n Subscribe Pranjal Tech" 

for char in text:
    sys.stdout.write(char)
    sys.stdout.flush()
    time.sleep(0.05)
