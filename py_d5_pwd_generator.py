import random
import string

print("Welcome to the PyPassword Generator!")
letters = int(input("How many letters would you like in your password?\n"))
symbols = int(input("How many symbols would you like in your password?\n"))
numbers = int(input("How many numbers would you like in your password?\n"))
password=[]
pwd=""

for num in range (0,letters):
    password.append(random.choice(string.ascii_letters))

for num in range (0,numbers):
    password.append(random.choice(string.digits))

for num in range (0,symbols):
    password.append(random.choice(string.punctuation))

password2=random.sample(password,len(password))

for letter in range (0, len(password2)):
    pwd+=password2[letter]

print(f"Here's your password: {pwd}")