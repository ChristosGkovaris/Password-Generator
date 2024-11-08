import random
import string


def generate_password():
    choice = input("Enter 'A' for 5 letters and 5 digits, or 'B' for alternating letters and digits: ").upper()

    if choice == 'A':
        # Generate 5 random letters and 5 random digits
        letters = ''.join(random.choice(string.ascii_letters) for _ in range(5))
        digits = ''.join(random.choice(string.digits) for _ in range(5))
        password = letters + digits
    elif choice == 'B':
        # Generate alternating letter and digit (1 letter, 1 digit, etc.)
        password = ''.join(random.choice(string.ascii_letters if i % 2 == 0 else string.digits) for i in range(10))
    else:
        print("Invalid input. Please enter 'A' or 'B'.")
        return None

    return password

# Generate and display the password
password = generate_password()
if password:
    print(f"Generated Password: {password}")
