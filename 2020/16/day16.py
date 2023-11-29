def solve_part_one(fields, neighbors):
    valid_nums = set()
    valid_tickets = []
    for field, pairs in fields.items():
        for pair in pairs:
            valid_nums = valid_nums.union(set(range(int(pair[0]), int(pair[1]) + 1)))

    error_rate = 0
    for ticket in neighbors:
        valid = True
        for num in ticket:
            if int(num) not in valid_nums:
                error_rate += int(num)
                valid = False
        if valid:
            valid_tickets.append(ticket)

    print(error_rate)
    return valid_tickets


def solve_part_two(fields, my_ticket, neighbors):
    valid_tickets = solve_part_one(fields, neighbors)

    for field, pairs in fields.items():
        valid_nums = set()
        for pair in pairs:
            valid_nums = valid_nums.union(set(range(int(pair[0]), int(pair[1]) + 1)))
        fields[field] = valid_nums

    possible_fields = {}
    for i in range(len(valid_tickets[0])):
        column = sorted([int(valid_tickets[x][i]) for x in range(len(valid_tickets))])
        possible_fields[i] = []
        for field in fields.keys():
            if set(column).issubset(fields[field]):
                possible_fields[i].append(field)

    found_fields = []
    for field in sorted(possible_fields.keys(), key=lambda l: len(possible_fields[l])):
        for found in found_fields:
            possible_fields[field].remove(found)
        if len(possible_fields[field]) == 1:
            found_fields.append(possible_fields[field][0])

    product = 1
    for index, field in possible_fields.items():
        if field[0].startswith('departure'):
            product *= my_ticket[index]
    print(product)


if __name__ == '__main__':
    with open('input') as file:
        data = file.read().split('\n\n')

    fields = {x.split(':')[0]: [z for y in x.split(':')[1].strip().split(' or ') for z in [y.split('-')]] for x in data[0].splitlines()}
    my_ticket = [int(x) for x in data[1].splitlines()[1].split(',')]
    nearby_tickets = [y for x in data[2].splitlines()[1:] for y in [x.split(',')]]

    solve_part_one(fields, nearby_tickets)
    solve_part_two(fields, my_ticket, nearby_tickets)
