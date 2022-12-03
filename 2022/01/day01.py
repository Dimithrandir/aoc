def find_elves(data):
    elves = []
    cals = 0
    for item in data:
        if item:
            cals += int(item)
        else:
            elves.append(cals)
            cals = 0
    elves.append(cals)
    return elves

def solve_part_one(data):
    print(max(find_elves(data)))

def solve_part_two(data):
    print(sum(sorted(find_elves(data))[-3:]))

if __name__ == '__main__':
    with open('input') as file:
        data = file.read().splitlines()

    solve_part_one(data)
    solve_part_two(data)
