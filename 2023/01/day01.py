def solve_part_one(text):
    result = 0
    for line in text:
        digits = [x for x in line if x.isdigit()]
        result += int(digits[0] + digits[-1])
    print(result)


def solve_part_two(text):
    digit_names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    result = 0
    for line in text:
        indices = [(line.find(name), str(i + 1)) for i, name in enumerate(digit_names) if line.find(name) != -1]
        indices.extend([(line.rfind(name), str(i + 1)) for i, name in enumerate(digit_names) if line.find(name) != -1 if (line.rfind(name), str(i + 1)) not in indices])
        indices.extend([(i, digit) for i, digit in enumerate(line) if digit.isdigit()])
        result += int(min(indices, key=lambda l: l[0])[1] + max(indices, key=lambda l: l[0])[1])
    print(result)


if __name__ == '__main__':
    with open('input') as file:
        data = [x for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
