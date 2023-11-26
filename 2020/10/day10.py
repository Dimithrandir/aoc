def solve_part_one(adapters):
    adapt_s = sorted(adapters)
    device = adapt_s[len(adapt_s) - 1] + 3
    adapt_s.insert(0, 0)
    adapt_s.append(device)
    diffs = [0, 0, 0, 0]
    for i in range(len(adapt_s) - 1):
        diff = adapt_s[i + 1] - adapt_s[i]
        diffs[diff] += 1
    print(diffs[1] * diffs[3])


def solve_part_two(adapters):
    adapt_s = sorted(adapters)
    device = adapt_s[-1:][0] + 3
    adapt_s.insert(0, 0)
    adapt_s.append(device)
    arrangs = {x: 0 for x in adapt_s}
    arrangs[adapt_s[-1:][0]] = 1
    for i in range(len(adapt_s) - 1, -1, -1):
        cur = adapt_s[i]
        nexts = [x for x in adapt_s[i:][1:4] if x - cur <= 3]
        for num in nexts:
            arrangs[cur] += arrangs[num]
    print(arrangs[adapt_s[0]])


if __name__ == '__main__':
    with open('input') as file:
        data = [int(x) for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
