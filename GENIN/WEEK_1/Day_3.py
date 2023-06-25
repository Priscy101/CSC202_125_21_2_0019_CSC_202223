
#Day 3
#conditional statement, logical operation, code block and scope
#exercise
#exercise_3.1

number = int(input("which number do you want to check? "))

mod = number % 2
if mod >=1:
    print("this number  is odd.")
else:
    print("this number is even!")

#exercise_3.2

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight / height ** 2)
if BMI < 18.5:
    print(f"your BMI is {BMI}, you're underweight. ")
elif BMI < 25:
    print(f"your BMI is {BMI}, you have a normal weight")
elif BMI < 30:
    print(f"your BMI is {BMI}, you are overweight")
elif BMI < 35:
    print(f"your BMI is {BMI}, you are obese ")
else:
    print(f"your BMI is {BMI}, you are clinically obese. ")

#exercise_3.3
year = int(input("which year do you want to know? \n"))
if year % 4 == 0:
    print("It is a leap year")
else:
    print("It is not a leap year")



#exercise_3.4
#pizza delivery
print("Welcome to Python Pizza Deliveries")
size = input("what size of pizza do you want? S, M, OR L ")
add_pepperoni= input("Do you want tomatoes? Y or N ")
more_cheese = input("Do you want more cheese? Y or N ")

bill = 0

if size == "5":
    bill += 15
elif size == "M":
    bill +=20
else:
    bill += 25

if add_pepperoni == "Y":
    if size == "5":
        bill += 2
    else:
        bill +=3
if more_cheese == "Y":

    print(f"your final bill is: ${bill}")


#exercise_3.5
#love calculator

print("Welcome to the love calculator")
name_1 = input("what is your name? \n")
name_2 = input("what is their name? \n")

combined_names = name_1 + name_2
lower_names = combined_names. lower()
t = lower_names.count("t")
r = lower_names. count("r")
u = lower_names.count("u")
e = lower_names.count("e")
first_digit = t + r + u + e

l = lower_names.count("l")
o = lower_names.count("o")
v = lower_names.count("v")
e = lower_names.count("e")
second_digit = l + o + v + e

score = int(str(first_digit) + str(second_digit))

if (score < 10) or (score > 90):
    print(f"your score is {score}, you go together like coke and mentos. ")
elif ( score >= 40) and (score <= 50):
    print(f"your score is {score}, you are alright together, ")
else:
    print(f"your score is {score}. ")