directions = {'R': (0, 1), 'D': (1, 0), 'L': (0, -1), 'U': (-1, 0)}


def solve_part_one(dig_plan):
    vertices = [(0, 0)]
    border = 0
    for inst in dig_plan:
        vertices.append((vertices[-1][0] + inst[1] * directions[inst[0]][0],
                         vertices[-1][1] + inst[1] * directions[inst[0]][1]))
        border += inst[1]

    total_inside = 0
    for i in range(len(vertices) - 1):
        v_1 = vertices[i]
        v_2 = vertices[i + 1]
        total_inside += (v_1[1] - v_2[1]) * (v_1[0] + v_2[0])

    print(total_inside // 2 + border // 2 + 1)


def solve_part_two(dig_plan):
    new_dig_plan = []
    for inst in dig_plan:
        new_dig_plan.append((list(directions.keys())[int(inst[2][-1])], int(inst[2][1:-1], 16)))

    solve_part_one(new_dig_plan)


if __name__ == '__main__':
    with open('input') as file:
        data = [(x.split()[0], int(x.split()[1]), x.split()[2].strip('()'))
                for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
