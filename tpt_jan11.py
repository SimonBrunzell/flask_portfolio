# simon and leah working together
import random

def guessing_game():
    user_range_min = input("lower bound: ")
    while not user_range_min.isdigit():
        user_range_min = input("Please provide a number for lower bound:")

    user_range_max = input("upper bound: ")
    while not user_range_max.isdigit():
        user_range_max = input("Please provide a number for upper bound:")

    while user_range_min > user_range_max:
        user_range_max = input("Please provide a higher number for upper bound: ")

    guess = input("your guess is: ")

    while not guess.isdigit():
        guess = input("please provide a number for guess")

    user_range_min = int(user_range_min)
    user_range_max = int(user_range_max)
    guess = int(guess)
    randomized = random.randint(user_range_min, user_range_max)

    if (guess < user_range_min) | (guess > user_range_max):
        guess = input("please provide a guess within the range: ")

    if (randomized == guess):
        print("good job! you got it right")
    else:
        print("the number was: ", randomized)
        replay = input("no luck, do you wanna try again? y/n ")

    if replay == "y":
        guessing_game()


guessing_game()



