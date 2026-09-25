for i in range(6):
    password = input("enter your password: ")

    has_upper = any(ch.isupper() for ch in password)
    has_lower = any(ch.islower() for ch in password)
    has_special = any(not ch.isalnum() for ch in password)

    if len(password) >= 8 and has_upper and has_lower and has_special:
        print("valid password")
    else:
        print("invalid password")
    