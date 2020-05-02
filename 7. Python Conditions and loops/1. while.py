secret = 22
guess = 0

while guess != secret:
    guess = int(input("guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You guessed it - congratulations ! It's number " + str(secret) + ".")
    else:
        print("Sorry, your guess is not correct... the secret number is not " + str(guess))
