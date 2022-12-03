def solve_part_one(data):
    depth = 0
    h_pos = 0

    for command in data:
        com = command.split(' ')
        if com[0] == 'forward':
            h_pos += int(com[1])
        elif com[0] == 'down':
            depth += int(com[1])
        elif com[0] == 'up':
            depth -= int(com[1])

    print(depth * h_pos)

def solve_part_two(data):
    depth = 0
    h_pos = 0
    aim = 0

    for command in data:
        com = command.split(' ')
        if com[0] == 'forward':
            h_pos += int(com[1])
            depth += aim * int(com[1])
        elif com[0] == 'down':
            aim += int(com[1])
        elif com[0] == 'up':
            aim -= int(com[1])

    print(depth * h_pos)

if __name__ == "__main__":

    with open("input") as file:
        data = file.read().splitlines()

    solve_part_one(data)
    solve_part_two(data)
