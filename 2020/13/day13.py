def solve_part_one(data):
    ids = [int(x) for x in data[1:] if x != 'x']
    ts = int(data[0])
    next_departs = []
    for bus in ids:
        next_departs.append(ts + bus - (ts % bus))
    first_depart = min(next_departs)
    wait_time = first_depart - ts
    print(ids[next_departs.index(first_depart)] * wait_time)


def solve_part_two(data):
    ids = [int(x) for x in data[1:] if x != 'x']
    ts = 0
    inc = ids[0]
    for i in range(1, len(ids)):
        while (ts + int(data[1:].index(str(ids[i])))) % ids[i] != 0:
            ts += inc
        inc *= ids[i]
    print(ts)


if __name__ == '__main__':
    with open('input') as file:
        data = [y for x in file.read().splitlines() for y in x.split(',')]

    solve_part_one(data)
    solve_part_two(data)
