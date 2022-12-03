def solve_part_one(data):
    score = 0
    for rnd in data:
        if rnd[0] == rnd[1]:
            score += 3 + rnd[1]
        elif rnd[0] % 3 == (rnd[1] - 1) % 3:
            score += 6 + rnd[1]
        elif rnd[0] % 3 == (rnd[1] + 1) % 3:
            score += rnd[1]
    print(score)

def solve_part_two(data):
    score = 0
    for rnd in data:
        if rnd[1] == 1:
            if rnd[0] - 1:
                score += rnd[0] - 1
            else:
                score += 3
        elif rnd[1] == 2:
            score += 3 + rnd[0]
        elif rnd[1] == 3:
            score += 6 + (rnd[0] % 3) + 1
    print(score)

if __name__ == '__main__':
    with open('input') as file:
        data = [ (ord(x.split(' ')[0]) - 64, ord(x.split(' ')[1]) - 87) for x in file.read().splitlines() ]

    solve_part_one(data)
    solve_part_two(data)
