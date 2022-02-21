# higher or lower game project
# who has more followers on instagram
from random import random, choice
import game_data
# from game_data import data

data = game_data.data

side_a = choice(data)
side_b = choice(data)
score = 0

def check_equality(side_a, side_b):
    """checks if the two sides have similar data and if they have it regenerates data for one side"""
    if side_a == side_b:
        side_b = choice(data)

check_equality(side_a=side_a, side_b=side_b)
game_playing = True
while game_playing:
    print(f'Compare A: {side_a["name"]}, a {side_a["description"]} from {side_a["country"]}\nAgainst B: {side_b["name"]} a {side_b["description"]} from {side_b["country"]}')

    answer = input("who has more followers? type 'a' or 'b': ").lower()

    if answer == 'a' and side_a["follower_count"] > side_b["follower_count"]:
        score += 1
        print(f"correct, current score {score}")
        side_b = choice(data)
        check_equality(side_a=side_a, side_b=side_b)
    elif answer == 'b' and side_b["follower_count"] > side_a["follower_count"]:
        print(f"correct, current score {score}")
        score += 1
        side_temp = side_a
        side_a = side_b
        side_b = choice(data)
        check_equality(side_a=side_a, side_b=side_b)
    else:
        print("You lost")
        print(f"Your final score is {score}")
        game_playing = False
