import functools


@functools.cache
def blink(stone, times):
    stone_str = str(stone)
    n = len(stone_str)
    if not times:
        return 1
    elif n % 2 == 0:
        return (blink(int(stone_str[:n//2]), times - 1)
                + blink(int(stone_str[n//2:]), times - 1))
    else:
        return blink((2024 * stone) if stone else 1, times - 1)


def solve_part_one(stones, blinks=25):
    total = 0
    for stone in stones:
        total += blink(stone, blinks)
    print(total)


def solve_part_two(stones, blinks=75):
    solve_part_one(stones, blinks)


if __name__ == '__main__':
    with open('input') as file:
        data = [int(x) for x in file.read().split()]

    solve_part_one(data)
    solve_part_two(data)
