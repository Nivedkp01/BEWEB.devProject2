import random

a = int(input("Enter the lower limit: "))
b = int(input("Enter the upper limit: "))
num = random.randint(a, b)
guess = None

while guess != num:
    guess = int(input("Enter your guess: "))

    if guess > num:
        print("Your guess is larger than the actual number.")
    elif guess < num:
        print("Your guess is smaller than the actual number.")
    else:
        print("Congratulations! You guessed the correct number.")
