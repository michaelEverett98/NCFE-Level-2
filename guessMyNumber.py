# ==================================================
#               Guess my number game
#          NCFE Level 2 certificate homework
#                 Michael Everett
# ==================================================

import random as rd

#numOfGuess = 1
#userGuessInput = 0
#randomNumber = rd.randint(1, 99)

welcomeMessage = "Welcome to my random number guessing game! Please guess a number between 1 and 99 to begin. You get 5 guesses in total! Good luck."

print(f"{welcomeMessage}\n{40 * '='}")

def guessingGame() :

    userGuessInput = int(input("Please guess a number between 1 and 99. "))
    numOfGuess = 1
    randomNumber = rd.randint(1, 99)

    while userGuessInput != randomNumber :
            
        #print(randomNumber)
        #print(userGuessInput)
        playAgain = ()

        if numOfGuess == 5 :
            print(f"{40 * '-'}\nUnlucky! You were unable to guess the number this time, which was {randomNumber}. Better luck next time!")
            
            playAgain = input(f"{40 * '-'}\nWould you like to try again? y/n: ")

            if playAgain == "y" :
                guessingGame()

            elif playAgain == "n" :
                print("Ok! Thank you for playing.")
                break

            else :
                playAgain = input("Invalid input, please enter y or n: ")

        elif numOfGuess <= 5 and userGuessInput < randomNumber :
            
            numOfGuess += 1
            userGuessInput = int(input(f"{40 * '-'}\nNot quite! Your guess is too small. Try again! You have {6 - numOfGuess} guesses remaining. "))

        elif numOfGuess <= 5 and userGuessInput > randomNumber :
            
            numOfGuess += 1
            userGuessInput = int(input(f"{40 * '-'}\nNot quite! Your guess is too big. Try again! You have {6 - numOfGuess} guesses remaining. "))

    else :

        playAgain = input(f"{40 * '-'}\nWow! You were able to guess the number {randomNumber} in {numOfGuess} attempts! Nice going. Play again? y/n: ")

        if playAgain == "y" :
            guessingGame()

        elif playAgain == "n" :
            print("Ok! Thank you for playing.")

        else :
            playAgain = input("Invalid input, please enter y or n: ")

guessingGame()