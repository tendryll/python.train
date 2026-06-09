# Python Fundamentals: Lesson 3
### Chapter 4 — *Python Illustrated*: Using Lists, Tuples, and Dictionaries
**Duration:** 50 minutes | **Audience:** Non-programmers | **IDE:** PyCharm

---

## Lesson Overview

| Segment | Topic | Time |
|---|---|---|
| Warm-Up | Recap of Chapter 3 & why collections exist | 5 min |
| Concept Block A | Lists — creating, accessing, modifying | 12 min |
| Concept Block B | Tuples — immutability, unpacking, when to use | 8 min |
| Concept Block C | Dictionaries — key-value pairs, access, methods | 12 min |
| Hands-On Lab | Building a contact book and favorite-things list | 8 min |
| Wrap-Up | Quiz questions, key takeaways, preview of Chapter 5 | 5 min |

---

## Learning Objectives

By the end of this lesson, participants will be able to:

1. Create a list, access its items by positive and negative index, and modify it using `append()`, `insert()`, `remove()`, and `pop()`.
2. Slice a list to extract a subset of items.
3. Create a tuple, explain why it cannot be modified, and unpack it into variables.
4. Create a dictionary, access values by key, add/update/remove entries, and use `keys()`, `values()`, and `items()`.
5. Combine collections — for example, a dictionary whose values are lists.
6. Choose the right collection type for a given situation.

---

## Materials Needed

- *Python Illustrated* (Chapter 4, pages 85–122)
- PyCharm open with a blank file `lesson3.py`
- Projector / screen share for live demos
- Optional: printed Quick Reference (see Appendix A)

---

## Instructor Preparation Notes

> Chapter 4 introduces the three main Python collection types in one go. The **list** is the longest section and the most important — spend the most time here. Tuples are quick to cover because they share most behaviour with lists. Dictionaries are conceptually fresh and need care around the key/value distinction.
>
> The nested data section (dict of lists, list of dicts) is introduced at the end of the chapter and is genuinely challenging for beginners. Keep the combined-types demo light — it's marked as a stretch in the lab. If the group is struggling, skip it and direct participants to the book exercises instead.

---

## Segment 1 — Warm-Up: Recap & Hook (5 min)

### Quick Recap Questions

- "What is the difference between `if`, `elif`, and `else`?" → *if checks a condition; elif checks another if the first was False; else catches everything that didn't match*
- "What does `and` do?" → *Both sides must be True for the overall condition to be True*
- "Can you have an `if` without an `else`?" → *Yes — else is always optional*

### The Hook

> "So far, every variable holds exactly one value. What if you need to keep a shopping list — say, 50 items? Would you write `item1 = ...`, `item2 = ...` all the way to `item50`? That's 50 variables, and changing any one of them is a nightmare."

Write this on the board:

```
# The painful way
toy1 = "feather"
toy2 = "ball"
toy3 = "laser pointer"

# The Python way
cat_toys = ["feather", "ball", "laser pointer"]
```

> "Collections let you store many values in one variable. Python has three main ones: **lists**, **tuples**, and **dictionaries**. Each has a different purpose. Let's explore them."

---

## Segment 2 — Concept Block A: Lists (12 min)

### Part 1: Creating and Accessing Lists (5 min)

#### What is a list?

> "A list is an ordered, changeable collection of items. The items can be of any type — strings, numbers, even other lists. Order is preserved, and each item has an index number."

#### Creating a list

```python
# Empty list
my_first_list = []

# List with items
cat_toys = ["feather", "ball", "laser pointer", "scratching post"]
```

Square brackets `[]` define the list. Items are separated by commas.

#### Accessing by positive index

> "Each item has an index — a position number. **Crucially: Python starts counting from 0, not 1.**"

```python
cat_toys = ["feather", "ball", "laser pointer", "scratching post"]

print(cat_toys[0])   # feather  (first item)
print(cat_toys[1])   # ball
print(cat_toys[3])   # scratching post  (last item, index = length - 1)
```

Draw on the board:

```
Index:    0          1       2               3
Value: "feather"  "ball"  "laser pointer"  "scratching post"
```

#### Accessing by negative index

> "Python also allows negative indexes — they count backwards from the end. `-1` is always the last item, no matter how long the list is."

```
Index:    0          1       2               3
         -4         -3      -2              -1
```

```python
print(cat_toys[-1])   # scratching post
print(cat_toys[-2])   # laser pointer
```

#### Slicing — getting a subset

```python
favorite_toys = cat_toys[1:4]
print(favorite_toys)
# ['ball', 'laser pointer', 'scratching post']
```

> "Slicing gives you a new list from index `start` up to — but **not including** — index `stop`. The original list is unchanged."

#### Checking if an item exists

```python
if "laser pointer" in cat_toys:
    print("Time to play!")
```

#### Finding the length

```python
print(len(cat_toys))   # 4
```

---

### Part 2: Modifying Lists (7 min)

> "Lists are **mutable** — you can change them after creation. This is one of the key differences from tuples, which we'll see next."

#### Adding items

```python
cat_toys = ["feather", "ball", "laser pointer", "scratching post"]

# Append — adds to the END
cat_toys.append("cardboard box")
print(cat_toys)
# ['feather', 'ball', 'laser pointer', 'scratching post', 'cardboard box']

# Insert — adds at a SPECIFIC INDEX (shifts everything right)
cat_toys.insert(1, "mouse toy")
print(cat_toys)
# ['feather', 'mouse toy', 'ball', 'laser pointer', 'scratching post', 'cardboard box']
```

#### Removing items

```python
# Remove by VALUE — removes first occurrence
cat_toys.remove("ball")

# Remove by INDEX — pop() returns the removed item
removed = cat_toys.pop(2)
print("Removed:", removed)

# Remove ALL items
cat_toys.clear()
print(cat_toys)   # []
```

#### Changing an item

```python
cat_toys = ["feather", "mouse toy", "ball", "laser pointer"]
cat_toys[0] = "cat wand"   # overwrites index 0
print(cat_toys)
# ['cat wand', 'mouse toy', 'ball', 'laser pointer']
```

#### Safe removal with `in`

```python
# Avoid ValueError by checking first
if "cardboard box" in cat_toys:
    cat_toys.remove("cardboard box")
```

#### Concept Check

> "If a list has 5 items and I call `pop()` with no argument, what happens?" *(The last item is removed and returned.)*

> "What is the maximum valid index for a list with 5 items?" *(4 — always length minus 1.)*

---

## Segment 3 — Concept Block B: Tuples (8 min)

### What is a tuple?

> "A tuple looks almost identical to a list — but with one critical difference: **once created, it cannot be changed**. We call that immutability."

### Creating tuples

```python
# Empty tuple
my_first_tuple = ()

# Tuple with items — use parentheses
position = (10, 20)
cat_info = ("Zia", 1, "grey")

# Single-item tuple — the comma is REQUIRED
single_item_tuple = ("only item",)   # with comma = tuple
not_a_tuple      = ("only item")     # without comma = just a string
```

> "The comma is the thing that makes it a tuple, not the parentheses. This trips everyone up at least once."

### Accessing tuple items

```python
cat_info = ("Zia", 1, "grey")
print(cat_info[0])   # Zia
print(cat_info[1])   # 1
print(cat_info[2])   # grey
```

Indexing works exactly the same as lists.

### Immutability — you cannot modify a tuple

```python
cat_info = ("Zia", 1, "grey")
cat_info[1] = 4   # TypeError: 'tuple' object does not support item assignment
```

> "If you need to change values later, use a list. Use a tuple when the data should stay fixed."

### Tuple unpacking

```python
cat_info = ("Zia", 1, "grey")
name, age, color = cat_info

print(name)    # Zia
print(age)     # 1
print(color)   # grey
```

> "Unpacking assigns each position in the tuple (or list — this works on lists too) to a variable in one clean statement. The number of variables must match the number of items."

### When to use tuples

| Use a **list** when… | Use a **tuple** when… |
|---|---|
| The collection will change over time | The data should never change |
| Order matters and items may be added/removed | Storing fixed coordinates, dates, settings |
| You need `append`, `insert`, `remove` | Using the collection as a dictionary key |

---

## Segment 4 — Concept Block C: Dictionaries (12 min)

### What is a dictionary?

> "A dictionary stores data as **key-value pairs**. Think of a real dictionary: you look up a word (the key) to find its definition (the value). In Python, keys are usually strings, and values can be anything."

### Creating a dictionary

```python
# Empty dictionary
my_first_dict = {}

# Dictionary with items
cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna"
}
```

Curly braces `{}`, key-value pairs separated by colons `:`, pairs separated by commas.

### Accessing values

```python
# By key — using square brackets
cat_name = cat_attributes["name"]
print(cat_name)   # Zia

# KeyError if key doesn't exist
breed = cat_attributes["breed"]   # KeyError: 'breed'
```

#### Safe access with `get()`

```python
# Returns None if key not found — no error
breed = cat_attributes.get("breed")
print(breed)   # None

# Returns a default value instead of None
breed = cat_attributes.get("breed", "Unknown")
print(breed)   # Unknown
```

> "Use `get()` when you're not sure if a key exists. Use `[]` when you're certain — it raises an error immediately if something is wrong, which can actually help you spot bugs faster."

### Modifying dictionaries

#### Adding and updating entries

```python
# Add a new key-value pair (key doesn't exist yet)
cat_attributes["hobby"] = "napping"

# Update an existing value (key already exists)
cat_attributes["age"] = 2

print(cat_attributes)
# {'name': 'Zia', 'age': 2, 'color': 'grey', 'favorite_food': 'tuna', 'hobby': 'napping'}
```

> "Adding and updating use the same syntax — Python checks whether the key exists and decides which operation to perform."

#### Removing entries

```python
# del — removes by key; raises KeyError if not found
del cat_attributes["favorite_food"]

# pop() — removes and RETURNS the value; can specify a default
hobby = cat_attributes.pop("hobby")
print("Removed:", hobby)   # Removed: napping

# Safe pop with default — no error if key missing
breed = cat_attributes.pop("breed", "Not specified")
```

### Dictionary methods

```python
cat_attributes = {"name": "Zia", "age": 1, "color": "grey"}

# All keys
print(list(cat_attributes.keys()))
# ['name', 'age', 'color']

# All values
print(list(cat_attributes.values()))
# ['Zia', 1, 'grey']

# All key-value pairs (returns list of tuples)
print(list(cat_attributes.items()))
# [('name', 'Zia'), ('age', 1), ('color', 'grey')]
```

### Checking key existence

```python
if "age" in cat_attributes:
    print("I know my age!")
```

### Common mistake — KeyError

```python
friends_ages = {"Zia": 1, "Wiesje": 7}

# Safe approach with in
if "Szara" in friends_ages:
    print(friends_ages["Szara"])
else:
    print("Key not found.")

# Safe approach with get()
print(friends_ages.get("Szara", "Key not found."))
```

---

### Stretch: Combining Data Types

> "The real power of collections is combining them. A dictionary value can be a list. A list can contain dictionaries. This is how real-world data is structured."

```python
cat_attributes = {
    "name": "Zia",
    "age": 1,
    "hobbies": ["napping", "programming", "playing"],   # list as a value
    "friends": [
        {"name": "Wiesje", "age": 7},                   # dict inside a list
        {"name": "Muchu",  "age": 0}
    ]
}

# Access Zia's second hobby
print(cat_attributes["hobbies"][1])          # programming

# Access Wiesje's name (first friend)
print(cat_attributes["friends"][0]["name"])  # Wiesje

# Access Muchu's name (second friend)
print(cat_attributes["friends"][1]["name"])  # Muchu
```

> "Read it one step at a time from left to right. Each `[]` narrows you down to the next level. If you get lost, print the intermediate result to see what type you're working with."

---

## Segment 5 — Hands-On Lab (8 min)

### Instructor Notes

Open `lesson3.py` on screen. Type and run each exercise live, then give participants 4–5 minutes to work through Exercise A independently. Exercise B is a stretch. Move around the room — focus help on index-off-by-one errors and missing colons in dictionaries.

---

### Exercise A — Favourite Animals List (4 min)

```python
# Exercise A: Favourite Animals
favourite_animals = ["dachshund", "axolotl", "capybara", "octopus", "red panda"]

# How many?
print("I have", len(favourite_animals), "favourite animals.")

# First item
print("The", favourite_animals[0], "is my first favourite animal.")

# Last item (using negative index)
print("The", favourite_animals[-1], "is the last favourite animal on my list.")

# Add one
favourite_animals.append("quokka")
print("After adding:", favourite_animals)

# Remove one
favourite_animals.remove("capybara")
print("After removing:", favourite_animals)

# Slice — first three
top_three = favourite_animals[:3]
print("Top three:", top_three)
```

Ask participants to use **their own** favourite animals and run it.

**Discussion prompt:** "What index would you use to get the second-to-last item without knowing the length of the list?" *(Answer: `-2`.)*

---

### Exercise B — Simple Contact Book (4 min)

```python
# Exercise B: Contact Book
contacts = {
    "Alice": "555-1234",
    "Bob":   "555-5678",
    "Carol": "555-9012"
}

# Add a new contact
contacts["Dave"] = "555-3456"

# Check if Maaike exists; add if not
if "Maaike" not in contacts:
    contacts["Maaike"] = "555-0000"

# Safe removal — no error if key missing
contacts.pop("Eve", None)

# Print all names
print("Contacts:", list(contacts.keys()))

# Print all entries
for name, number in contacts.items():
    print(name, "→", number)
```

> "We'll cover `for` loops in Chapter 5 — the last two lines are a preview. For now, just run it and observe the output."

---

## Segment 6 — Wrap-Up: Quiz, Takeaways, and Preview (5 min)

### Quick Quiz (select from the book's Chapter 4 quiz)

1. "Given `dog_names = ["Chewie", "Frits", "Wiesje"]`, which removes `"Wiesje"` — `pop(3)`, `pop(2)`, `del(2)`, or `remove("Wiesje")`?"
   *(Answer: `pop(2)` **or** `remove("Wiesje")` — both work. `pop(3)` is out of range. `del` is a statement, not a method called with dot notation.)*

2. "What is `mystery_variable = ("Hey there")` — a tuple, list, or string?"
   *(Answer: **string** — no trailing comma, so Python sees parentheses around a string, not a tuple.)*

3. "True or false: `get()` only prevents `KeyError` if you provide a default value."
   *(Answer: False — `get()` returns `None` even without a default, which avoids the error.)*

4. "What does `grocery_list[2:-2]` return for a 6-item list?"
   *(Answer: items at index 2 and 3 — `['peanut butter', 'bread']`)*

5. "What is happening here? `appetizer, main_course, dessert = menu`"
   *(Answer: unpacking — the three list values are assigned to the three variables in one statement.)*

### Key Takeaways

1. **Lists** `[]` — ordered, mutable, duplicates allowed. Use for collections that change.
2. **Tuples** `()` — ordered, **immutable**, duplicates allowed. Use for fixed data.
3. **Dictionaries** `{}` — key-value pairs, mutable, keys must be unique. Use for lookups by name.
4. Indexing starts at **0**. Negative indexes count from the end (`-1` = last).
5. Slicing `[start:stop]` returns a new collection — the `stop` index is **not** included.
6. Use `get()` instead of `[]` on dictionaries when a key might not exist.
7. Use `in` to check membership before accessing or removing — avoids `ValueError` and `KeyError`.
8. Collections can be nested: lists inside dicts, dicts inside lists, etc.

### Preview of Chapter 5

> "Next lesson we meet **loops** — `for` and `while`. Combined with the collections we learned today, loops let you process every item in a list or dictionary automatically. That's where the real programming power begins."

### Recommended Practice Before Next Session

Complete book exercises 4.1 (favourite animals), 4.2 (nap spots — list manipulation), 4.3 (phone book — dictionary), and as much of 4.4 (library database — nested data) as you can manage.

---

## Appendix A — Quick Reference Cheat Sheet

```
LISTS  [ ]
──────────────────────────────────────────────
my_list = ["a", "b", "c"]         # create
my_list[0]                         # first item  → "a"
my_list[-1]                        # last item   → "c"
my_list[1:3]                       # slice       → ["b", "c"]
len(my_list)                       # length      → 3
"b" in my_list                     # check       → True

my_list.append("d")                # add to end
my_list.insert(1, "x")            # add at index 1
my_list.remove("b")               # remove by value
my_list.pop(0)                     # remove by index; returns item
my_list.pop()                      # remove last item
my_list.clear()                    # remove all
my_list[0] = "z"                   # change item at index 0

TUPLES  ( )
──────────────────────────────────────────────
my_tuple = (10, 20, 30)           # create
my_tuple[0]                        # access → 10
a, b, c = my_tuple                # unpack
single = ("x",)                   # single-item tuple (comma required!)

DICTIONARIES  { }
──────────────────────────────────────────────
d = {"name": "Zia", "age": 1}     # create
d["name"]                          # access → "Zia"
d.get("breed")                     # safe access → None
d.get("breed", "Unknown")         # safe with default → "Unknown"

d["hobby"] = "napping"            # add new key
d["age"] = 2                       # update existing key
del d["hobby"]                     # remove (KeyError if missing)
d.pop("hobby")                     # remove and return value
d.pop("hobby", None)              # safe remove

list(d.keys())                     # all keys
list(d.values())                   # all values
list(d.items())                    # all (key, value) pairs
"age" in d                         # check key → True

NESTED EXAMPLE
──────────────────────────────────────────────
data = {
    "hobbies": ["napping", "playing"],
    "friends": [{"name": "Wiesje"}, {"name": "Muchu"}]
}
data["hobbies"][1]                 # "playing"
data["friends"][0]["name"]        # "Wiesje"

CHOOSING THE RIGHT COLLECTION
──────────────────────────────────────────────
Need to change items?         → list
Data must stay fixed?         → tuple
Need to look up by name/key?  → dictionary
```

---

## Appendix B — Instructor Troubleshooting Guide

| Error | Likely Cause | Fix |
|---|---|---|
| `IndexError: list index out of range` | Accessed index ≥ length of list | Check with `len()` before accessing; remember last valid index is `len - 1` |
| `IndexError` with negative index | Index more negative than list length | e.g. `[-5]` on a 4-item list — use `in range` check |
| `ValueError: list.remove(x): x not in list` | Tried to remove item that doesn't exist | Check with `if item in my_list:` first |
| `TypeError: 'tuple' object does not support item assignment` | Tried to change a tuple | Use a list instead if values need to change |
| `("item")` not recognised as a tuple | Missing trailing comma | Change to `("item",)` |
| `KeyError: 'key'` | Accessed dict key that doesn't exist | Use `get()` or check with `if key in dict:` first |
| Dict value is `None` unexpectedly | Used `get()` without a default | Add a default: `dict.get("key", "default")` |
| `SyntaxError` inside dict literal | Missing colon `:` or comma `,` between pairs | Check every pair follows `"key": value,` pattern |

---

*Lesson prepared for use with Python Illustrated (Markowska), Chapter 4. Duration: 50 minutes.*
