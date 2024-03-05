MAX_DICE_RESULT = 6  # Assume a standard 6-sided die.

def main():
    """The main function of the program"""

    all_rolls = get_dice()

    if all_rolls:
        counts = count_dice(all_rolls)
        points = get_points(counts)
        print_points(points)

def get_dice() -> list[int] | list[None]:
    """Get the player input and enter it into a list"""

    roll_list = []
    new_roll = input()
    while new_roll != "":
        try:
            new_roll = list(map(int, new_roll.split()))
            roll_list.append(new_roll)
            new_roll = input()
            
        except ValueError:
            pass

    return roll_list

def count_dice(rolls: list[list[int]]) -> list[list[int]]:
    """Create a list for each roll to see the count of each dice inside that roll"""

    counting_list = []
    for roll in rolls:
        counter = get_counts(roll)
        counting_list.append(counter)

    return counting_list

def get_counts(dice_results: list[int]) -> list[int]:
    """Counts how often each value appears.

    Returns a list of counts
    for each possible outcome on a die roll,
    where the first count in the list
    (at position 0 in the output list)
    indicates how many 1's appear
    in the given list of dice results,
    the second count (at position 1)
    indicates how many 2's appear, and so on.
    The count list is as long as there are sides on the dice.

    For example, if the dice list is [3, 3, 4, 4, 1],
    then the count list is [1, 0, 2, 2, 0, 0],
    indicating that the number 1 appears once,
    the numbers 3 and 4 appear twice each,
    but the numbers 2, 5 and 6 never appear.
    """

    counts = [dice_results.count(value) for value in range(1, MAX_DICE_RESULT + 1)]
    return counts

def get_points(counts: list[list[int]]) -> list[int]:
    """Get the points of each roll made and add them to a list"""

    point_list = []
    for counter_list in counts:
        new_points = check_points(counter_list)
        point_list.append(new_points)

    return point_list

def check_points(counter_list : list[int]) -> int:
    """Check given counter list for points"""

    if 5 in counter_list:
        return 50

    # check for both 3 and 4. If you have 4 of a kind, you must also have 3 of a kind
    elif 3 in counter_list or 4 in counter_list:
        if 3 in counter_list:
            search_numer = 3
        else:
            search_numer = 4

        return 3 * (counter_list.index(search_numer) + 1)

    elif 2 in counter_list:
        # Search through the list backwards to find highest value first with index()
        return 2 * (MAX_DICE_RESULT - counter_list[::-1].index(2))
        
    return 0

def print_points(points: list[int]):
    """Print the given points"""

    for point_total in points:
        print(point_total)

if __name__ == "__main__":
    main()
