# Python Fundamentals: Lesson 1
### Chapters 1 & 2 — *Python Illustrated*
**Duration:** 50 minutes | **Audience:** Non-programmers | **IDE:** PyCharm

---

## Lesson Overview

| Segment | Topic | Time |
|---|---|---|
| Warm-Up | What is programming? Why Python? | 5 min |
| Concept Block A | How Python works — the interpreter & REPL | 10 min |
| Concept Block B | Variables and assignment | 10 min |
| Concept Block C | Core data types | 10 min |
| Hands-On Lab | First Python program in PyCharm | 10 min |
| Wrap-Up | Q&A, key takeaways, preview of next lesson | 5 min |

---

## Learning Objectives

By the end of this lesson, participants will be able to:

1. Explain in plain terms what Python is and why it is widely used.
2. Identify the difference between source code, the interpreter, and program output.
3. Use the PyCharm interactive console (REPL) to evaluate simple expressions.
4. Create and name variables that store text, whole numbers, and decimal numbers.
5. Write and run a short Python script that uses `print()` and variables.

---

## Materials Needed

- *Python Illustrated* (Chapters 1–2)
- PyCharm Community Edition installed and open on each participant's machine
- Projector / screen share for live demonstrations
- Optional: printed "cheat sheet" (see Appendix A)

---

## Segment 1 — Warm-Up: What Is Programming? Why Python? (5 min)

### Instructor Notes

Open with an analogy participants can immediately grasp. Avoid technical jargon in this segment — the goal is emotional buy-in, not precision.

### Talking Points

**Programming is giving instructions to a very literal-minded helper.**

> "Imagine hiring an assistant who does *exactly* what you say — nothing more, nothing less. If you say 'make coffee,' they stand there confused unless you explain every step. Programming is writing those exact steps."

**Why Python specifically?**

- Reads almost like plain English — easier to learn than most languages.
- Used everywhere: web apps, data science, automation, AI, film visual effects.
- Huge community — if you get stuck, millions of people have been stuck before you.
- Free and runs on Windows, Mac, and Linux.

**Ask the room (quick show of hands):**
- Who has tried to record a macro in Excel or Word?
- Who has used a formula in a spreadsheet?

> "Congratulations — you've already been programming. Python is just a more powerful version of that."

---

## Segment 2 — Concept Block A: How Python Works (10 min)

### Key Concept: Source Code → Interpreter → Output

Draw or display this flow on the board:

```
  You write code          Python reads it         Result appears
  (plain text file)  →→   (the interpreter)  →→   (on screen / in file)
  hello.py                python hello.py          Hello, world!
```

### The Python Interpreter

- Python is an **interpreted** language — it reads and runs your code line by line.
- You don't need to "compile" or "build" anything before running.
- Think of the interpreter as a live translator: you speak, it immediately translates and acts.

### The REPL — Your Scratchpad

REPL stands for **Read → Evaluate → Print → Loop**.

> "It's a direct line to Python. You type something, Python tells you the answer instantly. No saving files, no running programs — perfect for experimenting."

### Live Demo: Opening the PyCharm Console

**Walk participants through this step-by-step:**

1. Open PyCharm.
2. At the bottom of the screen, click the **Python Console** tab.
3. You should see `>>>` — the Python prompt. This means Python is ready.

**Type these expressions one at a time, letting participants follow along:**

```python
>>> 2 + 2
4
>>> 10 - 3
7
>>> 5 * 6
30
>>> 10 / 4
2.5
>>> "Hello"
'Hello'
```

**Key observation to call out:**
> "Notice Python responds immediately. The `>>>` is Python asking: 'What's next?' Every time you see it, Python is waiting for your instruction."

### Concept Check Question (ask the room)
> "If I type `100 / 0` in the console, what do you think happens?"

*(Type it in — let them see the error message. Reassure them: errors are normal, they don't break anything.)*

---

## Segment 3 — Concept Block B: Variables and Assignment (10 min)

### Key Concept: Variables Are Labeled Boxes

Use the book's visual approach — a variable is a **box with a label** that holds a value.

```
  name = "Alice"

  ┌─────────┐
  │  "Alice" │  ← the value stored inside
  └─────────┘
      ↑
    name       ← the label (variable name)
```

> "Any time you need to remember something — a name, a number, an answer — you put it in a labeled box called a variable."

### The Assignment Operator `=`

**Important clarification** (very common misconception):

> "In Python, `=` does NOT mean 'equals' the way it does in math. It means 'store this value in this box.' We say it as: 'name *gets* Alice' or 'name *is assigned* Alice.'"

### Live Demo: Variables in the Console

```python
>>> name = "Alice"
>>> age = 28
>>> city = "Memphis"
```

*(Point out: Python doesn't print anything — it silently stores the values.)*

```python
>>> name
'Alice'
>>> age
28
>>> city
'Memphis'
```

*(Now type the variable name alone — Python shows what's inside the box.)*

**Reassigning a variable:**

```python
>>> age = 29
>>> age
29
```

> "The box only holds one value at a time. When you assign a new value, the old one is replaced."

### Naming Rules (keep it simple)

- Use lowercase letters and underscores: `first_name`, `score`, `total_price`
- No spaces: `first name` is wrong, `first_name` is right
- Can't start with a number: `1thing` is wrong, `thing1` is fine
- Avoid Python's reserved words: `for`, `if`, `while`, `print` (more on these later)

### Concept Check Question

> "If I write `score = 100` and then `score = 50`, what does `score` equal now?"

---

## Segment 4 — Concept Block C: Core Data Types (10 min)

### The Three Types We'll Use Today

Python automatically figures out what *kind* of data you're storing. These are called **data types**.

| Type | Name | Example | How you recognize it |
|---|---|---|---|
| `str` | String | `"Hello"` | Always in quotes |
| `int` | Integer | `42` | Whole number, no quotes |
| `float` | Float | `3.14` | Decimal number, no quotes |

### Strings — Text in Quotes

```python
>>> greeting = "Good morning"
>>> greeting
'Good morning'
```

- Use double `"` or single `'` quotes — Python accepts both, just be consistent.
- Strings can contain letters, numbers, spaces, symbols.
- `"42"` is a **string** (text). `42` is an **integer** (number). They are different!

**Concatenation — joining strings:**

```python
>>> first = "Python"
>>> second = " Illustrated"
>>> first + second
'Python Illustrated'
```

> "The `+` sign with strings means *glue these together*, not add."

### Integers and Floats — Numbers

```python
>>> apples = 5
>>> price = 1.25
>>> total = apples * price
>>> total
6.25
```

**Common arithmetic operators:**

| Symbol | Operation | Example | Result |
|---|---|---|---|
| `+` | Add | `3 + 4` | `7` |
| `-` | Subtract | `10 - 3` | `7` |
| `*` | Multiply | `3 * 4` | `12` |
| `/` | Divide | `10 / 4` | `2.5` |
| `**` | Power | `2 ** 3` | `8` |

### Checking the Type

```python
>>> type("Hello")
<class 'str'>
>>> type(42)
<class 'int'>
>>> type(3.14)
<class 'float'>
```

> "`type()` is like asking Python: 'What kind of thing is this?' It's a useful debugging tool."

### Common Beginner Trap

```python
>>> "5" + 5
```

*(Run this — it will error. Explain:)*

> "You can't add text and a number. It's like asking someone to combine the word 'five' with the number 5. Python refuses because it's ambiguous. You'd need to convert one of them first — we'll cover that in the next lesson."

---

## Segment 5 — Hands-On Lab: First Python Script in PyCharm (10 min)

### Instructor Notes

This is the most important segment — participants write and run their first real script. Move around the room and help anyone who falls behind. Emphasize: **errors are normal. Read the message and try again.**

### Step-by-Step: Create and Run a Script

**Step 1 — Create a new file in PyCharm:**
- File → New → Python File
- Name it `lesson1.py`
- Click OK

**Step 2 — Type this code exactly:**

```python
# My first Python program

name = "Alice"
age = 28
city = "Memphis"

print("Name:", name)
print("Age:", age)
print("City:", city)
```

**Step 3 — Run the script:**
- Right-click anywhere in the file
- Choose **Run 'lesson1'**
- OR press `Ctrl+Shift+F10` (Windows/Linux) / `Ctrl+Shift+R` (Mac)

**Expected output (bottom panel):**
```
Name: Alice
Age: 28
City: Memphis
```

### Explain What Just Happened

> "The `#` at the start of a line is a **comment** — Python ignores it completely. It's a note to yourself (or future you, or a teammate). Always comment your code."

> "`print()` is a **function** — a command that tells Python to display something. Whatever you put inside the parentheses appears on screen."

### Personalization Exercise (if time allows)

Ask participants to modify the script to use their own name, age, and city, and run it again. This small win makes the concepts click.

### Stretch Challenge (for fast finishers)

```python
# Stretch challenge
item = "coffee"
quantity = 3
price = 4.50
total = quantity * price

print("Order:", quantity, item)
print("Total: $", total)
```

---

## Segment 6 — Wrap-Up: Q&A and Key Takeaways (5 min)

### Key Takeaways (read these aloud or display them)

1. **Python is an interpreted language** — it runs your code line by line, no compilation needed.
2. **The REPL is your sandbox** — use the PyCharm console to experiment instantly.
3. **Variables are labeled boxes** — `=` stores a value, not a math equation.
4. **Three starter data types:** `str` (text), `int` (whole number), `float` (decimal).
5. **`print()` shows output** — your main tool for seeing what's happening in your program.
6. **Comments start with `#`** — use them to explain your code.

### Preview of Next Lesson

> "Next time we'll learn how to ask the user for input, how to convert between data types, and we'll start using `if` statements to make decisions. The programs get interesting fast."

### Recommended Practice Before Next Session

From *Python Illustrated*, complete the exercises at the end of Chapters 1 and 2. Spend 15–20 minutes in the PyCharm console experimenting freely — try calculations, create variables, play with strings.

---

## Appendix A — Quick Reference Cheat Sheet

*(Print and distribute to participants, or display on screen)*

```
VARIABLES
---------
name = "Alice"       # store text
age = 28             # store a whole number
score = 9.5          # store a decimal

PRINT
-----
print("Hello")       # prints:  Hello
print(name)          # prints:  Alice
print("Age:", age)   # prints:  Age: 28

DATA TYPES
----------
type("hi")    →  <class 'str'>
type(5)       →  <class 'int'>
type(3.14)    →  <class 'float'>

ARITHMETIC
----------
5 + 3  →  8
10 - 4 →  6
3 * 4  →  12
10 / 3 →  3.333...
2 ** 4 →  16

STRING TRICKS
-------------
"Hello" + " World"  →  'Hello World'
len("Python")       →  6

COMMENTS
--------
# This line is ignored by Python
```

---

## Appendix B — Instructor Troubleshooting Guide

| Problem | Likely Cause | Fix |
|---|---|---|
| `SyntaxError` | Mismatched quotes or missing parenthesis | Check the line highlighted in red; look for opening/closing pairs |
| `NameError: name 'x' is not defined` | Variable used before being assigned | Make sure the variable assignment line runs first |
| `TypeError: can only concatenate str (not "int") to str` | Mixing string and number with `+` | Use `str()` to convert the number, or use a comma in `print()` |
| Script doesn't run at all | File not saved | Press `Ctrl+S` and try again |
| Console shows old output | Ran previous version | Check the file is saved; re-run |
| PyCharm shows red underline | Possible syntax error | Hover over it for a hint; often a typo |

---

*Lesson prepared for use with Python Illustrated (Markowska). Duration: 50 minutes.*
