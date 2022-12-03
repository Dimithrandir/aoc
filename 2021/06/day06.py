def solve_part_one(fish, days):
    for day in range(days):
        for i, lf in enumerate(fish):
            fish[i] -= 1
            if fish[i] < 0:
                fish[i] = 6
                fish.append(9)

    print(len(fish))

def solve_part_two(fish, days):
    fish_counts = 9 * [0]

    for f in fish:
        fish_counts[f] += 1

    for i in range(days):
        deaths = fish_counts.pop(0)
        fish_counts.append(deaths)
        fish_counts[6] += deaths

    print(sum(fish_counts))

if __name__ == '__main__':
    with open('input') as file:
        data = [ int(x) for x in file.read()[:-1].split(',')]

    solve_part_one(data, 80)
    solve_part_two(data, 256)
