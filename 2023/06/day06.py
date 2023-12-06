def solve_part_one(races):
    product = 1
    for race in races:
        ways_num = 0
        for i in range(race[0] + 1 // 2):
            ways_num += 1 if i * (race[0] - i) > race[1] else 0
        product *= ways_num

    print(product)


def solve_part_two(time, distance):
    ways_num = 0
    for i in range(time + 1 // 2):
        ways_num += 1 if i * (time - i) > distance else 0

    print(ways_num)


if __name__ == '__main__':
    with open('input') as file:
        data = [x[10:].split() for x in file.read().splitlines()]
    races = [(int(data[0][i]), int(data[1][i])) for i in range(len(data[0]))]
    time = int(''.join(data[0]))
    distance = int(''.join(data[1]))

    solve_part_one(races)
    solve_part_two(time, distance)
