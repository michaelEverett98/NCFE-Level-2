# ==================================================
#               Guess my number game
#          NCFE Level 2 certificate homework
#                 Michael Everett
# ==================================================

import random as rd

welcomeMessage = "Welcome to my random number guessing game! Please guess a number between 1 and 99 to begin. You get 10 guesses in total! Good luck."

print(f"{welcomeMessage}\n{40 * '='}")

def guessingGame() :

    userGuessInput = int(input("Please guess a number between 1 and 99. "))
    numOfGuess = 1
    randomNumber = rd.randint(1, 99)

    while userGuessInput != randomNumber :
            
        playAgain = ()

        if numOfGuess == 10 :
            print(f"{40 * '-'}\nUnlucky! You were unable to guess the number this time, which was {randomNumber}. Better luck next time!")
            
            playAgain = input(f"{40 * '-'}\nWould you like to try again? y/n: ")

            if playAgain == "y" :
                guessingGame()

            elif playAgain == "n" :
                print("Ok! Thank you for playing.")
                break

            else :
                playAgain = input("Invalid input, please enter y or n: ")

        elif numOfGuess <= 10 and userGuessInput < randomNumber :
            
            numOfGuess += 1
            userGuessInput = int(input(f"{40 * '-'}\nNot quite! Your guess is too small. Try again! You have {11 - numOfGuess} guesses remaining. "))

        elif numOfGuess <= 10 and userGuessInput > randomNumber :
            
            numOfGuess += 1
            userGuessInput = int(input(f"{40 * '-'}\nNot quite! Your guess is too big. Try again! You have {11 - numOfGuess} guesses remaining. "))

    else :

        playAgain = input(f"{40 * '-'}\nWow! You were able to guess the number {randomNumber} in {numOfGuess} attempts! Nice going. Play again? y/n: ")

        if playAgain == "y" :
            guessingGame()

        elif playAgain == "n" :
            print("Ok! Thank you for playing.")

        else :
            playAgain = input("Invalid input, please enter y or n: ")

guessingGame()