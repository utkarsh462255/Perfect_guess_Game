import random
randnum = random.randint(1, 100)
# print(randnum)
userguess = None
guesses = 0
while userguess != randnum:
    userguess = int(input("Enter your guess: "))
    guesses += 1

    if userguess == randnum:
        print("You guessed it right!")
    elif userguess >= randnum-5 and userguess < randnum:
        print("You are near to guess, please guess greater number")
    elif userguess < randnum:
        print("You guessed less than the number!")
    elif userguess <= randnum+5 and userguess > randnum:
        print("You are near to guess, please guess less number")
    elif userguess > randnum:
        print("You guessed greater than the number!")

print(f"You guessed the number in {guesses} guesses!")
