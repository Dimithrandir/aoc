import functools


@functools.cache
def is_possible(design, patterns):
    if not design:
        return 1
    result = 0
    for pattern in patterns:
        if pattern == design[:len(pattern)]:
            result += is_possible(design[len(pattern):], patterns)
    return result


def solve_part_one(patterns, designs):
    possibles = 0
    for design in designs:
        if is_possible(design, tuple(patterns)):
            possibles += 1
    print(possibles)


def solve_part_two(patterns, designs):
    total = 0
    for design in designs:
        total += is_possible(design, tuple(patterns))
    print(total)


if __name__ == '__main__':
    with open('input') as file:
        data = file.read().split('\n\n')
    patterns = [x.strip() for x in data[0].split(',')]
    designs = [x for x in data[1].splitlines()]

    solve_part_one(patterns, designs)
    solve_part_two(patterns, designs)
