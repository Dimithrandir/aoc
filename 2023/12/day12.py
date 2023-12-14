import functools


@functools.cache
def count_arrangements(springs, groups):

    def spring_is_damaged():
        cur_group = springs[:groups[0]].replace('?', '#')
        if cur_group != '#' * groups[0]:
            return 0
        if len(springs) == groups[0]:
            return 1 if len(groups) == 1 else 0
        if springs[groups[0]] in '?.':
            return count_arrangements(springs[groups[0] + 1:], groups[1:])
        return 0

    if not groups:
        return 1 if '#' not in springs else 0
    if not springs:
        return 0

    if springs[0] == '.':
        return count_arrangements(springs[1:], groups)
    elif springs[0] == '#':
        return spring_is_damaged()
    elif springs[0] == '?':
        return spring_is_damaged() + count_arrangements(springs[1:], groups)


def solve_part_one(records):
    total = 0
    for record in records:
        total += count_arrangements(record[0], tuple(record[1]))
    print(total)


def solve_part_two(records):
    for i, record in enumerate(records):
        records[i][0] += ('?' + record[0]) * 4
        records[i][1] = records[i][1] * 5

    total = 0
    for record in records:
        total += count_arrangements(record[0], tuple(record[1]))
    print(total)


if __name__ == '__main__':
    with open('input') as file:
        data = [[x.split()[0], [int(y) for y in x.split()[1].split(',')]] for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
