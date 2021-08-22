'''
# while loops

num = 0
while num < 5:
    print(num)
    num += 1

print('-'*10)

for num2 in range(5):
    print(num2)

print('num:', num)
print('num2:',num2)

# We want a program that keeps letting a person input their name and stops when they're done
# How about letting the user just hit the return key when they're done
inmsg = 'xxxx'
while inmsg != '':
    inmsg = input('Enter your name: ')
    if inmsg != '':
        print('Your name is ', inmsg)
    else:
        print("Bye bye")


keepgoing = True
while keepgoing:
    inmsg = input('Enter your name: ')
    if inmsg != '':
        print('Your name is ', inmsg)
    else:
        keepgoing = False



while True:
    inmsg = input('Enter your name: ')
    if inmsg != '':
        print('Your name is ', inmsg)
    else:
        break


num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue;
    print(num)
print("We're done")

# Write a hi-lo game
Think of a number between 1 and 20
>OK
What number am I thinking of?
>5
Nope, too low
>15
Nope, too high
>8
You got it

The computer picks thenumber, you have to guess it

Guess a number: 5
Too low
Guess a number: 15
Too high
Guess a anumber: 8
You got it


First step: Psudeocode
store a random number
while the stored random number is not equal to the input number
loop


Computer guesses the number
while guess != number
   User inputs guess
   if guess is low print that
   else if guess is hight print that
   else print it's good
















# Add a feature to print out your list of guesses, in order, when the game is over
# Also, don't crash if the user enters a non-number



import random
guesses = []
# Computer guesses the number
the_number = random.randint(1,20)
guess = 0
while guess != the_number:
    try:
        guess = int(input("Enter your guess: "))
        guesses.append(guess)
        if guess < the_number:
            print("Too low")
        elif guess > the_number:
            print("Too high")
        else:
            print("Got it")
    except:
        print("That guess was not valid")
        
print(f"Your guesses were {guesses}")
'''
