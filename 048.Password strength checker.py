# Pass strength checker
import re
password = input('Enter your password: ')
strength =0

if len(password) >= 8: strength += 1
if re.search(r'[A-Z]', password): strength += 1
if re.search(r'\d' , password): strength += 1
if re.search(r'[@$!%*?&]', password): strength += 1

print("Password Strength: ", ["Weak", "Moderate", "Strong"][min(strength,2)])
