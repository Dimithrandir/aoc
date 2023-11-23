def count_trees(data, right, down):
    count = 0
    m = len(data[0])
    j = right
    for i in range(down, len(data), down):
        if data[i][j] == '#':
            count += 1
        j = (j + right) % m
    return count


def solve_part_one(data):
    print(count_trees(data, 3, 1))


def solve_part_two(data):
    product = 1
    for slope in [(x, y) for x in range(1, 3) for y in range(1, 8, 2)]:
        product *= count_trees(data, slope[1], slope[0])
        if slope[0] > 1:
            break
    print(product)


if __name__ == "__main__":

    with open("input") as file:
        data = file.read().splitlines()

    solve_part_one(data)
    solve_part_two(data)
