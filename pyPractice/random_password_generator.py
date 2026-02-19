import random, string

def generate_password(length=12):
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")

    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_chars)
    ]
    all_chars = uppercase + lowercase + digits + special_chars
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return ''.join(password)


try:
    length = int(input("Enter the desired password length (minimum 4): "))
    password = generate_password(length)
    print("Generated Password:", password)
except ValueError as e:
    print(e)