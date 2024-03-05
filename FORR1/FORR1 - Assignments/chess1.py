RANK = 0
COUNTRY = 1
RATING = 2
YEAR = 3

def main():
    # step 1: get data
    # step 2: organize data
    # step 3: present data

    data = get_data()
    if data is None:
        return
    
    players_by_name = organize_data(data)

    display_table("country", players_by_name)
    print()
    display_table("birth year", players_by_name)

def get_data() -> list[str] | None:
    """Gets data"""

    filename = input()
    try:
        with open(filename) as file:
            data = file.readlines()
    except FileNotFoundError:
        return None

    return data

def organize_data(
    lines: list[str]
) -> dict[str, tuple[int, str, int, int]]:
    """Organizes the given data
    
    Recieves a list of lines
    Returns a dictionary where
        a key is the name of a player
        and the corresponding value is
        the associated with the player."""
    players_by_name = {}

    for line in lines:
        rank, name, country, rating, year = cleanup_data(line)
        players_by_name[name] = (rank, country, rating, year)


    return players_by_name

def cleanup_data(line) -> tuple[str]:
    rank, name, country, rating, year = line.split(";")
    last_name, first_name = name.split(",")
    rank = int(rank)
    last_name = last_name.strip()
    first_name = first_name.strip()
    country = country.strip()
    rating = int(rating)
    year = int(year)
    name = f"{first_name} {last_name}"
    return rank, name, country, rating, year

def display_table(current_key, players_by_name: dict[str, tuple[int, str, int, int]]):
    """prints table"""
    # print heads
    # reorganise data by country
    # sort by country
    # print each country

    print_header(f"Players by {current_key}:")
    players_by_key = organize_by_key(current_key, players_by_name)
    for key_item in sorted(players_by_key.items()):
        print_key(key_item[0], players_by_key, players_by_name)

def print_header(header: str):
    dashes = "-" * len(header)
    print(header)
    print(dashes)
    
def organize_by_key(
    key: str, 
    players_by_name: dict[str, tuple[int, str, int, int]]
) -> dict[str, list[tuple[str, int]]]:
    """"""
    players_by_key = {}
    for name, player_info in players_by_name.items():
        rank, country, rating, year = player_info

        if key == "country":
            if country not in players_by_key:
                players_by_key[country] = []
            players_by_key[country].append(name)
        if key == "birth year":
            if year not in players_by_key:
                players_by_key[year] = []
            players_by_key[year].append(name)

    return players_by_key

def print_key(key: str,
    players_by_key: dict,
    players_by_name: dict
):
    # step 1: print subheader
    # step 2: print list of players from the key
    player_matching_key = players_by_key[key]
    print_subheader(key, player_matching_key, players_by_name)
    print_key_list(player_matching_key, players_by_name)

def print_subheader(
    key, 
    players: list, 
    players_by_name: dict):

    number_of_players = len(players)
    ratings = [players_by_name[name][RATING] for name in players]
    average = calculate_average(ratings)
    print(f"{key} ({number_of_players}) ({average:.1f}):")

def calculate_average(numbers:list) -> float:
    return sum(numbers) / len(numbers) if numbers else 0

def print_key_list(players: list, players_by_name: list) -> None:
    for player in players:
        rating = players_by_name[player][RATING]
        print(f"{player:>40}{rating:>10}")


if __name__ == "__main__":
    main()