# Data Structures and Algorithms — A Beginner's Guide

A plain-English introduction to how computers organize and process information, with diagrams and real-world analogies.

---

## What Are Data Structures?

**Data structures** are ways of organizing information so a computer can store and use it efficiently. Choosing the right one matters a lot — the same task can take milliseconds or many seconds depending on which structure you use.

---

## Array — Like a Row of Numbered Boxes

Each item has an **index** (a position number). Fast to find by position.

```
 ┌──────┬──────┬──────┬──────┬──────┐
 │  🍎  │  🍌 │  🍇 │  🍓  │  🍑  │
 └──────┴──────┴──────┴──────┴──────┘
   [0]    [1]    [2]    [3]    [4]
```

> "Give me item [2]" → instantly returns 🍇

**Best for:** Fast access by position (index). Things like lists of scores, pixels in an image.

---

## Linked List — Like a Treasure Hunt Chain

Each item holds a **value AND a pointer** to the next item. No index — you must walk from the start.

```
┌─────────┐     ┌─────────┐     ┌─────────┐     ┌──────────┐
│  Cat  → │───▶ │  Dog  → │───▶│  Bird → │───▶│  null    │
└─────────┘     └─────────┘     └─────────┘     └──────────┘
```

**Best for:** Inserting or deleting items in the middle frequently (e.g. a music playlist you rearrange often).

---

## Stack — Like a Stack of Plates

**Last In, First Out (LIFO).** You can only add or remove from the **top**.

```
          ┌──────────────────┐
          │  Top plate  ← PUSH / POP here
          ├──────────────────┤
          │  Middle plate    │
          ├──────────────────┤
          │  Bottom plate    │
          └──────────────────┘
```

- **push** = add to the top
- **pop** = remove from the top

**Best for:** Undo operations, browser back button history, depth-first search.

---

## Queue — Like a Line at a Shop

**First In, First Out (FIFO).** Join at the back, leave from the front.

```
dequeue ◀──  [ Alice ][ Bob ][ Carol ]  ──▶ enqueue
(front)                                      (back)
```

**Best for:** Task scheduling, print queues, chat message delivery — anything "first come, first served."

---

## Tree — Like a Family Tree or Org Chart

**Hierarchical.** Each node has a parent and can have children. The top node is called the **root**, the bottom nodes are **leaves**.

```
                    ┌─────────┐
                    │   CEO   │  ← root
                    └────┬────┘
           ┌─────────────┴─────────────┐
      ┌────┴────┐                 ┌────┴────┐
      │ VP Eng  │                 │ VP Sales│
      └────┬────┘                 └────┬────┘
     ┌─────┴─────┐             ┌──────┴──────┐
┌────┴───┐  ┌────┴───┐    ┌────┴───┐    ┌────┴───┐
│Dev team│  │QA team │    │  West  │    │  East  │  ← leaves
└────────┘  └────────┘    └────────┘    └────────┘
```

**Best for:** File systems, HTML document structure, organisation charts, decision trees, databases.

---

## Hash Map — Like a Filing Cabinet with Labeled Drawers

A **key** (like `"name"`) is run through a **hash function** that turns it into a drawer number. You go directly to that drawer — no searching required.

```
Key "name"
    │
    ▼
┌──────────────┐       ┌────┬────┬────┬──────────────┬────┐
│ Hash function│──────▶│ [0]│ [1]│ [2]│ [3] ← "name"│ [4]│
│  "name" → 3  │       ├────┼────┼────┼──────────────┼────┤
└──────────────┘       │age │city│    │  name: Jo    │    │
                       │ 30 │ Lon│    │              │    │
                       └────┴────┴────┴──────────────┴────┘
```

**Best for:** Dictionaries, caches, counting occurrences, database lookups. Extremely fast — often instant.

---

## What Are Algorithms?

**Algorithms** are step-by-step recipes for *doing things* with your data — searching, sorting, transforming. The same goal can be solved many ways, and some ways are dramatically faster than others.

---

## Algorithm 1: Linear Search

Check every item one by one from the start. Simple but slow for large lists.

**Analogy:** Looking for your keys by checking every pocket, one at a time.

**Example — searching for 31 in [3, 7, 12, 18, 25, **31**, 44, 57, 63, 78]:**

```
Step 1: Is [0]=3  our target? No.
Step 2: Is [1]=7  our target? No.
Step 3: Is [2]=12 our target? No.
Step 4: Is [3]=18 our target? No.
Step 5: Is [4]=25 our target? No.
Step 6: Is [5]=31 our target? YES ✓  ← Found in 6 checks
```

**Best for:** Small lists, or unsorted data.

---

## Algorithm 2: Binary Search

Works on **sorted lists only**. Check the middle — if too high, ignore the right half; if too low, ignore the left half. Repeat.

**Analogy:** Finding a word in a dictionary by opening to the middle, then discarding half the book.

**Example — searching for 31 in the same sorted list:**

```
Step 1: Middle is [4]=25. Target 31 is higher → discard left half.
                    ▼ search [5..9] only
Step 2: Middle is [7]=57. Target 31 is lower → discard right half.
                    ▼ search [5..6] only
Step 3: Middle is [5]=31. Found! ✓  ← Only 3 checks needed!
```

**Best for:** Any large sorted list. Orders of magnitude faster than linear search.

| List size | Linear search (worst case) | Binary search (worst case) |
|-----------|---------------------------|---------------------------|
| 10 items  | 10 checks | 4 checks |
| 1,000 items | 1,000 checks | 10 checks |
| 1,000,000 items | 1,000,000 checks | 20 checks |

---

## Algorithm 3: Bubble Sort

Repeatedly compare neighbouring items and swap them if they're in the wrong order. Heavier items "bubble up" to the end. Simple to understand, but slow on large lists.

**Example — sorting [5, 3, 8, 1, 9, 2]:**

```
Pass 1:
  Compare 5,3 → swap → [3, 5, 8, 1, 9, 2]
  Compare 8,1 → swap → [3, 5, 1, 8, 9, 2]
  Compare 9,2 → swap → [3, 5, 1, 8, 2, 9]  ← 9 bubbles to the end ✓

Pass 2:
  Compare 5,1 → swap → [3, 1, 5, 8, 2, 9]
  Compare 8,2 → swap → [3, 1, 5, 2, 8, 9]  ← 8 is now in place ✓

Pass 3:
  Compare 3,1 → swap → [1, 3, 5, 2, 8, 9]
  Compare 5,2 → swap → [1, 3, 2, 5, 8, 9]

Pass 4:
  Compare 3,2 → swap → [1, 2, 3, 5, 8, 9]

Done! Sorted: [1, 2, 3, 5, 8, 9] ✓
```

**Best for:** Learning sorting concepts. In practice, faster algorithms like Merge Sort or Quick Sort are preferred.

---

## The Big Picture

```
                    ┌─────────────────┐    ┌──────────────────┐
   Raw data ───────▶│  Data structure  │───▶│    Algorithm     │───▶ Result!
  (numbers,         │                  │    │                  │
   text,            │  Array / List    │    │  Search (find)   │
   records)         │  Stack / Queue   │    │  Sort (order)    │
                    │  Tree / Graph    │    │  Traverse (visit)│
                    │  Hash Map        │    │  Transform       │
                    └─────────────────┘    └──────────────────┘
```

**Real-world analogy:** A recipe book (data structure) + cooking instructions (algorithm) → a delicious meal (result).

Choosing the **right data structure** paired with the **right algorithm** is what makes programs fast and efficient — it's the engine underneath everything from Google Search to Spotify recommendations to GPS navigation.

---

## Quick Reference

### Data Structures

| Structure | Best used when… | Real-world example |
|-----------|----------------|-------------------|
| Array | You need fast access by position | Spreadsheet rows, pixel grids |
| Linked List | You insert/delete in the middle often | Music playlists |
| Stack | You need "last in, first out" | Browser back button, undo |
| Queue | You need "first in, first out" | Print queue, task scheduler |
| Tree | Data is naturally hierarchical | File system, org chart |
| Hash Map | You need instant lookup by key | Dictionary, cache, database index |

### Algorithms

| Algorithm | What it does | Speed |
|-----------|-------------|-------|
| Linear Search | Checks every item one by one | Slow on large lists |
| Binary Search | Halves the search space each step | Very fast (sorted lists only) |
| Bubble Sort | Swaps neighbours until sorted | Slow — good for learning |
| Merge Sort | Splits, sorts, then merges | Fast — used in practice |
| Quick Sort | Picks a pivot, partitions around it | Fast — very commonly used |

---

*This guide is intended as a friendly introduction. Each of these topics has years of depth to explore — but with these foundations, you understand the engine underneath all programs.*
