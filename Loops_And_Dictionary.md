Below is structured content on  **Loops (all types)** and looping over **Lists, Tuples, Sets, Dictionaries, and Arrays** in Python, with clear examples.

---

## 1) Loops in Python: Overview

Python supports two main loop types:

### A) `for` loop

Used to iterate over items of a sequence/collection (or any iterable).

**Syntax**

```python
for item in iterable:
    # block
```

### B) `while` loop

Runs as long as a condition remains `True`.

**Syntax**

```python
while condition:
    # block
```

Python also supports loop control statements:

* `break` → exit the loop immediately
* `continue` → skip to next iteration
* `pass` → do nothing (placeholder)
* `else` with loops → runs only if loop finishes normally (no `break`)

---

## 2) `for` Loop Types and Patterns

### 2.1 Looping over a range (counting)

```python
for i in range(5):     # 0 to 4
    print(i)
```

Range variations:

```python
for i in range(2, 7):      # 2 to 6
    print(i)

for i in range(10, 0, -2): # 10, 8, 6, 4, 2
    print(i)
```

### 2.2 Looping with `enumerate()` (index + value)

```python
names = ["A", "B", "C"]
for idx, val in enumerate(names):
    print(idx, val)
```

Start index from 1:

```python
for idx, val in enumerate(names, start=1):
    print(idx, val)
```

### 2.3 Looping with `zip()` (parallel iteration)

```python
students = ["A", "B", "C"]
marks = [90, 85, 92]

for s, m in zip(students, marks):
    print(s, m)
```

### 2.4 Nested loops

```python
for i in range(1, 4):
    for j in range(1, 3):
        print(i, j)
```

---

## 3) `while` Loop Types and Patterns

### 3.1 Basic while loop

```python
i = 0
while i < 5:
    print(i)
    i += 1
```

### 3.2 Infinite loop (must use `break`)

```python
while True:
    text = input("Type 'exit' to stop: ")
    if text == "exit":
        break
```

---

## 4) Loop Control Statements

### 4.1 `break`

```python
for i in range(10):
    if i == 5:
        break
    print(i)
```

### 4.2 `continue`

```python
for i in range(6):
    if i % 2 == 0:
        continue
    print(i)   # prints only odd numbers
```

### 4.3 `pass`

```python
for i in range(3):
    pass
```

### 4.4 `else` with loops

**`for-else`:** else runs only if loop completes without `break`

```python
nums = [2, 4, 6, 8]

for n in nums:
    if n % 2 != 0:
        print("Odd found")
        break
else:
    print("No odd number found")
```

---

## 5) Looping Through Collections

## 5.1 Lists (ordered, mutable)

```python
arr = [10, 20, 30]

for x in arr:
    print(x)
```

Index-based loop (less common, but useful):

```python
for i in range(len(arr)):
    print(i, arr[i])
```

---

## 5.2 Tuples (ordered, immutable)

```python
t = (1, 2, 3)
for x in t:
    print(x)
```

---

## 5.3 Sets (unordered, unique)

```python
s = {10, 20, 10, 30}  # duplicates removed
for x in s:
    print(x)          # order is not guaranteed
```

If you need sorted order:

```python
for x in sorted(s):
    print(x)
```

---

## 5.4 Dictionaries (key-value mapping)

### Loop over keys (default)

```python
d = {"A": 90, "B": 85, "C": 92}

for key in d:
    print(key, d[key])
```

### Loop over values

```python
for val in d.values():
    print(val)
```

### Loop over key-value pairs (recommended)

```python
for k, v in d.items():
    print(k, v)
```

---

## 6) Arrays in Python (3 common meanings)

### 6.1 Python list used as an “array” (most common)

In many beginner contexts, “array” means a list:

```python
a = [1, 2, 3, 4]
for x in a:
    print(x)
```

### 6.2 `array` module (typed arrays)

```python
from array import array

a = array('i', [1, 2, 3, 4])   # 'i' means signed int
for x in a:
    print(x)
```

### 6.3 NumPy arrays (used in Data Science)

```python
import numpy as np

a = np.array([1, 2, 3, 4])
for x in a:
    print(x)
```

Loop with index:

```python
for i in range(a.size):
    print(i, a[i])
```

---

## 7) Useful Loop Tools (Very Common)

### 7.1 `sum`, `min`, `max`

```python
nums = [10, 5, 20]
print(sum(nums))
print(min(nums))
print(max(nums))
```

### 7.2 Comprehensions (compact loops)

List comprehension:

```python
squares = [x*x for x in range(1, 6)]
print(squares)
```

With condition:

```python
evens = [x for x in range(1, 11) if x % 2 == 0]
print(evens)
```

Dictionary comprehension:

```python
d = {x: x*x for x in range(1, 6)}
print(d)
```

Set comprehension:

```python
unique_lengths = {len(w) for w in ["hi", "hello", "hi", "world"]}
print(unique_lengths)
```

---
