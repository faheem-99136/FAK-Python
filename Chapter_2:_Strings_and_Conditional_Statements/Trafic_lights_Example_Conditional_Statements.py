# Traffic Light Example - Conditional Statements
# This example shows how to use if / elif / else to choose behavior based on input.

light = input("Enter the traffic light color you are seeing: ").strip().lower()

# Use lower() so the check is case-insensitive (accepts 'Red', 'red', 'RED', etc.).
if light == "red":
    print("STOP")
elif light == "yellow":
    print("Get ready / Slow down")
elif light == "green":
    print("GO")
else:
    print("Unknown light color. The light may be broken or input was invalid.")

print("END of traffic light example")


# --- Demonstration: multiple if vs if/elif ---
# When you use separate `if` statements, each condition is checked independently.
num = 5
if num > 2:
    print("Greater than 2")
if num > 3:
    print("Greater than 3")

# If you replace the second `if` with `elif`, the second condition is checked only
# when the first `if` is False. Use `elif` for mutually exclusive branches.
print("Now using if/elif example:")
if num > 2:
    print("(if/elif) Greater than 2")
elif num > 3:
    print("(if/elif) Greater than 3")


# --- Example: using if/else for age-based decision ---
# Always convert user input to the correct type and handle errors.
try:
    age = int(input("Enter your age: "))
except ValueError:
    print("Please enter a valid integer for age.")
else:
    if age >= 18:
        print("You can vote")
    else:
        print("You can't vote yet")

# Notes for beginners:
# - `if` checks its condition and runs its block when True.
# - `elif` (else if) runs only when previous `if` (or `elif`) conditions were False.
# - `else` runs when none of the previous conditions match.
# - Indentation (spaces) is required to define blocks after if/elif/else.

