#               https://github.com/omarbessi04/TileTraveller

# 1. Create functions to move player and check for directions
# 2. Prompt player with input
# 3. Move player based on input OR don't
# 4. Once player has reached goal, end program


#functions that move player
import random

def goNorth():
    global y, coordinates_of_player
    y += 1
    coordinates_of_player = [x,y]

def goSouth():
    global y, coordinates_of_player
    y -= 1
    coordinates_of_player = [x,y]

def goEast():
    global x, coordinates_of_player
    x += 1
    coordinates_of_player = [x,y]

def goWest():
    global x, coordinates_of_player
    x -= 1
    coordinates_of_player = [x,y]

def Check_Valid_Directions():
    global coordinates_of_player, Valid_directions
    for i in range(len(directions)):
        if coordinates_of_player in (directions)[i]:

            if (directions)[i] == directions[0]:
                Valid_directions.append("(N)orth")

            if (directions)[i] == directions[1]:
                Valid_directions.append("(E)ast")

            if (directions)[i] == directions[2]:
                Valid_directions.append("(S)outh")

            if (directions)[i] == directions[3]:
                Valid_directions.append("(W)est")

def make_random_choice(option):
    if option == "lever":
        choice = random.choice(["y", "n"])
    else:
        choice = random.choice(["n", "e", "s", "w"])

    return choice

def Offer_coin():
    global coins
    lever_option = make_random_choice("lever")
    print(f"Pull a lever (y/n): {lever_option}")
    if lever_option.lower() == "y":
        coins += 1
        print(f"You received 1 coin, your total is now {coins}.")

def initialize():
    the_seed = int(input("Input seed:\n"))
    random.seed(the_seed)

#list of all the tiles that are available, N, E, S, W
directions = ([[1,1], [1,2], [2,1], [3,1], [3,2]], 
              [[1,3], [1,2], [2,3]],
              [[1,2], [1,3], [2,2], [3,3], [3,2]],    
              [[3,3], [2,3], [2,2]])

lever_locations = ([1,2], [2,2], [2,3], [3,2])

Play = True
initialize()
while Play:
    x = 1
    y = 1
    coordinates_of_player = [x,y]
    coins = 0
    Invalid_direction = True
    Valid_directions = []
    moves = 0
    Check_Valid_Directions()
    print("You can travel: ", " or ".join(Valid_directions), end=".\n")

    while coordinates_of_player != [3, 1]:

        Valid_directions = []
        Check_Valid_Directions()
        player_move = make_random_choice("movement")
        print(f"Direction: {player_move}")
        moves += 1

        if player_move.lower() == "n":
            if "(N)orth" in Valid_directions:
                goNorth()
                Invalid_direction = False
            else:
                Invalid_direction = True

        elif player_move.lower() == "s":
            if "(S)outh" in Valid_directions:
                goSouth()
                Invalid_direction = False
            else:
                Invalid_direction = True

        elif player_move.lower() == "e":
            if "(E)ast" in Valid_directions:
                goEast()
                Invalid_direction = False
            else:
                Invalid_direction = True

        elif player_move.lower() == "w":
            if "(W)est" in Valid_directions:
                goWest()
                Invalid_direction = False
            else:
                Invalid_direction = True

        if Invalid_direction:
            print("Not a valid direction!")
            Valid_directions = []
            Check_Valid_Directions()
            print("You can travel: ", " or ".join(Valid_directions), end=".\n")
        else:
            if coordinates_of_player != [3,1]:
                Valid_directions = []
                Check_Valid_Directions()
                if coordinates_of_player in lever_locations:
                    Offer_coin()
                print("You can travel: ", " or ".join(Valid_directions), end=".\n")

    print(f"Victory! Total coins {coins}. Moves {moves}.")

    repeat_game = input("Play again (y/n):\n")
    if repeat_game.lower() == "n":
        Play = False
