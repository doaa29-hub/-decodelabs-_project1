"""
main.py
--------
Simple command-line tool for checking password strength.

Usage:
    python main.py
"""

from checker import check_password_strength, print_result


def main():
    print("=== DecodeLabs Password Strength Checker ===")
    print("Type a password to check it, or type 'quit' to exit.\n")

    while True:
        password = input("Enter password: ")

        if password.lower() == "quit":
            print("Goodbye!")
            break

        if password == "":
            print("Please type something.\n")
            continue

        result = check_password_strength(password)
        print()
        print_result(result)
        print()


if __name__ == "__main__":
    main()
