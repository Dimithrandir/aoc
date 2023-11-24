def solve_part_one(numbers):
    pream_len = 25
    valid = False
    for i in range(pream_len, len(numbers)):
        for j in range(i - pream_len, i):
            for k in range(i - pream_len, i):
                if j != k and numbers[j] + numbers[k] == numbers[i]:
                    valid = True
                    break
        if valid:
            valid = False
            continue
        else:
            print(numbers[i])
            return numbers[i]


def solve_part_two(numbers):
    invalid_num = solve_part_one(numbers)
    for i in range(len(numbers)):
        s = numbers[i]
        for j in range(i + 1, len(numbers)):
            s += numbers[j]
            if s == invalid_num:
                print(min(numbers[i:j]) + max(numbers[i:j]))
                return
            elif s > invalid_num:
                break


if __name__ == '__main__':
    with open('input') as file:
        data = [int(x) for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
