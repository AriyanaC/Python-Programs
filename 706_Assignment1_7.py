import re

def check_password_strength(password):
    conditions = 0
    #Checks length atleast 8 characters
    if len(password) >= 8:
        conditions += 1

    #Checks for atleast 1 uppercase
    if re.search(r"[A-Z]", password):
        conditions += 1

    #checks for atleast 1 lowercase
    if re.search(r"[a-z]", password):
        conditions += 1

    #checks for atleast 1 digit
    if re.search(r"[0-9]", password):
        conditions += 1

    #checks for atleast 1 of the given special characters
    if re.search(r"[!@#$%^&*]", password):
        conditions += 1

    #Classification of Password
    if conditions <= 2:
        return "Password Stength: Weak"
    elif conditions <= 4:
        return "Password Stength: Moderate"
    else:
        return "Password Stength: Strong"

password = input("Enter Password: ")

strength = check_password_strength(password)

print(strength)

