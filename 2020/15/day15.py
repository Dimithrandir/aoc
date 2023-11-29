def solve_part_one(data):
    turn = len(data)
    while True:
        turn += 1
        last_num = data[-1:][0]
        new_num = 0
        if last_num in data[:-1]:
            prev_turn = turn - 1 - list(reversed(data[:-1])).index(last_num)
            new_num = turn - prev_turn
        data.append(new_num)

        if turn == 2020:
            print(new_num)
            return


def solve_part_two(data):
    numbers = {x: [i + 1] for i, x in enumerate(data)}
    turn = len(data)
    last_num = data[-1:][0]
    while True:
        turn += 1
        new_num = 0
        if len(numbers[last_num]) == 2:
            new_num = numbers[last_num][0] - numbers[last_num][1]
        if new_num not in numbers.keys():
            numbers[new_num] = [turn]
        else:
            numbers[new_num].insert(0, turn)
        numbers[new_num] = numbers[new_num][:2]
        last_num = new_num

        if turn == 30000000:
            print(new_num)
            return


if __name__ == '__main__':
    data_example = [0, 3, 6]
    data = [8, 0, 17, 4, 1, 12]

    solve_part_one(data.copy())
    solve_part_two(data)
