def solve_part_one(readings):
    total = 0
    for sequence in readings:
        last_nums = []
        while len(set(sequence)) > 1:
            new_seq = []
            for i in range(len(sequence) - 1):
                new_seq.append(sequence[i + 1] - sequence[i])
            last_nums.append(sequence[-1])
            sequence = new_seq
        total += sequence[-1] + sum(last_nums)

    print(total)


def solve_part_two(readings):
    total = 0
    for sequence in readings:
        first_nums = []
        while len(set(sequence)) > 1:
            new_seq = []
            for i in range(len(sequence) - 1):
                new_seq.append(sequence[i + 1] - sequence[i])
            first_nums.append(sequence[0])
            sequence = new_seq
        first_value = sequence[0]
        for num in reversed(first_nums):
            first_value = num - first_value
        total += first_value

    print(total)


if __name__ == '__main__':
    with open('input') as file:
        data = [[int(y) for y in x.split()] for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
