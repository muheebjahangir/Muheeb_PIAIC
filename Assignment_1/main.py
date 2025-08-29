# 📝 Python Assignment – 01
# Topics: Variables, Data Types & Operators

# ---------------------------
# Q1: Variables & Data Types
# ---------------------------

# Creating variables
name = "Muheeb Ahmed"     # Full name
age = 18                  # Age
is_student = True         # Boolean value

# Printing all variables in one line
print(name, age, is_student)

# Printing the data type of each variable
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of is_student:", type(is_student))


# ---------------------------
# Q2: Arithmetic Operators
# ---------------------------

x = 20
y = 6

print("Addition:", x + y)
print("Subtraction:", x - y)
print("Multiplication:", x * y)
print("Division:", x / y)
print("Floor Division:", x // y)
print("Modulus:", x % y)
print("Exponent:", x ** y)


# ---------------------------
# Q3: Assignment Operators
# ---------------------------

num = 10
num += 5   # Add 5
num *= 2   # Multiply by 2
num -= 4   # Subtract 4
print("Final value of num:", num)


# ---------------------------
# Q4: Comparison Operators
# ---------------------------

a = 15
b = 12

print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)


# ---------------------------
# Q5: Logical Operators
# ---------------------------

p = True
q = False

print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)
print("not q:", not q)


# ---------------------------
# Q6: Real-Life Example
# ---------------------------

notebook_price = 80
quantity = 7
total_price = notebook_price * quantity
money = 600

print("Total price of 7 notebooks:", total_price)

if money >= total_price:
    print("Yes, you have enough money to buy the notebooks.")
else:
    print("No, you don’t have enough money to buy the notebooks.")


# ---------------------------
# Q7: Bonus (Optional)
# ---------------------------

# Taking input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

# Printing their sum
print("Sum:", num1 + num2)

# Checking comparison
if num1 > num2:
    print("The first number is greater than the second number.")
else:
    print("The first number is not greater than the second number.")
