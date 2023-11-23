def get_seat_coord(low, high, chars):
    if low == high:
        return low
    else:
        char = chars.pop(0)
        new_low = low + (high + 1 - low) // 2 if char in {'B', 'R'} else low
        new_high = high - 1 - (high - low) // 2 if char in {'F', 'L'} else high
        return get_seat_coord(new_low, new_high, chars)


def get_seat_ids(seats):
    seat_ids = []
    for seat in seats:
        row = get_seat_coord(0, 127, list(seat)[:7])
        column = get_seat_coord(0, 7, list(seat)[-3:])
        seat_ids.append(row * 8 + column)
    return seat_ids


def solve_part_one(seats):
    print(max(get_seat_ids(seats)))


def solve_part_two(seats):
    seat_ids = get_seat_ids(seats)
    print(set(range(min(seat_ids), max(seat_ids) + 1)).difference(seat_ids))


if __name__ == '__main__':
    with open('input') as file:
        data = file.read().splitlines()

    solve_part_one(data)
    solve_part_two(data)
