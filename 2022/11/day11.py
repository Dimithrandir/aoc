class Monkey:
    def __init__(self, items, operation, divisible, if_true, if_false):
        self.items = items
        self.operator = operation.split(' ')[1]
        self.operand = operation.split(' ')[2]
        self.divisible = int(divisible)
        self.if_true = int(if_true)
        self.if_false = int(if_false)
        self.inspections = 0

    def inspect_1(self):
        items_to_throw = []
        for item in self.items:
            opr = (item if self.operand.isalpha() else int(self.operand))
            new_level = (item * opr if self.operator == '*' else item + opr)
            new_level //= 3
            items_to_throw.append((new_level, self.if_true if not new_level % self.divisible else self.if_false))
            self.inspections += 1
        self.items = []
        return items_to_throw

    def inspect_2(self, prod):
        items_to_throw = []
        for item in self.items:
            opr = (item if self.operand.isalpha() else int(self.operand))
            new_level = (item * opr if self.operator == '*' else item + opr) % prod
            items_to_throw.append((new_level, self.if_true if not new_level % self.divisible else self.if_false))
            self.inspections += 1
        self.items = []
        return items_to_throw

def solve_part_one(monkeys):
    for rnd in range(20):
        for (i, monkey) in enumerate(monkeys):
            for item in monkey.inspect_1():
                monkeys[item[1]].items.append(item[0])

    top_monkeys = sorted([ x.inspections for x in monkeys ])[-2:]
    print(top_monkeys[0] * top_monkeys[1])

def solve_part_two(monkeys):
    prod = 1
    for m in monkeys:
        prod *= m.divisible
    for rnd in range(10000):
        for (i, monkey) in enumerate(monkeys):
            for item in monkey.inspect_2(prod):
                monkeys[item[1]].items.append(item[0])

    top_monkeys = sorted([ x.inspections for x in monkeys ])[-2:]
    print(top_monkeys[0] * top_monkeys[1])

if __name__ == '__main__':
    with open('input') as file:
        data = [ Monkey([ int(y.strip()) for y in x.splitlines()[1].split(':')[1].split(',') ], 
                        x.splitlines()[2].split('=')[1].strip(), 
                        x.splitlines()[3].rsplit(' ', 1)[1], 
                        x.splitlines()[4].rsplit(' ', 1)[1], 
                        x.splitlines()[5].rsplit(' ', 1)[1]) for x in file.read().split('\n\n') ]

    solve_part_one(data)
    solve_part_two(data)
