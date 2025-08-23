
# NESTING CONDITIONAL STATEMENTS (beginner friendly)
"""
Nesting means placing an if (or if/else) block inside another if (or elif/else) block.
Use nesting when a decision depends on a previous decision.
"""

try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid integer for age.")
else:
    # Outer check: are they an adult?
    if age >= 18:
        # Inner check: is the person very old (example rule)?
        if age >= 80:
            print("Based on this simple rule: 'Too old to drive' (consult rules in your country).")
        else:
            print("You are allowed to drive (subject to local laws and tests).")
    else:
        print("You are not old enough to drive yet.")


# Another nested example: check registration and then membership level
registered = input("Are you registered? (yes/no): ").strip().lower()
if registered == 'yes':
    member_type = input("Enter membership type (basic/premium): ").strip().lower()
    if member_type == 'premium':
        print("Welcome, premium member! You have full access.")
    else:
        print("Welcome, basic member. Some features may be limited.")
else:
    print("Please register to access member features.")

# Note for beginners:
# - The inner if runs only when the outer if condition is True.
# - Keep nesting shallow (1-2 levels) to keep code readable.
# - An alternative to heavy nesting is combining conditions (e.g., if 18 <= age < 80:),
#   but that is optional for now.