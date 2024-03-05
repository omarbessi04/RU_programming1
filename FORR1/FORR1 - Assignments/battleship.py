# Translate coordinates from ex D6 to (7, 6)
def translate_coordinate(coordinate):
    coordinate = list(coordinate)
    y_string = coordinate[0]
    x = int("".join(coordinate[1::]))

    if y_string == "A":
        y = 10
    elif y_string == "B":
        y = 9
    elif y_string == "C":
        y = 8
    elif y_string == "D":
        y = 7
    elif y_string == "E":
        y = 6
    elif y_string == "F":
        y = 5
    elif y_string == "G":
        y = 4
    elif y_string == "H":
        y = 3
    elif y_string == "I":
        y = 2
    elif y_string == "J":
        y = 1

    xy_coordinates = (x,y)
    return xy_coordinates

# Create battleship 
def create_battleship(xy_coordinates, type, shape):
    if type == "carrier":
        length = 5

    elif type == "battleship":
        length = 4

    elif type == "destroyer" or type == "submarine":
        length = 3

    elif type == "patrol":
        length = 2

    x, y = xy_coordinates
    x = int(x)
    y = int(y)

    head = (x, y)

    all_coordinates_of_ship = [head]

    for i in range(1, length):
        if shape == "vertical":
            tail_cooridante = (x, y-i)
            
        elif shape == "horizontal":
            tail_cooridante = (x+i, y)
        
        all_coordinates_of_ship.append(tail_cooridante)
    
    return all_coordinates_of_ship

# Get all inputs needed to start the game
def start_game():
    carrier_input = input("Location and orientation of your carrier:\n").split()
    carrier_head_coordinate = translate_coordinate(carrier_input[0])
    carrier_coordinates = create_battleship(carrier_head_coordinate, "carrier", carrier_input[1])

    battleship_input = input("Location and orientation of your battleship:\n").split()
    battleship_head_coordinate = translate_coordinate(battleship_input[0])
    battleship_coordinates = create_battleship(battleship_head_coordinate, "battleship", battleship_input[1])

    destroyer_input = input("Location and orientation of your destroyer:\n").split()
    destroyer_head_coordinate = translate_coordinate(destroyer_input[0])
    destroyer_coordinates = create_battleship(destroyer_head_coordinate, "destroyer", destroyer_input[1])

    submarine_input = input("Location and orientation of your submarine:\n").split()
    submarine_head_coordinate = translate_coordinate(submarine_input[0])
    submarine_coordinates = create_battleship(submarine_head_coordinate, "submarine", submarine_input[1])

    patrol_boat_input = input("Location and orientation of your patrol boat:\n").split()
    patrol_boat_head_coordinate = translate_coordinate(patrol_boat_input[0])
    patrol_boat_coordinates = create_battleship(patrol_boat_head_coordinate, "patrol", patrol_boat_input[1])

    all_coordinates = [carrier_coordinates, battleship_coordinates, destroyer_coordinates, submarine_coordinates, patrol_boat_coordinates]

    return all_coordinates

def check_for_hit():
    attack = translate_coordinate(input())

    i = -1
    hit = False
    for boat_coordinates in all_coordinates:
        i += 1
        if attack in boat_coordinates:
            hit = True
            if i == 0:
                boat = "carrier"
            elif i == 1:
                boat = "battleship"
            elif i == 2:
                boat = "destroyer"
            elif i == 3:
                boat = "submarine"
            elif i == 4:
                boat = "patrol boat"

            damaged_coordinates.append(attack)

            all_coordinates_have_been_destroyed = True

            for coordinate in boat_coordinates:
                if coordinate not in damaged_coordinates:
                    all_coordinates_have_been_destroyed = False

            if all_coordinates_have_been_destroyed:
                print("You have sunk my", boat, end=".\n")
            else:
                print("Hit,", boat, end=".\n")
            
            break
    
    if hit == False:
        print("Miss.")

damaged_coordinates = []
all_coordinates = start_game()

while len(damaged_coordinates) != 17:
    check_for_hit()

print("The entire fleet has been sunk.")