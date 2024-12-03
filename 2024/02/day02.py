def is_safe(report):
    difs = [report[i] - report[i-1] for i in range(1, len(report))]
    return set(difs) <= {-1, -2, -3} or set(difs) <= {1, 2, 3}


def solve_part_one(reports):
    safe_count = 0

    for report in reports:
        if is_safe(report):
            safe_count += 1

    print(safe_count)


def solve_part_two(reports):
    safe_count = 0

    for report in reports:
        if is_safe(report):
            safe_count += 1
        else:
            for i in range(len(report)):
                if is_safe(report[:i] + report[i+1:]):
                    safe_count += 1
                    break

    print(safe_count)


if __name__ == '__main__':
    with open('input') as file:
        data = [[int(y) for y in x.split()] for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
