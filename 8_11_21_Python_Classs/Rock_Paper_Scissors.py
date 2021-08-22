
import random
1
2
3
4
5
6
7
8
9
10
11
12
13
14
15
16
17
18
19
20
21
22
23
24
25
26
27
28
29
30
31
32
33
34
35
36
""" Rock Paper Scissors
------------------------
"""

while (True):
    print("\nRock, Paper, Scissors - Shoot!")

    userChoice = input(
        "Choose your weapon [R]ock], [P]aper, or [S]cissors or [Q} to quit]: ")
    userChoice = userChoice.upper()
    if userChoice == "Q":
        exit()
    elif (userChoice != "R" and userChoice != "P" and userChoice != "S"):
        print("Please choose a letter:")
        print("[R]ock, [S]cissors or [P]aper.")
        continue

    # Echo the user's choice
    print("You chose: " + userChoice)

    choices = ['R', 'P', 'S']
    opponenetChoice = random.choice(choices)
    print("I chose: " + opponenetChoice)
    if opponenetChoice == str.upper(userChoice):
        print("Tie! ")
    elif opponenetChoice == 'R' and userChoice.upper() == 'S':
        print("Scissors beats rock, I win! ")
        continue
    elif opponenetChoice == 'S' and userChoice.upper() == 'P':
        print("Scissors beats paper! I win! ")
        continue
    elif opponenetChoice == 'P' and userChoice.upper() == 'R':
        print("Paper beat rock, I win! ")
        continue
    else:
        print("You win!")
