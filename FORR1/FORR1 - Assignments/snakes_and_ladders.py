import random
random.seed(1337)

def start_game():
    number_of_snakes_or_ladders = int(input())

    snakes = []
    snake_locations = []
    ladders = []
    ladder_locations = []

    for i in range(number_of_snakes_or_ladders):
        a, b = input().split()
        a = int(a)
        b = int(b)

        if a > b:
            snakes.append(a)
            snake_locations.append(b)
        else:
            ladders.append(a)
            ladder_locations.append(b)
    
    snakes_and_ladders = [snakes, snake_locations, ladders, ladder_locations]
    return snakes_and_ladders


def roll_dice():
    dice = random.randint(1,6)
    return dice

def check_snake_or_ladder(space, player):
    new_location = space
    if space in snakes:
        new_location = snake_locations[snakes.index(space)]
        if new_location < 0:
            new_location = 0
        print(f"Darn! A snake brought {player} down to square {new_location}.")

    elif space in ladders:
        new_location = ladder_locations[ladders.index(space)]
        if new_location > 100:
            new_location = 100
        print(f"Splendid! {player} climbed a ladder up to square {new_location}.")

    return new_location

def check_safety(player_total):
    if player_total >= 100:
        player_total = 100
    if player_total < 0:
        player_total = 0
    
    return player_total

def do_turn(player):
    global turn, player1_total, player2_total
    roll = roll_dice()

    if player == player1:
        player1_total += roll

        player1_total = check_safety(player1_total)

        print(f"{player} rolled {roll} and is now at square {player1_total}.")
        if player1_total != 100 or not(player1_total > 100):
            player1_total = check_snake_or_ladder(player1_total, player)


    else:
        player2_total += roll

        player2_total = check_safety(player2_total)

        print(f"{player} rolled {roll} and is now at square {player2_total}.")
        if player2_total != 100 or not(player2_total > 100):
            player2_total = check_snake_or_ladder(player2_total, player)

    if player1_total != 100 and player2_total != 100:
        if roll == 6:
            do_turn(player)

snakes_and_ladders = start_game()

snakes = snakes_and_ladders[0]
snake_locations = snakes_and_ladders[1]
ladders = snakes_and_ladders[2]
ladder_locations = snakes_and_ladders[3]

player1 = input()
player2 = input()

player1_total = 0
player2_total = 0

turn = 1

while not(player1_total >= 100) and not(player2_total >= 100):

    if turn == 1:
        do_turn(player1)
        turn = 2
    else:
        do_turn(player2)
        turn = 1

if player1_total >= 100:
    print(f"{player1} won the game.")
else:
    print(f"{player2} won the game.")