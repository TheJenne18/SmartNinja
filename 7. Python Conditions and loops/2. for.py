secret = 22

for x in range(5):
    guess = int(input("guess the secret number (between 1 and 30): "))

    if guess == secret:
        print("You guessed it - congratulations ! It's number " + str(secret) + ".")
        break
    else:
        print("Sorry, your guess is not correct... the secret number is not " + str(guess))
