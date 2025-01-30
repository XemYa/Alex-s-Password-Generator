import random
import string


print("Alex's Password Generator")

response=input("Would you like a Password Generated? yes/no")

if response == "yes":
    passwords = []
    for _ in range(5):
        password = ''.join(random.choices(string.ascii_letters + string.digits,k=10))
        passwords.append(password)

    print("Generated passwords:")
    print(passwords)
else:
    print("Have a good day!")
