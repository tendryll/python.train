# Python Fundamentals: Lessons 3 & 4
### Chapter 4 — *Python Illustrated*: Using Lists, Tuples, and Dictionaries
**Format:** Two 50-minute sessions, one week apart | **Audience:** Non-programmers | **IDE:** PyCharm

---

## Why Split This Chapter Over Two Weeks?

Chapter 4 introduces three substantial data structures in one go. In a single 50-minute session, dictionaries inevitably get rushed and the combined-types section gets cut entirely — yet that's often where the most "aha" moments happen. Splitting the chapter gives:

- **Week 1** — a deep, unhurried treatment of **lists**, the most-used and most foundational collection.
- **Week 2** — **tuples** (quick, since they share most behaviour with lists) and a properly-paced treatment of **dictionaries**, including the combined-types material that's normally cut for time.

---

# WEEK 1 — Lists

## Lesson Overview

| Segment | Topic | Time |
|---|---|---|
| Warm-Up | Recap of Chapter 3 & why collections exist | 5 min |
| Concept Block A | Creating and accessing lists (indexing, slicing) | 15 min |
| Concept Block B | Modifying lists (add, remove, change) | 15 min |
| Hands-On Lab | Favourite animals & nap spots exercises | 10 min |
| Wrap-Up | Quiz, key takeaways, preview of Week 2 | 5 min |

## Learning Objectives — Week 1

By the end of this session, participants will be able to:

1. Create an empty list and a list containing items of mixed types.
2. Access list items using both positive and negative indices.
3. Use slicing to extract a sublist without modifying the original.
4. Use `len()` and `in` to inspect a list.
5. Modify a list using `append()`, `insert()`, `remove()`, `pop()`, `clear()`, and direct index assignment.

## Materials Needed

- *Python Illustrated* (Chapter 4, pages 85–96)
- PyCharm open with a blank file `lesson3a.py`
- Projector / screen share for live demos
- Optional: printed Quick Reference (see Appendix A)

---

## Segment 1 — Warm-Up: Recap & Hook (5 min)

### Quick Recap Questions

- "What is the difference between `if`, `elif`, and `else`?" → *if checks a condition; elif checks another if the first was False; else catches everything that didn't match*
- "What does `and` do?" → *Both sides must be True for the overall condition to be True*
- "Can you have an `if` without an `else`?" → *Yes — else is always optional*

### The Hook

> "So far, every variable holds exactly one value. What if you need to keep a shopping list — say, 50 items? Would you write `item1 = ...`, `item2 = ...` all the way to `item50`? That's 50 variables, and changing any one of them is a nightmare."

Write this on the board:

```python
# The painful way
toy1 = "feather"
toy2 = "ball"
toy3 = "laser pointer"

# The Python way
cat_toys = ["feather", "ball", "laser pointer"]
```

> "Collections let you store many values in one variable. Python has three main ones: lists, tuples, and dictionaries. Today we focus entirely on lists — the most commonly used of the three. Next week, we'll cover the other two."

---

## Segment 2 — Concept Block A: Creating and Accessing Lists (15 min)

### What is a List?

> "A list is an ordered, changeable collection of items. The items can be of any type — strings, numbers, even other lists. Order is preserved, and each item has an index number."

### Creating a List

```python
# Empty list
my_first_list = []

# List with items
cat_toys = ["feather", "ball", "laser pointer", "scratching post"]
```

Square brackets `[]` define the list. Items are separated by commas. Items in this example are strings, so they're enclosed in quotes.

### Accessing by Positive Index

> "Each item has an index — a position number. **Crucially: Python starts counting from 0, not 1.**"

```python
cat_toys = ["feather", "ball", "laser pointer", "scratching post"]

print("First toy:", cat_toys[0])    # feather
print("Second toy:", cat_toys[1])   # ball
print("Third toy:", cat_toys[2])    # laser pointer
print("Fourth toy:", cat_toys[3])   # scratching post
```

Draw on the board:

```
Index:    0          1       2               3
Value: "feather"  "ball"  "laser pointer"  "scratching post"
```

> "If we try to access an index that doesn't exist — like `cat_toys[4]` — we get an `IndexError`. The maximum valid index is always the length of the list minus one."

### Accessing by Negative Index

> "Python also allows negative indices — they count backwards from the end. `-1` is always the last item, no matter how long the list is."

```
Element              Positive index    Negative index
feather              0                 -4
ball                 1                 -3
laser pointer        2                 -2
scratching post      3                 -1
```

```python
last_toy = cat_toys[-1]
print("Last toy:", last_toy)
# Last toy: scratching post
```

> "If we try `cat_toys[-5]` on this 4-item list, we get an error too — there's nothing that far back."

### Concept Check

> "Can you have an `if` without an `else`?" — already covered, swap for: "What index would give us the third item — the laser pointer — using a negative index?" *(Answer: `-2`)*

---

### Slicing Lists (5 min)

> "Slicing lets you grab a *subset* of a list — a sublist — without changing the original."

The syntax is `list_name[start:stop]` — note that `stop` is **not included**.

```python
cat_toys = ["feather", "mouse toy", "ball", "laser pointer", "scratching post"]

favorite_toys = cat_toys[1:4]
print("Favorite toys:", favorite_toys)
# Favorite toys: ['mouse toy', 'ball', 'laser pointer']
```

> "`cat_toys[1:4]` gets items from index 1 up to, but not including, index 4 — so indices 1, 2, and 3. The original `cat_toys` list is completely unchanged. The new `favorite_toys` list has its own fresh indices: 0, 1, and 2."

---

### List Length and Membership (5 min)

```python
cat_toys = ["feather", "mouse toy", "ball", "laser pointer", "scratching post"]

# How many items?
number_of_toys = len(cat_toys)
print("I have", number_of_toys, "toys.")
# I have 5 toys.
```

> "`len()` is a **function**, not a method. The difference: a method is called *on* a variable with a dot, like `cat_toys.append(...)`. A function exists independently and is called with the variable passed in, like `len(cat_toys)`."

**Checking if an item exists with `in`:**

```python
if "laser pointer" in cat_toys:
    print("Time to play with the laser pointer!")
else:
    print("No laser pointer found.")
# Time to play with the laser pointer!
```

> "`in` returns `True` or `False`. We'll use this constantly when modifying lists, to avoid errors — which brings us to our next section."

---

## Segment 3 — Concept Block B: Modifying Lists (15 min)

> "Lists are **mutable** — you can change them after creation. This is a defining feature of lists, and it's something tuples (next week) cannot do."

### Adding Items (5 min)

**`append()`** — adds an item to the **end** of the list:

```python
cat_toys = ["feather", "ball", "laser pointer", "scratching post"]

cat_toys.append("cardboard box")
print("Updated toys:", cat_toys)
# Updated toys: ['feather', 'ball', 'laser pointer', 'scratching post', 'cardboard box']
```

**`insert()`** — adds an item at a **specific index**, shifting everything after it to the right:

```python
cat_toys.insert(1, "mouse toy")
print("After inserting at index 1:", cat_toys)
# After inserting at index 1: ['feather', 'mouse toy', 'ball', 'laser pointer', 'scratching post', 'cardboard box']
```

> "Notice `insert()` takes **two** arguments: the index, then the value. It doesn't overwrite — it shifts everything from that position onwards one slot to the right."

Draw the updated index table on the board:

```
Element              Positive index    Negative index
feather              0                 -6
mouse toy            1                 -5
ball                 2                 -4
laser pointer        3                 -3
scratching post      4                 -2
cardboard box        5                 -1
```

### Removing Items (6 min)

**`remove()`** — removes the **first occurrence of a value**:

```python
cat_toys = ["feather", "mouse toy", "ball", "laser pointer", "scratching post", "cardboard box"]

cat_toys.remove("ball")
print("After removing 'ball':", cat_toys)
# After removing 'ball': ['feather', 'mouse toy', 'laser pointer', 'scratching post', 'cardboard box']
```

> "If `'ball'` weren't in the list, `remove()` would raise a `ValueError`. We'll see how to guard against that shortly. Also note: everything after the removed item shifts left by one — there are never gaps in the indices."

**`pop()`** — removes by **index** (or removes the last item if no index given):

```python
cat_toys.pop(2)
print("After popping index 2:", cat_toys)
# After popping index 2: ['feather', 'mouse toy', 'scratching post', 'cardboard box']
```

> "`pop(2)` removed `'laser pointer'` (which was at index 2). Like `remove()`, everything after it shifts left."

**`clear()`** — removes **everything**:

```python
cat_toys.clear()
print("After clearing:", cat_toys)
# After clearing: []
```

### Changing Items (2 min)

```python
cat_toys = ["feather", "mouse toy", "ball", "laser pointer", "scratching post", "cardboard box"]

cat_toys[0] = "cat wand"
print("After changing:", cat_toys)
# After changing: ['cat wand', 'mouse toy', 'ball', 'laser pointer', 'scratching post', 'cardboard box']
```

> "Just assign directly to an index using `=`, and the existing item at that position is overwritten."

### Safe Removal Using `in` (2 min)

```python
cat_toys = ["feather", "mouse toy", "ball", "laser pointer", "scratching post", "cardboard box"]

if "cardboard box" in cat_toys:
    print("Oh no, she's throwing away my box!")
    cat_toys.remove("cardboard box")
else:
    print("No box to throw away.")
```

> "This combines what we learned today: checking membership with `in` *before* calling `remove()`. This avoids a `ValueError` if the item isn't there. We'll see this same pattern again next week with dictionaries."

---

## Segment 4 — Hands-On Lab: Favourite Animals & Nap Spots (10 min)

### Instructor Notes

Open `lesson3a.py` on screen. Walk through Exercise A together as a class (3–4 minutes), then give participants the remaining time to attempt Exercise B independently. Move around the room — focus help on off-by-one indexing errors.

### Exercise A — Favourite Animals (4 min, demo together)

```python
# Exercise A: Favourite Animals
favourite_animals = ["dachshund", "axolotl", "capybara", "octopus", "red panda"]

print("My favourite animals:", favourite_animals)

# How many?
print("I have", len(favourite_animals), "favourite animals.")

# First item
print("The", favourite_animals[0], "is my first favourite animal.")

# Last item (using negative index)
print("The", favourite_animals[-1], "is the last favourite animal on my list.")
```

Ask participants to swap in their own favourite animals and re-run.

### Exercise B — Favourite Nap Spots (6 min, independent)

This exercise mirrors the book's Exercise 4.2 and uses every list operation from today's lesson.

```python
# Exercise B: Favourite Nap Spots
fav_nap_spots = ["window", "cardboard box", "human's lap", "luxurious cat bed"]

# 1. Remove "luxurious cat bed" — turns out it's not that great after all
fav_nap_spots.remove("luxurious cat bed")

# 2. Add "keyboard" as the very first item
fav_nap_spots.insert(0, "keyboard")

# 3. Add "sunbeam on the floor" as the third item
fav_nap_spots.insert(2, "sunbeam on the floor")

# 4. Add "Wiesje's bed" at the end
fav_nap_spots.append("Wiesje's bed")

# 5. How many nap spots now?
print("Number of nap spots:", len(fav_nap_spots))

# 6. Add "human bed" only if it's not already there
if "human bed" not in fav_nap_spots:
    fav_nap_spots.append("human bed")

print("Final list:", fav_nap_spots)

# 7. Top three favourite spots, using slicing
top_three = fav_nap_spots[:3]
print("Top three:", top_three)
```

**Bonus challenge** (for fast finishers — from the book):

> "The cardboard box didn't make it into the top three! Swap `'cardboard box'` with `'window'` so the box ends up in the top three. Use index assignment — grab the items by their indices, store them in temporary variables, and swap them."

```python
# Bonus: swap two items by index
fav_nap_spots[0], fav_nap_spots[1] = fav_nap_spots[1], fav_nap_spots[0]
print("After swap:", fav_nap_spots)
```

> "This double-assignment trick — `a, b = b, a` — is a neat bit of Python. We won't dwell on *why* it works today, but it's a handy pattern to recognise."

---

## Segment 5 — Wrap-Up: Quiz, Takeaways, and Preview (5 min)

### Quick Quiz (selected from the book's Chapter 4 quiz — list-focused questions)

1. "Given `dog_names = ["Chewie", "Frits", "Wiesje", "Doesie", "Takkie", "Timo", "Bobby"]`, which option(s) remove `"Wiesje"` from the list — `pop("Wiesje")`, `pop(2)`, `del(2)`, or `remove("Wiesje")`?"
   *(Answer: `pop(2)` and `remove("Wiesje")` both work. `pop("Wiesje")` fails — `pop()` takes an index, not a value. `del(2)` isn't valid method syntax.)*

2. "What method allows you to add an item at a specific index of a list?"
   *(Answer: `insert()`)*

3. "What will `grocery_list[2:-2]` return for `["apples", "cucumber", "peanut butter", "bread", "coffee", "chocolate"]`?"
   *(Answer: `['peanut butter', 'bread']` — items at index 2 and 3, since -2 means "stop two before the end".)*

4. "How can you find the number of items in a list?"
   *(Answer: `len(list_name)`)*

### Key Takeaways — Week 1

1. Lists `[]` are **ordered** and **mutable** — you can change them after creation.
2. Indexing starts at **0**. Negative indices count backwards from the end (`-1` = last item).
3. Slicing `[start:stop]` returns a **new** list — the `stop` index is **not** included; the original list is unchanged.
4. `len()` and `in` are your inspection tools — use `in` *before* removing to avoid errors.
5. To add: `append()` (end), `insert(index, value)` (specific position).
6. To remove: `remove(value)` (by value), `pop(index)` (by index, returns the item), `clear()` (everything).
7. To change: assign directly to an index, e.g. `my_list[0] = "new value"`.

### Preview of Week 2

> "Today we mastered lists — the workhorse of Python collections. Next week we meet two more collection types: **tuples**, which are like lists but cannot be changed, and **dictionaries**, which let you look things up by name instead of by position. We'll also see how to combine all three into more complex, realistic data structures."

### Recommended Practice Before Next Session

Complete book Exercise 4.1 (favourite animals) if not already done, and finish Exercise 4.2 (nap spots) including the bonus swap challenge.

---
---

# WEEK 2 — Tuples and Dictionaries

## Lesson Overview

| Segment | Topic | Time |
|---|---|---|
| Warm-Up | Recap of lists & quick-fire list quiz | 5 min |
| Concept Block A | Tuples — immutability and unpacking | 10 min |
| Concept Block B | Dictionaries — creating, accessing, modifying | 15 min |
| Concept Block C | Dictionary methods, common mistakes, combining types | 10 min |
| Hands-On Lab | Contact book + combined-types stretch | 8 min |
| Wrap-Up | Quiz, key takeaways, preview of Chapter 5 | 2 min |

## Learning Objectives — Week 2

By the end of this session, participants will be able to:

1. Create a tuple, explain why it cannot be modified, and unpack it into variables.
2. Create a dictionary, access values by key safely, and add, update, and remove entries.
3. Use `keys()`, `values()`, and `items()` to inspect a dictionary.
4. Avoid `IndexError` and `KeyError` using `len()`, `in`, and `get()`.
5. Combine collections — for example, a dictionary whose values are lists or other dictionaries.
6. Choose an appropriate collection type (list, tuple, or dictionary) for a given scenario.

## Materials Needed

- *Python Illustrated* (Chapter 4, pages 96–122)
- PyCharm open with a blank file `lesson3b.py`
- Projector / screen share for live demos
- Optional: printed Quick Reference (see Appendix B)

---

## Segment 1 — Warm-Up: Recap & Quick-Fire Quiz (5 min)

### Recap Questions (call-and-response)

- "How do you get the last item of a list without knowing its length?" → `my_list[-1]`
- "What's the difference between `append()` and `insert()`?" → *append adds to the end; insert adds at a chosen index and shifts everything else right*
- "What does slicing `[1:4]` actually include?" → *indices 1, 2, and 3 — not 4*
- "Name one way to avoid an error when removing an item that might not be in a list." → *check with `in` first*

### Today's Hook

> "Lists are great when your data needs to change. But sometimes you want the *opposite* guarantee — data that should **never** change, like someone's date of birth. And sometimes you don't care about *position* at all — you want to look things up by *name*, like a phone book. That's where tuples and dictionaries come in."

---

## Segment 2 — Concept Block A: Tuples (10 min)

### What is a Tuple?

> "A tuple is similar to a list. There is one important difference: after you create a tuple, it **cannot be modified**. We call that immutability. It's like your date of birth — you can't change it, no matter how badly you might want to be younger!"

### Creating Tuples

```python
# Empty tuple — parentheses instead of square brackets
my_first_tuple = ()

# Tuple with items
position = (10, 20)

# Tuples can mix data types, just like lists
cat_info = ("Zia", 1, "grey")
```

### The Single-Item Tuple Trap

```python
# NOT a tuple — just a string in parentheses
not_a_tuple = ("only item")

# Correct way to create a single-item tuple — note the comma!
single_item_tuple = ("only item",)
```

> "Without the comma, Python sees `("only item")` as just a string with parentheses around it — the parentheses don't do anything. **The comma is what makes it a tuple**, not the parentheses. This is one of the most common 'gotchas' in Python — even experienced developers get caught by this occasionally."

> "As a side note: you can technically create a tuple without parentheses at all — `still_a_tuple = "Zia", 1, "grey"` — but I don't recommend it, since it can be confusing about what type you're creating."

### Accessing Tuple Items

```python
cat_info = ("Zia", 1, "grey")

name = cat_info[0]
age = cat_info[1]
color = cat_info[2]

print("Name:", name)    # Name: Zia
print("Age:", age)      # Age: 1
print("Color:", color)  # Color: grey
```

> "Indexing works exactly the same as with lists — including negative indices and slicing."

### Immutability in Action

```python
cat_info = ("Zia", 1, "grey")

cat_info[1] = 4
# Error: 'tuple' object does not support item assignment
```

> "Python raises a `TypeError` because tuples cannot be changed after creation. If you find yourself needing to change values, that's your signal to use a list instead."

### Tuple Unpacking (3 min)

> "Here's something cool we haven't seen yet: we can assign each item in a tuple to its own variable, all in a single line."

```python
cat_info = ("Zia", 1, "grey")
name, age, color = cat_info

print(name)    # Zia
print(age)     # 1
print(color)   # grey
```

> "The first item, `'Zia'`, goes to `name`. The second, `1`, goes to `age`. The third, `'grey'`, goes to `color`. This is called **unpacking**. The number of variables on the left must match the number of items in the tuple — if they don't match, Python raises an error."

> "Bonus: this works with lists too! `name, age, color = ["Zia", 1, "grey"]` works exactly the same way."

### Why Use Tuples? (Discussion, 1 min)

> "Two reasons: First, when you want a guarantee the data can't accidentally change — useful for things like fixed coordinates or configuration values. Second — and this is more advanced — tuples can be used as dictionary keys, which lists cannot. We'll see dictionary keys in a moment."

---

## Segment 3 — Concept Block B: Dictionaries (15 min)

### What is a Dictionary?

> "In English, a dictionary is a big book with words and their meanings. In Python, a dictionary is a collection of **key-value pairs**. You look up a word — the key — to get its definition — the value. Dictionaries let you store and retrieve data based on unique keys, rather than by position like lists and tuples."

### Creating Dictionaries (3 min)

```python
# Empty dictionary — curly braces
my_first_dict = {}

# Dictionary with items
cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna"
}
```

> "Each key-value pair is written as `\"key\": value`. Pairs are separated by commas, just like list items. Keys are usually strings, but they can be any **immutable** type — strings, numbers, or tuples. That's the second reason tuples matter!"

### Accessing Values (4 min)

```python
cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna"
}

cat_name = cat_attributes["name"]
print("My name is", cat_name)
# My name is Zia
```

> "`cat_attributes[\"name\"]` retrieves the value associated with the key `\"name\"`. Note: we **cannot** use a numeric index like `cat_attributes[0]` — dictionaries are accessed by key, not by position."

**What happens with a missing key?**

```python
breed = cat_attributes["breed"]
# KeyError: 'breed'
```

> "Since `\"breed\"` isn't a key in this dictionary, Python raises a `KeyError`. Just like `IndexError` for lists, this is a very common error you'll encounter — and there's a clean way to avoid it."

**The `get()` method:**

```python
# Returns None if the key doesn't exist — no error
breed = cat_attributes.get("breed")
print("Breed:", breed)
# Breed: None

# Returns a default value of your choosing instead of None
breed = cat_attributes.get("breed", "Unknown")
print("Breed:", breed)
# Breed: Unknown
```

> "`None` is a special Python value meaning 'nothing here' — similar to `null` in other languages. With `get()`, we can also supply our own fallback value as a second argument."

### Modifying Dictionaries (5 min)

**Adding and updating — same syntax for both:**

```python
# "hobby" doesn't exist yet — this ADDS it
cat_attributes["hobby"] = "napping"

# "age" already exists — this UPDATES it
cat_attributes["age"] = 2

print("Updated attributes:", cat_attributes)
# Updated attributes: {'name': 'Zia', 'age': 2, 'color': 'grey', 'favorite_food': 'tuna', 'hobby': 'napping'}
```

> "Python checks: does this key already exist? If yes, update its value. If no, add a new key-value pair. Same line of code, two different behaviours depending on the situation."

**Removing entries — three ways:**

```python
# del — removes a key-value pair; raises KeyError if the key doesn't exist
del cat_attributes["favorite_food"]
print("After deletion:", cat_attributes)

# This would raise KeyError: 'breed'
# del cat_attributes["breed"]
```

```python
# pop() — removes the key AND returns its value
hobby = cat_attributes.pop("hobby")
print("Removed hobby:", hobby)
print("After popping 'hobby':", cat_attributes)
# Removed hobby: napping
```

```python
# pop() with a default — avoids KeyError entirely
breed = cat_attributes.pop("breed", "Not specified")
print(breed)
# Not specified
```

> "Notice the pattern: `del` and plain `pop()` both raise `KeyError` for missing keys. Adding a default value to `pop()` — just like with `get()` — avoids the error."

### Concept Check

> "If `cat_attributes` has the key `\"age\"` already, what happens when I run `cat_attributes[\"age\"] = 5`?" *(Answer: the existing value is updated to 5 — no new key is created.)*

---

## Segment 4 — Concept Block C: Dictionary Methods, Common Mistakes & Combining Types (10 min)

### Dictionary Methods (3 min)

```python
cat_attributes = {"name": "Zia", "age": 1, "color": "grey"}

# All keys
keys = cat_attributes.keys()
print("Keys:", list(keys))
# Keys: ['name', 'age', 'color']

# All values
values = cat_attributes.values()
print("Values:", list(values))
# Values: ['Zia', 1, 'grey']

# All key-value pairs, as tuples!
items = cat_attributes.items()
print("Items:", list(items))
# Items: [('name', 'Zia'), ('age', 1), ('color', 'grey')]
```

> "`keys()`, `values()`, and `items()` each return a special 'view object'. We convert these to lists with `list()` so we can see and work with them. Notice `items()` gives us a list of **tuples** — everything we learned today connects!"

**Checking key existence:**

```python
if "age" in cat_attributes:
    print("I know my age!")
else:
    print("Age is unknown.")
# I know my age!
```

> "Just like checking membership in a list — `in` works on dictionaries too, but it checks **keys**, not values."

### Common Mistakes (3 min)

**`IndexError` with lists/tuples — recap from last week:**

```python
some_numbers = [1, 2, 3]

index = 3
if index < len(some_numbers):
    print(some_numbers[index])
else:
    print("Index out of range.")
# Index out of range.
```

**`KeyError` with dictionaries — today's equivalent:**

```python
friends_ages = {"Zia": 1, "Wiesje": 7, "Muchu": 0}

key = "Szara"
if key in friends_ages:
    print(friends_ages[key])
else:
    print("Key not found.")
# Key not found.

# Or, equivalently, using get():
value = friends_ages.get(key, "Key not found.")
print(value)
# Key not found.
```

> "Both approaches are valid — `in` plus an `if/else`, or `get()` with a default. Use `get()` when a simple default value makes sense. Use `in` when the 'not found' case needs more complex handling — for example, if you'd otherwise need to keep working with whatever `get()` returned, and a placeholder value might cause *further* errors down the line."

### Combining Data Types (4 min)

> "The values in lists, tuples, and dictionaries can be anything — including other lists, tuples, and dictionaries. This is how we build realistic, structured data."

```python
cat_attributes = {
    "name": "Zia",
    "age": 1,
    "color": "grey",
    "favorite_food": "tuna",
    "hobbies": ["napping", "programming", "playing"]
}

# Print the whole list of hobbies
print(cat_attributes["hobbies"])
# ['napping', 'programming', 'playing']

# Print just the second hobby
print(cat_attributes["hobbies"][1])
# programming
```

> "`cat_attributes[\"hobbies\"]` gives us a list. Once we have that list, we can index into it normally with `[1]`. Each `[]` takes you one level deeper."

**One level deeper still — a list of dictionaries inside a dictionary:**

```python
cat_attributes = {
    "name": "Zia",
    "age": 1,
    "hobbies": ["napping", "programming", "playing"],
    "friends": [
        {"name": "Wiesje", "age": 7, "hobbies": ["napping", "visiting the forest"]},
        {"name": "Muchu", "age": 0, "hobbies": ["napping in the couch", "chasing anything"]}
    ]
}

# Get Wiesje's name (first friend)
print(cat_attributes["friends"][0]["name"])
# Wiesje

# Get Wiesje's second hobby
print(cat_attributes["friends"][0]["hobbies"][1])
# visiting the forest

# Get Muchu's name and first hobby
print(cat_attributes["friends"][1]["name"], "loves", cat_attributes["friends"][1]["hobbies"][0])
# Muchu loves napping in the couch
```

> "Take it one step at a time: `[\"friends\"]` gets the list of friends. `[0]` gets the first friend — a dictionary. `[\"name\"]` gets that friend's name. If you ever get lost, `print()` the intermediate result to see exactly what type you're working with at each step."

---

## Segment 5 — Hands-On Lab: Contact Book + Combined Types (8 min)

### Instructor Notes

Open `lesson3b.py` on screen. Exercise A is the core exercise — give it most of the time. Exercise B is a stretch for fast finishers; don't worry if most participants don't reach it.

### Exercise A — Phone Book (5 min)

This mirrors the book's Exercise 4.3 and exercises everything from today's dictionary content.

```python
# Exercise A: Phone Book
contacts = {
    "Alice": "555-1234",
    "Bob": "555-5678",
    "Carol": "555-9012"
}

# 1. Add a new contact
contacts["Dave"] = "555-3456"

# 2. Check if "Maaike" exists; if not, add her with a made-up number
if "Maaike" not in contacts:
    contacts["Maaike"] = "555-0000"

# 3. Delete a contact safely — won't error if missing
contacts.pop("Eve", None)

# 4. Print all the names
print("All contacts:", list(contacts.keys()))
```

Ask participants to add 1–2 of their own contacts and verify with `print(contacts)`.

### Exercise B — Combining Types: A Mini Library (3 min, stretch)

This is a simplified taste of the book's Exercise 4.4.

```python
# Exercise B (stretch): Mini library catalog
library = {
    "Jane Eyre": {
        "author": "Charlotte Brontë",
        "page_count": 659,
        "available": True,
        "genres": ["Victorian fiction", "Bildungsroman"]
    },
    "Python Illustrated": {
        "author": "Zia van Putten",
        "page_count": 432,
        "available": False,
        "borrowed_by": "Jacob",
        "genres": ["Informative", "Education"]
    }
}

# Print all book titles
print("Titles:", list(library.keys()))

# Check if "Python Illustrated" is available
if not library["Python Illustrated"]["available"]:
    print("Python Illustrated is borrowed by", library["Python Illustrated"]["borrowed_by"])

# Check if "Romance" is a genre of "Python Illustrated"
if "Romance" in library["Python Illustrated"]["genres"]:
    print("Yes, it's a romance.")
else:
    print("No, it's not a romance.")
```

> "If time allows, ask: 'How would you check the page count of Jane Eyre?'" *(Answer: `library["Jane Eyre"]["page_count"]`)*

---

## Segment 6 — Wrap-Up: Quiz, Takeaways, and Preview (2 min)

### Quick Quiz (selected from the book's Chapter 4 quiz — tuple/dictionary-focused questions)

1. "What is the type of `mystery_variable = (\"Hey there\")`?"
   *(Answer: **String** — without a trailing comma, parentheses around a single value don't create a tuple.)*

2. "What is **not** allowed with a tuple — accessing by index, nested data, changing an element, or duplicate items?"
   *(Answer: **Changing an element directly** — tuples are immutable.)*

3. "Given `human_attributes` with `\"hobbies\": [\"crochet\", \"skating\", \"sewing\"]`, how would you change `\"crochet\"` to `\"knitting\"`?"
   *(Answer: `human_attributes["hobbies"][0] = "knitting"`)*

4. "What is the correct way to check if a key exists in a dictionary?"
   *(Answer: `key in dictionary`)*

5. "True or false: using `get()` to access a dictionary key only prevents errors if you specify a default value."
   *(Answer: **False** — `get()` returns `None` even without a default, avoiding the `KeyError` either way.)*

### Key Takeaways — Week 2

1. Tuples `()` are ordered and **immutable** — once created, they cannot change. A trailing comma is required for single-item tuples: `("item",)`.
2. **Unpacking** lets you assign tuple (or list) items to multiple variables in one line: `name, age, color = cat_info`.
3. Dictionaries `{}` store **key-value pairs** and are accessed by key, not position.
4. `dict["key"]` raises `KeyError` if the key is missing; `dict.get("key", default)` returns a fallback instead.
5. Adding and updating a dictionary entry use the same syntax — Python decides based on whether the key already exists.
6. `keys()`, `values()`, and `items()` give views you can convert with `list()` — `items()` returns key-value pairs as tuples.
7. Collections can be **nested** — a dictionary can hold lists, which can hold dictionaries, and so on. Work through nested access one `[]` at a time.

### Choosing Between Lists, Tuples, and Dictionaries — Quick Reference

| Collection | Ordered? | Mutable? | Duplicates? | Best for… |
|---|---|---|---|---|
| **List** | Yes | Yes | Yes | Collections that change — to-do lists, shopping lists |
| **Tuple** | Yes | No | Yes | Fixed data — coordinates, dates, dictionary keys |
| **Dictionary** | Yes (insertion order) | Yes | Keys must be unique | Lookups by name — phonebooks, profiles, settings |

> "If you're not sure which to use, the book's advice is simple: when in doubt, use a list."

### Preview of Chapter 5

> "Over these two sessions, we've built up the full toolkit of Python collections. Next time, we meet **loops** — `for` and `while`. Combined with everything we've learned about lists, tuples, and dictionaries, loops let your programs process every item automatically, without writing repetitive code. That's where things start to feel like 'real' programming."

### Recommended Practice Before Next Session

Complete book Exercise 4.3 (phone book) if not finished in class, and attempt as much of Exercise 4.4 (library database) as you can — it's a great way to practise combining all three collection types.

---

## Appendix A — Week 1 Quick Reference: Lists

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

COMMON ERRORS
──────────────────────────────────────────────
IndexError: list index out of range
   → accessed an index >= len(my_list)
   → fix: check with len() first

ValueError: list.remove(x): x not in list
   → tried to remove a value that isn't there
   → fix: check with "if x in my_list:" first
```

---

## Appendix B — Week 2 Quick Reference: Tuples & Dictionaries

```
TUPLES  ( )
──────────────────────────────────────────────
my_tuple = (10, 20, 30)            # create
my_tuple[0]                        # access → 10
a, b, c = my_tuple                 # unpack
single = ("x",)                    # single-item tuple (comma required!)

# Immutable — this raises TypeError:
# my_tuple[0] = 99

DICTIONARIES  { }
──────────────────────────────────────────────
d = {"name": "Zia", "age": 1}     # create
d["name"]                           # access → "Zia"
d.get("breed")                      # safe access → None
d.get("breed", "Unknown")          # safe with default → "Unknown"

d["hobby"] = "napping"             # add new key
d["age"] = 2                        # update existing key
del d["hobby"]                      # remove (KeyError if missing)
d.pop("hobby")                      # remove and return value
d.pop("hobby", None)               # safe remove

list(d.keys())                      # all keys
list(d.values())                    # all values
list(d.items())                     # all (key, value) pairs as tuples
"age" in d                          # check key → True

NESTED EXAMPLE
──────────────────────────────────────────────
data = {
    "hobbies": ["napping", "playing"],
    "friends": [{"name": "Wiesje"}, {"name": "Muchu"}]
}
data["hobbies"][1]                  # "playing"
data["friends"][0]["name"]          # "Wiesje"

CHOOSING THE RIGHT COLLECTION
──────────────────────────────────────────────
Need to change items?         → list
Data must stay fixed?         → tuple
Need to look up by name/key?  → dictionary
```

---

## Appendix C — Instructor Troubleshooting Guide (Both Weeks)

| Error | Likely Cause | Fix |
|---|---|---|
| `IndexError: list index out of range` | Accessed index ≥ length of list | Check with `len()` before accessing; max valid index is `len - 1` |
| `IndexError` with negative index | Index more negative than list length | e.g. `[-5]` on a 4-item list — verify with `len()` |
| `ValueError: list.remove(x): x not in list` | Tried to remove an item that doesn't exist | Check `if item in my_list:` first |
| `TypeError: 'tuple' object does not support item assignment` | Tried to change a tuple element | Use a list instead if values need to change |
| `("item")` not recognised as a tuple | Missing trailing comma | Change to `("item",)` |
| `KeyError: 'key'` | Accessed a dict key that doesn't exist | Use `get()` or check `if key in dict:` first |
| Dict value is `None` unexpectedly | Used `get()` without a default | Add a default: `dict.get("key", "default")` |
| `SyntaxError` inside dict literal | Missing colon `:` or comma `,` between pairs | Check every pair follows `"key": value,` pattern |
| Confusion: "Why didn't this list/dict change after slicing/`get()`?" | Slicing and `get()` return **new** values, they don't modify the original | Reassure participants — this is expected behaviour |

---

*Lesson prepared for use with Python Illustrated (Markowska), Chapter 4. Format: two 50-minute sessions, one week apart.*
