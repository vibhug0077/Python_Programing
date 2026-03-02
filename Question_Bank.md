### Q1. Explain why Python is called an interpreted language and a dynamically typed language. Show a tiny example where a variable changes type.

**Answer:** Python is called **interpreted** because your source code is executed by a **Python interpreter** at runtime rather than being fully converted into machine code ahead of time like a traditional compiled language. In practice, Python code is translated into **bytecode** and executed by the **Python Virtual Machine (PVM)**, which still behaves like interpretation from the user’s perspective. Python is also **dynamically typed** because the **type belongs to the object**, not to the variable name. A variable is only a **reference (name binding)**, so it can point to different objects of different types during execution.

```python
x = 10
print(type(x))   # int
x = 3.5
print(type(x))   # float
x = "hello"
print(type(x))   # str
```

---

### Q2. Differentiate between compiled and interpreted languages. Why is Python commonly described as interpreted?

**Answer:** In a **compiled language** (like C/C++), the entire program is translated into **machine code** before execution, producing an executable file. This often gives faster performance and earlier detection of some errors. In an **interpreted language** (like Python), code is executed under an **interpreter** at runtime, enabling fast testing and interactive development. Python is commonly described as interpreted because you typically run `.py` files directly with the interpreter, and execution happens step-by-step in the **runtime environment**. Internally, Python compiles to **bytecode**, but it is still executed by the **PVM**, not directly by the CPU like native binaries.

---

### Q3. Define dynamic typing. Demonstrate with a short code snippet using `type()` that a name can bind to different object types.

**Answer:** **Dynamic typing** means Python does not require variable type declarations (like `int x`), and the **type is determined at runtime** based on the object currently referenced by a name. In Python, variables are **labels** pointing to objects, and each object carries its own **type information**. Because of this, the same variable name can be rebound to a different object type at any time. This improves **flexibility** and speeds up development but requires careful handling to avoid runtime type errors.

```python
x = 100
print(type(x))     # <class 'int'>
x = 99.9
print(type(x))     # <class 'float'>
x = "99.9"
print(type(x))     # <class 'str'>
```

---

### Q4. Explain what happens at runtime when you execute `x=10; x='10'`. Mention how Python treats the variable name and object.

**Answer:** When Python executes `x = 10`, it creates an **integer object** `10` (or references an existing one) and binds the name **x** to that object. When `x = '10'` is executed next, Python creates a new **string object** `'10'` and **rebinds** the name **x** to this new object. This shows that in Python, **variables do not have fixed types**; instead, **objects have types** and variable names are simply references. The old integer object may remain in memory if referenced elsewhere, otherwise it may be cleared later by **garbage collection**.

---

### Q5. State two advantages and one disadvantage of dynamic typing in Python with a one-line example.

**Answer:** Two advantages of **dynamic typing** are **faster development** (no need to declare types) and **flexibility** (the same function can work with multiple types). This supports rapid prototyping and reusable logic. One disadvantage is that type-related mistakes may only appear at **runtime**, which can cause unexpected errors in large programs if not tested well. A simple example: if `x` becomes a string unexpectedly, arithmetic fails.
Example: `x = "10"; print(x + 5)` will raise a **TypeError** because `"10"` is not an integer.

---

### Q6. Using list comprehension, create (i) squares of even numbers and (ii) cubes of odd numbers from a given list `nums`.

**Answer:** **List comprehension** is a compact way to build lists using an expression and a loop inside brackets. It often replaces longer `for` loops and improves clarity when used correctly. Here, we filter numbers based on **even/odd condition** using `if` inside the comprehension. Even numbers satisfy `x % 2 == 0` and odd numbers satisfy `x % 2 != 0`. Then we transform them using `x*x` (square) or `x**3` (cube). This demonstrates **filter + transform** in a single readable line.

```python
nums = [1, 2, 3, 4, 5, 6]
even_sq = [x * x for x in nums if x % 2 == 0]
odd_cube = [x ** 3 for x in nums if x % 2 != 0]
print(even_sq)   # [4, 16, 36]
print(odd_cube)  # [1, 27, 125]
```

---

### Q7. From `nums=[-3,-2,-1,0,1,2,3]`, build two lists using comprehension: negatives’ absolute values and non-negatives’ squares.

**Answer:** This problem uses list comprehension to perform **conditional selection** and **value transformation**. For negative numbers, we want the **absolute value**, which can be computed as `-x` when `x < 0`. For non-negative numbers (0 and positives), we compute squares using `x*x`. This approach is efficient and readable because it avoids nested loops and keeps logic close to data transformation. It also reinforces the idea that list comprehension can implement both **filtering** and **mapping** behavior.

```python
nums = [-3, -2, -1, 0, 1, 2, 3]
neg_abs = [-x for x in nums if x < 0]
nonneg_sq = [x * x for x in nums if x >= 0]
print(neg_abs)    # [3, 2, 1]
print(nonneg_sq)  # [0, 1, 4, 9]
```

---

### Q8. Using list comprehension, filter vowels from a string `s` and store them in a list.

**Answer:** A string in Python is a **sequence**, so it can be iterated character by character. Using list comprehension, we can scan each character and include it only if it belongs to a set of vowel characters. This is a classic example of a **filtering task**. The key idea is to use the **membership operator `in`** to test whether a character exists in `"aeiouAEIOU"`, ensuring both uppercase and lowercase vowels are captured. The result is a list of vowel characters in the same order they appear in the string.

```python
s = "Education"
vowels = [ch for ch in s if ch in "aeiouAEIOU"]
print(vowels)  # ['E', 'u', 'a', 'i', 'o']
```

---

### Q9. Given a list of words, use comprehension to create a list of word lengths only for words longer than 3 characters.

**Answer:** This task combines a **condition** and a **transformation** using list comprehension. We first filter the words using the condition `len(word) > 3`, and for the selected words we transform each word into its **length** using `len(word)`. This is useful in many practical cases such as text analytics, where we often filter tokens and compute properties like length, frequency, or pattern matching. Using comprehension keeps the code short and expressive while still following a clear logic.

```python
words = ["py", "data", "science", "ai", "cloud"]
lengths = [len(w) for w in words if len(w) > 3]
print(lengths)  # [4, 7, 5]
```

---

### Q10. Given two lists `a` and `b` of equal length, use comprehension to create element-wise sums.

**Answer:** Element-wise summation means adding corresponding elements from two lists based on their index positions. Since list comprehension can iterate over indices using `range(len(a))`, we can compute sums as `a[i] + b[i]`. This demonstrates using **index-based iteration** and emphasizes assumptions like both lists having the **same length**. This approach is common in basic data processing when we combine aligned datasets (e.g., marks of two tests, monthly figures of two years). It also trains the concept of **parallel traversal**.

```python
a = [1, 2, 3]
b = [10, 20, 30]
sums = [a[i] + b[i] for i in range(len(a))]
print(sums)  # [11, 22, 33]
```

---

### Q11. Define mutable and immutable objects with one example each. Explain how immutability affects item assignment in strings.

**Answer:** A **mutable** object is one whose internal contents can be changed **in-place** after creation, such as a **list** or **dictionary**. An **immutable** object cannot be changed after it is created; any “modification” creates a new object, such as an **integer**, **string**, or **tuple**. Strings are immutable, so item assignment like `s[0] = 'P'` is not allowed and produces an error. This immutability helps in **security**, **hashing**, and safe sharing of objects without accidental changes, but it requires using methods that return new strings like `replace()` or slicing.

---

### Q12. Explain why lists are mutable but tuples are immutable. Mention how this impacts their use as dictionary keys.

**Answer:** Lists are designed for **dynamic storage**, meaning elements can be added, removed, or updated during program execution. Therefore, lists are **mutable** and offer many in-place methods such as `append`, `remove`, and `sort`. Tuples represent **fixed records** and are intentionally **immutable**, which makes them safer and faster for constant data. This immutability also makes tuples **hashable** (if their elements are hashable), allowing tuples to be used as **dictionary keys**. Lists cannot be dictionary keys because their contents can change, which would break the dictionary’s hashing and lookup logic.

---

### Q13. Explain the difference between `==` and `is` using mutable/immutable examples.

**Answer:** The operator `==` checks **value equality**, meaning it compares whether two objects contain the same data. The operator `is` checks **identity**, meaning it checks whether both names point to the **same object in memory**. With mutable objects like lists, two separate lists can have the same contents but different identities, so `a == b` may be True while `a is b` is False. With immutables, you may sometimes observe `is` being True due to internal optimizations, but conceptually `is` should be used only when you truly want identity (e.g., `x is None`).

```python
a = [1,2]
b = [1,2]
print(a == b)  # True
print(a is b)  # False
```

---

### Q14. Why does `s.replace('a','b')` not change the original string `s`? Explain with immutability concept.

**Answer:** Strings are **immutable** in Python, meaning their characters cannot be changed in-place once the string object is created. Methods like `replace()` do not modify the existing string; instead, they create and return a **new string object** with the requested modifications. If you want the variable `s` to reflect the changed text, you must **reassign** it: `s = s.replace('a','b')`. This design ensures strings are safe for sharing, help maintain stable **hash values**, and avoid unexpected changes when the same string is referenced in multiple places.

---

### Q15. Compare string (immutable sequence) and dictionary (mutable mapping) in terms of in-place updates and typical operations.

**Answer:** A string is an **immutable sequence**, so you cannot change its characters directly using indexing. Operations on strings typically create **new strings**, such as concatenation, slicing, `replace()`, and case conversion methods. In contrast, a dictionary is a **mutable mapping** of key-value pairs, so it supports in-place updates like `d[key] = value`, insertion of new keys, deletion using `pop()` or `del`, and update using `update()`. Strings are ideal for **text processing** and ordered character access, while dictionaries are ideal for **fast lookup**, structured records, and frequency counting.

---

### Q16. Write a reusable function `normalize_text(s)` that trims spaces, lowercases, removes punctuation, and returns tokens. Show 2 examples.

**Answer:** A robust `normalize_text` function performs **text cleaning** so that comparisons and counting become consistent. The typical steps are **strip()** to remove leading/trailing spaces, **lower()** to convert to a uniform case, and **punctuation removal** so tokens like “data,” and “data” become the same. Since punctuation can appear anywhere, a character loop is commonly used: keep only **alphanumeric** characters and spaces. Finally, `split()` converts the cleaned string into a **token list** (words). This is a fundamental step in basic NLP tasks like word frequency analysis.

```python
def normalize_text(s):
    s = s.strip().lower()
    cleaned = ""
    for ch in s:
        if ch.isalnum() or ch.isspace():
            cleaned += ch
    return [t for t in cleaned.split() if t]

print(normalize_text("  Hello, World!  "))
print(normalize_text("AI-tools: map/filter; LAMBDA."))
```

---

### Q17. Create a function that normalizes multiple sentences in a list and returns a list of token lists using `normalize_text`.

**Answer:** When working with multiple sentences, we often need consistent preprocessing for each sentence before further analysis. A practical design is to write a single reusable normalizer function (like `normalize_text`) and then apply it to each sentence in a list using a loop or list comprehension. This produces a **list of token lists**, where each inner list contains clean tokens for a sentence. This representation is useful for tasks like calculating per-sentence word counts, building vocabulary, or preparing data for further processing.

```python
def normalize_all(sentences):
    out = []
    for s in sentences:
        out.append(normalize_text(s))
    return out

sentences = [" Hi, there! ", "Python is FUN."]
print(normalize_all(sentences))
```

---

### Q18. Modify `normalize_text` so it also removes extra internal spaces (multiple spaces). Explain your approach briefly.

**Answer:** Multiple internal spaces can occur due to inconsistent typing or formatting. The easiest and most reliable way to collapse extra spaces is to rely on `split()` without arguments, because `split()` automatically treats repeated whitespace as a single separator. After punctuation removal, when we call `cleaned.split()`, it returns only meaningful tokens and removes empty strings created by extra spaces. If we need a clean normalized sentence again, we can join tokens with a single space. Returning tokens directly already solves the extra-space issue and is commonly preferred in text analytics.

```python
def normalize_text(s):
    s = s.strip().lower()
    cleaned = ""
    for ch in s:
        if ch.isalnum() or ch.isspace():
            cleaned += ch
    tokens = cleaned.split()   # collapses multiple spaces
    return tokens
```

---

### Q19. Write `normalize_text` without using `replace` for each punctuation; use a loop and keep only alphanumerics and spaces.

**Answer:** Removing punctuation one-by-one using `replace()` is not scalable because we must list all punctuation characters. A better approach is to scan each character and keep only those that are valid for tokens: **letters, digits, and spaces**. Python’s character methods like `isalnum()` and `isspace()` are useful here. This technique makes the function general and works for many punctuation types without having to explicitly mention them. After building a clean string, `split()` creates tokens. This is an efficient, exam-friendly approach for normalization problems.

```python
def normalize_text(s):
    s = s.strip().lower()
    out = []
    for ch in s:
        if ch.isalnum() or ch == " ":
            out.append(ch)
    cleaned = "".join(out)
    return cleaned.split()
```

---

### Q20. Write a function that counts normalized word frequencies from a sentence using `normalize_text` and a dictionary.

**Answer:** Word frequency counting is a classic use case for dictionaries because dictionaries provide fast key-based access. After normalizing the sentence into tokens (so “Python,” and “python” become the same), we iterate through tokens and update counts. The dictionary method `get(key, default)` is helpful because it avoids KeyError and allows counting in a single line: `freq[word] = freq.get(word, 0) + 1`. This approach produces a reliable frequency map used in many tasks such as text statistics, keyword extraction, and basic search indexing.

```python
def word_freq(sentence):
    tokens = normalize_text(sentence)
    freq = {}
    for t in tokens:
        freq[t] = freq.get(t, 0) + 1
    return freq

print(word_freq("Python, python! is easy; Python is fun."))
```

---

### Q21. Differentiate syntax error and runtime error with one example each.

**Answer:** A **syntax error** occurs when code violates Python’s grammar rules, so the program cannot even start execution. For example, missing a colon after an `if` statement or incorrect indentation causes a syntax error and Python stops before running any line. A **runtime error** happens during execution when Python meets an illegal operation, such as dividing by zero, using an undefined variable, or accessing an invalid index. Syntax errors are detected during parsing, while runtime errors are detected while the program is running and can happen only when that line is executed.

---

### Q22. What is a NameError? Give a small example and classify it (syntax/runtime).

**Answer:** A **NameError** occurs at **runtime** when Python finds a variable name that has not been defined in the current scope. It is not a syntax error because the code structure is correct; the issue is that the name does not exist at execution time. This commonly happens due to spelling mistakes, using a variable before assignment, or trying to access a variable declared inside a function from outside. To fix it, ensure the variable is defined before use or is in the correct scope.

```python
print(x)   # NameError: name 'x' is not defined
```

---

### Q23. What is a ZeroDivisionError? Give an example and explain when it occurs.

**Answer:** A **ZeroDivisionError** is a runtime error raised when you try to divide any number by zero using division operators like `/`, `//`, or `%`. Python prevents division by zero because it is mathematically undefined. This error occurs only when the line is executed, so it depends on input and program flow. In real programs, this is commonly handled using **condition checks** (like `if b != 0`) or by using **exception handling** (`try/except`). This ensures the program remains stable even with invalid input.

```python
a = 10
b = 0
print(a / b)  # ZeroDivisionError
```

---

### Q24. Explain why indentation mistakes raise errors in Python. Is it syntax or runtime? Give an example.

**Answer:** In Python, indentation is part of the **syntax** because it defines code blocks for structures like `if`, `for`, `while`, `def`, and `class`. If indentation is missing or inconsistent, Python cannot correctly determine the boundaries of a block, so it raises an error before executing the program. Therefore, indentation problems are generally classified as **syntax-related errors** (IndentationError). This design enforces readability and prevents ambiguous code layouts. Correct indentation ensures Python understands which statements belong inside a condition or loop.

```python
if True:
print("Hello")  # IndentationError
```

---

### Q25. Give one example of a TypeError during execution and explain its cause.

**Answer:** A **TypeError** is a runtime error that occurs when an operation is applied to objects of inappropriate types. For example, Python cannot add a string and an integer directly because `+` has different meanings: it performs concatenation for strings and arithmetic addition for numbers. This kind of error is common when using `input()` (which returns a string) without converting it to `int` or `float`. The fix is to ensure compatible types using explicit conversion or consistent data handling.

```python
print("2" + 2)   # TypeError: can only concatenate str (not "int") to str
```

---
### Q26. Design a Student Records Analyzer (Coding) — 25 Marks

**Question:** You are given a list of strings. Each string is one record in the format: **"roll,name,marks,section"**.
Example: `"101,Aman,78,A"`
Some records may be invalid.

Write a function **`build_valid_records(lines)`** that returns a **dictionary of dictionaries** containing only valid records.

**Validation Rules (all must be satisfied):**

* **roll** must be an **integer > 0**
* **name** must be **non-empty** after `strip()`
* **marks** must be an **integer in [0, 100]**
* **section** must be a **single alphabet** letter (A–Z or a–z)

**Duplicate roll rule:**
If the same **roll** appears again, **keep only the first valid record** and ignore later ones for that roll.

**Return format:**
`{101: {"name":"Aman","marks":78,"section":"A"}, ...}`

---

**Answer:** This solution uses **loops**, **basic validation**, and a **dictionary-of-dictionaries** to store the first valid record for each roll. We split each line by comma, apply `strip()` to remove extra spaces, validate each field using simple checks (`isdigit()`, range checks, `isalpha()`, length check), and then enforce the **first-valid-wins** rule by checking whether the roll already exists in the output dictionary.

```python
def build_valid_records(lines):
    records = {}

    for line in lines:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) != 4:
            continue

        roll_s, name, marks_s, section = parts

        if not roll_s.isdigit():
            continue
        roll = int(roll_s)
        if roll <= 0:
            continue

        if name == "":
            continue

        if not marks_s.isdigit():
            continue
        marks = int(marks_s)
        if marks < 0 or marks > 100:
            continue

        if len(section) != 1 or not section.isalpha():
            continue

        if roll in records:
            continue  # keep first valid record only

        records[roll] = {"name": name, "marks": marks, "section": section}

    return records
```

---

### Q27. Lambda Function (Theory + Practice) — 25 Marks

**Question:**

**(A) Describe lambda functions (5 Marks)**
Explain what a **lambda function** is in Python. Write the **general syntax**. List **three limitations** of lambda compared to `def`.

**(B) Write lambda expressions (10 Marks)**
Write a **lambda expression** for each:

1. **square** of a number
2. check if a number is **divisible by 5**
3. return **last digit** of an integer
4. convert a string to **uppercase**
5. return **True** if **length of string > 6**

**(C) Using lambda with map/filter (10 Marks)**
Given:
`nums = [3, 10, 15, 22, 25, 30, 41]`

1. Use **map() + lambda** to create a list of **squares** of all numbers.
2. Use **filter() + lambda** to create a list of numbers **divisible by 5**.
3. Use **filter() + lambda** to create a list of numbers **greater than 20**.
   Print all three outputs.

---

**Answer:** A **lambda function** is an **anonymous function** written in a single line, used for short and temporary logic. The syntax is **`lambda arguments: expression`**. Unlike `def`, lambda can only contain **one expression**, it becomes **less readable** for complex logic, and debugging can be harder because it doesn’t carry a clear function name in tracebacks. Lambda is commonly used with **higher-order functions** like **map()** and **filter()**, where a small function is passed as an argument for transformation or selection.

```python
# Part (B)
sq = lambda x: x * x
div5 = lambda x: x % 5 == 0
last_digit = lambda x: abs(x) % 10
upper = lambda s: s.upper()
len_gt6 = lambda s: len(s) > 6

# Part (C)
nums = [3, 10, 15, 22, 25, 30, 41]

squares = list(map(lambda x: x * x, nums))
by5 = list(filter(lambda x: x % 5 == 0, nums))
gt20 = list(filter(lambda x: x > 20, nums))

print(squares)
print(by5)
print(gt20)
```

---


### Q28. (Coding) Build Valid Records + Invalid Count — 25 Marks

**Question:** Using the same input format **"roll,name,marks,section"**, write a function `build_valid_records_and_invalid_count(lines)` that:

1. returns the valid records dictionary (same rules as Q26)
2. also returns an integer `invalid_count` representing how many lines were invalid (do not count duplicates as invalid; just ignored).

**Answer:**

```python
def build_valid_records_and_invalid_count(lines):
    records = {}
    invalid_count = 0

    for line in lines:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) != 4:
            invalid_count += 1
            continue

        roll_s, name, marks_s, section = parts

        ok = True
        if not roll_s.isdigit():
            ok = False
        else:
            roll = int(roll_s)
            if roll <= 0:
                ok = False

        if name == "":
            ok = False

        if not marks_s.isdigit():
            ok = False
        else:
            marks = int(marks_s)
            if marks < 0 or marks > 100:
                ok = False

        if len(section) != 1 or not section.isalpha():
            ok = False

        if not ok:
            invalid_count += 1
            continue

        # duplicate roll is ignored (not counted invalid)
        if roll in records:
            continue

        records[roll] = {"name": name, "marks": marks, "section": section}

    return records, invalid_count
```

---

### Q29. (Coding) Section-wise Summary — 25 Marks

**Question:** From a valid records dictionary (output of Q26), write `section_summary(records)` that returns:
`{"A":{"count":..,"total":..,"average":..}, "B":{...}}`

**Answer:**

```python
def section_summary(records):
    summary = {}

    for rec in records.values():
        sec = rec["section"]
        if sec not in summary:
            summary[sec] = {"count": 0, "total": 0}

        summary[sec]["count"] += 1
        summary[sec]["total"] += rec["marks"]

    for sec in summary:
        c = summary[sec]["count"]
        summary[sec]["average"] = summary[sec]["total"] / c if c else 0.0

    return summary
```

---

### Q30. (Coding) Find Topper (Stable by First Appearance) — 25 Marks

**Question:** Given `lines` and the `records` dict (from Q26), write `topper_stable(lines, records)` that returns topper dict:
`{"roll":..., "name":..., "marks":..., "section":...}`
If marks tie, choose the student whose valid record appeared **earlier in lines**.

**Answer:**

```python
def topper_stable(lines, records):
    best = None

    for line in lines:
        parts = [p.strip() for p in line.split(",")]
        if len(parts) != 4:
            continue
        roll_s = parts[0]
        if not roll_s.isdigit():
            continue
        roll = int(roll_s)
        if roll not in records:
            continue

        rec = records[roll]
        if best is None or rec["marks"] > best["marks"]:
            best = {"roll": roll, "name": rec["name"], "marks": rec["marks"], "section": rec["section"]}

    return best
```

---

### Q31. (Lambda) Create 5 lambdas and test them — 25 Marks

**Question:** Write lambda expressions for: square, divisible by 5, last digit, uppercase, length>6. Then test each on sample inputs and print outputs.

**Answer:**

```python
sq = lambda x: x * x
div5 = lambda x: x % 5 == 0
last_digit = lambda x: abs(x) % 10
upper = lambda s: s.upper()
len_gt6 = lambda s: len(s) > 6

print(sq(7))              # 49
print(div5(25))           # True
print(last_digit(-123))   # 3
print(upper("python"))    # PYTHON
print(len_gt6("science")) # True
```

---

### Q32. (map + lambda) Convert marks to grades — 25 Marks

**Question:** Given `marks = [32, 45, 76, 88, 91]`, use `map()` + `lambda` to convert marks into bands:
90–100 A+, 75–89 A, 60–74 B, 40–59 C, else F.

**Answer:**

```python
marks = [32, 45, 76, 88, 91]

grade = lambda m: "A+" if m >= 90 else ("A" if m >= 75 else ("B" if m >= 60 else ("C" if m >= 40 else "F")))

bands = list(map(grade, marks))
print(bands)
```

---

### Q33. (filter + lambda) Select high scorers — 25 Marks

**Question:** Given `marks = [32, 45, 76, 88, 91]`, use `filter()` + `lambda` to select marks >= 75.

**Answer:**

```python
marks = [32, 45, 76, 88, 91]
hi = list(filter(lambda m: m >= 75, marks))
print(hi)  # [76, 88, 91]
```

---

### Q34. (map + filter + lambda) Squares of even numbers — 25 Marks

**Question:** Given `nums = [1,2,3,4,5,6,7,8]`, first filter even numbers using `filter()+lambda`, then square them using `map()+lambda`.

**Answer:**

```python
nums = [1,2,3,4,5,6,7,8]
evens = filter(lambda x: x % 2 == 0, nums)
squares = list(map(lambda x: x * x, evens))
print(squares)  # [4, 16, 36, 64]
```

---

### Q35. (Lambda + dict processing) Extract all names — 25 Marks

**Question:** Given records dict `{roll: {"name":..., "marks":..., "section":...}}`, use `map()+lambda` on `records.values()` to extract all names into a list.

**Answer:**

```python
records = {
    101: {"name": "Aman", "marks": 78, "section": "A"},
    102: {"name": "Neha", "marks": 91, "section": "B"}
}

names = list(map(lambda rec: rec["name"], records.values()))
print(names)
```

---

### Q36. (Lambda) Sort dictionary items by marks — 25 Marks

**Question:** Given records dict, use `sorted()` with `key=lambda ...` to sort `(roll, rec)` pairs by `rec["marks"]` ascending.

**Answer:**

```python
records = {
    101: {"name": "Aman", "marks": 78, "section": "A"},
    102: {"name": "Neha", "marks": 91, "section": "B"},
    103: {"name": "Raj", "marks": 67, "section": "A"}
}

sorted_items = sorted(records.items(), key=lambda item: item[1]["marks"])
print(sorted_items)
```

---

### Q37. (Theory) Compare lambda with def + use cases — 25 Marks

**Question:** Explain lambda vs def. Write two situations where lambda is better and two where def is better.

**Answer:** Lambda is best for **short, single-expression logic** especially when passing a function to `map`, `filter`, or `sorted(key=...)`. It reduces code length and keeps the logic close to usage. However, `def` is better for **multi-step logic**, readability, documentation with docstrings, and debugging, because named functions appear clearly in tracebacks. Lambda also cannot contain statements like loops and try/except, so complex logic should always be written using `def`.

---

