import random

print("Number Guessing Game")
print("Guess a number (between 1 and 9)")

num = random.randint(1, 9)

chances = 0

while chances < 5:
    guessedNumber = int(input("Enter your guess: "))
    if guessedNumber == num:
        print("You Won!!")
        break

    elif guessedNumber < num:
        print("Your guess was too low! Please guess a little higher.")
    
    else:
        print("Your guess was too high! Please guess a little lower.")

    chances = chances + 1

if not chances < 5:
    print("Oh no! Your chances are over! You lose!")
