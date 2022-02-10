import random
print("Number Guessing Game")
number=random.randint(1,9)
print("Enter your guess: ")
chances=0

while chances < 5:
    guess=int(input("Enter your guess: "))

    if guess == number:
        print("Congratulations You WON!!")
        break
    elif guess < number:
        print("Your guess is too low")
    else:
        print("Your guess is too high")

    chances+=1
if not chances < 5:
    print("You lose, the number is",number)