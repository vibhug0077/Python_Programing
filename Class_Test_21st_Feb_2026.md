
# Python Coding Test

## Based on Syllabus Topics: Classes, Objects, Methods, Variables, and Operator Overloading

**Total Marks: 100**
**Duration: 2 Hours**

## Instructions

1. Attempt all questions.
2. Write programs in Python only.
3. Do not change the function name or class name where already given.
4. Use proper indentation.
5. Add comments wherever needed.
6. For class-based questions, create objects and show output.
7. The first 3 questions are extremely easy. The later questions gradually become tougher.

---

# Section A — Very Easy Coding Questions

## (3 × 15 = 45 Marks)

### Q1. Class Variable vs Instance Variable

Create a class `Student` with:

* one **class variable**: `school_name = "UPES"`
* two **instance variables**: `name` and `age`

Create two objects and print:

* school name using both objects
* name and age of both students

### Expected Concept

This question checks your understanding of **class variable vs instance variable**. 

### Sample Output

```python
School: UPES
Student 1: Aman 20
Student 2: Riya 21
```

---

### Q2. Instance Method and Class Method

Create a class `Employee` with:

* class variable: `company = "ABC Ltd"`
* instance variables: `name`, `salary`
* instance method `show_details()` to print employee details
* class method `change_company(new_name)` to change company name for all employees

Create two objects. Change the company name using class method. Print details before and after change.

### Expected Concept

This follows the syllabus topic of **instance method and class method**.  

---

### Q3. Static Method

Create a class `MathHelper` with a static method:

```python
is_even(num)
```

It should return `True` if the number is even, otherwise `False`.

Test the method with:

* 8
* 11

### Expected Concept

This is based on the syllabus section on **static methods as utility methods**. 

### Sample Output

```python
True
False
```

---

# Section B — Easy to Moderate Coding Questions

## (2 × 15 = 30 Marks)

### Q4. Public and Private Data Members

Create a class `BankAccount` with:

* public variable: `name`
* private variable: `__balance`

Add methods:

* `deposit(amount)`
* `withdraw(amount)`
* `show_balance()`

Requirements:

* deposit should increase balance
* withdraw should reduce balance only if sufficient balance exists
* if balance is not enough, print `"Insufficient balance"`

Create one object and test all methods.

### Expected Concept

This is directly from the syllabus topic of **public/private data members**.  

---

### Q5. Built-in Class Attributes

Create a class `Student` with a docstring. Then print:

* `Student.__name__`
* `Student.__doc__`
* `Student.__module__`

Also print `Student.__dict__` in the end.

### Expected Concept

This matches the syllabus section on **built-in class attributes**.   

---

# Section C — Slightly Tougher Coding Question

## (1 × 25 = 25 Marks)

### Q6. Magic Methods / Operator Overloading

Create a class `Product` with:

* attributes: `name`, `price`

Implement the following magic methods:

* `__init__()`
* `__str__()`
* `__add__()` → should return sum of prices of two products
* `__eq__()` → should return `True` if both products have same price

Create three objects:

```python
p1 = Product("Laptop", 50000)
p2 = Product("Phone", 30000)
p3 = Product("Tablet", 50000)
```

Then print:

* `p1`
* `p1 + p2`
* `p1 == p3`
* `p1 == p2`

### Expected Concept

This is based directly on the question-bank pattern for **magic functions and operator overloading**.  

### Sample Output

```python
Product: Laptop, Price: 50000
80000
True
False
```

---