guess = 0
tries = 0

while guess != 6 and tries != 6:
    guess = int(input("Guess the number:  "))
    tries += 1


if tries == 6 and guess != 6:
    print("Sorry you're all out of attempts.")
elif tries <= 6 and guess == 6:
    print("You got it!")