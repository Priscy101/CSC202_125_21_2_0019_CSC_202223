#DAY 2
#printing string members
print("Hello"[4])
#concatinating numbers
print("123" + "345")
#integers
print(123 + 345)

#data types
Two_digit_number = input("Enter two number: ")

First_digit = Two_digit_number[0]
Second_digit = Two_digit_number[1]

Result = int(First_digit) + int(Second_digit)
print(Result)

#BMI Calculator
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
BMI = float(weight) / float(height) ** 2
BMI_as_int = int(BMI)
print(BMI_as_int)

#LIFE IN WEEKS (exercise 2.3)
Age = input("What is your current age? ")
Age_as_int = int(Age)
years_remaining = 90 - Age_as_int
Days_remaining = years_remaining * 365
Weeks_remaining =  years_remaining * 52
Month_remaining = years_remaining * 12

Message = f"you have {Days_remaining}days, {Weeks_remaining}weeks, {Month_remaining}month"
print(Message)

#Tip calculator (project day 2)
print("welcome to tip calculator!")
Bill = float(input("What is the total bill? $"))
Tip = int(input("How much tip would you like to give? 5, 10, or 15?"))
People = int(input("How many people would split the bills? "))
Bill_with_tip = Tip / 100 * Bill + Bill
print(Bill_with_tip)
