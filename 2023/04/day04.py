def solve_part_one(cards):
    points_total = 0
    for card in cards:
        points = 0
        for win_num in card[0]:
            if win_num in card[1]:
                points = 1 if not points else points * 2
        points_total += points

    print(points_total)


def solve_part_two(cards):
    instances = len(cards) * [1]
    for i in range(len(cards)):
        match_num = set(cards[i][0]).intersection(cards[i][1])
        for j in range(i + 1, i + len(match_num) + 1):
            instances[j] += instances[i]

    print(sum(instances))


if __name__ == '__main__':
    with open('input') as file:
        data = [[[int(i) for i in y[0][y[0].index(':') + 1:].split()], [int(j) for j in y[1].split()]]
                for x in file.read().splitlines() for y in [x.split(' | ')]]

    solve_part_one(data)
    solve_part_two(data)
