"""
Python Illustrated – Chapter 5: Iterating with Loops
=====================================================
Examples demonstrating every concept from the chapter.
Run this file top-to-bottom, or jump to any section with Ctrl+F.

Sections
--------
1.  The problem with repetitive code
2.  The while loop – basics
3.  Avoiding infinite loops
4.  while loops – practical examples
5.  The for loop – basics
6.  range() with for loops
7.  Looping over collections (list, tuple, dictionary)
8.  Nested loops
9.  Loop control – break
10. Loop control – continue
11. for-else (and while-else)
12. Common mistakes
13. Chapter exercises (5.1 – 5.6)
"""

# ─────────────────────────────────────────────────────────────────────────────
# 1. THE PROBLEM WITH REPETITIVE CODE
# ─────────────────────────────────────────────────────────────────────────────
print("=" * 58)
print("1. THE PROBLEM WITH REPETITIVE CODE")
print("=" * 58)

# Without a loop – tedious and hard to maintain
print("Without a loop:")
print("I love Python!")
print("I love Python!")
print("I love Python!")
print("I love Python!")
print("I love Python!")

# Any change (e.g. wording) must be made in every single line.
# If we needed 10 000 repetitions, this approach simply won't work.


# ─────────────────────────────────────────────────────────────────────────────
# 2. THE WHILE LOOP – BASICS
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("2. THE WHILE LOOP – BASICS")
print("=" * 58)

# Syntax:  while condition:
#              # block runs as long as condition is True

# Print a message 5 times with a while loop
count = 0
while count < 5:
    print("I love Python!")
    count += 1          # MUST update count, or we loop forever

# What happens at each iteration:
#  Iter 1: count=0, 0<5 True  → print, count→1
#  Iter 2: count=1, 1<5 True  → print, count→2
#  Iter 3: count=2, 2<5 True  → print, count→3
#  Iter 4: count=3, 3<5 True  → print, count→4
#  Iter 5: count=4, 4<5 True  → print, count→5
#  Exit  : count=5, 5<5 False → loop stops

# Counting up to 3 and printing the value
i = 1
while i <= 3:
    print("Count:", i)
    i += 1


# ─────────────────────────────────────────────────────────────────────────────
# 3. AVOIDING INFINITE LOOPS
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("3. AVOIDING INFINITE LOOPS")
print("=" * 58)

# ❌ This would loop forever – count never changes so count < 5 stays True
# count = 0
# while count < 5:
#     print("This prints forever!")  ← DO NOT run this

# ✅ Always make sure the condition can eventually become False
count = 0
while count < 5:
    print("Safe loop, iteration:", count)
    # count += 1   # ← this is what prevents an infinite loop

print("Loop finished safely.")

# Another common pattern: a boolean flag that you flip
running = True
iterations = 0
while running:
    iterations += 1
    if iterations == 3:
        running = False   # flip the flag to exit
print(f"Exited after {iterations} iterations.")


# ─────────────────────────────────────────────────────────────────────────────
# 4. WHILE LOOPS – PRACTICAL EXAMPLES
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("4. WHILE LOOPS – PRACTICAL EXAMPLES")
print("=" * 58)

# ── Countdown ────────────────────────────────────────────────────
number = 5
while number > 0:
    print("Countdown:", number)
    number -= 1
print("Blast off! 🚀")

# ── Guess the secret word (simulated without real input) ──────────
# In a real program: attempt = input("Guess the word: ")
# Here we simulate the user's guesses with a list
secret_word = "python123"
guesses = ["hello", "cats", "python123"]   # simulated user input

attempt_index = 0
while True:
    attempt = guesses[attempt_index]
    print(f"Guess: '{attempt}'")
    attempt_index += 1
    if attempt == secret_word:
        break
print("You've guessed it!")

# ── Sum numbers until total exceeds a threshold ────────────────────
total = 0
value = 1
while total < 20:
    total += value
    print(f"  Added {value}, total is now {total}")
    value += 1
print("Total exceeded 20 – stopped at:", total)


# ─────────────────────────────────────────────────────────────────────────────
# 5. THE FOR LOOP – BASICS
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("5. THE FOR LOOP – BASICS")
print("=" * 58)

# Syntax:  for variable in sequence:
#              # block runs once per item

# Iterating over a list
basket_toys = ["feather", "ball", "laser pointer"]
for toy in basket_toys:
    print("Checking:", toy)

# The loop variable name is your choice – be descriptive
countries = ["Netherlands", "Germany", "Japan"]
for country in countries:
    print("Visited:", country)

# for loop with a list of numbers
for score in [85, 92, 78, 95]:
    print("Score:", score)


# ─────────────────────────────────────────────────────────────────────────────
# 6. range() WITH FOR LOOPS
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("6. range() WITH FOR LOOPS")
print("=" * 58)

# range(stop) – starts at 0, exclusive stop
print("range(5):")
for i in range(5):
    print(i, end=" ")   # 0 1 2 3 4
print()

# range(start, stop) – custom start, exclusive stop
print("range(1, 6):")
for i in range(1, 6):
    print(i, end=" ")   # 1 2 3 4 5
print()

# range(start, stop, step) – custom step
print("range(2, 10, 2) – even numbers:")
for i in range(2, 10, 2):
    print(i, end=" ")   # 2 4 6 8
print()

# Negative step – countdown
print("range(5, 0, -1) – countdown:")
for number in range(5, 0, -1):
    print("Countdown:", number)
print("Blast off! 🚀")

# Using range when the index value itself is not needed
print("Repeat 3 times:")
for _ in range(3):      # _ is convention for "I don't need this variable"
    print("  Hello!")

# Off-by-one reminder: range(0, 4, 2) → [0, 2], NOT [0, 2, 4]
print("range(0, 4, 2) produces:", list(range(0, 4, 2)))


# ─────────────────────────────────────────────────────────────────────────────
# 7. LOOPING OVER COLLECTIONS
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("7. LOOPING OVER COLLECTIONS")
print("=" * 58)

# ── List ──────────────────────────────────────────────────────────
cat_toys = ["feather", "ball", "laser pointer", "scratching post"]
print("Listing all toys:")
for toy in cat_toys:
    print("-", toy)

# ── Tuple (same syntax as list) ───────────────────────────────────
coordinates = (10, 20, 30)
print("Coordinates:")
for coordinate in coordinates:
    print(coordinate)

# ── Dictionary – keys (default) ───────────────────────────────────
cat_attributes = {"name": "Zia", "age": 1, "color": "grey", "food": "tuna"}

print("Keys only:")
for key in cat_attributes:
    print("-", key)

# ── Dictionary – keys + values via [] ────────────────────────────
print("Keys and values (via key):")
for key in cat_attributes:
    print(f"  {key}: {cat_attributes[key]}")

# ── Dictionary – values only ──────────────────────────────────────
print("Values only:")
for value in cat_attributes.values():
    print("-", value)

# ── Dictionary – key-value pairs with items() ─────────────────────
print("Key-value pairs (items):")
for key, value in cat_attributes.items():
    print(f"  {key}: {value}")    # f-string: variables inside {}


# ─────────────────────────────────────────────────────────────────────────────
# 8. NESTED LOOPS
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("8. NESTED LOOPS")
print("=" * 58)

# Multiplication table 1–3
print("Multiplication table (1-3):")
for i in range(1, 4):          # outer loop: i = 1, 2, 3
    for j in range(1, 4):      # inner loop: j = 1, 2, 3 (for every i)
        print(f"  {i} x {j} = {i * j}")
    print("  ---")

# Iterating over a list of lists
list_of_lists = [
    ["Wiesje", "Pino", "Hedgehog"],
    ["Zia", "Python", "Writing"],
    ["Muchu", "Napping"],
]
print("List of lists:")
for inner_list in list_of_lists:
    for item in inner_list:
        print(" ", item)

# Nested loop: find all pairs from two lists
colors = ["red", "blue"]
sizes  = ["S", "M", "L"]
print("All color-size combinations:")
for color in colors:
    for size in sizes:
        print(f"  {color}-{size}")


# ─────────────────────────────────────────────────────────────────────────────
# 9. LOOP CONTROL – break
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("9. LOOP CONTROL – break")
print("=" * 58)

# break exits the loop immediately
for number in range(1, 10):
    if number == 5:
        print("Number 5 found! Exiting loop.")
        break
    print("Current number:", number)
print("The loop has ended.")

# break inside a while loop (intentional "infinite" loop pattern)
# Simulated: keep asking until the user says "yes"
# In a real program: answer = input("Stop? ")
answers = ["no", "no", "yes"]   # simulated responses
idx = 0
while True:
    answer = answers[idx]
    idx += 1
    print(f"  User said: '{answer}'")
    if answer == "yes":
        break
print("Stopped.")

# Searching a list – break once found
fruits = ["apple", "banana", "cherry", "date"]
target = "cherry"
for fruit in fruits:
    if fruit == target:
        print(f"Found {target}!")
        break
else:
    # This else belongs to the for loop – runs only if break was NOT hit
    print(f"{target} not in list.")


# ─────────────────────────────────────────────────────────────────────────────
# 10. LOOP CONTROL – continue
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("10. LOOP CONTROL – continue")
print("=" * 58)

# continue skips the rest of THIS iteration and moves to the next
for number in range(1, 6):
    if number == 3:
        print("Skipping number 3...")
        continue              # jumps back to the top of the loop
    print("Current number:", number)

# Print only even numbers using continue
print("Even numbers 1–10:")
for n in range(1, 11):
    if n % 2 != 0:
        continue
    print(n, end=" ")
print()

# Skip empty strings in a list
words = ["hello", "", "world", "", "Python"]
print("Non-empty words:")
for word in words:
    if word == "":
        continue
    print(" ", word)


# ─────────────────────────────────────────────────────────────────────────────
# 11. for-else  (and while-else)
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("11. for-else (and while-else)")
print("=" * 58)

# The else block runs when the loop finishes ALL iterations normally
# (i.e. it was NOT exited early with break)

# Example: searching for a feather toy
toys = ["ball", "mouse", "string"]
for toy in toys:
    print("Checking:", toy)
    if toy == "feather":
        print("Found my feather! Time to play!")
        break
else:
    print("No feather found. I guess I'll nap instead.")  # ← runs

# Now with feather present – else is SKIPPED
toys_with_feather = ["ball", "feather", "string"]
for toy in toys_with_feather:
    print("Checking:", toy)
    if toy == "feather":
        print("Found my feather!")
        break
else:
    print("This won't print because break was hit.")

# while-else works the same way
count = 0
while count < 3:
    print("  while iteration:", count)
    count += 1
else:
    print("  while loop ended normally.")   # ← runs (no break)


# ─────────────────────────────────────────────────────────────────────────────
# 12. COMMON MISTAKES
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("12. COMMON MISTAKES")
print("=" * 58)

# ── Mistake 1: missing increment → infinite loop ─────────────────
# ❌ WRONG (loops forever – do NOT uncomment):
# i = 0
# while i < 5:
#     print(i)        ← i never changes, so i < 5 is always True

# ✅ RIGHT: update the variable inside the loop
i = 0
while i < 5:
    print("Safe:", i)
    i += 1

# ── Mistake 2: modifying a list while looping over it ─────────────
numbers = [1, 2, 2, 3, 4, 4, 5]

# ❌ WRONG – skips elements because the list shrinks under the loop
wrong_result = numbers.copy()
for num in wrong_result[:]:
    pass  # just demonstrating – don't mutate the real list here

# Demonstrate the issue:
bad = [1, 2, 2, 3]
for num in bad:
    if num == 2:
        bad.remove(num)
print("Bad removal (one 2 remains):", bad)   # [1, 2, 3] – misses second 2

# ✅ RIGHT – loop over a copy of the list with [:]
numbers_copy = [1, 2, 2, 3, 4, 4, 5]
for num in numbers_copy[:]:       # [:] makes a full copy
    if num == 2:
        numbers_copy.remove(num)
print("Correct removal:", numbers_copy)   # [1, 3, 4, 4, 5]  ← wait, still one 4?
# Actually remove() removes first occurrence each time;
# using [:] just prevents index-skipping for the ITERATOR.
# For truly deduplicating, build a new list instead:
cleaned = [n for n in [1, 2, 2, 3, 4, 4, 5] if n != 2]
print("Built new list:", cleaned)   # [1, 3, 4, 4, 5]

# ── Mistake 3: off-by-one errors with range() ─────────────────────
# range() stop is EXCLUSIVE – 4 is NOT printed here:
print("range(0, 4, 2) →", list(range(0, 4, 2)))   # [0, 2], not [0, 2, 4]

# To include 4, use range(0, 5, 2) or range(0, 6, 2)
print("range(0, 5, 2) →", list(range(0, 5, 2)))   # [0, 2, 4]


# ─────────────────────────────────────────────────────────────────────────────
# 13. CHAPTER EXERCISES
# ─────────────────────────────────────────────────────────────────────────────
print("\n" + "=" * 58)
print("13. CHAPTER EXERCISES")
print("=" * 58)

# ── Exercise 5.1 – Summing Numbers ───────────────────────────────
print("\n-- Exercise 5.1: Summing Numbers --")

total = 0
for n in range(1, 11):   # 1 through 10 inclusive
    total += n
print("Sum of 1 to 10:", total)   # 55


# ── Exercise 5.2 – Greeting a List of Friends ─────────────────────
print("\n-- Exercise 5.2: Greeting a List of Friends --")

names = ["Zia", "Wiesje", "Muchu"]
for name in names:
    print(f"Hello, {name}! Great to see you!")


# ── Exercise 5.3 – Infinite Squirrel Chasing ─────────────────────
print("\n-- Exercise 5.3: Squirrel Chasing --")

# Basic: loop until Wiesje runs out of energy
wiesje_energy = 5
while wiesje_energy > 0:
    print(f"Wiesje chases the squirrel! (energy: {wiesje_energy})")
    wiesje_energy -= 1
print("Wiesje is too tired and gives up.")

# Bonus: squirrel also has energy – whoever runs out first loses
print()
wiesje_energy  = 6
squirrel_energy = 4

while wiesje_energy > 0 and squirrel_energy > 0:
    print(f"Chase! Wiesje: {wiesje_energy}, Squirrel: {squirrel_energy}")
    wiesje_energy  -= 1
    squirrel_energy -= 1

if wiesje_energy <= 0 and squirrel_energy <= 0:
    print("It's a tie – both collapse at the same time!")
elif squirrel_energy <= 0:
    print("Wiesje caught the squirrel! 🐿️")
else:
    print("Wiesje is too tired and gives up.")


# ── Exercise 5.4 – Team Up for Game Night ─────────────────────────
print("\n-- Exercise 5.4: Team Up for Game Night --")

friends = ["Max", "Louise", "Jacob", "Sam", "Farah", "Selim"]
team_a = []
team_b = []

for i in range(len(friends)):
    if i % 2 == 0:        # even index → Team A
        team_a.append(friends[i])
    else:                 # odd index  → Team B
        team_b.append(friends[i])

print("Team A:")
for member in team_a:
    print(" ", member)

print("Team B:")
for member in team_b:
    print(" ", member)


# ── Exercise 5.5 – Factorial Calculation ──────────────────────────
print("\n-- Exercise 5.5: Factorial Calculation --")

number = 5
factorial = 1

if number < 0:
    print("Factorials are only defined for non-negative integers.")
else:
    for n in range(1, number + 1):   # 1 up to and including number
        factorial *= n
    print(f"{number}! = {factorial}")   # 5! = 120

# Test with 0 (0! = 1 – range(1, 1) is empty, so factorial stays 1)
number = 0
factorial = 1
for n in range(1, number + 1):
    factorial *= n
print(f"{number}! = {factorial}")   # 0! = 1

# Test with a negative number
number = -3
if number < 0:
    print("Factorials are only defined for non-negative integers.")


# ── Exercise 5.6 – Secret Pet Gym ────────────────────────────────
print("\n-- Exercise 5.6: Secret Pet Gym --")

workouts = {
    "Zia": {
        "bench_press":       {"weight": 5,  "sets": 3, "reps": 10},
        "bicep_curls":       {"weight": 2,  "sets": 3, "reps": 10},
        "box_jumps":         {"weight": 0,  "sets": 2, "reps": 10},
        "deadlifts":         {"weight": 10, "sets": 2, "reps": 1},
        "kettle_bell_swings":{"weight": 2,  "sets": 3, "reps": 10},
        "lateral_raises":    {"weight": 1,  "sets": 3, "reps": 10},
        "stair_climber":     {"minutes": 10},
    },
    "Wiesje": {
        "bench_press":  {"weight": 5, "sets": 1, "reps": 1},
        "leg_extension":{"weight": 1, "sets": 2, "reps": 5},
        "planking":     {"minutes": 5},
        "zoomies":      {"minutes": 2},
    },
}

for member, exercises in workouts.items():
    print(f"\n{member}'s workout:")
    total_weight = 0
    for exercise, details in exercises.items():
        if "minutes" in details:
            # Cardio / timed exercise – no weight lifted
            print(f"  - {exercise}: {details['minutes']} minutes")
        else:
            w, s, r = details["weight"], details["sets"], details["reps"]
            print(f"  - {exercise}: weight {w}kg, {s} sets of {r} reps")
            total_weight += w * s * r   # weight × sets × reps
    print(f"Total weight lifted by {member}: {total_weight}kg")