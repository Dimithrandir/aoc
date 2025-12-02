def solve_part_one(ranges):

    total = 0

    for r in ranges:
        first_id = r[0]
        last_id = r[1]

        len_first = len(r[0])
        len_last = len(r[1])

        if (len_first % 2 and len_last % 2):
            continue

        start = str(10 ** len_first) if len_first % 2 else first_id
        end = str(10 ** (len_last - 1) - 1) if len_last % 2 else last_id

        start = start[:len(start)//2]
        end = end[:len(end)//2]

        for sequence in range(int(start), int(end) + 1):
            id_num = int(str(sequence) + str(sequence))
            if id_num in range(int(first_id), int(last_id) + 1):
                total += id_num

    print(total)


def solve_part_two(ranges):

    invalid_ids = set()

    for r in ranges:
        first_id = r[0]
        last_id = r[1]

        len_first = len(r[0])
        len_last = len(r[1])

        # rep = number of times some sequence is repeated
        for rep in range(2, len_last + 1):

            if (len_first % rep and len_last % rep):
                continue

            start = str(10 ** len_first) if len_first % rep else first_id
            end = str(10 ** (len_last - 1) - 1) if len_last % rep else last_id

            start = start[:len(start)//rep]
            end = end[:len(end)//rep]

            for sequence in range(int(start), int(end) + 1):
                id_num = int(str(sequence) * rep)
                if id_num in range(int(first_id), int(last_id) + 1):
                    invalid_ids.add(id_num)

    print(sum(invalid_ids))


if __name__ == '__main__':
    with open('input') as file:
        data = [x.split('-') for x in file.read().rstrip().split(',')]

    solve_part_one(data)
    solve_part_two(data)
