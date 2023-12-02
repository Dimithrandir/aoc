bag = {'red': 12, 'green': 13, 'blue': 14}


def solve_part_one(games):
    possible_sum = 0
    for game_id, game_hands in games.items():
        possible = True
        max_values = {key: max([x[key] for x in game_hands if key in x.keys()]) for key in bag.keys()}
        for color in bag:
            if max_values[color] > bag[color]:
                possible = False
                break
        if possible:
            possible_sum += game_id

    print(possible_sum)


def solve_part_two(games):
    power_sum = 0
    for game_id, game_hands in games.items():
        max_values = {key: max([x[key] for x in game_hands if key in x.keys()]) for key in bag.keys()}
        power = 1
        for val in max_values.values():
            power *= val
        power_sum += power
    print(power_sum)


if __name__ == '__main__':
    with open('input') as file:
        data = {int(x.split(':')[0][5:]): [{z.split()[1]: int(z.split()[0]) for z in y.split(', ')} for y in x.split(': ')[1].split(';')] for x in file.read().splitlines()}

    solve_part_one(data)
    solve_part_two(data)
