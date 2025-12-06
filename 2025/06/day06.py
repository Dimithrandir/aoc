def get_product(nums):
    product = 1
    for num in nums:
        product *= num
    return product


def solve_part_one(problems):

    n = len(problems)
    m = len(problems[0])
    total = 0
    for j in range(m):
        nums = [int(problems[x][j]) for x in range(n - 1)]
        total += sum(nums) if problems[n-1][j] == '+' else get_product(nums)

    print(total)


def solve_part_two(problems):

    n = len(problems)
    m = len(problems[0])

    signs = [(i, x) for i, x in enumerate(problems[n-1]) if x != ' ']

    total = 0
    j = m + 1
    for sign in reversed(signs):
        nums = [int(''.join([problems[y][x] for y in range(n - 1)]))
                for x in range(j - 2, sign[0] - 1, -1)]
        total += sum(nums) if sign[1] == '+' else get_product(nums)
        j = sign[0]

    print(total)


if __name__ == '__main__':
    with open('input') as file:
        data = file.read().splitlines()

    solve_part_one([x.split() for x in data])
    solve_part_two(data)
