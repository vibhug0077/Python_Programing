# PYTHON PROGRAMMING — DETAILED THEORY NOTES (CHAPTER 1 + CHAPTER 2)

*(Paragraph style + clear headings + **subheadings for every built-in function / method**)*

---

## CHAPTER 1 — PYTHON FUNDAMENTALS

### 1. Introduction to Python

Python is a high-level, general-purpose programming language designed to emphasize simplicity and readability. Python is called an interpreted language because the Python interpreter executes code step-by-step rather than producing a separate machine-code executable before running. This makes Python ideal for rapid development, learning, automation, data processing, and scripting. Python also supports object-oriented programming and functional programming features, which allows it to be used for both small scripts and large applications.

---

### 2. Running Python: Interactive Mode vs Scripting Mode

Python is commonly used in two modes. In interactive mode, we enter commands in a Python shell or notebook and get output immediately, which is useful for experimentation and learning. In scripting mode, we write a complete program in a `.py` file and run it as a script, which is better for building structured programs and reusable solutions. Interactive mode emphasizes quick feedback, while scripting mode emphasizes organization, repeatability, and maintainability.

---

### 3. Variables, Names, and Dynamic Typing

A Python variable is a name that refers to an object in memory rather than a fixed container holding a value. When we write an assignment statement, Python creates (or reuses) an object and binds the name to it. Python is dynamically typed because the type is associated with the object, not with the variable name, and therefore the same name can refer to objects of different types at different times. This makes Python flexible, but it also requires the programmer to be careful about the kind of values being used at each stage of execution.

---

### 4. Python Object Model: Identity, Type, Value

Python follows the concept that “everything is an object.” Each object can be understood through identity, type, and value/state. Identity means the object’s unique existence; type means the class/category of the object; value means the data stored in the object. This model is important for understanding how Python behaves with copying, comparison, mutability, and function argument passing.

#### Built-in Function: `type()`

**Meaning:** `type(x)` returns the type/class of the object referenced by `x`.
**Why it matters:** It helps confirm what kind of object we are working with and is useful in debugging and validation.
**Conceptual point:** In Python, types are classes, so `type()` tells which class created the object.

#### Built-in Function: `id()`

**Meaning:** `id(x)` returns the identity of the object referenced by `x` (unique for that object during its lifetime).
**Why it matters:** It helps us see whether two names refer to the same object, and it is especially useful when studying mutability and object creation.
**Conceptual point:** Identity is not the same as value. Two different objects can hold the same value but have different identities.

---

### 5. Mutable vs Immutable Data Types

Mutability describes whether an object’s internal content can change after creation. Immutable types (like integers, floats, booleans, strings, and tuples) cannot be changed in-place; any “change” operation produces a new object. Mutable types (like lists, dictionaries, and sets) can be modified in-place, meaning their content can change while the object identity remains the same. This topic is crucial because it impacts program behavior in assignments, function calls, and data manipulation.

---

### 6. Dot Operator (`.`): Attributes and Methods

The dot operator is used to access attributes and methods belonging to an object. A method is a function defined inside a class and meant to operate on objects of that class. When we call an object’s method like `s.upper()`, Python automatically passes the object to that method as an internal parameter (`self`). This is why method calls look different from calling a normal built-in function.

---

### 7. Built-in Functions vs Methods (Core Distinction)

Built-in functions like `len(x)` or `type(x)` are general-purpose functions available globally in Python. Methods belong to a specific object type and are called using the dot operator. For example, `len(s)` is a built-in function that works on many sequence types, while `s.upper()` is a string method and only applies to string objects. Understanding this distinction helps learners read documentation and predict which operations are available for a given data type.

#### Built-in Function: `len()`

**Meaning:** `len(x)` returns the number of elements in a sequence or collection.
**Where used:** strings (characters), lists (items), tuples (items), dictionaries (keys).
**Important note:** `len()` is a built-in function because it works across multiple collection types.

#### String Method: `upper()`

**Meaning:** `s.upper()` returns a new string with all letters converted to uppercase.
**Why it returns a new string:** strings are immutable, so methods like `upper()` produce a new object rather than changing the original.

---

### 8. Input and Output (I/O)

Python programs commonly interact with users using input and output functions. Output is usually displayed using `print()`. User input is collected using `input()`, but a major theoretical point is that input is always read as text (string). Therefore, numeric input must be converted using `int()` or `float()` if we want arithmetic operations.

#### Built-in Function: `print()`

**Meaning:** Displays output to the screen (standard output).
**Key idea:** It can print multiple values separated by commas and can be formatted.

#### Built-in Function: `input()`

**Meaning:** Reads user input as a string.
**Key idea:** Even if the user enters `25`, it comes as `"25"` and must be converted for math.

#### Built-in Function: `int()`

**Meaning:** Converts a value into an integer when possible.
**Common use:** `int(input())` to read numbers correctly.

#### Built-in Function: `float()`

**Meaning:** Converts a value into a floating-point number.
**Common use:** reading decimal values from input.

---

### 9. Operators in Python

Operators are symbols or keywords used to perform operations on values. Arithmetic operators perform mathematical calculations, comparison operators compare values and return booleans, and logical operators combine conditions. Python also provides membership operators to check presence and identity operators to check whether two names refer to the same object. Understanding operator precedence is essential to avoid unexpected results in expressions.

---

### 10. Indentation and Block Structure

Python uses indentation to define the scope of blocks such as `if`, loops, and functions. Indentation is not optional; it is part of Python’s syntax. Correct indentation improves readability and clearly shows program structure. Incorrect indentation leads to errors and can also change program meaning.

---

### 11. Conditional Statements (Decision Making)

Conditionals control program flow based on boolean expressions. The `if` statement executes a block when a condition is true. `if-else` provides two branches, while `if-elif-else` is used to handle multiple conditions in sequence. Python also supports nested conditionals. Another important concept is truthy and falsy values: empty collections, zero values, and `None` are treated as false; most other values are treated as true.

---

### 12. Loops and Iteration

Loops repeat code execution. The `for` loop iterates over sequences and iterables, while the `while` loop repeats as long as a condition stays true. The `range()` function is commonly used with for loops to generate integer sequences. Python provides `break` to exit a loop early, `continue` to skip the current iteration, and `pass` as a placeholder. Python also supports `else` with loops; this else block runs only if the loop completes normally without a break.

#### Built-in Function: `range()`

**Meaning:** Produces a sequence of integers for iteration.
**Forms:** `range(stop)`, `range(start, stop)`, `range(start, stop, step)`.
**Key idea:** stop is excluded; step can be negative for reverse iteration.

---

## CHAPTER 2 — STRINGS, COLLECTIONS, AND FUNCTIONS

### 1. Strings: Sequence Theory and Processing

A string is an immutable sequence of characters. Because it is a sequence, it supports indexing and slicing. Indexing retrieves a single character, while slicing returns a substring. Strings support common operations such as concatenation and membership testing. Many text-processing tasks rely on string methods, and because strings are immutable, most methods return new strings rather than modifying the original.

#### String Method: `split()`

**Meaning:** Splits a string into a list of substrings based on a delimiter.
**Default behavior:** If no delimiter is given, it splits on whitespace.
**Use-case:** Tokenizing sentences into words.

#### String Method: `join()`

**Meaning:** Joins a list of strings into a single string using a delimiter.
**Use-case:** Rebuilding a sentence from words or creating CSV-like output.

---

### 2. Lists: Mutable Sequence and Core Methods

A list is an ordered, mutable collection used to store multiple items. Lists support indexing, slicing, and iteration. Because lists are mutable, they can grow or shrink during program execution. This makes lists suitable for dynamic data storage such as collected inputs, intermediate results, and processed outputs.

#### List Method: `append()`

**Meaning:** Adds a single element to the end of the list.
**Key point:** Only one item is added; it does not “flatten” another list.

#### List Method: `extend()`

**Meaning:** Adds all elements of an iterable (like another list) to the list.
**Key point:** Extends the list with multiple items rather than adding the iterable as one item.

#### List Method: `insert()`

**Meaning:** Inserts an element at a given index position.
**Key point:** Shifts existing elements to the right.

#### List Method: `remove()`

**Meaning:** Removes the first occurrence of a given value from the list.
**Key point:** Raises error if value not found.

#### List Method: `pop()`

**Meaning:** Removes and returns an element by index (default last element).
**Use-case:** Stack-like behavior.

#### List Method: `sort()`

**Meaning:** Sorts the list in-place.
**Key point:** Modifies original list; returns None.

#### List Method: `reverse()`

**Meaning:** Reverses the list in-place.
**Key point:** Changes the list order directly.

---

### 3. Tuples: Immutable Collections

A tuple is an ordered, immutable collection. Tuples are often used to represent fixed records or data that should not change. Because tuples are immutable, they are safer for representing constant data and can be used as dictionary keys if their contents are also immutable.

#### Tuple Method: `count()`

**Meaning:** Returns how many times a value appears in the tuple.

#### Tuple Method: `index()`

**Meaning:** Returns the first index at which a value appears.

---

### 4. Sets: Unique Unordered Collections

Sets store unique items and automatically remove duplicates. They are unordered and do not support indexing. Sets are used for membership testing and for operations like union and intersection. They are especially useful when we want to eliminate duplicates or compare groups of items.

---

### 5. Dictionaries: Key-Value Data Structures

Dictionaries store mappings from keys to values, allowing fast lookup. Keys must be immutable/hashable. Dictionaries are used for structured records, counting frequency of items, and representing configuration-like data. Dictionaries support nesting, which allows complex structured information to be stored efficiently.

#### Dictionary Method: `get()`

**Meaning:** Returns the value for a key if present, otherwise returns a default value.
**Why important:** Prevents KeyError and supports safe access.

#### Dictionary Method: `items()`

**Meaning:** Returns a view of key-value pairs, used in loops to iterate over both keys and values.

#### Dictionary Method: `keys()`

**Meaning:** Returns a view of all keys.

#### Dictionary Method: `values()`

**Meaning:** Returns a view of all values.

#### Dictionary Method: `update()`

**Meaning:** Updates dictionary with new key-value pairs from another dict or iterable of pairs.

#### Dictionary Method: `pop()`

**Meaning:** Removes a key and returns its value (can provide default to avoid errors).

---

### 6. Functions: Definition and Components

Functions are reusable named blocks of code defined with `def`. They allow modular programming, reduce repetition, and improve readability. A function consists of its name, parameters, body, and optional return value. If no return statement is used, the function returns `None`. Python supports positional arguments, keyword arguments, default arguments, and variable-length arguments. Docstrings provide built-in documentation and help make code self-explanatory.

#### Keyword: `def`

**Meaning:** Used to define a function.

#### Keyword: `return`

**Meaning:** Sends a value back to the caller and ends the function execution.

#### Function Attribute: `__doc__`

**Meaning:** Stores the docstring of a function, useful for documentation.

---

### 7. Recursion

Recursion is when a function calls itself to solve a problem by dividing it into smaller parts. A recursive function must always have a base case to stop recursion. Without a base case, recursion continues indefinitely and results in error. Recursion is useful for factorial, tree traversal, and divide-and-conquer style problems, but it must be used carefully.

---

### 8. Advanced Functions: lambda, map, filter, inner functions, passing functions

A lambda is an anonymous one-line function used for short computations. The map function applies a transformation function to every element of an iterable and produces a mapped result. Filter selects only those elements that satisfy a condition. Inner functions are functions defined inside other functions, commonly used for encapsulating helper logic and creating closures. Python treats functions as first-class objects, meaning they can be stored in variables, placed in collections, passed as parameters, and returned from other functions.

#### Keyword: `lambda`

**Meaning:** Defines an anonymous one-line function.
**Key point:** Best used for short logic, often with map/filter/sorting keys.

#### Built-in Function: `map()`

**Meaning:** Applies a function to every element and returns an iterator-like result.
**Key point:** Transformation operation; output length equals input length.

#### Built-in Function: `filter()`

**Meaning:** Keeps elements for which the function returns true.
**Key point:** Selection operation; output length may be smaller.

---

### 9. Mutability in Function Arguments (Critical Topic)

When lists or dictionaries are passed to a function, the function receives a reference to the same object, not a copy. Therefore, if the function modifies the object (such as appending to a list or adding keys to a dictionary), the changes are visible outside the function. However, if the function reassigns the parameter name to a new object, the original object outside the function remains unchanged. This difference between modifying the object and rebinding the name is a core theory point in Python and appears frequently in exams.

---

If you want, I can add **subheadings for more built-ins** mentioned in your chapters too (like `sorted()`, `min()`, `max()`, `sum()`, `any()`, `all()`, etc.) and write the same paragraph-style explanation for each, exactly like above.
