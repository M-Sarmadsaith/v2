#Create two variables a = 10 and b = 3.
#Perform and print: addition (+), subtraction (−), multiplication (×), division (/), modulus (%), exponentiation (), and floor division (//).**
a=10
b=3
print("addition",a + b)
print("subtraction",a - b)
print("multiplication",a * b)
print("division",a / b )
print("Modulus:", a % b)
print("Exponentiation:", a ** b)
print("Floor Division:", a // b)
#Compare a and b using comparison operators: ==, !=, >, <, >=, <=
#Print the result of each comparison.
a=10
b=3
print("a==b:",a == b)
print("a!=b:",a != b)
print("a>b:",a > b)
print("a<b:",a < b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)
#Create two boolean variables: x = True, y = False.
#Perform and print results of: x and y, x or y, and not x.
x = True 
y = False
print("x and y:", x and y)
print("x or y:", x or y)
print("not x:", not x)
#Create num = 5 and perform assignment operations: +=, -=, =, /=, %=, *=, //=
#Print the result after each operation.
num = 5
num += 2
print("After += 2:", num)
num -= 1
print("After -= 1:", num)
num = 10
print("After = 10:", num)
num /= 2
print("After /= 2:", num)
num %= 3
print("After %= 3:", num)
num *= 4
print("After *= 4:", num)
num //= 2
print("After //= 2:", num)
#Create m = 100, n = 100.
#Check if they are the same object using is and is not, and print the result.
m = 100
n = 100
print("m is n:", m is n)
print("m is not n:", m is not n)
#Create a string text = "Python Programming".Check if "Python" is in text and if "Java" is not in text.
text = "Python Programming"

print('"Python" in text:', "Python" in text)
print('"Java" not in text:', "Java" not in text)
# Write a Python program to print all keywords using the keyword module.
import keyword
print("Python Keywords:")
print(keyword.kwlist)
#Declare: name = "Ali", age = 20, height = 5.9.Print their values and data types using the type() function.
name = "Ali"
age = 20
height = 5.9
print(name)
print(type(name))
print(age)
print(type(age))
print(height)
print(type(height))
#Write 5 valid variable names (e.g., user_name, x1, _value, TotalAmount, data123)
#Also write 3 invalid ones (as comments): 1name, user-name, class
#Explain why invalid names are not allowed.
#5valid variable names:
user_name="Muhammad Sarmad"
x1=52
_value=3.14
total_amount=600
data123=[1,2,3]
#3invalid variable name:
 #name→ Invalid: Variable names cannot start with a digit.
 #user-name → Invalid: Hyphens are not allowed; use underscores (_) instead. 
#class     → Invalid: 'class' is a reserved keyword in Python.
#Create special-naming variables: _hidden = 5, __private = 10, MAX_SIZE = 100
#Print their values.
_hidden=5
_private=10
max_size=100
print(_hidden)
print(_private)
print(max_size)
#Assign values in one line: x = 1, y = 2, z = 3
#Print them.
x, y, z = 1, 2, 3
print("x=",x)
print("y=",y)
print("z=",z)
#assign same value0 to a,b,c in one line.Print them.
a=b=c=0
print("a =",a)
print("b =", b)
print("c =", c)
#Create temp = 100, print it, delete it using del, then try to print again and observe the error.
temp = 100
print("temp =", temp)
del temp
print(temp) 
#Create a string using triple single quotes: '''Hello'''Print it.
msg='''hello'''
print(msg)
#**Create a multi-line string using triple double quotes"""This is line one.\nThis is line two."""Print it.**
text = """This is line one.\nThis is line two."""
print(text)
#**Use type() to check and print the data types of:An integerA floatA stringA boolean**
num_int = 10
num_float = 3.14
text = "Hello"
flag = True
print(type(num_int))
print(type(num_float))
print(type(text))
print(type(flag))
#Create score = 85 Check: score > 50 and score < 100 Print the result.
score = 85
result = score > 50 and score < 100
print("Is score between 50 and 100?", result)
# Create message = "Welcome to Python" Use in and not in to check for the word "Python" Print the result.
message = "Welcome to Python"
contains_python = "Python" in message
not_contains_python = "Python" not in message
print("Does the message contain 'Python'? ->", contains_python)
print("Does the message NOT contain 'Python'? ->", not_contains_python)
#Write a code block using only comments that explains what your program does.
Assign values to variables
Perform arithmetic operations (addition, subtraction, etc.)
Check conditions using logical operators
Use membership operators to search within a string
Print all results to the console
# Create data = 123Use id(data) to print its memory address.
data = 123
print("Memory address of data:", id(data))






