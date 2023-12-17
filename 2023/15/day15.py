def get_hash(string):
    cur_val = 0
    for char in string:
        cur_val += ord(char)
        cur_val *= 17
        cur_val %= 256
    return cur_val


def solve_part_one(sequence):
    total = 0
    for step in sequence:
        total += get_hash(step)

    print(total)


def solve_part_two(sequence):
    boxes = {x: {} for x in range(256)}
    for step in sequence:
        operation = step[max(step.find('='), step.find('-'))]
        label = step.split(operation)[0]
        box_num = get_hash(label)
        if operation == '=':
            focal_len = int(step[-1])
            if label not in boxes[box_num].keys():
                boxes[box_num][label] = [focal_len, len(boxes[box_num].keys())]
            else:
                boxes[box_num][label] = [focal_len, boxes[box_num][label][1]]
        elif operation == '-':
            if label in boxes[box_num].keys():
                lens_index = boxes[box_num][label][1]
                boxes[box_num].pop(label)
                for key, val in boxes[box_num].items():
                    if val[1] > lens_index:
                        boxes[box_num][key][1] -= 1

    total = 0
    for i in range(256):
        for lens in boxes[i].keys():
            total += (i + 1) * (boxes[i][lens][1] + 1) * boxes[i][lens][0]

    print(total)


if __name__ == '__main__':
    with open('input') as file:
        data = file.read().replace('\n', '').split(',')

    solve_part_one(data)
    solve_part_two(data)
