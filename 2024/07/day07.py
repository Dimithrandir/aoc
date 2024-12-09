def is_true(nums, trinity=False):
    if len(nums) == 3:
        total = nums[1] + nums[2]
        product = nums[1] * nums[2]
        concat = int('%d%d' % (nums[1], nums[2]))
        return (total if nums[0] == total
                else product if nums[0] == product
                else concat if trinity and nums[0] == concat
                else False)
    else:
        total = is_true([nums[0] - nums[-1]] + nums[1:-1], trinity)
        product = is_true([nums[0] // nums[-1]] + nums[1:-1], trinity)
        first_num_str = str(nums[0]).removesuffix(str(nums[-1]))
        concat = (is_true([int(first_num_str)] + nums[1:-1], trinity)
                  if (first_num_str not in '-'
                      and nums[0] == int(nums[0])
                      and trinity)
                  else False)
        return (total + nums[-1] if nums[0] == total + nums[-1]
                else product * nums[-1] if nums[0] == product * nums[-1]
                else int('%d%d' % (concat, nums[-1])) if trinity
                else False)


def solve_part_one(equations, trinity=False):
    total = 0
    for equation in equations:
        if is_true(equation, trinity) == equation[0]:
            total += equation[0]
    print(total)


def solve_part_two(equations):
    solve_part_one(equations, trinity=True)


if __name__ == '__main__':
    with open('input') as file:
        data = [[int(z.strip(':')) for z in x] for x in
                [y.split() for y in file.read().splitlines()]]

    solve_part_one(data)
    solve_part_two(data)
