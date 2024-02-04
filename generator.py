
import random

print("welcome to password generawtor")

text = "qwertyuiopasdfghjklzxcvbnm"

number = int(input("Amout of password you want to generate: "))

lenght = int(input("Amout of lenght: "))

print ("Here's your password")

for psw in range(number):
    passwords = ""
    for i in range(lenght):
        passwords += random.choice(text)

    print(passwords)