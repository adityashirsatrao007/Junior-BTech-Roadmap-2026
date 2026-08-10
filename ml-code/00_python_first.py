"""
00 — PYTHON FIRST: run this and watch it explain itself.
Run:  python ml-code/00_python_first.py
This is literally your first program. Read each line, then edit and run again.
No installs needed — plain Python, matches 01_PYTHON_FROM_ZERO.md.
"""

# 1. print  — show things on screen
print("HELLO! You just ran your first program.")

# 2. variables  — boxes that hold values
name = "riya"
age = 20
print("Name:", name, "| Age:", age)

# 3. types
print("types ->", type(20), type("hi"), type(2.5), type(True))

# 4. if / else
score = 75
if score >= 60:
    print("PASS")
else:
    print("FAIL")

# 5. loops
print("counting 0..4:")
for i in range(5):
    print(" step", i)

# 6. lists
subjects = ["math", "dsa", "physics"]
subjects.append("ml")
for s in subjects:
    print(" subject:", s)

# 7. dictionaries
student = {"name": name, "age": age, "branch": "AI&DS"}
for key in student:
    print(" key:", key, "=", student[key])

# 8. functions
def area(length, width):
    return length * width
print("area(5,3) =", area(5, 3))

# 9. your turn: change this, then run again.
city = "your city here"
print("My city is:", city)

print("\nDone writing-part 1. Open 01_PYTHON_FROM_ZERO.md and do the 5-day ramp.")