def solve_part_one(data):
    print(len([x for x in data if x[3].count(x[2]) in range(x[0], x[1]+1)]))


def solve_part_two(data):
    print(len([x for x in data if [x[3][x[0]-1], x[3][x[1]-1]].count(x[2]) == 1]))


if __name__ == "__main__":
    with open("input") as file:
        data = [(int(y[0].split('-')[0]), int(y[0].split('-')[1]), y[1][:-1], y[2])
                for x in file.read().splitlines() for y in [x.split(' ')]]

    solve_part_one(data)
    solve_part_two(data)
