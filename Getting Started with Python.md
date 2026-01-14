# Chapter 1 — Getting Started with Python

## Step 1: Write your first program (Hello World)
1. Create a folder named `python_work`.
2. Create a file named `hello_world.py` inside `python_work`.
3. Write this code in the file:
```python
print("Hello Python world!")
```

## Step 2: Install Python 3

### Windows

1. Download Python 3 and run the installer.
2. Enable **Add Python to PATH** during installation.
3. Verify in Command Prompt:

```bat
python --version
```

If it doesn’t work:

```bat
py --version
```

### macOS

1. Open Terminal and verify:

```bash
python3 --version
```

### Linux

1. Open Terminal and verify:

```bash
python3 --version
```

---

## Step 3: Install VS Code

1. Download and install Visual Studio Code.
2. Open VS Code.

---

## Step 4: Set up VS Code for Python

1. Open VS Code → **Extensions**
2. Search **Python** (Microsoft) → Install
3. Open Command Palette:

   * Windows/Linux: `Ctrl+Shift+P`
   * macOS: `Cmd+Shift+P`
4. Run:

```text
Python: Select Interpreter
```

5. Select your Python 3 interpreter.

---

## Step 5: Run `hello_world.py` in VS Code

1. Open the folder `python_work` in VS Code (**File → Open Folder…**).
2. Open `hello_world.py`.
3. Run:

   * Click **Run Python File in Terminal**, or
   * Right-click → **Run Python File in Terminal**
4. Expected output:

```text
Hello Python world!
```

---

## Step 6: Run Python program from Terminal

### Linux / macOS

```bash
cd ~/Desktop/python_work
ls
python3 hello_world.py
```

### Windows

```bat
cd Desktop\python_work
dir
python hello_world.py
```

If needed:

```bat
py hello_world.py
```

---

## Step 7: Run Python in the interpreter (snippets)

### Start interpreter

* Linux/macOS:

```bash
python3
```

* Windows:

```bat
python
```

(or `py`)

### Try a snippet

```text
>>> print("Hello Python interpreter!")
Hello Python interpreter!
```

### Exit interpreter

* Linux/macOS: `Ctrl+D` or `exit()`
* Windows: `Ctrl+Z` then Enter, or `exit()`

---

## Step 8: Troubleshooting

* Recheck: `print`, quotes, parentheses.
* In VS Code: re-run `Python: Select Interpreter` and choose Python 3.
* Windows “python not recognized”: reinstall with **Add Python to PATH** or use `py`.
* * *