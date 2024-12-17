w = 101
h = 103
s = 100


def solve_part_one(robots):
    end_positions = []

    for robot in robots:
        end_pos = (
                (robot[0][0] + s * robot[1][0]) % w,
                (robot[0][1] + s * robot[1][1]) % h)
        end_positions.append(end_pos)

    q_1 = len([x for x in end_positions if x[0] < w // 2 and x[1] < h // 2])
    q_2 = len([x for x in end_positions if x[0] < w // 2 and x[1] > h // 2])
    q_3 = len([x for x in end_positions if x[0] > w // 2 and x[1] > h // 2])
    q_4 = len([x for x in end_positions if x[0] > w // 2 and x[1] < h // 2])

    print(q_1 * q_2 * q_3 * q_4)


def solve_part_two(robots):

    def is_tree_top(top, positions):
        segment = [top]
        for i in range(5):
            segment = [(x, segment[0][1] + 1)
                       for x in range(segment[0][0] - 1, segment[-1][0] + 2)]
            if not set(segment) <= set(positions):
                return False
        return True

    sec = 1
    while True:
        end_positions = []
        for robot in robots:
            end_pos = (
                    (robot[0][0] + sec * robot[1][0]) % w,
                    (robot[0][1] + sec * robot[1][1]) % h)
            end_positions.append(end_pos)

        for pos in end_positions:
            if is_tree_top(pos, end_positions):
                print(sec)
                return
        sec += 1


if __name__ == '__main__':
    with open('input') as file:
        data = [[[int(z) for z in y.strip('pv=').split(',')]
                 for y in x.split()] for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
