def solve_part_one(platform):
    total = 0
    rotated = [''.join([platform[i][j] for i in range(len(platform))]) for j in range(len(platform[0]) - 1, -1, -1)]
    for row in rotated:
        new_row = ''
        for segment in row.split('#'):
            rock_count = segment.count('O')
            new_row += rock_count * 'O' + (len(segment) - rock_count) * '.' + '#'
        for i, rock in enumerate(new_row[:-1]):
            total += len(new_row) - i - 1 if rock == 'O' else 0

    print(total)


def solve_part_two(platform):
    cube_rocks = [(i, j) for i in range(len(platform)) for j in range(len(platform[i])) if platform[i][j] == '#']
    round_rocks = [(i, j) for i in range(len(platform)) for j in range(len(platform[i])) if platform[i][j] == 'O']
    loads = []
    for cycle in range(10000000):
        for direction in 'nwse':
            new_rocks = []
            for k, rock in enumerate(round_rocks):
                if direction in 'ns':
                    if direction == 'n':
                        prev_cubes = [x for x in cube_rocks if x[0] < rock[0] and x[1] == rock[1]]
                        first_cube_rock_i = 0 if not len(prev_cubes) else prev_cubes[-1][0] + 1
                        prev_round_rocks = len([x for x in round_rocks if x[1] == rock[1] and x[0] < rock[0] and x[0] >= first_cube_rock_i])
                        i = first_cube_rock_i + prev_round_rocks
                    elif direction == 's':
                        prev_cubes = [x for x in cube_rocks if x[0] > rock[0] and x[1] == rock[1]]
                        last_cube_rock_i = len(platform) - 1 if not len(prev_cubes) else prev_cubes[0][0] - 1
                        next_round_rocks = len([x for x in round_rocks if x[1] == rock[1] and x[0] > rock[0] and x[0] <= last_cube_rock_i])
                        i = last_cube_rock_i - next_round_rocks
                    j = rock[1]
                if direction in 'we':
                    i = rock[0]
                    if direction == 'w':
                        prev_cubes = [x for x in cube_rocks if x[0] == rock[0] and x[1] < rock[1]]
                        first_cube_rock_j = 0 if not len(prev_cubes) else prev_cubes[-1][1] + 1
                        prev_round_rocks = len([x for x in round_rocks if x[0] == rock[0] and x[1] < rock[1] and x[1] >= first_cube_rock_j])
                        j = first_cube_rock_j + prev_round_rocks
                    elif direction == 'e':
                        prev_cubes = [x for x in cube_rocks if x[0] == rock[0] and x[1] > rock[1]]
                        last_cube_rock_j = len(platform[0]) - 1 if not len(prev_cubes) else prev_cubes[0][1] - 1
                        next_round_rocks = len([x for x in round_rocks if x[0] == rock[0] and x[1] > rock[1] and x[1] <= last_cube_rock_j])
                        j = last_cube_rock_j - next_round_rocks
                new_rocks.append((i, j))
            round_rocks = new_rocks

        load = 0
        for rock in round_rocks:
            load += len(platform) - rock[0]

        if loads.count(load) >= 2:
            indices = [i for i, x in enumerate(loads) if x == load]
            jump = 1
            while jump * 2 <= len(indices):
                diff_1 = cycle - indices[-1 * jump]
                diff_2 = indices[-1 * jump] - indices[-2 * jump]
                if diff_1 == diff_2 and diff_1 > 2:
                    non_rep = cycle - diff_1 - diff_2
                    print(loads[non_rep + (999999999 - non_rep) % diff_1])
                    return
                jump += 1

        loads.append(load)


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
