ROUNDING_NUMBER = 2

def main():
    """Main functionality of the program"""

    javelin_data = open_file()
    if javelin_data:
        scoreboard = generate_scoreboard(javelin_data)
        print_scores(scoreboard)

def open_file() -> list[str] | None:
    """Tries to open a file.
    Returns the file if one is available.
    Returns None if not."""

    filename = input()
    try:
        with open(filename) as file:
            data = file.readlines()

    except FileNotFoundError:
        return None

    return data

def generate_scoreboard(javelin_data: list[str]) -> dict[str, list[int]]:
    """Create a scoreboard dictionary that lists competitors and their throws"""

    scoreboard = {}
    for line in javelin_data:
        first_name, last_name, score = line.split()

        first_name = first_name.strip()
        last_name = last_name.strip()
        score = float(score)
        full_name = f"{first_name} {last_name}"

        if full_name not in scoreboard:
            scoreboard[full_name] = []
        
        scoreboard[full_name].append(score)

    return scoreboard

def print_scores(scoreboard: dict[str, list[int]]):
    """Print out formatted scores from the scoreboard"""

    for competitor in scoreboard:
        output = make_pretty(competitor, scoreboard)
        print(output)

    highest_average = calculate_highest_average(scoreboard)
    if highest_average:
        print(f"{highest_average[0]}: {highest_average[1]}")
    
def make_pretty(competitor, scoreboard):
    """Format string for given competitor"""

    throw_string = ""
    for throw in scoreboard[competitor]:
        throw_string += f" {round(throw, ROUNDING_NUMBER)}"

    return f"{competitor:<19} Throws:{throw_string}"

def calculate_highest_average(scoreboard):
    """Calculate the highest average from the scoreboard"""

    highest_average = ["", 0]
    for competitor in scoreboard:
        # only calculate average if the competitor threw more than once
        throws = scoreboard[competitor]
        if len(throws) > 1:
            average = sum(throws) / len(throws)
            average = round(average, ROUNDING_NUMBER)

            if average > highest_average[1]:
                highest_average = [competitor, average]

    if highest_average == ["", 0]:
        return None
    
    return highest_average

if __name__ == "__main__":
    main()