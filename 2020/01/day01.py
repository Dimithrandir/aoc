def solve_part_one(data):
    for i in data:
        for j in data:
            if i + j == 2020:
                print(i * j)
                return


def solve_part_two(data):
    for i in data:
        for j in data:
            if i + j >= 2020:
                continue
            for k in data:
                if i + j + k == 2020:
                    print(i * j * k)
                    return


if __name__ == "__main__":
    with open("input") as file:
        data = [int(x) for x in file.readlines()]

    solve_part_one(data)
    solve_part_two(data)
