
from random import randint

LOSS = 0
WIN = 1


def dummy_craps():
    lose_or_win = randint(0, 1)
    number_of_rolls = randint(1, 10)
    print(f"Craps! You {lose_or_win} in {number_of_rolls} rolls")
    if lose_or_win == LOSS:
        results[number_of_rolls][LOSS] += 1
    else:
        results[number_of_rolls][WIN] += 1


# Initialize the results list
results = []
for roll in range(11):
    results.append([0, 0])

number_of_games = 100
for gameno in range(number_of_games):
    dummy_craps()
for num_rolls in range(1, len(results)):
    print(
        f"You won {results[num_rolls][WIN]} times and lost {results[num_rolls][LOSS]} times in {num_rolls} rolls")
print(results)
