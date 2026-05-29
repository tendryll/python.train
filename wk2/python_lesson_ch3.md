# Python Fundamentals: Lesson 2
### Chapter 3 — *Python Illustrated*: Working with Conditional Statements
**Duration:** 50 minutes | **Audience:** Non-programmers | **IDE:** PyCharm

---

## Lesson Overview

| Segment | Topic | Time |
|---|---|---|
| Warm-Up | Recap of Chapter 2 & the "decision-making" hook | 5 min |
| Concept Block A | `if` and `else` — the fork in the road | 12 min |
| Concept Block B | `elif`, nested `if`, and logical operators | 12 min |
| Concept Block C | `match`, ternary operator, and common mistakes | 8 min |
| Hands-On Lab | Writing decision programs in PyCharm | 8 min |
| Wrap-Up | Quiz questions, key takeaways, preview of Chapter 4 | 5 min |

---

## Learning Objectives

By the end of this lesson, participants will be able to:

1. Write an `if` statement with a correct condition and indented code block.
2. Extend an `if` statement with `else` and one or more `elif` branches.
3. Combine conditions using the logical operators `and`, `or`, and `not`.
4. Read and write a basic `match` statement (Python 3.10+).
5. Recognise and fix the three most common conditional-statement errors.

---

## Materials Needed

- *Python Illustrated* (Chapter 3, pages 61–84)
- PyCharm open with a blank file `lesson2.py`
- Projector / screen share for live demos
- Optional: printed Quick Reference (see Appendix A)

---

## Instructor Preparation Notes

> Chapter 3 builds directly on the **booleans and comparison operators** introduced at the end of Chapter 2. Before this lesson, confirm participants can recall:
> - The difference between `=` (assignment) and `==` (comparison)
> - That `True` / `False` are the two boolean values
> - At least two comparison operators (`==`, `!=`, `<`, `>`, `>=`, `<=`)
>
> If the group is shaky on these, spend 2 extra minutes on the warm-up review. You can safely trim Segment 4 (match / ternary) to compensate — those topics are "read-only" for beginners.

---

## Segment 1 — Warm-Up: Recap & Hook (5 min)

### Quick Recap Questions (call-and-response)

Ask the room — accept quick verbal answers:

- "What do we call `True` and `False` in Python?" → *Booleans*
- "What does `!=` mean?" → *Not equal to*
- "What does `==` do?" → *Compares two values; returns True or False*

### The Hook: Code That Makes Decisions

> "Everything we've written so far runs top-to-bottom like a recipe with no choices. Today we add the power to say: *if this is true, do one thing — otherwise, do something different*. That's what makes programs actually useful."

Write this pseudocode on the board (non-Python, plain English):

```
IF it is raining:
    bring an umbrella
ELSE:
    wear sunglasses
```

> "Python's `if` statement is almost that readable. Let's see it for real."

---

## Segment 2 — Concept Block A: `if` and `else` (12 min)

### Part 1: The `if` Statement (6 min)

#### Syntax

```python
if condition:
    # Code to run if condition is True
```

Two critical rules to point out immediately:

1. **The condition** evaluates to `True` or `False` — that's it.
2. **The indented block** (4 spaces, or Tab in PyCharm) is the code that only runs when the condition is `True`. Python uses indentation to define the block — there are no curly braces like in other languages.

#### Live Demo — Dinner Time

Type this in the PyCharm console, or in `lesson2.py` and run it:

```python
hour = 18   # 6 PM

if hour == 18:
    print("Time for dinner!")
```

**Expected output:**
```
Time for dinner!
```

Change `hour = 18` to `hour = 15` and run again:

```
(nothing printed)
```

> "When the condition is `False`, the indented block is completely skipped. Python moves on to whatever comes next."

#### Live Demo — All comparison operators with `if`

Walk through each briefly, demoing one or two in the console:

```python
# Equal to
if 5 == 5:
    print("Equal!")

# Not equal to
if 7 != 3:
    print("Not equal!")

# Less than
if 2.2 < 2.5:
    print("Zia is lighter than Wiesje")

# Greater than or equal to
if 5 >= 5:
    print("Had enough sleep")

# Less than or equal to
if 1 <= 1:
    print("Room for more fish")
```

#### Concept Check

> "What happens if the condition is `False` and there is no `else`?"

*(Answer: nothing — the block is skipped, execution continues after the `if`.)*

---

### Part 2: The `else` Statement (6 min)

#### Why `else` Exists

Show the "two `if` statements" problem from the book:

```python
wiesje_age = 7
zia_age = 0.8

if wiesje_age > zia_age:
    print("Wiesje is older than Zia.")
if wiesje_age < zia_age:
    print("Zia is older than Wiesje.")
```

> "This works, but it checks *both* conditions every time, even after the first one is already `True`. It's like asking two separate questions when you only need one. There's a better way."

#### Syntax

```python
if condition:
    # Runs when condition is True
else:
    # Runs when condition is False
```

#### Live Demo — Hungry or Not?

```python
is_hungry = False

if is_hungry:
    print("Time to eat!")
else:
    print("Maybe later.")
```

**Output:** `Maybe later.`

> "Notice the condition for `if` here is just a boolean variable — `is_hungry`. Python evaluates it directly: if the value is `True`, run the `if` block; if `False`, run `else`."

Change `is_hungry = True` and run again to show the other path.

#### Key Point to Emphasise

> "`else` never has its own condition — it catches everything that `if` (and any `elif`s) didn't."

---

## Segment 3 — Concept Block B: `elif`, Nested `if`, and Logical Operators (12 min)

### Part 1: `elif` — More Than Two Choices (5 min)

#### Syntax

```python
if condition1:
    # runs if condition1 is True
elif condition2:
    # runs if condition1 is False AND condition2 is True
elif condition3:
    # runs if condition1 & condition2 are False AND condition3 is True
else:
    # runs if none of the above matched
```

> "`elif` stands for 'else if'. Python checks them in order from top to bottom and stops at the first `True` match — it never checks the rest."

#### Live Demo — Weather Activity

```python
weather = "rainy"

if weather == "sunny":
    print("Let's go sunbathing!")
elif weather == "rainy":
    print("Better stay inside and nap.")
else:
    print("Let's watch the birds from the window.")
```

**Output:** `Better stay inside and nap.`

Change `weather` to `"cloudy"` and show the `else` branch fires. Then change to `"sunny"` and explain that `elif` is never even evaluated when `if` already matched.

#### Concept Check

> "Can you have more than one `elif`?" *(Yes, as many as needed.)*
> "Can you have an `elif` without a final `else`?" *(Yes — `else` is always optional.)*

---

### Part 2: Nested `if` (2 min)

#### Brief Explanation

```python
is_awake = True
has_toy = False

if is_awake:
    if has_toy:
        print("Let's play with the toy!")
    else:
        print("Time to find a toy!")
else:
    print("Sleeping... Dreaming of the red dot.")
```

**Output:** `Time to find a toy!`

> "You *can* put an `if` inside another `if`. It's called nesting. But nesting deeply makes code hard to read. Usually there's a cleaner way — which brings us to logical operators."

---

### Part 3: Logical Operators — `and`, `or`, `not` (5 min)

These let you combine multiple boolean conditions into one, avoiding deep nesting.

#### `and` — Both must be True

```python
is_sunny = True
is_human_home = True

if is_sunny and is_human_home:
    print("Perfect moment for a long nap in the sun!")
```

> "With `and`, if *either* side is `False`, the whole condition is `False`."

**Truth table (draw on board):**

| Left | Right | `and` result |
|---|---|---|
| True | True | **True** |
| True | False | False |
| False | True | False |
| False | False | False |

#### `or` — At least one must be True

```python
is_bored = False
has_toy = True

if is_bored or has_toy:
    print("Time to play!")
```

**Output:** `Time to play!`

> "With `or`, if *either* side is `True`, the whole condition is `True`."

| Left | Right | `or` result |
|---|---|---|
| True | True | True |
| True | False | True |
| False | True | True |
| False | False | **False** |

#### `not` — Flip the value

```python
is_raining = False

if not is_raining:
    print("Let's go outside!")
```

**Output:** `Let's go outside!`

> "`not` inverts the boolean. `not False` becomes `True`; `not True` becomes `False`. Read it like plain English: 'if it is not raining…'"

#### Rewriting the Nested Example with `and`

Show participants how logical operators can flatten nested code:

```python
# Nested version (harder to read)
if is_awake:
    if has_toy:
        print("Let's play!")

# Flat version with 'and' (cleaner)
if is_awake and has_toy:
    print("Let's play!")
```

---

## Segment 4 — Concept Block C: `match`, Ternary Operator, and Common Mistakes (8 min)

### Part 1: The `match` Statement (3 min)

> "`match` is Python's alternative to long `if/elif/elif/elif` chains when you're checking one variable against many specific values. It requires Python 3.10 or later."

#### The Problem It Solves

```python
# Long if/elif chain — works, but repetitive
pet_type = "axolotl"

if pet_type == "cat":
    print("Meow!")
elif pet_type == "dog":
    print("Woof!")
elif pet_type == "parrot":
    print("Polly wants a cracker!")
else:
    print("I'm not sure what sound this pet makes!")
```

#### The `match` Version

```python
match pet_type:
    case "cat":
        print("Meow!")
    case "dog":
        print("Woof!")
    case "parrot":
        print("Polly wants a cracker!")
    case _:
        print("I'm not sure what sound this pet makes!")
```

> "The `case _:` is the default — just like `else`. It catches anything that didn't match the cases above. The pipe symbol `|` lets one case handle multiple values:"

```python
case "dog" | "puppy":
    print("Woof!")
```

---

### Part 2: The Ternary Operator (2 min)

> "A one-liner shortcut for very simple `if/else` logic. You'll see this in other people's code, so you need to be able to read it."

**Syntax:**
```python
value_if_true if condition else value_if_false
```

**Example:**
```python
hour = 14  # 2 PM
activity = "Nap time" if hour < 17 else "Play time"
print(activity)
```

**Output:** `Nap time`

> "Read it left to right: 'It is Nap time… if hour is less than 17… otherwise it is Play time.' You don't need to write code this way as a beginner — but do practise reading it."

---

### Part 3: Three Common Mistakes (3 min)

Demonstrate each one live by *deliberately making the error*, then fixing it.

**Mistake 1 — Using `=` instead of `==`**

```python
# WRONG — SyntaxError
if a = 5:
    print("a is 5")

# CORRECT
if a == 5:
    print("a is 5")
```

> "Remember: `=` stores a value. `==` asks a question."

**Mistake 2 — Wrong indentation**

```python
# WRONG — IndentationError
if a == 5:
print("a is 5")

# CORRECT
if a == 5:
    print("a is 5")
```

> "PyCharm will usually highlight this with a red squiggle. If you see `IndentationError`, look for a line that should be inside a block but isn't indented."

**Mistake 3 — Forgetting the colon**

```python
# WRONG — SyntaxError
if a == 5
    print("a is 5")

# CORRECT
if a == 5:
    print("a is 5")
```

> "Every `if`, `elif`, `else`, `match`, and `case` line must end with a colon. Think of it as Python's way of saying 'the block starts here'."

---

## Segment 5 — Hands-On Lab: Decision Programs in PyCharm (8 min)

### Instructor Notes

Open `lesson2.py` on screen. Type and run each exercise, then give participants 3–4 minutes to personalise or extend them. Move around the room; focus help on indentation and colon errors.

### Exercise A — Even or Odd (3 min)

Introduce the **modulo** trick: a number is even if `number % 2 == 0`.

```python
# Exercise A: Even or Odd
number = 17

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
```

Ask participants to change `number` to a few different values (even and odd) to verify it works.

**Ternary bonus** (for fast finishers):
```python
result = "even" if number % 2 == 0 else "odd"
print(number, "is", result)
```

### Exercise B — Grade Classifier (5 min)

This uses a full `if/elif/else` chain — the most important pattern in the chapter.

```python
# Exercise B: Grade Classifier
score = 85

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is:", grade)
```

Ask participants to:
1. Run it with `score = 85` → should print `B`
2. Change to `score = 92` → should print `A`
3. Change to `score = 55` → should print `F`

**Discussion prompt:**
> "Why do we check `>= 90` first, rather than last? What would go wrong if we checked `>= 60` first?"

*(Answer: `score = 85` would match the `>= 60` case immediately and print `D`, which is wrong. Order matters — check the most restrictive condition first.)*

---

## Segment 6 — Wrap-Up: Quiz, Takeaways, and Preview (5 min)

### Quick Quiz (verbal, call on volunteers)

Use selected questions from the book's Chapter 3 quiz:

1. "What is the correct syntax for an `if` statement?"
   - *(Answer: `if x == 42:` — needs `==`, no parentheses required, ends with colon)*

2. "True or false: an `else` block is mandatory in an `if` statement."
   - *(Answer: False — `else` is optional)*

3. "What does `not False` evaluate to?"
   - *(Answer: `True`)*

4. "Given `temperature = 25`, what is `outfit = "T-shirt" if temperature > 20 else "Sweater"`?"
   - *(Answer: `"T-shirt"`)*

5. "Will this code produce output? `x = 10` / `if not x != 10:` / `print("Confusing!")`"
   - *(Answer: Yes — `x != 10` is `False`, `not False` is `True`, so the block runs)*

### Key Takeaways (read aloud)

1. `if condition:` runs a block only when the condition is `True`.
2. `else:` catches everything that `if` (and any `elif`s) did not.
3. `elif` checks additional conditions in sequence — Python stops at the first match.
4. `and`, `or`, `not` combine booleans and can replace deeply nested `if` statements.
5. `match` is a cleaner alternative to long `if/elif` chains (Python 3.10+).
6. The ternary operator (`value_if_true if condition else value_if_false`) is one-line `if/else`.
7. The three most common errors: `=` vs `==`, missing indentation, missing colon.

### Preview of Chapter 4

> "Next lesson we move to **collections** — lists, tuples, and dictionaries. These let you store many values in one variable, and when you combine them with `if` statements, your programs can do genuinely useful things."

### Recommended Practice Before Next Session

Complete Chapter 3 exercises 3.1 through 3.4 from the book. They cover even/odd detection, dachshund weight classification, a password checker, and the grading system — all great `if/elif/else` practice.

---

## Appendix A — Quick Reference Cheat Sheet

*(Print and distribute, or display on screen during the lab)*

```
THE if STATEMENT
────────────────────────────────
if condition:
    # runs if True

if / else:
    if condition:
        # True path
    else:
        # False path (no condition)

if / elif / else:
    if condition1:
        # True path 1
    elif condition2:
        # True path 2
    else:
        # None matched

COMPARISON OPERATORS
────────────────────────────────
==   equal to
!=   not equal to
<    less than
>    greater than
<=   less than or equal to
>=   greater than or equal to

LOGICAL OPERATORS
────────────────────────────────
and   both must be True
or    at least one must be True
not   inverts the boolean

MATCH STATEMENT (Python 3.10+)
────────────────────────────────
match variable:
    case value1:
        # matched value1
    case value2 | value3:
        # matched either
    case _:
        # default (like else)

TERNARY OPERATOR
────────────────────────────────
x = "yes" if condition else "no"

THE THREE COMMON ERRORS
────────────────────────────────
= vs ==         →  use == inside if
No indent       →  IndentationError
No colon        →  SyntaxError
```

---

## Appendix B — Instructor Troubleshooting Guide

| Error | Likely Cause | Fix |
|---|---|---|
| `SyntaxError: invalid syntax` on `if` line | Used `=` instead of `==`, or missing colon | Check the `if` line carefully |
| `IndentationError: expected an indented block` | Nothing indented after `if:` | Add 4 spaces before the code inside the block |
| `IndentationError: unexpected indent` | Extra indentation where it shouldn't be | Remove extra leading spaces |
| `SyntaxError` on `if a = 5:` | Assignment inside `if` | Change to `if a == 5:` |
| `else` branch always runs even when condition is True | `else` accidentally indented into the `if` block | Align `else:` with its `if:` |
| `match` causes `SyntaxError` | Python version below 3.10 | Check version: `import sys; print(sys.version)` — upgrade or use `if/elif` instead |
| Code after `if` block always runs | Forgot that code outside the block is not conditional | Indent it if it should be inside the block |

---

*Lesson prepared for use with Python Illustrated (Markowska), Chapter 3. Duration: 50 minutes.*
