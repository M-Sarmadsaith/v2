#Write a program that checks if a number is positive or negative. If it is zero, print "Zero".
num=5
if num > 0:
    print(positive)
elif num < 0:
    print(negative)
else:
    print('zero')
#Input a number from the user and print whether it is even or odd.
num=6
if num%2==0:
    print("even")
else:
    print("odd")
#Ask the user to enter their age. If age is 18 or above, print "Eligible to vote" Else, print "Not eligible"
age=20
if age>=18:
    print("Eligible to vote")
else:
    print("not eligible")
#Enter a number and check whether it is divisible by: 3,5,BothPrint an appropriate message.
num=15
if num%3==0 and num%5==0:
    print('divisible by  both 3 and 5')
elif num % 3 == 0:
    print("Divisible by 3")
elif num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 3 or 5")
#**Ask for a student's marks and assign a grade:90+ → "A+"80+ → "A"70+ → "B"Otherwise → "Fail"**
num=95
if marks >= 90:
    print("Grade: A+")
elif marks >= 80:
    print("Grade: A")
elif marks >= 70:
    print("Grade: B")
else:
    print("Grade: Fail")
#**Take a temperature input:Above 40 → "Too hot"Below 10 → "Too cold"Otherwise → "Moderate weather"**
temperature=45
if temperature > 40:
    print("Too hot")
elif temperature < 10:
    print("Too cold")
else:
    print("Moderate weather")
#Ask the user to enter a year. Check whether it is a leap year or not.
year=2025
if year%5==0 and year%100==0:
    print("leap year")
else:
    print("not a leap year")
#input three numbers and print the largest number.
num1=64
num2=88
num3=98
if num1>=num2 and num1>=num3:
    print("the largest number is",num1)
 elif num2>=num1 and num2>=num3:
    print("the largest number is",num2)
 else:
    print("the largest number is",num3)
#Ask the user to enter a password.If password matches "admin123" → print "Access granted" Else → "Access denied"
password="Saith Muhammad Sarmad"
if password=="Saith Muhammad Sarmad":
    print("ccess granted")
else:
    print("access denied")
# **Take an integer input.If number > 0, check if it’s less than 100Print appropriate messages for both checks**
num=50
if num > 0:
    print("Number is positive")
    if num < 100:
        print("Number is less than 100")
    else:
        print("Number is 100 or more")
else:
    print("Number is not positive")
















