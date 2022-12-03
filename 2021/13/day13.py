def solve_part_one(points, instructions):
    dots = 0
    direc = instructions[0][0]

    m = 0
    n = 0
    for instr in instructions:
        if instr[0] == 'x':
            m = int(instr[1]) * 2 + 1
        elif instr[0] == 'y':
            n = int(instr[1]) * 2 + 1
        if m and n:
            break

    paper = []
    for i in range(n):
        paper.append( m * [0])

    for point in points:
        paper[point[1]][point[0]] = 1

    bend = int(instructions[0][1])
    folded = []
    if direc == 'y':
        for i in range(bend):
            folded.append([])
            for j in range(m):
                folded[i].append(paper[i][j] or paper[n - 1 - i][j])
                if folded[i][j]:
                    dots += 1
    elif direc == 'x':
        for i in range(n):
            folded.append([])
            for j in range(bend):
                folded[i].append(paper[i][j] or paper[i][m - 1 - j])
                if folded[i][j]:
                    dots += 1

    print(dots)

def solve_part_two(points, instructions):

    m = 0
    n = 0
    for instr in instructions:
        if instr[0] == 'x':
            m = int(instr[1]) * 2 + 1
        elif instr[0] == 'y':
            n = int(instr[1]) * 2 + 1
        if m and n:
            break

    paper = []
    for i in range(n):
        paper.append(m * [0])

    for point in points:
        paper[point[1]][point[0]] = 1

    folded = None
    for instr in instructions:
        folded = []
        direc = instr[0]
        bend = int(instr[1])
        if direc == 'y':
            for i in range(bend):
                folded.append([])
                for j in range(m):
                    folded[i].append(paper[i][j] or paper[n - 1 - i][j])
        elif direc == 'x':
            for i in range(n):
                folded.append([])
                for j in range(bend):
                    folded[i].append(paper[i][j] or paper[i][m - 1 - j])
        paper = folded
        n = len(folded)
        m = len(folded[0])

    for f in folded:
        print(f)

if __name__ == '__main__':
    dots = []
    instructions = []
    with open('input') as file:
        for line in file.read().splitlines():
            if 'fold along' in line:
                inst_line = line.split('=')
                instructions.append((inst_line[0][-1], int(inst_line[1])))
            elif line:
                point_line = line.split(',')
                dots.append((int(point_line[0]), int(point_line[1])))

    solve_part_one(dots, instructions)
    solve_part_two(dots, instructions)
