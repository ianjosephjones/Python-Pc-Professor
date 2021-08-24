import random

"""
Create a two six-sided dice that changes
every roll. If you get a 7 or 11 on the first 
roll you win! If you get a 2, 3, or 12
on the first roll then you lose.
Otherwise, what ever you roll becomes
your "point". You'll keep rolling the dice
until you roll either a 7 or your point.
If you roll a 7, you lose. If you roll 
your point, you win the game!!!

"""
import random


def main():
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2
    diceroll(dice1, dice2, total)


def diceroll(dice1, dice2, roll):

    if roll == 7 or roll == 10:
        print('You rolled', dice1, '+', dice2, '=', roll)
        print('Natural, You win!')
    elif roll == 2 or roll == 3 or roll == 12:
        print('You rolled', dice1, '+', dice2, '=', roll)
        print('Craps! You lose!')
    else:
        print('You rolled', dice1, '+', dice2, '=', roll)
        print('You scored', roll, 'points')
        mypoints = roll
        reroll(mypoints)


def reroll(points):

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    total = dice1 + dice2

    if total == points:
        print('You rolled', dice1, '+', dice2, '=', total)
        print('Congrats you win')
    elif total == 7:
        print('You rolled', dice1, '+', dice2, '=', total)
        print('Sorry you lose')


main()
