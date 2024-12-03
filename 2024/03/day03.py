import re


def solve_part_one(memory):
    pairs = re.findall(r'mul\((\d+),(\d+)\)', memory)
    total = 0
    for pair in pairs:
        total += int(pair[0]) * int(pair[1])
    print(total)


def solve_part_two(memory):
    do = True
    total = 0
    while True:
        match = re.search(r'mul\(\d+,\d+\)|do(n\'t)?\(\)', memory)
        if not match:
            break
        if do:
            if 'don\'t()' in match.group():
                do = not do
            elif 'mul' in match.group():
                args = match.group().strip('mul()').split(',')
                total += int(args[0]) * int(args[1])
        else:
            if 'do()' in match.group():
                do = not do
        memory = memory[match.end():]
    print(total)


if __name__ == '__main__':
    with open('input') as file:
        data = file.read()

    solve_part_one(data)
    solve_part_two(data)
