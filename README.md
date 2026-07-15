# -decodelabs-_project1
# 🔐 Password Strength Checker

**DecodeLabs Industrial Training Kit — Cyber Security Track, Project 1**

A simple command-line tool that checks a password and rates it
**Weak**, **Medium**, or **Strong**.

## What it checks

- Length (8+ characters minimum, 12+ recommended)
- Uppercase letter (A-Z)
- Lowercase letter (a-z)
- Number (0-9)
- Symbol (e.g. `! @ # $ %`)
- Whether it's on a common/leaked password list

## Rating rules

- **Weak** — under 8 characters, or a common password
- **Medium** — 8+ characters with at least 3 of the 4 character types
- **Strong** — 12+ characters with all 4 character types

## Files

```
password_strength_checker/
├── checker.py         # The strength-checking logic
├── main.py             # Run this to use the tool
├── test_checker.py     # Tests
└── README.md
```

## How to run it

```bash
python main.py
```

Example:

```
=== DecodeLabs Password Strength Checker ===
Type a password to check it, or type 'quit' to exit.

Enter password: Tr0ub4dor&Zebra

Rating: Strong
Length: 15 characters
Uppercase letter: yes
Lowercase letter: yes
Number: yes
Symbol: yes

Enter password: quit
Goodbye!
```

## Running the tests

```bash
python -m unittest test_checker.py -v
```

## Using it in your own code

```python
from checker import check_password_strength

result = check_password_strength("MyPassword123!")
print(result["rating"])  # "Weak", "Medium", or "Strong"
print(result["tips"])    # list of suggestions
```

## Ideas to extend it

- Load a bigger list of leaked passwords from a file
- Reject passwords that contain the username
- Build a Streamlit version with a colored strength bar
