def find_min_tokens(rules):
    a_x = rules[0][0]
    a_y = rules[0][1]
    b_x = rules[1][0]
    b_y = rules[1][1]
    p_x = rules[2][0]
    p_y = rules[2][1]

    a_times = (b_y * p_x - b_x * p_y) / (a_x * b_y - b_x * a_y)
    b_times = (p_y - a_times * a_y) / b_y

    if a_times % 1 or b_times % 1:
        return 0
    else:
        return int(a_times * 3 + b_times)


def solve_part_one(machines):
    total = 0
    for machine in machines:
        total += find_min_tokens(machine)
    print(total)


def solve_part_two(machines, factor=10000000000000):
    total = 0
    for machine in machines:
        machine[2] = (machine[2][0] + factor, machine[2][1] + factor)
        total += find_min_tokens(machine)
    print(total)


if __name__ == '__main__':
    with open('input') as file:
        data = [[
            (int(y.split()[1 if i == 2 else 2].strip('XY+=,')),
             int(y.split()[2 if i == 2 else 3].strip('XY+=,')))
            for i, y in enumerate(x.splitlines())]
                for x in file.read().split('\n\n')]

    solve_part_one(data)
    solve_part_two(data)
