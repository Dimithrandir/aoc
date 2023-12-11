def expand(galaxies, expansion, n, m):
    empty_rows = set(range(n)).difference([x[0] for x in galaxies])
    empty_columns = set(range(m)).difference([x[1] for x in galaxies])
    return [(galaxy[0] + (expansion - 1) * len([x for x in empty_rows if x < galaxy[0]]),
             galaxy[1] + (expansion - 1) * len([x for x in empty_columns if x < galaxy[1]]))
            for galaxy in galaxies]


def solve_part_one(image, expansion=2):
    galaxies = [(i, j) for i in range(len(image)) for j in range(len(image[i])) if image[i][j] == '#']
    galaxies = expand(galaxies, expansion, len(image), len(image[0]))
    pairs = []
    for (x, y) in [(x, y) for x in galaxies for y in galaxies if x != y]:
        if (y, x) not in pairs:
            pairs.append((x, y))

    total = 0
    for pair in pairs:
        total += (abs(pair[1][0] - pair[0][0]) + abs(pair[1][1] - pair[0][1]))

    print(total)


def solve_part_two(image, expansion):
    solve_part_one(image, expansion)


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data, 1000000)
