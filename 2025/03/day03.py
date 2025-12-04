def solve_part_one(banks):

    total = 0

    for bank in banks:
        bank_tuples = [(i, x) for i, x in enumerate(bank)]
        bank_tuples.sort(key=lambda l: l[1], reverse=True)
        indices = [x[0] for x in bank_tuples]

        max_jolt = 0
        for i in range(len(bank)):
            next_indices = [x for x in indices if x > i]

            if not next_indices:
                continue

            k = next_indices[0]

            jolt = int(bank[i] + bank[k])
            max_jolt = max(max_jolt, jolt)

        total += max_jolt

    print(total)


def solve_part_two(banks):

    total = 0
    bank_len = len(banks[0])
    bat_len = 12

    for bank in banks:
        win_len = 1 + bank_len - bat_len
        i = 0
        max_jolt = ''
        while len(max_jolt) < bat_len:
            window = bank[i:i+win_len]
            j = window.index(max(window))
            i += j + 1
            win_len -= j
            max_jolt += window[j]

        total += int(max_jolt)

    print(total)


if __name__ == '__main__':
    with open('input') as file:
        data = file.read().splitlines()

    solve_part_one(data)
    solve_part_two(data)
