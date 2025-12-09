from math import dist, prod


def solve_part_one(boxes, part_two=False):

    distances = []
    for i, a in enumerate(boxes):
        for j, b in enumerate(boxes):
            if i >= j:
                continue
            distances.append([(i, j), dist(a, b)])

    distances.sort(key=lambda l: l[1])

    # circuits with > 1 junction boxes
    circuits = []
    for i in range(len(distances) if part_two else 1000):
        box_a = distances[i][0][0]
        box_b = distances[i][0][1]

        circ_a = -1
        circ_b = -1

        for j, circuit in enumerate(circuits):
            if box_a in circuit:
                circ_a = j
            if box_b in circuit:
                circ_b = j

        if circ_a >= 0 and circ_b >= 0:
            if circ_a == circ_b:
                continue
            circuits[circ_b].update((box_a, box_b))
            circuits[circ_a].update(circuits[circ_b])
            circuits.pop(circ_b)
        elif circ_a >= 0:
            circuits[circ_a].update((box_a, box_b))
        elif circ_b >= 0:
            circuits[circ_b].update((box_a, box_b))
        # new circuit
        else:
            circuits.append(set(distances[i][0]))

        if part_two and len(circuits[0]) == len(boxes):
            print(boxes[box_a][0] * boxes[box_b][0])
            return

    print(prod(sorted([len(x) for x in circuits], reverse=True)[:3]))


def solve_part_two(boxes):

    solve_part_one(boxes, part_two=True)
    return


if __name__ == '__main__':
    with open('input') as file:
        data = [[int(y) for y in x.split(',')]
                for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
