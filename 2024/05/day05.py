def build_successors_graph(rules):
    succs = {}
    for rule in rules:
        if rule[0] in succs.keys():
            succs[rule[0]].add(rule[1])
        else:
            succs[rule[0]] = {rule[1]}
    return succs


def is_correct(update, succs):
    for i in range(len(update) - 1):
        if (update[i] not in succs.keys()
                or not set(update[i+1:]) <= succs[update[i]]):
            return False
    return True


def solve_part_one(rules, updates):
    succs = build_successors_graph(rules)
    total = 0
    for update in updates:
        if is_correct(update, succs):
            total += int(update[len(update) // 2])
    print(total)


def solve_part_two(rules, updates):
    succs = build_successors_graph(rules)
    total = 0
    for update in updates:
        if not is_correct(update, succs):
            swapped = True
            while swapped:
                swapped = False
                for i in range(1, len(update)):
                    if (update[i-1] in succs.keys()
                            and update[i] in succs[update[i-1]]):
                        temp = update[i-1]
                        update[i-1] = update[i]
                        update[i] = temp
                        swapped = True
            total += int(update[len(update) // 2])
    print(total)


if __name__ == '__main__':
    with open('input') as file:
        data = file.read().split('\n\n')
    rules = [x.split('|') for x in data[0].splitlines()]
    updates = [x.split(',') for x in data[1].splitlines()]

    solve_part_one(rules, updates)
    solve_part_two(rules, updates)
