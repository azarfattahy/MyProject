print("Hello World")

print("Hello, I'm Alex!")

# 3. Multiple lines
print("Python")
print("Day 1")
print("Let's goooo!")

# 5. Empty line + separator
print("─" * 40)
print("   My first Python day!   ")
print("─" * 40)

name = "Sarah"          # string (text)
age = 24                # integer (whole number)
height = 1.68           # float (decimal number)
loves_python = True     # boolean (True/False)


print(name)
print(age)
print("Height:", height, "meters")
print("Loves Python?", loves_python)

# You can change them anytime
age = age + 1           # birthday!
print("Tomorrow I will be", age)

print(type(42))          # <class 'int'>
print(type(3.14))        # <class 'float'>
print(type("hello"))     # <class 'str'>
print(type(True))        # <class 'bool'>

# Explicit type conversion (casting)
age = "25"              # comes from input() usually
age_number = int(age)   # → 25 (integer)
height = float("1.78")  # → 1.78

# Arithmetic Operators
a = 10
b = 3

print(a + b)   # 13    addition
print(a - b)   # 7     subtraction
print(a * b)   # 30    multiplication
print(a / b)   # 3.333…  true division (always float)
print(a // b)  # 3     floor division (integer result)
print(a % b)   # 1     modulo (remainder)
print(a ** b)  # 1000  exponentiation

# String Operations
first = "Hello"
second = "World"

print(first + " " + second)         # concatenation
print(first * 3)                    # "HelloHelloHello"
print(len("Python"))                # 6
print("python".upper())             # "PYTHON"
print("PYTHON".lower())             # "python"
print("  hello world  ".strip())    # "hello world"

# Handy string formatting (modern & recommended)
name = "Emma"
age = 28
height = 1.72

# f-string (best option since Python 3.6+)
print(f"My name is {name}, I'm {age} years old and {height}m tall.")

# Alternative (still very common)
print("My name is {}, I'm {} years old.".format(name, age))

name = input("Please enter your name: ")
print(f"My name is {name}")
print("My name is {}".format(name))