import random
import string

print('Password Generator')

password_length = int(input('Password Length: '))

lower = string.ascii_lowercase
upper = string.ascii_uppercase
num = string.digits
punct = string.punctuation

pot = lower + upper + num + punct

temp = random.sample(pot,password_length)

password = "".join(temp)

print('Password: ' + password)
