def map_city(city):
    n = len(city)
    antennas = {}
    for i in range(n):
        for j in range(n):
            if city[i][j].isalnum():
                if city[i][j] in antennas.keys():
                    antennas[city[i][j]].append((i, j))
                else:
                    antennas[city[i][j]] = [(i, j)]
    return antennas


def solve_part_one(city, harmonics=False):
    n = len(city)
    antennas = map_city(city)
    antinodes = set()

    for freq in antennas.keys():
        lines = []
        for ant_1 in antennas[freq]:
            for ant_2 in antennas[freq]:
                if (ant_1 == ant_2
                        or (ant_1, ant_2) in lines or (ant_2, ant_1) in lines):
                    continue
                lines.append((ant_1, ant_2))

                dx = ant_1[1] - ant_2[1]
                dy = ant_1[0] - ant_2[0]

                m = 2
                while True:
                    and_1 = (ant_1[0] + (m - 1) * dy, ant_1[1] + (m - 1) * dx)
                    and_2 = (ant_1[0] - m * dy, ant_1[1] - m * dx)

                    and_1_cond = and_1[0] in range(n) and and_1[1] in range(n)
                    and_2_cond = and_2[0] in range(n) and and_2[1] in range(n)

                    if and_1_cond:
                        antinodes.add((and_1[0], and_1[1]))
                    if and_2_cond:
                        antinodes.add((and_2[0], and_2[1]))

                    if not harmonics:
                        break
                    elif not and_1_cond and not and_2_cond:
                        antinodes.add((ant_1[0], ant_1[1]))
                        antinodes.add((ant_2[0], ant_2[1]))
                        break
                    m += 1
    print(len(antinodes))


def solve_part_two(city):
    solve_part_one(city, harmonics=True)


if __name__ == '__main__':
    with open('input') as file:
        data = file.read().splitlines()

    solve_part_one(data)
    solve_part_two(data)
