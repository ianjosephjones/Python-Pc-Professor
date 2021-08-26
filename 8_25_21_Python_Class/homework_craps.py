"""
Write a program that will run many games of craps. 
By many, I mean say 100 for testing and 1000000+ for evaluating the games

Record if a game is won or lost and how many roll it took to get there

Calculate the overall winning percentage for craps 
Do this as an overall number, as well as for each number of rolls that a game might have


Roll 1: 5 wins, 7 losses, nn percent won
Roll 2: 3 wins, 2 losses, nn percent won
Roll 3: 2 wins, 4 losses, nn percent won
Roll 4: 0 wins, 7 losses, nn percent won
....

Write your results to the screen and to a csv file that can be read by Excel
Number of rolls, wins losses
1,5,7
2,3,2
3,2,4
4,0,7
"""

from random import randint


def play_craps_game():
    point = randint(1, 6) + randint(1, 6)

    if point in (7, 11):
        print(f"You got {point}. You win!")
    elif point in (2, 3, 12):
        print(f"You got {point}. You lose!")
    else:
        print(f"The point is {point}")
        roll = 0
        while roll not in (point, 7):
            roll = randint(1, 6) + randint(1, 6)

            if roll == point:
                print(f"You got {roll}. You win")
            elif roll == 7:
                print(f"You got {roll}. You lose.")
            else:
                print(f"You got {roll}. Keep playing")


def play_multiple_craps_games():
    play_again = 'y'
    while not play_again.lower().startswith('n'):
        play_craps_game()
        play_again = input("Play again (y/n)? ")


play_multiple_craps_games()
