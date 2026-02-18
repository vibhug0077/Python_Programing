# 18/02/2026 11:44

#  PYTHON PROGRAMMING TEST

### Code Completion & Code Correction

**Total Marks: 100**
**Duration: 1 Hours**
**Marks per Question: 10**

---

## Instructions

1. Attempt all questions.
2. Do not use external libraries unless mentioned.
3. Do not change function names.
4. Write clean, efficient Python code.
5. Mention assumptions clearly.
6. Handle all edge cases described.
7. Explain time complexity where appropriate.
8. Switch on screen recording using snipping tool
9. You can use chat gpt but only for full coding lecture
10. When using CHAT GPT dont copy code line by line
11. Read CHAT GPT and wirte it yourself.
12. Create a jupyter notebook with A no in markdown

---

# SECTION A — CODE CORRECTION (40 Marks)

---

## Question 1 (10 Marks)

### Stable Top-K Selection

The function should return the top `k` elements based on score.

### Input

* `items`: List of tuples `(name, score)`
* `k`: Integer

Example:

```
items = [("A", 90), ("B", 95), ("C", 95), ("D", 85)]
k = 2
```

### Expected Output

```
[("B", 95), ("C", 95)]
```

(Tie must preserve original order.)

### Given Code (Incorrect)

```python
def top_k(items, k):
    items.sort(key=lambda x: x[1], reverse=True)
    return items[:k]
```

Correct the function.

---

## Question 2 (10 Marks)

### Category Word Counter

Count occurrences of words under each category.

### Input

```
pairs = [("sports","win"), ("sports","win"), ("tech","ai")]
```

### Expected Output

```
{
    "sports": {"win": 2},
    "tech": {"ai": 1}
}
```

### Given Code (Incorrect)

```python
def count_by_category(pairs):
    d = {}
    for cat, word in pairs:
        d.setdefault(cat, {})
        d[cat].setdefault(word, 0)
        d[cat][word] =+ 1
    return d
```

Correct the function.

---

## Question 3 (10 Marks)

### Missing Number (0 to n)

You are given `n` distinct numbers from range `0 to n`.
Return the missing number.

### Input

```
nums = [3, 0, 1]
```

### Expected Output

```
2
```

### Given Code (Incorrect)

```python
def missing_number(nums):
    n = len(nums)
    total = n * (n + 1) / 2
    return int(total - sum(nums))
```

Correct the function.

---

## Question 4 (10 Marks)

### Default Argument Bug

The function should:

* Return a list of unique values added.
* If no second argument provided, each call should start fresh.

### Input

```
add_unique(1)
add_unique(2)
```

### Expected Output

Each call should return:

```
[1]
[2]
```

### Given Code (Incorrect)

```python
def add_unique(x, seen=set()):
    if x not in seen:
        seen.add(x)
    return list(seen)
```

Correct the function.

---

# SECTION B — CODE COMPLETION (60 Marks)

---

## Question 5 (10 Marks)

### Moving Average of Last w Elements

Write a function:

```
def moving_average(stream, w):
```

### Input

* `stream`: List of integers
* `w`: Window size

Example:

```
stream = [1,2,3,4,5]
w = 3
```

### Expected Output

Return list of averages:

```
[1.0, 1.5, 2.0, 3.0, 4.0]
```

(Each index shows average of last `w` elements up to that position.)

Must run in O(n).

---

## Question 6 (10 Marks)

### Run-Length Decode with Escape Support

Write a function:

```
def rle_decode(s):
```

### Input

```
"3a2b1c"
```

### Output

```
"aaabbc"
```

Rules:

* Digits may have multiple digits (e.g., 12a)
* Backslash `\` escapes next character
* Invalid format → raise ValueError

Example:

```
"2\\3"
```

Output:

```
"33"
```

---

## Question 7 (10 Marks)

### Longest Unique Substring

Write:

```
def longest_unique_substring(s):
```

### Input

```
"abcabcbb"
```

### Output

```
3
```

Explanation: "abc" is longest substring without repeating characters.

Must run in O(n).

---

## Question 8 (10 Marks)

### Balanced Brackets with Quotes

Write:

```
def is_balanced_quoted(s):
```

### Input

```
("(]")
```

### Output

```
True
```

Rules:

* Ignore brackets inside quotes `'...'` or `"..."`.
* Quotes may be escaped.
* Validate (), {}, [].

---

## Question 9 (10 Marks)

### Merge Overlapping Intervals with IDs

Write:

```
def merge_intervals_with_ids(intervals):
```

### Input

```
[(1,1,3), (2,2,5), (3,7,8)]
```

### Output

```
[(1,5,[1,2]), (7,8,[3])]
```

Rules:

* Touching intervals (3,5) and (5,7) are overlapping.
* IDs in merged group must be sorted.

---

## Question 10 (10 Marks)

### Robust File Data Parser

Write:

```
def parse(lines):
```

### Input

```
[
"John,25,90",
"John,25,80",
"Anna,130,70",
"Bob,20,105"
]
```

### Output

```
{
"John": (25, 85.0)
}
```

Rules:

* Ignore invalid lines.
* Age: 1–120
* Score: 0–100
* If same name repeats:

  * Age must match.
  * Average all valid scores.
* Must handle very large inputs efficiently.

---


