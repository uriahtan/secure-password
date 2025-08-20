import hashlib
import requests 

def generate_password():
    print()

def check_password():
    password = input("Enter password: ")

    # compute sha1 hash of password
    sha1_hash = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    print(sha1_hash)
    
    # obtain first 5 characters of password to check against the Have I been Pwned API
    prefix = sha1_hash[:5]

    # obtain remaining characters to check if password shows up in the database
    suffix = sha1_hash[5:]
    print(prefix)
    print(suffix)
    print(type(suffix))
    url = f"https://api.pwnedpasswords.com/range/{prefix}"
    print(url)
    response = requests.get(url)
    # print(response.text)
    with open("matches.txt", "w") as f:
        f.write(response.text)

    count = 0
    with open("matches.txt", "r") as f:
        for line in f:
            if suffix in line:
                strip = line.strip()
                print(f"Strip: {strip}")
                split = strip.split(":")
                print(split)
                count = int(split[1])
                break
        
    if count >= 1000000:
        print(f"Your password has appeared {count} times in database leaks! Please change your password as soon as possible!")
    elif count >= 100000:
        print(f"Your password has ")
    elif count >= 10000:
        print()
    elif count >= 1000:
        print()
    elif count >= 100:
        print()
    elif count >= 10:
        print()
    elif count == 0:
        print("Your password did not appear in the Have I been Pwned database!\n It is safe for you to keep using your password")

options = ["Generate password", "Check password"]

def menu():
    print("What would you like to do?")
    for i in range(len(options)):
        print(f"{i+1}. {options[i]}")

    choice = input("Choice: ")
    if choice == 1:
        generate_password()
    elif choice == 2:
        check_password()
# check_password()

menu()