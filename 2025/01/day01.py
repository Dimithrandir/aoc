def solve_part_one(instructions):

    point = 50
    count = 0

    for inst in instructions:
        point = (point + inst) % 100
        count += (0 if point else 1)

    print(count)


def solve_part_two(instructions):

    point = 50
    count = 0

    for inst in instructions:
        diff = point if inst < 0 else (100 - point)
        count += (1 if point else 0) + (abs(inst) - (diff if point else 0)) // 100
        point = (point + inst) % 100

    print(count)


if __name__ == '__main__':
    with open('input') as file:
        data = [int(x[1:]) * (-1 if x[0] == 'L' else 1)
                for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
