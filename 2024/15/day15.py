dirs = {'^': (-1, 0), '>': (0, 1), 'v': (1, 0), '<': (0, -1)}


def map_warehouse(warehouse, wide=False):
    n = len(warehouse)
    walls = []
    boxes = {'[': [], ']': []} if wide else set()
    rob = ()
    for i in range(n):
        for j in range(len(warehouse[i])):
            if warehouse[i][j] == '#':
                if wide:
                    walls.append((i, j * 2))
                    walls.append((i, j * 2 + 1))
                else:
                    walls.append((i, j))
            elif warehouse[i][j] == 'O':
                if wide:
                    boxes['['].append((i, j * 2))
                    boxes[']'].append((i, j * 2 + 1))
                else:
                    boxes.add((i, j))
            elif warehouse[i][j] == '@':
                if wide:
                    rob = (i, j * 2)
                else:
                    rob = (i, j)
    return rob, walls, boxes


def solve_part_one(warehouse, moves):
    rob, walls, boxes = map_warehouse(warehouse)
    total = 0

    for move in moves:
        next_pos = (rob[0] + dirs[move][0], rob[1] + dirs[move][1])
        if next_pos in walls:
            continue
        elif next_pos in boxes:
            temp_pos = next_pos
            box_line = set()
            while temp_pos in boxes:
                box_line.add(temp_pos)
                temp_pos = (temp_pos[0] + dirs[move][0],
                            temp_pos[1] + dirs[move][1])

            if temp_pos not in walls:
                boxes -= box_line
                for box in box_line:
                    boxes.add((box[0] + dirs[move][0], box[1] + dirs[move][1]))
                rob = next_pos
        else:
            rob = next_pos

    for box in boxes:
        total += 100 * box[0] + box[1]

    print(total)


def solve_part_two(warehouse, moves):

    def get_all_boxes(root, boxes, move):
        left_brack = (boxes['['][root][0] + dirs[move][0], boxes['['][root][1])
        right_brack = (boxes[']'][root][0] + dirs[move][0], boxes[']'][root][1])
        left_root = None
        right_root = None

        if left_brack in boxes['[']:
            left_root = boxes['['].index(left_brack)
        else:
            if left_brack in boxes[']']:
                left_root = boxes[']'].index(left_brack)
            if right_brack in boxes['[']:
                right_root = boxes['['].index(right_brack)

        return ((get_all_boxes(left_root, boxes, move) if left_root is not None else [])
                + [root]
                + (get_all_boxes(right_root, boxes, move) if right_root is not None else []))

    rob, walls, boxes = map_warehouse(warehouse, True)
    total = 0

    for o, move in enumerate(moves):
        next_pos = (rob[0] + dirs[move][0], rob[1] + dirs[move][1])
        if next_pos in walls:
            continue
        elif next_pos in boxes['['] or next_pos in boxes[']']:
            if move in '<>':
                temp_pos = next_pos
                boxes_to_move = []
                while temp_pos in boxes['['] or temp_pos in boxes[']']:
                    boxes_to_move.append(boxes['['].index(temp_pos)
                                         if temp_pos in boxes['[']
                                         else boxes[']'].index(temp_pos))
                    temp_pos = (temp_pos[0], temp_pos[1] + 2 * dirs[move][1])
                if temp_pos not in walls:
                    for box_i in boxes_to_move:
                        boxes['['][box_i] = (
                                boxes['['][box_i][0],
                                boxes['['][box_i][1] + dirs[move][1])
                        boxes[']'][box_i] = (
                                boxes[']'][box_i][0],
                                boxes[']'][box_i][1] + dirs[move][1])
                    rob = next_pos
            else:
                temp_pos_i = (boxes['['].index(next_pos)
                              if next_pos in boxes['[']
                              else boxes[']'].index(next_pos))

                boxes_to_move = set(get_all_boxes(temp_pos_i, boxes, move))

                wall_adjacent = [x for x in boxes_to_move
                                 if (boxes['['][x][0] + dirs[move][0], boxes['['][x][1]) in walls
                                 or (boxes[']'][x][0] + dirs[move][0], boxes[']'][x][1]) in walls]

                if wall_adjacent:
                    continue

                for box in boxes_to_move:
                    boxes['['][box] = (
                            boxes['['][box][0] + dirs[move][0],
                            boxes['['][box][1])
                    boxes[']'][box] = (
                            boxes[']'][box][0] + dirs[move][0],
                            boxes[']'][box][1])

                rob = (rob[0] + dirs[move][0], rob[1])
        else:
            rob = next_pos

    for box in boxes['[']:
        total += 100 * box[0] + box[1]

    print(total)


if __name__ == '__main__':
    with open('input') as file:
        data = file.read().split('\n\n')
        warehouse = [x for x in data[0].splitlines()]
        moves = data[1].replace('\n', '')

    solve_part_one(warehouse, moves)
    solve_part_two(warehouse, moves)
