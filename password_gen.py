import random
import string

def generate_password(length):
    # Define characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate the password
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def generate_passwords(num_passwords, password_length):
    passwords = []
    for _ in range(num_passwords):
        password = generate_password(password_length)
        passwords.append(password)
    return passwords

def main():
    print("Welcome to the Password Generator!")
    
    # Prompt user for password length
    while True:
        try:
            password_length = int(input("Enter the length of each password: "))
            if password_length <= 0:
                raise ValueError("Length must be a positive integer")
            break
        except ValueError as e:
            print("Invalid input. Please enter a positive integer.")

    # Prompt user for the number of passwords to generate
    while True:
        try:
            num_passwords = int(input("How many passwords would you like to generate? "))
            if num_passwords <= 0:
                raise ValueError("Number of passwords must be a positive integer")
            break
        except ValueError as e:
            print("Invalid input. Please enter a positive integer.")
    
    # Generate and print the passwords
    print("\nGenerated Passwords:")
    passwords = generate_passwords(num_passwords, password_length)
    for password in passwords:
        print(password)
        
    print("\nThank you for using the Password Generator!")

if __name__ == "__main__":
    main()
