def solve_part_one(data):
    count = 0
    for pair in data:
        if pair[0] >= pair[2] and pair[1] <= pair[3] or pair[0] <= pair[2] and pair[1] >= pair[3]:
            count += 1
    print(count)

def solve_part_two(data):
    count = 0
    for pair in data:
        if [ x for x in [ y for y in range(pair[0], pair[1] + 1) ] if x in [ z for z in range(pair[2], pair[3] + 1) ] ]:
            count += 1
    print(count)

if __name__ == '__main__':
    with open('input') as file:
        data = [ [ int(z) for y in x.split(',') for z in y.split('-')] for x in file.read().splitlines() ]

    solve_part_one(data)
    solve_part_two(data)
