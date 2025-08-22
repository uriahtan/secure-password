import hashlib
import requests
import secrets 
import string
import math

def check_password():
    password = input("Enter password: ")

    # compute sha1 hash of password
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    
    # obtain first 5 characters of password to check against the Have I been Pwned API
    prefix = sha1_hash[:5]

    # obtain remaining characters to check if password shows up in the database
    suffix = sha1_hash[5:]
    # print(prefix)
    # print(suffix)
    # print(type(suffix))

    # Have I been Pwned API
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    response = requests.get(url)

    # Write passwords that match the prefix to a text file
    with open("matches.txt", "w") as f:
        f.write(response.text)

    count = 0
    with open("matches.txt", "r") as f:
        for line in f:
            if suffix in line:
                strip = line.strip()
                split = strip.split(":")
                count = int(split[1])
                break
        
    if count >= 1000000:
        print(f"Your password has appeared {count} times in database leaks! Please change your password as soon as possible!")
    elif count >= 100000:
        print(f"Your password has appeared {count} times in database leaks! Please change your password as soon as possible!")
    elif count >= 10000:
        print(f"Your password has appeared {count} times in database leaks! Please change your password as soon as possible!")
    elif count >= 1000:
        print(f"Your password has appeared {count} times in database leaks! Please change your password as soon as possible!")
    elif count >= 100:
        print(f"Your password has appeared {count} times in database leaks! Please change your password as soon as possible!")
    elif count >= 10:
        print(f"Your password has appeared {count} times in database leaks! Please change your password within the next")
    elif count == 0:
        print("Your password did not appear in the Have I been Pwned database!\n It is safe for you to keep using your password")


def generate_password():
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?"
    characters = string.ascii_letters + string.digits + symbols
    passw = ""
    for a in range(15): 
        passw += secrets.choice(characters) 
        # print (secrets.choice(characters))
    
    passw_array = []
    for e in passw:
        passw_array += e

    lower_alphabet_count = 0
    upper_alphabet_count = 0
    number_count = 0
    symbol_count = 0

    print(f"Array {passw_array}")
    for b in range(len(passw_array)):
        if passw_array[b] in string.ascii_letters:
            if passw_array[b].islower() == True:
                lower_alphabet_count += 1
            else:
                upper_alphabet_count += 1
        elif passw_array[b] in string.digits:
            number_count += 1            
        else:
            symbol_count += 1
        
    print(f"lower abc: {lower_alphabet_count}, upper abc: {upper_alphabet_count}, number: {number_count}, symbols: {symbol_count}")

    did_not_meet_req = 0
    if lower_alphabet_count == 0 or upper_alphabet_count == 0 or number_count == 0 or symbol_count == 0:
        did_not_meet_req += 1
        generate_password()
    else:
        print(f"Did not meet reqs {did_not_meet_req} times")
        print(f"Generated password: {passw}")

def calculate_entropy():
    password = input("Enter your password: ")
    length = len(password)
    # password_array = list(password)
    # print("passw arr ", password_array)
    symbols = "!@#$%^&*()-_=+[]{};:,.<>?"
    n = 0
    lower_count = 0
    upper_count = 0
    number_count = 0
    symbol_count = 0
    for ent in password:
        if ent.islower() == True and lower_count == 0:
            n += 26
            lower_count += 1
        elif ent.isupper() == True and upper_count == 0:
            n += 26
            upper_count += 1
        elif ent.isdigit() == True and number_count == 0:
            n += 10
            number_count += 1
        elif ent in symbols and symbol_count == 0:
            n += 25
            symbol_count += 1
    # print(f"n: {n}")
    entropy_value = round(length * math.log2(n))
    print(f"Entropy value: {entropy_value} bytes")
    
    # example ranges
    if entropy_value >= 128:
        print("Password strength: Very strong")
    elif entropy_value >= 60:
        print("Password strength: Strong")
    elif entropy_value >= 36:
        print("Password strength: Medium")
    elif entropy_value >= 28:
        print("Password strength: Weak")
    else:
        print("Password strength: Very weak")

options = ["Generate password", "Check password", "Calculate entropy of password"]

def menu():
    print("What would you like to do?")
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")

    choice = input("Choice: ")
    if choice == "1":
        generate_password()
    elif choice == "2":
        check_password()
    elif choice == "3":
        calculate_entropy()

menu()
# check_password()
# generate_password()