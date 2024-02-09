correct = False

while (not correct):
    guess = input("Guess a number between 1 and 100.\n")

    if not guess.isnumeric(): # Prevent guesses which are not numbers
        print("Please guess a number!")
        continue

    guess = int(guess)
    if guess < 1 or guess > 100: # Prevent guesses out of bounds
        print("Guess is out of range!")
        continue

    if guess == 42: # Correct guess
        print("Correct")
        correct = True

    if guess != 42: # Incorrect guess
        print("Incorrect")

