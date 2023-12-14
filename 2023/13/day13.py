def check_reflection(pattern, smudges):
    for i in range(1, len(pattern)):
        mirror_len = min(i, len(pattern) - i)
        up_side = pattern[:i][-mirror_len:]
        down_side = list(reversed(pattern[i:][:mirror_len]))
        if smudges:
            up_rows = ''.join(up_side).replace('.', '0').replace('#', '1')
            down_rows = ''.join(down_side).replace('.', '0').replace('#', '1')
            if bin(int(up_rows, 2) ^ int(down_rows, 2)).count('1') == 1:
                return i
        elif up_side == down_side:
            return i

    return 0


def solve_part_one(patterns, smudges=False):
    total = 0
    for pattern in patterns:
        above = check_reflection(pattern, smudges)
        if above:
            total += 100 * above
        else:
            rotated = [''.join(reversed([pattern[i][j] for i in range(len(pattern))]))
                       for j in range(len(pattern[0]))]
            total += check_reflection(rotated, smudges)

    print(total)


def solve_part_two(patterns, smudges=True):
    solve_part_one(patterns, smudges)


if __name__ == '__main__':
    with open('input') as file:
        data = [[y for y in x.splitlines()] for x in file.read().split('\n\n')]

    solve_part_one(data)
    solve_part_two(data)
