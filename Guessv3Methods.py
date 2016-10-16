import time

def guessCheck(guess, number):
    if guess>number:
        print("Too Big!")
    if guess<number:
        print("Too Small!")

def roundSummary(guesses, limit, rounds, totalGuesses, score):
    print("Guesses:",guesses,"\n+",limit*10-guesses,"Points")
    if limit!=rounds:
        print("\nTotal guesses so far:",totalGuesses,"\nScore so far:",score)
    time.sleep(1)
