import re
import random
import string

def check_password_strength(password):
    # Check the length of the password
    if len(password) < 8:
        return "Password is too short. It should be at least 8 characters long."

    # Check if the password contains both uppercase and lowercase letters
    if not any(c.isupper() for c in password) or not any(c.islower() for c in password):
        return "Password should contain both uppercase and lowercase letters."

    # Check if the password contains at least one digit
    if not any(c.isdigit() for c in password):
        return "Password should contain at least one digit."
    # Check if the password contains at least one special character
    special_characters = r"[!@#$%^&*(),.?\":{}|<>]"
    if not re.search(special_characters, password):
        return "Password should contain at least one special character."

    # Assign a score based on the complexity of the password
    score = 0
    if len(password) >= 12:
        score += 2
    elif len(password) >= 10:
        score += 1

    if any(c.isnumeric() for c in password):
        score += 1

    if any(c.isalpha() for c in password):
        score += 1

    if any(c.isupper() for c in password) and any(c.islower() for c in password):
        score += 1

    if re.search(special_characters, password):
        score += 1

    # Strength meter
    strength_meter = ["Very Weak", "Weak", "Moderate", "Strong", "Very Strong"]
    strength_index = min(score, 4)  # Cap the index at 4
    password_strength = strength_meter[strength_index]

    # Provide feedback based on the score and display the strength meter
    feedback = f"Password Strength: {password_strength}\n"
    if score <= 2:
        suggestions = "Consider making the password longer and including a mix of uppercase letters, lowercase letters, digits, and special characters."
        return f"Weak password. {suggestions}\n{feedback}"
    elif 2 < score <= 4:
        suggestions = "Consider adding more complexity by using a mix of uppercase letters, lowercase letters, digits, and special characters."
        return f"Moderate password strength. {suggestions}\n{feedback}"
    else:
        return f"Strong password!\n{feedback}"

def generate_strong_password(length=12):
    """Generate a strong password with the specified length."""
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_characters = r"!@#$%^&*()-=_+[]{}|;':,.<>?/`~"

    # Combine character sets
    all_characters = uppercase_letters + lowercase_letters + digits + special_characters

    # Ensure at least one character from each set is included
    password = random.choice(uppercase_letters) + random.choice(lowercase_letters) + random.choice(digits) + random.choice(special_characters)

    # Fill the rest of the password
    password += ''.join(random.choice(all_characters) for _ in range(length - 4))

    # Shuffle the password to make it more random
    password_list = list(password)
    random.shuffle(password_list)
    password = ''.join(password_list)

    return password

# Interactive usage with numeric options and continue option
print("Welcome to the Password Checker and Generator!")

while True:
    print("\nChoose an action:")
    print("1. Check Password Strength")
    print("2. Generate Strong Password")
    print("3. Exit")

    choice = input("Enter the number corresponding to your choice: ")

    if choice == "1":
        password = input("Enter your password to check its strength: ")
        result = check_password_strength(password)
        print(result)
    elif choice == "2":
        password_length = int(input("Enter the desired length for the new password: "))
        new_password = generate_strong_password(length=password_length)
        print(f"Generated Strong Password: {new_password}")
    elif choice == "3":
        print("Exiting the Password Checker and Generator. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 3.")

    continue_option = input("Do you want to perform another action? (yes/no): ").lower()
    if continue_option != "yes":
        print("Exiting the Password Checker and Generator. Goodbye!")
        break
