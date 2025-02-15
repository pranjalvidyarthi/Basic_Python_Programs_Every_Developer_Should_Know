# Email validator
import re

email = input("Enter email: ")
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"

print('Valid Email' if re.match(pattern, email) else "Invalid Email")