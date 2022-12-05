def solve_part_one(crates, proc):

    for step in proc:
        for i in range(step[0]):
            crates[step[2] - 1].append(crates[step[1] - 1].pop())

    print(''.join([ x[-1] for x in crates ]))

def solve_part_two(crates, proc):

    for step in proc:
        crates[step[2] - 1].extend(crates[step[1] - 1][-step[0]:])
        del crates[step[1] - 1][-step[0]:]

    print(''.join([ x[-1] for x in crates ]))

if __name__ == '__main__':
    with open('input') as file:
        data = file.read().split('\n\n')
        crts = data[0].splitlines()
        crates = [ [ crts[y][x] for y in range(len(crts) - 1, -1, -1) if crts[y][x].isalpha() ] for x in range(len(crts[0]) - 1 ) if not (x - 1) % 4 ] 
        proc = [ [ int(y) for y in x.split(' ') if y.isdigit()] for x in data[1].splitlines() ]

    solve_part_one(crates, proc)
    solve_part_two(crates, proc)
