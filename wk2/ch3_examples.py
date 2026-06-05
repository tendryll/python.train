"""
Python Illustrated – Chapter 3: Working with Conditional Statements
====================================================================
Examples demonstrating every concept from the chapter.
Run this file top-to-bottom, or jump to any section with Ctrl+F.

Sections
--------
1.  The if statement
2.  Comparison operators
3.  The else statement
4.  The elif statement
5.  Nested if statements
6.  Logical operators  (and / or / not)
7.  The match statement  (Python 3.10+)
8.  The ternary operator
9.  Common mistakes & how to avoid them
10. Chapter exercises (3.1 – 3.5)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 1. THE IF STATEMENT
# ─────────────────────────────────────────────────────────────────────────────
print("=" * 55)
print("1. THE IF STATEMENT")
print("=" * 55)

# Basic if: only runs when the condition is True
hour = 18  # 6 PM
if hour == 18:
    print("Time for dinner!")  # ✅ prints – condition is True

hour = 10
if hour == 18:
    print("This won't print.")  # ❌ skipped – condition is False

# The indented block can be multiple lines
temperature = 35
if temperature > 30:
    print("It's hot outside!")
    print("Stay hydrated.")
    print("Maybe skip the afternoon run.")


# ─────────────────────────────────────────────────────────────────────────────
# 2. COMPARISON OPERATORS
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("2. COMPARISON OPERATORS")
print("=" * 55)

speed = 80
speed_limit = 100

print(speed == speed_limit)   # False – equal?
print(speed != speed_limit)   # True  – not equal?
print(speed < speed_limit)    # True  – less than?
print(speed > speed_limit)    # False – greater than?
print(speed <= speed_limit)   # True  – less than or equal?
print(speed >= speed_limit)   # False – greater than or equal?

# The result of a comparison is always a boolean
is_speeding = speed > speed_limit
print("Speeding?", is_speeding)   # False

# Works with strings, too
favourite_pet = "dog"
print(favourite_pet == "dog")   # True
print(favourite_pet == "cat")   # False


# ─────────────────────────────────────────────────────────────────────────────
# 3. THE ELSE STATEMENT
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("3. THE ELSE STATEMENT")
print("=" * 55)

# else runs when the if condition is False – exactly one branch always executes
battery = 15  # percent

if battery >= 20:
    print("Battery is fine.")
else:
    print("Low battery! Plug in soon.")  # ← runs

# Another example
age = 17

if age >= 18:
    print("You may vote.")
else:
    print("You are not old enough to vote yet.")  # ← runs


# ─────────────────────────────────────────────────────────────────────────────
# 4. THE ELIF STATEMENT
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("4. THE ELIF STATEMENT")
print("=" * 55)

# elif adds extra conditions between if and else
# Python checks each branch in order and stops at the first True one

score = 74

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"   # ← matches (74 >= 70)
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Grade:", grade)   # Grade: C

# Temperature comfort level example
temp = 22

if temp < 0:
    print("It's freezing!")
elif temp < 10:
    print("It's cold.")
elif temp < 20:
    print("It's a bit chilly.")
elif temp < 30:
    print("It's comfortable.")   # ← runs (22 is between 20 and 30)
else:
    print("It's hot!")


# ─────────────────────────────────────────────────────────────────────────────
# 5. NESTED IF STATEMENTS
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("5. NESTED IF STATEMENTS")
print("=" * 55)

# An if inside another if – use sparingly; logical operators often cleaner
has_ticket = True
is_vip = False

if has_ticket:
    print("Welcome to the concert!")
    if is_vip:
        print("Enjoy the VIP lounge.")
    else:
        print("Head to the general admission area.")
else:
    print("Sorry, no ticket, no entry.")

# Nested with numbers
account_balance = 500
withdrawal = 200

if account_balance > 0:
    if withdrawal <= account_balance:
        account_balance -= withdrawal
        print(f"Withdrawal successful. Balance: ${account_balance}")
    else:
        print("Insufficient funds.")
else:
    print("Your account is empty.")


# ─────────────────────────────────────────────────────────────────────────────
# 6. LOGICAL OPERATORS (and / or / not)
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("6. LOGICAL OPERATORS")
print("=" * 55)

# ── and ── both sides must be True ──────────────────────────────
is_weekend = True
is_sunny = True
go_hiking = is_weekend and is_sunny
print("Go hiking?", go_hiking)   # True

is_weekend = False
go_hiking = is_weekend and is_sunny
print("Go hiking?", go_hiking)   # False (one side is False)

# and inside an if
username_ok = True
password_ok = True
if username_ok and password_ok:
    print("Login successful!")
else:
    print("Login failed.")

# ── or ── at least one side must be True ────────────────────────
has_umbrella = False
has_raincoat = True
can_go_out = has_umbrella or has_raincoat
print("Can go out in rain?", can_go_out)   # True

has_umbrella = False
has_raincoat = False
can_go_out = has_umbrella or has_raincoat
print("Can go out in rain?", can_go_out)   # False (both False)

# or inside an if
day = "Saturday"
if day == "Saturday" or day == "Sunday":
    print("It's the weekend – time to relax!")
else:
    print("Back to work.")

# ── not ── flips the boolean ─────────────────────────────────────
is_raining = False
if not is_raining:
    print("Let's go for a walk!")   # runs because not False == True

is_member = False
if not is_member:
    print("Please sign up for an account.")

# Combining all three logical operators
age = 25
has_licence = True
has_car = False

# You can drive if you're old enough, have a licence, and own a car OR can rent one
can_drive = age >= 18 and has_licence and (has_car or age >= 21)
print("Can drive?", can_drive)   # True (age >= 21 satisfies the rental part)


# ─────────────────────────────────────────────────────────────────────────────
# 7. THE MATCH STATEMENT  (Python 3.10+)
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("7. THE MATCH STATEMENT  (Python 3.10+)")
print("=" * 55)

# match is a cleaner alternative to a long if-elif chain
# when you are comparing one variable to many fixed values

# Basic match
day = "Wednesday"
match day:
    case "Monday":
        print("Back to the grind.")
    case "Wednesday":
        print("Hump day – halfway there!")   # ← matches
    case "Friday":
        print("TGIF!")
    case _:                                  # default (like else)
        print("Just another day.")

# Multiple values per case with | (pipe = "or")
pet_type = "kitten"
match pet_type:
    case "cat" | "kitten":
        print("Meow!")   # ← matches because "kitten" is included
    case "dog" | "puppy":
        print("Woof!")
    case _:
        print("Some other animal sound.")

# match with a command-handler pattern
command = "quit"
match command:
    case "start":
        print("Starting the engine…")
    case "stop":
        print("Stopping the engine…")
    case "quit" | "exit":
        print("Goodbye!")   # ← runs
    case _:
        print(f"Unknown command: '{command}'")


# ─────────────────────────────────────────────────────────────────────────────
# 8. THE TERNARY OPERATOR
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("8. THE TERNARY OPERATOR")
print("=" * 55)

# Syntax: value_if_true  if  condition  else  value_if_false

hour = 14   # 2 PM
activity = "Nap time" if hour < 17 else "Play time"
print(activity)   # Nap time

# Even / odd in one line
number = 7
parity = "even" if number % 2 == 0 else "odd"
print(f"{number} is {parity}")   # 7 is odd

# Access label based on age
age = 20
label = "adult" if age >= 18 else "minor"
print(f"Age {age} – classified as: {label}")   # adult

# Temperature description
temp = 5
description = "warm" if temp >= 20 else "cold"
print(f"{temp}°C is {description}.")   # 5°C is cold.

# Assigning to a variable is the most common use; avoid chaining ternaries
# (it works, but becomes very hard to read)


# ─────────────────────────────────────────────────────────────────────────────
# 9. COMMON MISTAKES & HOW TO AVOID THEM
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("9. COMMON MISTAKES & HOW TO AVOID THEM")
print("=" * 55)

# ── Mistake 1: using = instead of == ────────────────────────────
a = 5
# WRONG (syntax error):  if a = 5:
# RIGHT:
if a == 5:
    print("a equals 5 ✅")

# ── Mistake 2: missing colon ────────────────────────────────────
# WRONG (syntax error):  if a == 5
# RIGHT: always end if / elif / else / match / case with a colon

# ── Mistake 3: incorrect indentation ────────────────────────────
# WRONG (IndentationError):
# if a == 5:
# print("no indent!")

# RIGHT: indent consistently (4 spaces recommended)
if a == 5:
    print("Correctly indented ✅")

# ── Mistake 4: confusing and / or logic ─────────────────────────
x = 15
# Common confusion: "I want x between 10 and 20"
# WRONG reading: if x > 10 or x < 20 – this is ALWAYS True for any number!
# RIGHT:
if x > 10 and x < 20:
    print(f"{x} is between 10 and 20 ✅")

# Python shorthand for range checks (also valid):
if 10 < x < 20:
    print(f"{x} is between 10 and 20 (shorthand) ✅")


# ─────────────────────────────────────────────────────────────────────────────
# 10. CHAPTER EXERCISES
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("10. CHAPTER EXERCISES")
print("=" * 55)

# ── Exercise 3.1 – Even or Odd ───────────────────────────────────
print("\n-- Exercise 3.1: Even or Odd --")

number = 42

if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")

# Bonus: same logic as a ternary operator
result = "even" if number % 2 == 0 else "odd"
print(f"{number} is {result}. (ternary version)")


# ── Exercise 3.2 – Dachshund Weight Classification ───────────────
print("\n-- Exercise 3.2: Dachshund Weight Classification --")

name = "Wiesje"
weight_kg = 2.5
weight_lbs = weight_kg * 2.2   # convert kg → lbs

if weight_lbs >= 16:
    size = "Standard"
elif weight_lbs >= 12:
    size = "Miniature"
else:
    size = "Kaninchen"   # < 12 lbs

print(
    f"With a weight of {weight_kg} kgs, "
    f"{weight_lbs:.1f} lbs, dachshund {name} is classified as: {size}"
)


# ── Exercise 3.3 – Password Checker ─────────────────────────────
print("\n-- Exercise 3.3: Password Checker --")

stored_password = "whiskers123"
input_password = "whiskers123"   # pretend this came from the user

if input_password == stored_password:
    print("Access granted! Welcome.")
else:
    print("Incorrect password. Access denied.")

# Bonus: also check username
stored_username = "zia_cat"
stored_password = "whiskers123"
input_username = "zia_cat"
input_password = "whiskers123"

if input_username == stored_username and input_password == stored_password:
    print(f"Hello, {input_username}! Login successful.")
else:
    print("Invalid username or password.")


# ── Exercise 3.4 – Grading System ───────────────────────────────
print("\n-- Exercise 3.4: Grading System --")

score = 85   # try different values to test all branches

if score >= 90:
    letter = "A"
elif score >= 80:
    letter = "B"   # ← 85 lands here
elif score >= 70:
    letter = "C"
elif score >= 60:
    letter = "D"
else:
    letter = "F"

print(f"Score: {score}% → Your grade is: {letter}")


# ── Exercise 3.5 – Fun Activities for Humans per Weekday ─────────
print("\n-- Exercise 3.5: Fun Activities for Humans --")

weekday = "Thursday"   # change this to try other days

match weekday:
    case "Monday":
        activity = "take a yoga class"
    case "Tuesday":
        activity = "cook a new recipe"
    case "Wednesday":
        activity = "go for a bike ride"
    case "Thursday":
        activity = "visit a local museum"   # ← matches
    case "Friday":
        activity = "catch a live music show"
    case "Saturday":
        activity = "explore a hiking trail"
    case "Sunday":
        activity = "read a good book in the park"
    case _:
        activity = "double-check that day's spelling!"

print(f"On {weekday}, you should: {activity}.")