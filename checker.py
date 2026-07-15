"""
checker.py
-----------
Core logic for the DecodeLabs Password Strength Checker (Project 1).

Simple version: one function, plain variables, no extra classes.
"""

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "12345678",
    "111111", "1234567", "letmein", "admin", "welcome",
    "monkey", "login", "abc123", "iloveyou", "football",
}

SYMBOLS = "!@#$%^&*()-_=+[]{};:'\",.<>/?\\|`~"


def check_password_strength(password):
    """
    Look at a password and return a dict with:
      - the checks that passed/failed
      - a rating: "Weak", "Medium", or "Strong"
      - simple tips to improve it
    """
    length = len(password)

    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in SYMBOLS for char in password)
    is_common = password.lower() in COMMON_PASSWORDS

    # How many character types are used (0 to 4)
    variety = sum([has_upper, has_lower, has_digit, has_symbol])

    # Decide the rating
    if is_common or length < 8:
        rating = "Weak"
    elif length >= 12 and variety == 4:
        rating = "Strong"
    elif length >= 8 and variety >= 3:
        rating = "Medium"
    else:
        rating = "Weak"

    # Build simple tips
    tips = []
    if is_common:
        tips.append("This password is on a common/leaked password list. Choose a different one.")
    if length < 8:
        tips.append("Use at least 8 characters.")
    elif length < 12:
        tips.append("Use 12+ characters for extra safety.")
    if not has_upper:
        tips.append("Add an uppercase letter (A-Z).")
    if not has_lower:
        tips.append("Add a lowercase letter (a-z).")
    if not has_digit:
        tips.append("Add a number (0-9).")
    if not has_symbol:
        tips.append("Add a symbol (e.g. ! @ # $).")

    return {
        "length": length,
        "has_upper": has_upper,
        "has_lower": has_lower,
        "has_digit": has_digit,
        "has_symbol": has_symbol,
        "is_common": is_common,
        "rating": rating,
        "tips": tips,
    }


def print_result(result):
    """Print a check_password_strength() result in a readable way."""
    print(f"Rating: {result['rating']}")
    print(f"Length: {result['length']} characters")
    print(f"Uppercase letter: {'yes' if result['has_upper'] else 'no'}")
    print(f"Lowercase letter: {'yes' if result['has_lower'] else 'no'}")
    print(f"Number: {'yes' if result['has_digit'] else 'no'}")
    print(f"Symbol: {'yes' if result['has_symbol'] else 'no'}")

    if result["tips"]:
        print("Tips:")
        for tip in result["tips"]:
            print(f"  - {tip}")
