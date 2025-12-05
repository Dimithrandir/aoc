def solve_part_one(ranges, ids):

    count = 0
    for i in ids:
        fresh = False
        for r in ranges:
            if i in range(r[0], r[1] + 1):
                fresh = True
                break
        if fresh:
            count += 1

    print(count)


def solve_part_two(ranges):

    ranges.sort(key=lambda l: l[0])
    total_fresh = 0
    last_right = 0

    for r in ranges:
        if r[1] < last_right:
            continue

        left = max(r[0], last_right + 1)
        right = r[1]

        last_right = right

        total_fresh += right + 1 - left

    print(total_fresh)


if __name__ == '__main__':
    with open('input') as file:
        data = file.read().split('\n\n')
    ranges = [(int(x.split('-')[0]), int(x.split('-')[1]))
              for x in data[0].splitlines()]
    ids = [int(x) for x in data[1].splitlines()]

    solve_part_one(ranges, ids)
    solve_part_two(ranges)
