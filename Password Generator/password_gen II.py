import string
import random
from csv import writer

def passgen():
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation

    Platform = input("Enter the platform:\n")
    pass_length = int(input("Enter the length of the password:\n"))

    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    s.extend(list(s4))

    random.shuffle(s)
    Password = "".join(random.sample(s, pass_length))
    print("Generated Password:", Password)

    passdata = [Platform, Password]
    with open('pass.csv', 'a', newline='') as f:
        writedata = writer(f)
        writedata.writerow(passdata)

# Call the function to generate a password and store it in the CSV file
passgen()
