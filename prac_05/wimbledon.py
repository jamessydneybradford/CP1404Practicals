"""
Wimbledon.py
"""


def main():
    games = get_data_from_file()
    calculate_display_total_wins(games)
    display_wimbledon_winning_countries(games)


def get_data_from_file():  # Read each game detail line  in the into a list of lists called games
    game = []
    games = []
    with open("wimbledon.csv", "r", encoding="utf-8-sig") as in_file:
        for line in in_file:
            game = line.strip().split(',')
            games.append(game)
    del games[0]
    return games


def display_wimbledon_winning_countries(games):
    countries = []
    country_column = 3
    for i in range(len(games)):
        countries += [games[i][country_column]]
    countries = set(countries)
    print(f"These {len(countries)} countries have won Wimbledon:")
    countries = sorted(countries)
    countries_to_display = (', '.join(countries))
    print(countries_to_display)


def calculate_display_total_wins(games):
    names = []  # a list of winners to be taken from games
    winner_column = 2  # the column that has the winner name in it
    names = []  # a list for storing the names of the winners
    name_to_win_total = {}  # a disctionary to store win totals
    # copy the winner name column
    for i in range(len(games)):
        names += [games[i][winner_column]]
    # totals into the name_to_win_total dictionary
    for name in names:
        name_to_win_total[name] = names.count(name)
    print(name_to_win_total)
    print("Wimbledon Champions:")
    for name, win_total in name_to_win_total.items():
        print(f"{name:}, {win_total}")


main()

# Wimbledon Champions:
# Rod Laver 2
# ...
# Lleyton Hewitt 1
# Roger Federer 8
# Rafael Nadal 2
# Novak Djokovic 7
# Andy Murray 2
#
# These 12 countries have won Wimbledon:
# AUS, CRO, ESP, FRG, GBR, GER, NED, SRB, SUI, SWE, TCH, USA
