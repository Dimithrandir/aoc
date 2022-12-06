def solve_part_one(polymer, rules):

    for step in range(10):
        new_polymer = polymer[0]
        for i in range(len(polymer) - 1):
            if polymer[i:i+2] in rules:
                new_polymer += rules[polymer[i:i+2]]
            new_polymer += polymer[i+1]

        polymer = new_polymer

    counts = {}
    for p in polymer:
        if p not in counts:
            counts[p] = 1
        else:
            counts[p] += 1

    print(sorted(counts.values())[-1] - sorted(counts.values())[0])

def solve_part_two(polymer, rules):

    pair_counts = {}
    for el in [ polymer[x:x+2] for x in range(len(polymer) - 1) ]:
        if el in pair_counts:
            pair_counts[el] += 1
        else:
            pair_counts[el] = 1

    for step in range(40):
        for (pair, count) in [ (x, y) for (x, y) in pair_counts.items() ]:
            if pair in rules:
                new_pair_1 = pair[0] + rules[pair]
                new_pair_2 = rules[pair] + pair[1]

                if new_pair_1 in pair_counts:
                    pair_counts[new_pair_1] += count
                else:
                    pair_counts[new_pair_1] = count
                if new_pair_2 in pair_counts:
                    pair_counts[new_pair_2] += count
                else:
                    pair_counts[new_pair_2] = count
                pair_counts[pair] -= count

    counts = {}
    for (pair, count) in pair_counts.items():
        for el in pair:
            if el in counts:
                counts[el] += count
            else:
                counts[el] = count

    counts = { key : value // 2 for (key, value) in counts.items() }
    counts[polymer[0]] += 1
    counts[polymer[-1]] += 1

    print(sorted(counts.values())[-1] - sorted(counts.values())[0])

if __name__ == '__main__':
    with open('input') as file:
        data = file.read().split('\n\n')
        polymer = data[0]
        rules = { x.split('->')[0].strip() : x.split('->')[1].strip() for x in data[1].splitlines() }

    solve_part_one(polymer, rules)
    solve_part_two(polymer, rules)
