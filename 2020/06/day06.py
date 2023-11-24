def solve_part_one(groups):
    total = 0
    for group in groups:
        answers = ''
        for person in group:
            answers += person
        total += len(set(answers))
    print(total)


def solve_part_two(groups):
    total = 0
    for group in groups:
        answers = set(group.pop(0))
        for person in group:
            answers.intersection_update(person)
            if not answers:
                break
        total += len(answers)
    print(total)


if __name__ == '__main__':
    with open('input') as file:
        data = [y for x in file.read().split('\n\n') for y in [x.splitlines()]]

    solve_part_one(data)
    solve_part_two(data)
