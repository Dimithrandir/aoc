import re

def solve_part_one(polymer, rules):

    for step in range(20):
        new_polymer = polymer[0]
        for i in range(len(polymer) - 1):
            if polymer[i:i+2] in rules:
                new_polymer += rules[polymer[i:i+2]]
            new_polymer += polymer[i+1]

        polymer = new_polymer

    count = {}
    for p in polymer:
        if p not in count:
            count[p] = 1
        else:
            count[p] += 1

    print(sorted(count.values())[-1] - sorted(count.values())[0])

def solve_part_two(polymer, rules):

    count = { key : len([ x for x in polymer if x == key ]) for key in polymer }

    for step in range(20):
        for rule in rules:
            while True:
                (polymer, n) = re.subn(rule, rule[0] + rules[rule].lower() + rule[1], polymer)
                if rules[rule] in count:
                    count[rules[rule]] += n
                else:
                    count[rules[rule]] = n
                if not n:
                    break
        polymer = polymer.upper()

    print(sorted(count.values())[-1] - sorted(count.values())[0])

if __name__ == '__main__':
    with open('input-example') as file:
        data = file.read().split('\n\n')
        polymer = data[0]
        rules = { x.split('->')[0].strip() : x.split('->')[1].strip() for x in data[1].splitlines() }

    solve_part_one(polymer, rules)
    solve_part_two(polymer, rules)
