#Day_4
#conditonal statement, logical operators, code blocks and scope


#ROLLERCOSTER ELIGIBILITY CHECKER
print("Welcome to Roller_coaster!\n")
bill = 0
height = int(input("what is your height in cm? \n"))
if height >= 120:
    print("you can ride the Roller_coaster!")
    age = int(input("what is your age? "))
    if age < 12:
        bill = 5
        print(f"child's tickets are ${bill}\n")
    elif age <= 18:
        bill = 7
        print(f"youth's tickets are ${bill}\n ")
    photo = input("do you want a photo taken? \n please enter Y to represent yes or N to represent no \n")
    if photo == "Y" or "y":
        bill = bill + 3

        print(f"your final bill is ${bill}")
    else:
        print("sorry you have to grow taller before you can ride ")


