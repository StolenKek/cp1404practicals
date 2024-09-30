"""
CP1404 - Practical 2
Password Check with Functions
"""

def main():
    """Main function to drive the password check program."""
    user_password = get_password()
    print_asterisks(user_password)

def get_password():
    """Prompt the user for a password."""
    password = input(f"Enter a password: ")
    return password

def print_asterisks(password):
    """Print asterisks equal to the length of the password."""
    print("*" * len(password))

if __name__ == "__main__":
    main()
