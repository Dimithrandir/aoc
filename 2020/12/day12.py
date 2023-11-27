def solve_part_one(instructions):
    directions = 'NESW'
    rotations = 'LR'
    face = 'E'
    pos = [0, 0]

    for inst in instructions:
        action = inst[0]
        if action in set(directions).union('F'):
            dir_index = directions.index(action if action != 'F' else face) + 1
            pos[dir_index % 2] = pos[dir_index % 2] + inst[1] * pow(-1, dir_index // 3)
        else:
            rot_index = rotations.index(action) + 1
            face_index = directions.index(face) + (inst[1] // 90) * pow(-1, rot_index)
            face = directions[face_index % 4 if face_index >= 0 else face_index + 4]

    print(sum([abs(x) for x in pos]))


def solve_part_two(instructions):
    directions = 'NESW'
    rotations = 'LR'
    pos = [0, 0]
    waypoint = [10, 1]

    for inst in instructions:
        action = inst[0]
        if action in directions:
            dir_index = directions.index(action) + 1
            waypoint[dir_index % 2] = waypoint[dir_index % 2] + inst[1] * pow(-1, dir_index // 3)
        elif action in rotations:
            rot_index = rotations.index(action)
            for i in range(inst[1] // 90):
                waypoint.insert(rot_index, (waypoint.pop((rot_index + 1) % 2) * -1))
        else:
            for i in range(inst[1]):
                pos[0] += waypoint[0]
                pos[1] += waypoint[1]

    print(sum([abs(x) for x in pos]))


if __name__ == '__main__':
    with open('input') as file:
        data = [(x[0], int(x[1:])) for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
