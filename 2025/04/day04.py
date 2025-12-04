def get_neighbors(i, j, n, m):
    return [(x, y)
            for x in range(max(0, i-1), min(i+2, n))
            for y in range(max(0, j-1), min(j+2, m))
            if x != i or y != j]


def solve_part_one(grid):

    n = len(grid)
    m = n

    count = 0
    for i in range(n):
        for j in range(m):

            if grid[i][j] == '.':
                continue

            neighbors = get_neighbors(i, j, n, m)
            if len([x for x in neighbors if grid[x[0]][x[1]] == '@']) < 4:
                count += 1

    print(count)


def solve_part_two(grid):

    n = len(grid)
    m = n

    rolls = set([(x, y)
                 for x in range(n) for y in range(m)
                 if grid[x][y] == '@'])

    count = 0
    while True:

        removed = set()
        for roll in rolls:
            neighbors = get_neighbors(roll[0], roll[1], n, m)
            if len([x for x in neighbors if (x[0], x[1]) in rolls]) < 4:
                count += 1
                removed.add(roll)

        if not removed:
            break

        rolls.difference_update(removed)

    print(count)


if __name__ == '__main__':
    with open('input') as file:
        data = file.read().splitlines()

    solve_part_one(data)
    solve_part_two(data)
