correct = False

while (not correct):
    guess = int(input("Guess a number between 1 and 100.\n"))

    if guess < 1 or guess > 100: # Prevent guesses out of bounds
        print("Guess is out of range!")
        continue

    if guess == 42: # Correct guess
        print("Correct")
        correct = True

    if guess != 42: # Incorrect guess
        print("Incorrect")

