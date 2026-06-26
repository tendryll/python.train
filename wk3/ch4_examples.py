"""
Python Illustrated – Chapter 4: Using Lists, Tuples, and Dictionaries
======================================================================
Examples demonstrating every concept from the chapter.
Run this file top-to-bottom, or jump to any section with Ctrl+F.

Sections
--------
1.  Lists – creating
2.  Lists – accessing items (positive & negative index)
3.  Lists – modifying  (append, insert, remove, pop, clear, change)
4.  Lists – slicing
5.  Lists – length with len()
6.  Lists – checking item existence with in
7.  Tuples – creating
8.  Tuples – accessing items
9.  Tuples – immutability
10. Tuples – unpacking
11. Dictionaries – creating
12. Dictionaries – accessing values ([] and get())
13. Dictionaries – modifying  (add, update, del, pop)
14. Dictionaries – methods  (keys, values, items, in)
15. Choosing between lists, tuples, and dictionaries
16. Combining different data types
17. Common mistakes  (IndexError, KeyError)
18. Chapter exercises (4.1 – 4.4)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 1. LISTS – CREATING
# ─────────────────────────────────────────────────────────────────────────────
print("=" * 58)
print("1. LISTS – CREATING")
print("=" * 58)

# An empty list – square brackets with nothing inside
shopping_cart = []
print("Empty list:", shopping_cart)

# A list created with items right away
fruit_1 = "apple"
fruit_2 = "banana"
fruit_3 = "cherry"
fruit_4 = "mango"


fruits = ["apple", "banana", "cherry", "mango"]
print("Fruits:", fruits)

# Lists can mix different data types
mixed = ["hello", 42, 3.14, True]
print("Mixed types:", mixed)

# A list of numbers
scores = [95, 87, 72, 100, 68]
print("Scores:", scores)


# ─────────────────────────────────────────────────────────────────────────────
# 2. LISTS – ACCESSING ITEMS
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("2. LISTS – ACCESSING ITEMS")
print("=" * 58)

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter"]

# ── Positive index (starts at 0) ─────────────────────────────────
print(planets[0])   # Mercury  ← first item
print(planets[2])   # Earth    ← third item
print(planets[4])   # Jupiter  ← last item (index = length - 1)

# ── Negative index (counts from the end) ─────────────────────────
print(planets[-1])  # Jupiter  ← last item
print(planets[-2])  # Mars     ← second-to-last
print(planets[-5])  # Mercury  ← same as index 0

# Visual reminder of both index styles:
#  Element  │ Mercury │ Venus │ Earth │ Mars │ Jupiter
#  Pos idx  │    0    │   1   │   2   │   3  │    4
#  Neg idx  │   -5    │  -4   │  -3   │  -2  │   -1

# Store an item before using it
first_planet = planets[0]
last_planet  = planets[-1]
print(f"First: {first_planet}, Last: {last_planet}")


# ─────────────────────────────────────────────────────────────────────────────
# 3. LISTS – MODIFYING
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("3. LISTS – MODIFYING")
print("=" * 58)

colours = ["red", "green", "blue"]

# ── append() – add to the end ────────────────────────────────────
colours.append("yellow")
print("After append:", colours)   # ['red', 'green', 'blue', 'yellow']

# ── insert() – add at a specific index ──────────────────────────
colours.insert(1, "orange")       # shifts everything from index 1 right
print("After insert:", colours)   # ['red', 'orange', 'green', 'blue', 'yellow']

# ── remove() – remove by value (first occurrence only) ───────────
colours.remove("green")
print("After remove:", colours)   # ['red', 'orange', 'blue', 'yellow']

# ── pop() – remove by index (returns the removed item) ───────────
removed = colours.pop(1)          # removes 'orange'
print("Popped:", removed)
print("After pop:", colours)      # ['red', 'blue', 'yellow']

# pop() with no argument removes the last item
last = colours.pop()
print("Popped last:", last)
print("After pop():", colours)    # ['red', 'blue']

# ── Change an item by assigning to its index ─────────────────────
colours[0] = "pink"
print("After change:", colours)   # ['pink', 'blue']

# ── clear() – remove everything ──────────────────────────────────
colours.clear()
print("After clear:", colours)    # []


# ─────────────────────────────────────────────────────────────────────────────
# 4. LISTS – SLICING
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("4. LISTS – SLICING")
print("=" * 58)

# Slicing returns a new list – the original is unchanged
# Syntax: list[start:stop]  → includes start, excludes stop

letters = ["a", "b", "c", "d", "e", "f"]

print(letters[1:4])    # ['b', 'c', 'd']  ← index 1, 2, 3 (not 4)
print(letters[0:3])    # ['a', 'b', 'c']
print(letters[3:])     # ['d', 'e', 'f']  ← from index 3 to end
print(letters[:4])     # ['a', 'b', 'c', 'd']  ← from start to index 3
print(letters[:])      # ['a', 'b', 'c', 'd', 'e', 'f']  ← full copy

# The original list is untouched
print("Original:", letters)

# Practical use: grab the top 3 scores from a sorted list
results = [100, 95, 90, 85, 70, 60]
top_three = results[0:3]
print("Top 3 scores:", top_three)


# ─────────────────────────────────────────────────────────────────────────────
# 5. LISTS – LENGTH WITH len()
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("5. LISTS – LENGTH WITH len()")
print("=" * 58)

animals = ["cat", "dog", "rabbit", "hamster", "parrot"]

count = len(animals)
print("Number of animals:", count)       # 5

# Maximum valid index is always len() - 1
print("Last item:", animals[len(animals) - 1])   # parrot
# (same as animals[-1], but shows why len() matters)

# len() works on strings too
word = "dachshund"
print("Letters in 'dachshund':", len(word))   # 9


# ─────────────────────────────────────────────────────────────────────────────
# 6. LISTS – CHECKING ITEM EXISTENCE WITH in
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("6. LISTS – CHECKING ITEM EXISTENCE WITH in")
print("=" * 58)

invited = ["Alice", "Bob", "Carol", "Dave"]

# in returns a boolean
print("Alice" in invited)    # True
print("Eve"   in invited)    # False

# Most useful inside an if statement
guest = "Eve"
if guest in invited:
    print(f"{guest} is on the list. Welcome!")
else:
    print(f"{guest} is not on the list.")

# Safe removal – avoid ValueError when item might not be present
if "Bob" in invited:
    invited.remove("Bob")
    print("Bob removed:", invited)


# ─────────────────────────────────────────────────────────────────────────────
# 7. TUPLES – CREATING
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("7. TUPLES – CREATING")
print("=" * 58)

# Empty tuple
empty_tuple = ()
print("Empty tuple:", empty_tuple)

# Tuple with items – use parentheses
coordinates = (52.3676, 4.9041)        # Amsterdam lat/lon
print("Coordinates:", coordinates)

# Mixed types are fine
pet_record = ("Wiesje", 7, "dachshund", True)
print("Pet record:", pet_record)

# Single-item tuple MUST have a trailing comma
single = ("only item",)
not_a_tuple = ("only item")            # this is just a string!
print("Single-item tuple:", type(single))       # <class 'tuple'>
print("Without comma:    ", type(not_a_tuple))  # <class 'str'>


# ─────────────────────────────────────────────────────────────────────────────
# 8. TUPLES – ACCESSING ITEMS
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("8. TUPLES – ACCESSING ITEMS")
print("=" * 58)

# Indexing works exactly like lists
rgb_red = (255, 0, 0)

print("R:", rgb_red[0])    # 255
print("G:", rgb_red[1])    # 0
print("B:", rgb_red[2])    # 0
print("Last value:", rgb_red[-1])   # 0

# Slicing also works
week = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
weekdays  = week[0:5]
weekend   = week[5:]
print("Weekdays:", weekdays)
print("Weekend: ", weekend)


# ─────────────────────────────────────────────────────────────────────────────
# 9. TUPLES – IMMUTABILITY
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("9. TUPLES – IMMUTABILITY")
print("=" * 58)

birth_date = (1995, 6, 15)   # year, month, day

# Reading is fine
print("Year:", birth_date[0])

# Trying to change raises a TypeError – uncomment to see the error:
# birth_date[0] = 2000   ← TypeError: 'tuple' object does not support item assignment

print("Tuples cannot be changed after creation – that's the point!")
print("Use a tuple when data should stay fixed (coordinates, dates, config values).")


# ─────────────────────────────────────────────────────────────────────────────
# 10. TUPLES – UNPACKING
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("10. TUPLES – UNPACKING")
print("=" * 58)

# Assign each element to its own variable in one line
person = ("Maaike", 30, "Netherlands")
name, age, country = person

print("Name:   ", name)
print("Age:    ", age)
print("Country:", country)

# Works with lists too
scores = [95, 87, 72]
first, second, third = scores
print(f"Gold: {first}, Silver: {second}, Bronze: {third}")

# Useful for coordinate pairs
point = (10, 20)
x, y = point
print(f"x = {x}, y = {y}")


# ─────────────────────────────────────────────────────────────────────────────
# 11. DICTIONARIES – CREATING
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("11. DICTIONARIES – CREATING")
print("=" * 58)

# Empty dictionary – curly braces
phonebook = {}
print("Empty dict:", phonebook)

# Dictionary with key-value pairs
# Keys are usually strings; values can be anything
book = {
    "title":  "Python Illustrated",
    "author": "Maaike van Putten",
    "year":   2026,
    "pages":  433,
}
print("Book:", book)

# Keys can also be numbers or tuples (any immutable type)
coordinates_map = {
    (52.37, 4.90): "Amsterdam",
    (48.85, 2.35): "Paris",
}
print("Coord map:", coordinates_map)


# ─────────────────────────────────────────────────────────────────────────────
# 12. DICTIONARIES – ACCESSING VALUES
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("12. DICTIONARIES – ACCESSING VALUES")
print("=" * 58)

student = {
    "name":   "Alex",
    "grade":  "B",
    "score":  85,
    "active": True,
}

# ── Square brackets – raises KeyError if key missing ─────────────
print(student["name"])     # Alex
print(student["score"])    # 85

# ── get() – returns None (or a default) if key missing ──────────
print(student.get("grade"))               # B
print(student.get("email"))               # None  ← no error
print(student.get("email", "No email"))   # No email  ← custom default

# When to use each:
# [] when you're certain the key exists (or want an error if it doesn't)
# get() when the key might be absent and you want a safe fallback


# ─────────────────────────────────────────────────────────────────────────────
# 13. DICTIONARIES – MODIFYING
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("13. DICTIONARIES – MODIFYING")
print("=" * 58)

cafe_menu = {
    "espresso": 2.50,
    "latte":    3.80,
    "muffin":   2.00,
}

# ── Add a new key-value pair ──────────────────────────────────────
cafe_menu["cappuccino"] = 3.50
print("After add:", cafe_menu)

# ── Update an existing value ──────────────────────────────────────
cafe_menu["muffin"] = 2.50    # price increase
print("After update:", cafe_menu)

# ── del – remove a key-value pair ────────────────────────────────
del cafe_menu["espresso"]
print("After del:", cafe_menu)

# ── pop() – remove and return the value ──────────────────────────
price = cafe_menu.pop("latte")
print("Removed latte, price was:", price)
print("After pop:", cafe_menu)

# pop() with a default avoids KeyError when key may not exist
price = cafe_menu.pop("tea", "Not on menu")
print("Tea price:", price)    # Not on menu – no error


# ─────────────────────────────────────────────────────────────────────────────
# 14. DICTIONARIES – METHODS (keys, values, items, in)
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("14. DICTIONARIES – METHODS")
print("=" * 58)

country_capitals = {
    "France":  "Paris",
    "Japan":   "Tokyo",
    "Brazil":  "Brasília",
    "Germany": "Berlin",
}

# ── keys() – all keys as a view object ───────────────────────────
keys = list(country_capitals.keys())
print("Countries:", keys)

# ── values() – all values ────────────────────────────────────────
capitals = list(country_capitals.values())
print("Capitals:", capitals)

# ── items() – all key-value pairs as tuples ──────────────────────
pairs = list(country_capitals.items())
print("Pairs:", pairs)

# ── in – check if a key exists ───────────────────────────────────
print("France" in country_capitals)    # True
print("Spain"  in country_capitals)    # False

if "Japan" in country_capitals:
    print("Capital of Japan:", country_capitals["Japan"])


# ─────────────────────────────────────────────────────────────────────────────
# 15. CHOOSING BETWEEN LISTS, TUPLES, AND DICTIONARIES
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("15. CHOOSING BETWEEN LISTS, TUPLES, AND DICTIONARIES")
print("=" * 58)

# LIST  – ordered, mutable, allows duplicates
# → use when the collection changes over time
to_do = ["buy groceries", "walk the dog", "read chapter 5"]
to_do.append("call the vet")
to_do.remove("walk the dog")
print("To-do:", to_do)

# TUPLE – ordered, immutable, allows duplicates
# → use when data must stay fixed
screen_resolution = (1920, 1080)
gps_location      = (52.3676, 4.9041)
print("Resolution:", screen_resolution)
print("Location:  ", gps_location)

# DICTIONARY – key-value pairs, mutable, keys must be unique
# → use when you need to look up values by a meaningful label
user_profile = {
    "username": "pythoncat",
    "email":    "zia@example.com",
    "level":    5,
}
print("User:", user_profile["username"], "– level", user_profile["level"])


# ─────────────────────────────────────────────────────────────────────────────
# 16. COMBINING DIFFERENT DATA TYPES
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("16. COMBINING DIFFERENT DATA TYPES")
print("=" * 58)

# Dictionary whose values are lists and nested dictionaries
library = {
    "name": "City Library",
    "open": True,
    "genres": ["fiction", "science", "history"],
    "staff": [
        {"name": "Sara",  "role": "librarian"},
        {"name": "James", "role": "assistant"},
    ],
}

# Access a simple value
print("Library:", library["name"])

# Access an item inside a list value
print("First genre:", library["genres"][0])   # fiction

# Access a value inside a nested dictionary inside a list
print("Staff lead:", library["staff"][0]["name"])    # Sara
print("Their role:", library["staff"][0]["role"])    # librarian

# Access the second staff member's name
print("Second staff:", library["staff"][1]["name"])  # James

# Step-by-step to make it less intimidating:
staff_list   = library["staff"]          # grab the list
first_member = staff_list[0]             # grab first dict in list
role         = first_member["role"]      # grab the value
print("Step-by-step role:", role)

# A list of dictionaries (common pattern – like a table of records)
inventory = [
    {"item": "notebook",  "qty": 50, "price": 1.99},
    {"item": "pen",       "qty": 200,"price": 0.49},
    {"item": "backpack",  "qty": 30, "price": 24.99},
]

# Access the price of the third item
print("Backpack price: $", inventory[2]["price"])

# Drill down multiple levels in one go
cat_attributes = {
    "name": "Zia",
    "age": 1,
    "hobbies": ["napping", "programming", "playing"],
    "friends": [
        {
            "name": "Wiesje",
            "age": 7,
            "hobbies": ["napping", "visiting the forest"]
        },
        {
            "name": "Muchu",
            "age": 0,
            "hobbies": ["napping in the couch", "chasing anything", "exploring"]
        }
    ]
}

# Zia's second hobby
print(cat_attributes["hobbies"][1])                               # programming

# Wiesje's second hobby
print(cat_attributes["friends"][0]["hobbies"][1])                 # visiting the forest

# Muchu's name and first hobby
print(cat_attributes["friends"][1]["name"], "loves",
      cat_attributes["friends"][1]["hobbies"][0])                 # Muchu loves napping in the couch


# ─────────────────────────────────────────────────────────────────────────────
# 17. COMMON MISTAKES
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("17. COMMON MISTAKES")
print("=" * 58)

# ── IndexError with lists and tuples ─────────────────────────────
some_numbers = [1, 2, 3]   # valid indices: 0, 1, 2

# WRONG – uncomment to see the error:
# print(some_numbers[3])   ← IndexError: list index out of range

# RIGHT – guard with len() before accessing
index = 3
if index < len(some_numbers):
    print(some_numbers[index])
else:
    print("Index out of range – access blocked safely.")

# ── KeyError with dictionaries ────────────────────────────────────
friends_ages = {"Zia": 1, "Wiesje": 7, "Muchu": 0}

# WRONG – uncomment to see the error:
# print(friends_ages["Szara"])   ← KeyError: 'Szara'

# RIGHT option 1 – check with in first
key = "Szara"
if key in friends_ages:
    print(friends_ages[key])
else:
    print(f"'{key}' not found in dictionary.")

# RIGHT option 2 – use get() with a default
value = friends_ages.get(key, "Key not found.")
print(value)

# ── Single-item tuple mistake ─────────────────────────────────────
wrong_tuple  = ("only item")     # this is a STRING, not a tuple
right_tuple  = ("only item",)    # trailing comma makes it a tuple
print("Wrong:", type(wrong_tuple))    # <class 'str'>
print("Right:", type(right_tuple))   # <class 'tuple'>


# ─────────────────────────────────────────────────────────────────────────────
# 18. CHAPTER EXERCISES
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("18. CHAPTER EXERCISES")
print("=" * 58)

# ── Exercise 4.1 – Favourite Animals ─────────────────────────────
print("\n-- Exercise 4.1: Favourite Animals --")

favourite_animals = ["elephant", "dolphin", "red panda"]
print("Favourite animals:", favourite_animals)

# Add a new favourite
favourite_animals.append("axolotl")
print("After adding axolotl:", favourite_animals)

# Remove one
favourite_animals.remove("dolphin")
print("After removing dolphin:", favourite_animals)

# Print how many are left
print("Total favourites:", len(favourite_animals))

# Check whether a specific animal is in the list
animal = "red panda"
if animal in favourite_animals:
    print(f"{animal} is still in the list!")
else:
    print(f"{animal} was removed.")


# ── Exercise 4.2 – Favourite Nap Spots ───────────────────────────
print("\n-- Exercise 4.2: Favourite Nap Spots (Tuple) --")

# A tuple is perfect here: nap spots don't change mid-nap
nap_spots = ("sunny windowsill", "couch corner", "under the bed", "top of bookshelf")

print("Favourite nap spot #1:", nap_spots[0])
print("Secret nap spot (last):", nap_spots[-1])
print("Total nap spots:", len(nap_spots))

# Unpack the first two into named variables
first_choice, second_choice, *rest = nap_spots
print("First choice:", first_choice)
print("Second choice:", second_choice)

# Confirm it's immutable (reading is fine; changing would error)
print("Nap spot type:", type(nap_spots))


# ── Exercise 4.3 – Phone Book ────────────────────────────────────
print("\n-- Exercise 4.3: Phone Book (Dictionary) --")

phone_book = {
    "Alice":   "555-0101",
    "Bob":     "555-0182",
    "Carol":   "555-0193",
    "Dave":    "555-0174",
}

# Look up a number
contact = "Carol"
if contact in phone_book:
    print(f"{contact}'s number: {phone_book[contact]}")

# Add a new contact
phone_book["Eve"] = "555-0165"
print("Added Eve:", phone_book)

# Update an existing number
phone_book["Bob"] = "555-9999"
print("Bob's new number:", phone_book["Bob"])

# Remove a contact
del phone_book["Dave"]
print("After removing Dave:", phone_book)

# Safe lookup for a contact that may not exist
number = phone_book.get("Zara", "Contact not found")
print("Zara:", number)


# ── Exercise 4.4 – Library Database ──────────────────────────────
print("\n-- Exercise 4.4: Library Database (Combined Types) --")

library_db = [
    {
        "title":    "Python Illustrated",
        "author":   "Maaike van Putten",
        "year":     2026,
        "genres":   ["programming", "education"],
        "available": True,
    },
    {
        "title":    "Clean Code",
        "author":   "Robert C. Martin",
        "year":     2008,
        "genres":   ["programming", "best practices"],
        "available": False,
    },
    {
        "title":    "The Pragmatic Programmer",
        "author":   "Andrew Hunt",
        "year":     1999,
        "genres":   ["programming", "career"],
        "available": True,
    },
]

# Print all book titles
print("Books in the library:")
for i in range(len(library_db)):
    print(f"  {i + 1}. {library_db[i]['title']} by {library_db[i]['author']}")

# Access a specific detail – first book's first genre
print("First book, first genre:", library_db[0]["genres"][0])

# Check availability of the second book
book = library_db[1]
status = "available" if book["available"] else "checked out"
print(f"'{book['title']}' is currently {status}.")

# Count how many books are available
available_count = 0
for i in range(len(library_db)):
    if library_db[i]["available"]:
        available_count += 1
print("Books available to borrow:", available_count)
