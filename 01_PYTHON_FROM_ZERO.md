# 01 — Python from absolute zero (no prior coding needed)

You have never written code. That is completely fine — every famous engineer started
here. This page turns a total beginner into someone who can read and write small
Python programs. **Do it in Week 1 before anything else.**

**How to use it:** read one section → run the matching lines in `ml-code/00_python_first.py` → then try the "TRY IT" box. Don't rush. 60 min a day, ~5 days.

---

## 1. What even is code?

A computer only understands machine instructions. Programming = writing plain-English-ish
**instructions** (in a language like Python) and using a **translator** to turn them
into machine actions.

- Your **code** = a normal text file, e.g. `hello.py`.
- You **run** it: `python hello.py` in the terminal — the computer executes your lines top to bottom.
- **Printing** shows output on the screen. `print("hello")` is the first thing everyone writes.

> Don't worry why yet. Just know: code is text, print shows it.

## 2. Variables — labelled boxes

A variable stores a value under a name. `name = "riya"` puts the text "riya" into a box called `name`.

```python
age = 20                # number
name = "riya"           # text (called a *string*)
marks = 87.5            # decimal number
print(name, age, marks)  # riya 20 87.5
```

**TRY IT:** make a box `city` with your city name, print it.

## 3. Data types — the kinds of values

- `int` — whole numbers: `3, -2, 100`
- `float` — decimals: `3.5, 99.9`
- `str` — text in quotes: `"hello", 'hi'`
- `bool` — `True` or `False` (notice capital letters!)

```python
print(type(20), type("hi"), type(2.5), type(True))
# <class 'int'> <class 'str'> <class 'float'> <class 'bool'>
```

**TRY IT:** print the type of your favourite number.

## 4. if / else — the computer decides

Compare values and pick a branch:

```python
score = 75
if score >= 60:
    print("pass")
else:
    print("fail")
```

Indentation (the 4 spaces) is REQUIRED — it tells Python what belongs to the `if`.
Comparison operators: `==` (equal), `!=` (not equal), `>`, `<`, `>=`, `<=`.

**TRY IT:** if your age is 18 or more, print "adult", else "minor".

## 5. Loops — repeat without copy-pasting

- **`for`** counts over things. `range(5)` gives `0,1,2,3,4`:

```python
for i in range(5):
    print("step", i)     # prints step 0 .. step 4
```

- **`while`** repeats *while a condition is true*:

```python
n = 3
while n > 0:
    print(n)
    n = n - 1            # careful: change n or the loop never ends
```

**TRY IT:** print the numbers 1 to 10 using a `for` loop.

## 6. Lists — one box holding many things

```python
subjects = ["math", "dsa", "physics"]
print(subjects[0])       # math  (indexing starts at 0!)
print(len(subjects))     # 3
subjects.append("ml")    # add to the end
for s in subjects:
    print(s)             # prints every item
```

**TRY IT:** make a list of 3 friends, print the first, add one more, print all.

## 7. Dictionaries — labels → values (like a real dictionary)

```python
student = {"name": "riya", "age": 20, "branch": "AI&DS"}
print(student["branch"])     # AI&DS
student["cgpa"] = 8.6        # add a new key
for key in student:
    print(key, "=", student[key])
```

**TRY IT:** make a dict for yourself (name, age, city) and print your age.

## 8. Functions — reusable blocks with a name

```python
def area(length, width):
    return length * width

print(area(5, 3))       # 15
print(area(10, 2))      # 20
```

`return` hands the result back. Functions stop you from repeating code.

**TRY IT:** write `def is_even(n)` that returns `True` if `n` is even (`n % 2 == 0`).

## 9. Input — let the user talk to the program

```python
name = input("What is your name? ")
print("Hello", name)
```

**TRY IT:** ask the user their marks and print "pass" or "fail" using `if`.

---

## 10. Your 5-day routine (Week 1, replaces DSA for now)

| Day | Sections | Do |
|-----|----------|----|
| 1 | 1–3 | run `ml-code/00_python_first.py`; fix any error (error = learning) |
| 2 | 4 | solve the if TRY IT boxes |
| 3 | 5 | solve the loops TRY IT boxes |
| 4 | 6–7 | solve lists + dicts TRY IT boxes |
| 5 | 8–9 | write `is_even` + the pass/fail program from scratch, save as your own `.py` |

**Finish line:** you can open VS Code, write a `.py` file, run it, and fix a simple
syntax error by reading the error message. That's ~95% of what beginners ever fear.
After Day 5, start **LeetCode Day 1** (`03_LEETCODE_150.md`).

> Error messages are not attacks — they literally point at the line to fix. Read them aloud; you'll be surprised how often the fix is obvious.