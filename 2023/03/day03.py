def get_neighbors(i, j_start, j_end, n, m):
    return [(x, y)
            for x in range(i - 1, i + 2)
            for y in range(j_start - 1, j_end + 1)
            if (x, y) not in [(i, z) for z in range(j_start, j_end)] and
            x in range(n) and y in range(m)]


def solve_part_one(engine):
    parts_sum = 0
    for i, row in enumerate(engine):
        j = 0
        while j < len(row):
            if row[j].isdigit():
                num_start = j
                while j < len(row) and row[j].isdigit():
                    j += 1
                for neigh in get_neighbors(i, num_start, j, len(engine), len(row)):
                    if engine[neigh[0]][neigh[1]] != '.' and not engine[neigh[0]][neigh[1]].isdecimal():
                        parts_sum += int(row[num_start:j])
            else:
                j += 1

    print(parts_sum)


def solve_part_two(engine):
    stars = {}
    gear_ratios = []
    for i, row in enumerate(engine):
        j = 0
        while j < len(row):
            if row[j].isdigit():
                num_start = j
                while j < len(row) and row[j].isdigit():
                    j += 1
                for neigh in get_neighbors(i, num_start, j, len(engine), len(row)):
                    if engine[neigh[0]][neigh[1]] == '*':
                        if neigh not in stars.keys():
                            stars[neigh] = [int(row[num_start:j])]
                        else:
                            stars[neigh].append(int(row[num_start:j]))
            else:
                j += 1

    for key in stars.keys():
        if len(stars[key]) == 2:
            product = 1
            for num in stars[key]:
                product *= num
            gear_ratios.append(product)

    print(sum(gear_ratios))


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
