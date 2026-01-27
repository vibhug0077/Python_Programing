# Getting Started with Python

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
* * *
* * *

# Make an account on GitHub

1. Open **github.com**
2. Click **Sign up**
3. Enter: **email → password → username**
4. Verify your email (GitHub will send a verification mail)
5. After login, keep your **username** noted (you’ll use it later in VS Code)

---

## 2) Create a repo for “Python Programming”

1. In GitHub (top-right), click **+** → **New repository**
2. Fill:

   * **Repository name:** `python-programming` (or `Python-Programming`)
   * **Description (optional):** “Python Programming practice and notes”
   * Choose **Public** (or **Private**)
3. Tick:

   * ✅ **Add a README file**
   * (Optional) ✅ **Add .gitignore** → choose **Python**
4. Click **Create repository**

---

## 3) Download GitHub Desktop

1. Open **desktop.github.com**
2. Download and install **GitHub Desktop**
3. Open GitHub Desktop → **Sign in to GitHub.com**
4. Complete the browser login/authorization, then return to GitHub Desktop

---

## 4) Link VS Code to GitHub using web authorization

1. Open **VS Code**
2. Press **Ctrl + Shift + P**
3. Type and select: **GitHub: Sign in**
4. Choose **Sign in with browser**
5. Your browser opens GitHub → click **Authorize** (approve VS Code access)
6. After success, VS Code will show you are signed in (Accounts icon/profile in the bottom-left or top-right depending on layout)

That’s it—your GitHub account is now connected to VS Code via web authorization, and your “Python Programming” repo is ready to use.
