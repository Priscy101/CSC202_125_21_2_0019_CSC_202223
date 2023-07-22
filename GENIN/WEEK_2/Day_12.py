#Day_12
#number_guessing_game


import random

print("welcome to the number guessing game ")
print("I'm thinking of a number between 1 and 100 ")
difficulty = input("choose a difficult. Type 'easy' or 'hard' ").lower()
number = random.randint(1, 100)

#print(number)
chances = 0
times_run = True
if difficulty == "easy":
    chances = 0
elif difficulty == "hard":
    chances = 5

    # while times_run:
    def check():
        global times_run
        while times_run:
            user_choice = int(input("make a guess: "))
            global chances
            if user_choice < number:
                print("too low")
                chances -= 1
                print(f"you have{chances} attempts remaining")

            elif user_choice > number:
                print("too high")
                chances -= 1
                print(f"you have {chances} attempts remainimg")
            if user_choice == number:
                # times_run = False
                print(f"you won. The answer was {user_choice}")
                times_run = False
            if chances == 0:
                times_run = False

                # for i in range(chances)
        check()



