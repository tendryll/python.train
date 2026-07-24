"""
chapter6_functions_demo.py

Companion demo file for the 1-hour lesson:
"Writing Functions and Using Built-In Functions"
Based on Python Illustrated, Chapter 6.

HOW TO USE THIS FILE
---------------------
Each section below is numbered to match the lesson's timed agenda.
Run this file top to bottom with:

    python chapter6_functions_demo.py

Read the comments as you go, then try changing values and re-running
to see how the output changes. Some sections are intentionally
commented OUT because they demonstrate an error on purpose --
uncomment them one at a time to see (and understand) the error.
"""

import math
import random
from datetime import datetime, timedelta


def section_divider(title):
    """Small helper (not part of the lesson) to make console output readable."""
    print("\n" + "=" * 60)
    print(title)
    print("=" * 60)


# ---------------------------------------------------------------------------
# 2. DEFINING AND CALLING YOUR FIRST FUNCTION
# ---------------------------------------------------------------------------
section_divider("2. Defining and Calling Your First Function")


def greet():
    # This is the function BODY. It only runs when greet() is CALLED below.
    print("Hello humans!")


greet()  # Calling the function -- this is what actually runs the code above.


# ---------------------------------------------------------------------------
# 3. PARAMETERS VS. ARGUMENTS
# ---------------------------------------------------------------------------
section_divider("3. Parameters vs. Arguments")


def greet_by_name(name):  # "name" is a PARAMETER (a placeholder)
    print("Hello", name)


greet_by_name("Zia")     # "Zia" is an ARGUMENT (the actual value)
greet_by_name("Wiesje")  # "Wiesje" is a different ARGUMENT, same parameter


def feed_pet(pet_name, food):  # two parameters, separated by a comma
    print("Feeding", pet_name, "some delicious", food)


feed_pet("Zia", "tuna")
feed_pet("Wiesje", "kibble")


# ---------------------------------------------------------------------------
# 4. CHECKPOINT 1 -- QUICK PRACTICE (worked solution)
# ---------------------------------------------------------------------------
section_divider("4. Checkpoint 1 -- Quick Practice (worked solution)")


def describe_animal(name, sound):
    """Prints a sentence describing the animal's sound."""
    print(f"{name} says {sound}!")


describe_animal("The dog", "Woof")
describe_animal("The cat", "Meow")


# ---------------------------------------------------------------------------
# 5. RETURN VALUES
# ---------------------------------------------------------------------------
section_divider("5. Return Values")


def area_of_rectangle(length, width):
    area = length * width
    return area  # sends this value back to wherever the function was called


result = area_of_rectangle(5, 3)  # result now holds 15
print("Area is:", result)


def return_nothing():
    print("Hi")
    # no return statement here


val = return_nothing()
print(val)  # prints None -- a function with no "return" gives back None


# ---------------------------------------------------------------------------
# 6. DEFAULT PARAMETERS & KEYWORD ARGUMENTS
# ---------------------------------------------------------------------------
section_divider("6. Default Parameters & Keyword Arguments")


def greet_friend(name, greeting="Hello"):  # "greeting" has a DEFAULT value
    print(greeting, name)


greet_friend("Zia")            # uses the default: "Hello Zia"
greet_friend("Wiesje", "Hi")   # overrides the default: "Hi Wiesje"


def describe_pet(pet_name, species, age):
    print(f"{pet_name} is a {species} who is {age} years old.")


# KEYWORD arguments -- naming each value means order no longer matters
describe_pet(species="dachshund", pet_name="Wiesje", age=7)


# ---------------------------------------------------------------------------
# 7. A PEEK AT *args AND **kwargs
# ---------------------------------------------------------------------------
section_divider("7. A Peek at *args and **kwargs")


def show_off(*args, **kwargs):
    # *args collects extra POSITIONAL arguments into a tuple
    # **kwargs collects extra KEYWORD arguments into a dictionary
    print("Positional args:", args)
    print("Keyword args:", kwargs)


show_off("Zia", "Wiesje", toy="feather wand", snack="tuna")


# ---------------------------------------------------------------------------
# 8. SCOPE: LOCAL VS. GLOBAL
# ---------------------------------------------------------------------------
section_divider("8. Scope: Local vs. Global")

# --- Step 1: a local variable can't be used outside its function ---
# Uncomment the three lines below to see the NameError for yourself:
#
# def feed_cat_local_only():
#     food = "tuna"          # "food" only exists INSIDE this function
#     print("Feeding cat with", food)
#
# feed_cat_local_only()
# print(food)  # NameError: name 'food' is not defined

# --- Step 2: a global variable CAN be read inside a function ---
food = "kibble"  # this is a GLOBAL variable (defined outside any function)


def feed_cat_reads_global():
    print("Feeding cat with", food)  # reads the global "food"


feed_cat_reads_global()
print(food)

# --- Step 3: assigning inside a function creates a NEW local variable ---
# It does NOT overwrite the global one, even if the names match.
food = "kibble"


def feed_cat_local_shadow():
    food = "tuna"  # this creates a LOCAL "food", separate from the global one
    print("Feeding cat with", food)


feed_cat_local_shadow()
print(food)  # still "kibble" -- the global variable was never touched

# --- Step 4: the "global" keyword -- use sparingly! ---
food = "kibble"


def feed_cat_uses_global():
    global food  # tells Python: "don't create a local copy, use the global one"
    food = "tuna"
    print("Feeding cat with", food)


feed_cat_uses_global()
print(food)  # now "tuna" -- the global variable WAS changed

# --- The generally preferred alternative to "global": pass in and return ---
food = "kibble"


def feed_cat_pass_and_return(current_food):
    current_food = "tuna"
    print("Feeding cat with", current_food)
    return current_food


food = feed_cat_pass_and_return(food)  # explicitly reassign the global
print(food)


# ---------------------------------------------------------------------------
# 9. BUILT-IN FUNCTIONS & THE STANDARD LIBRARY
# ---------------------------------------------------------------------------
section_divider("9. Built-In Functions & the Standard Library")

# A few built-ins for data types (no import needed):
items = ["feather", "laser pointer", "ball"]
count = len(items)
print("Count:", count, "| Type:", type(count))
print("As text:", str(count), "| Type:", type(str(count)))

# The math module
print("\n-- math module --")
print("Square root of 25:", math.sqrt(25))
print("2 to the power of 3:", math.pow(2, 3))
print("5 factorial:", math.factorial(5))
print("Pi is about:", math.pi)

# The random module
print("\n-- random module --")
print("Dice roll (1-6):", random.randint(1, 6))
pets = ["Zia", "Wiesje", "Axolotl King"]
print("Random pet:", random.choice(pets))

# The datetime module
print("\n-- datetime module --")
now = datetime.now()
print("Right now:", now)
print("Year:", now.year, "Month:", now.month, "Day:", now.day)
five_days_later = now + timedelta(days=5)
print("Five days from now:", five_days_later)


# ---------------------------------------------------------------------------
# 10. DOCSTRINGS
# ---------------------------------------------------------------------------
section_divider("10. Docstrings")


def area_of_circle(radius):
    """Returns the area of a circle with a given radius, using pi * r^2."""
    return math.pi * radius * radius


print("Area of a circle with radius 4:", area_of_circle(4))
print("Docstring for area_of_circle:", area_of_circle.__doc__)


# ---------------------------------------------------------------------------
# BONUS: putting it all together -- a mini version of the book's
# interactive pet-feeding example, refactored into small functions
# with clear jobs and docstrings. (Not run automatically -- call
# interactive_feeding() yourself if you want to try the interactive
# version in a real terminal.)
# ---------------------------------------------------------------------------


def get_pet_info():
    """
    Asks the user for pet information and returns it as (pet_name, species, food).
    If the user types 'quit' for pet_name, returns None to signal we're done.
    """
    pet_name = input("What's your pet's name? ")
    if pet_name.lower() == "quit":
        return None
    species = input("What species is your pet? (e.g. cat, dog): ")
    food = input("What food do you want to give them? ")
    return (pet_name, species, food)


def feed_pet_with_reaction(pet_name, species, food):
    """Decides how a pet reacts based on its species and prints a feeding message."""
    if species.lower() == "cat":
        print(pet_name, "arches their back and sniffs the", food)
    elif species.lower() == "dog":
        print(pet_name, "wags their tail excitedly at the sight of", food)
    else:
        print(pet_name, "looks curious about the", food)
    print("Feeding", pet_name, "some delicious", food, "now!\n")


def interactive_feeding():
    """Loops, gathering pet info and feeding them until the user quits."""
    print("Welcome to the pet feeding station!")
    print("Type 'quit' when you're done feeding your pets.")

    while True:
        pet_data = get_pet_info()

        if pet_data is None:  # user typed 'quit' for the pet's name
            print("All done feeding pets! Bye!")
            break

        pet_name, species, food = pet_data
        feed_pet_with_reaction(pet_name, species, food)


if __name__ == "__main__":
    section_divider("Demo finished")
    print("Want to try the interactive example? Call interactive_feeding()")
    print("from a Python shell, or uncomment the line below and re-run:")
    print("# interactive_feeding()")
    # interactive_feeding()
