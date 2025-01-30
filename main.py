import random
import string


print("Alex's Password Generator")

response=input("Would you like a Password Generated? yes/no")

if response == "yes":
    password = ''.join(random.choices(string.ascii_letters+string.digits,k=10))
    
    print(f"Password: {password}")
    
else:
    print("Have a good day!")
