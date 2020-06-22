# Dice Guess Game

from random import randint # Needed to generate Random Numbers

print("Welcome to the DiceGame!")

quit = "a"          # Initialize Quit variable & Highscore Dictionary
highscore = {}

while quit != "Quit":

    i = 1 # To play 3 rounds
    score = 0 # Reset Score after each round

    name = input("What's your Name?")

    while i <= 3:

        guess = input("What's your guess? 1, 2 or 3?")
        rand = randint(1, 3) # Generates Random Number 1, 2 or 3
        guess = int(guess) # Needed Conversion to Integer so that if statement work

        if ( guess == rand ):
            score += 1
            print("Right!")
        else:
            print(f"False, Dice shows: {rand}")

        i+=1

    highscore[name] = score # Saves the player's score.
    
    print("GAME OVER")
    print("Highscores:")

    sort = sorted(highscore.items(), key=lambda x: x[1], reverse=True) # Sorts the highscore values decending by value(, not by key!)
    for i in sort:
        print(i[0], i[1])
        
    quit = input("Wanna Quit the Game? Type Quit!")
