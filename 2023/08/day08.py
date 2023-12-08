directions = 'LR'


def solve_part_one(instructions, network):
    steps = i = 0
    node = 'AAA'
    while node != 'ZZZ':
        node = network[node][directions.index(instructions[i])]
        i = (i + 1) % len(instructions)
        steps += 1

    print(steps)


def solve_part_two(instructions, network):
    steps_list = []
    for node in [x for x in network if x[2] == 'A']:
        steps = i = 0
        while node[2] != 'Z':
            node = network[node][directions.index(instructions[i])]
            i = (i + 1) % len(instructions)
            steps += 1
        steps_list.append(steps)

    total_steps = steps_list.pop(0)
    for num in steps_list:
        eucl = (num, total_steps)
        while eucl[0]:
            eucl = (eucl[1] % eucl[0], eucl[0])
        total_steps = (total_steps * num) // eucl[1]

    print(total_steps)


if __name__ == '__main__':
    with open('input') as file:
        data = file.read().split('\n\n')
    instructions = data[0]
    network = {x.split(' = ')[0][:3]: x.split(' = ')[1].strip('()').split(', ') for x in data[1].splitlines()}

    solve_part_one(instructions, network)
    solve_part_two(instructions, network)
