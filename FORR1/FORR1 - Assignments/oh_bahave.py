def moveThing(thing, origin):
    if origin == "left":
        left_options.remove(thing)
        right_options.append(thing)
    else:
        right_options.remove(thing)
        left_options.append(thing)

def checkScene():
    global game
    i = -1
    for option in scene:
        i += 1
        danger_check1 = ("w" in option) and ("g" in option) and ("c" not in option)
        danger_check2 = ("g" in option) and ("c" in option) and ("w" not in option)
        side_check = (not(side == "left" and i == 0)) and (not(side == "right" and i == 1))

        if danger_check1 and side_check:
            print("The wolf ate the goat.")
            game = False

        if danger_check2 and side_check:
            print("The goat ate the cabbage.")
            game = False

game = True
side = "left"
left_options = ["w", "g", "c"]
right_options = []
scene = [left_options, right_options]

while game:
    print(f"You are on the {side} side.")
    print(*left_options, "~ ", *right_options)

        
    if left_options == []:
        print("You solved the puzzle!")
        game = False
    
    else:
        checkScene()
        if game:
            move = False
            while not move:
                move_over = input("What would you like to take over the river? (w/g/c/n):\n").lower()
                if (side == "left" and move_over in left_options) or (side == "right" and move_over in right_options) or move_over == "n":
                    if move_over != "n":
                        moveThing(move_over, side)

                    if side == "left":
                        side = "right"
                    elif side == "right":
                        side = "left"
                    
                    move = True

                else:
                    print("Not a valid choice!")
