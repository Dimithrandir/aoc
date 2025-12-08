def solve_part_one(diagram):

    beams = diagram[0][1]
    splits = 0
    for i in range(1, len(diagram)):
        new_beams = []
        for beam in beams:
            if beam in diagram[i][1]:
                new_beams.extend([beam - 1, beam + 1])
                splits += 1
            else:
                new_beams.append(beam)
        beams = list(set(new_beams))

    print(splits)


def solve_part_two(diagram):

    beams = {diagram[0][1][0]: 1}
    for i in range(1, len(diagram)):
        for beam in sorted([x for x in beams.keys()]):
            if beam in diagram[i][1]:
                beams[beam-1] = (beams[beam] if beam - 1 not in beams.keys()
                                 else beams[beam-1] + beams[beam])
                beams[beam+1] = (beams[beam] if beam + 1 not in beams.keys()
                                 else beams[beam+1] + beams[beam])
                beams[beam] = 0

    print(sum(beams.values()))


if __name__ == '__main__':
    with open('input') as file:
        data = [(i, [j for j, y in enumerate(x) if y in 'S^'])
                for i, x in enumerate(file.read().splitlines())]

    solve_part_one(data)
    solve_part_two(data)
