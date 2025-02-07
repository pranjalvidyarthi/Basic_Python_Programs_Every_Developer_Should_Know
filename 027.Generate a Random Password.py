# Generate a random password
import random
import string

length = int(input('enter password lenght: '))
chars = string.ascii_letters + string.digits + string.punctuation
password = "" .join(random.choice(chars) for _ in range(length))

print('Generated password: ', password)
