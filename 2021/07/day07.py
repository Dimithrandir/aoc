def solve_part_one(crabs):

    min_fuel = (max(crabs) - min(crabs)) * len(crabs)

    for i in range(min(crabs), max(crabs)+1):
        fuel = 0
        for crab in crabs:
            fuel += abs(crab - i)
        if fuel < min_fuel:
            min_fuel = fuel

    print(min_fuel)

def solve_part_two(crabs):

    min_fuel = None

    for i in range(min(crabs), max(crabs) + 1):
        fuel = 0
        for crab in crabs:
            fib = abs(crab - i) * (abs(crab - i) + 1) / 2
            fuel += int(fib)
        if not min_fuel or fuel < min_fuel:
            min_fuel = fuel

    print(min_fuel)

if __name__ == '__main__':
    with open('input') as file:
        data = [ int(x) for x in file.read().split(',') ]

    solve_part_one(data)
    solve_part_two(data)
