password = input("Enter your password: ")

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*"

for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_chars:
        has_special = True

score = 0

if len(password) >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

if score <= 2:
    print("Weak Password")
elif score == 3 or score == 4:
    print("Medium Password")
else:
    print("Strong Password")