#Create a variable greeting and store a message. Print it.
greeting = "hello world"
print(greeting)
#2. Change the value of greeting and print the new message.
greeting = "we are learning python"
print(greeting)
#3.Create first_name and last_name, then print full name using f-string.
first_name = "Khalid"
last_name = "Mehmood"
full_name = f"{first_name}-{last_name}"
print(full_name)
#4.Print a famous quote with author’s name using f-string.
quote = "the only limit to our realization of tomorrow will be our doubts of today"
author = "Franklin D. Roosevelt"
print(f"{quote} - {author}")
#5.Store a name with extra spaces, strip them, and print clean output.
name = " Khalid Mehmood "
clean_name = name.strip()
print(f"clean_name: {clean_name}")
#Take a number, add 5, multiply by 2, subtract 3, and print the result.
number = "2"
result = int(number) + 5 * 2 - 3
print(result)
#Create a and b; print their sum, difference, product, and quotient.
a = 6
b = 3
print(a + b)
print(a - b)
print(a * b)
print(a / b)
#Find square and cube of a number using ** operator.
number = 12
print(number ** 2)
print(number ** 3)
#
#Add three floating-point numbers and print the total.
num1 = 2.5
num2 = 3.7
num3 = 4.4
total = num1 + num2 + num3
print(total)
#Assign x, y, z in one line and print them.
x,y,z = 1,2,3
print(x,y,z)
#Create a list of 5 favorite fruits and print each one separately.
list = ["cherry","stawbery","orange","apple","mango"]
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(list[4])
#Modify the 2nd item in the list and print the updated list.
list = ["cherry","stawbery","orange","apple","mango"]
print(list[2])
#Append a new fruit and insert one at the beginning.
fruit = ["cherry","stawbery","orange","apple","mango"]
fruit.append("banana")
for fruit in fruit:
 print(fruit)
 #Delete items using del, pop(), and remove().
 fruits = ["apple","banana","cherry","orange","stawbery"]
del fruits[0]
print(fruits)
#
#delete using pop()
fruits = ["apple","banana","cherry","orange","stawbery"]
fruits.pop(1)
print(fruits)
#
#delete using remove()
fruits = ["apple","banana","cherry","orange","stawbery"]
fruits.remove("cherry")
print(fruits)
#Use sort() and sorted() to sort the list. Show before and after.
numbers = [5, 2, 9, 1, 5, 6]
print("Before sorting with sort():", numbers)
print("After sorting with sort():", numbers)
#Create a list of dream travel destinations:
#- Sort alphabetically
#- Reverse the order
#-Count total destinations
destinations = ["Japan", "Iceland", "New Zealand", "Italy", "Canada", "Norway", "Greece"]
print("Alphabetically sorted:", destinations)
print("Reversed order:", destinations)
total = len(destinations)
print("Total number of destinations:", total)
#17. Start with an empty guest list:
# - Append 3 guests
#- Insert 1 at the beginning
#- Remove one using pop()
#-Print final list
guest_list = []
guest_list.append("Alice")
guest_list.append("Bob")
guest_list.append("Charlie")
guest_list.insert(0, "Diana")
removed_guest = guest_list.pop()
print("Final guest list:", guest_list)
print("Removed guest:", removed_guest)
#Access the last 3 elements of a list without negative indexing.
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
last_three = my_list[-3:]
print(last_three)
#From a list of numbers, print only even numbers.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("even numers:")
for number in numbers:
    if number % 2 == 0:
        print(number)
#Print squares of the first 10 natural numbers in a list.
squares = []
for num in range(1, 11):
    squares.append(num ** 2)
print("Squares of first 10 natural numbers:", squares)
