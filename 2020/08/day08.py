def solve_part_one(instr):
    i = 0
    prev_i = []
    acc = 0
    while True:
        if i in prev_i:
            break
        else:
            prev_i.append(i)
        if instr[i][0] == 'jmp':
            i = i + instr[i][2] if instr[i][1] == '+' else i - instr[i][2]
            continue
        elif instr[i][0] == 'acc':
            acc = acc + instr[i][2] if instr[i][1] == '+' else acc - instr[i][2]
        i += 1
    print(acc)


def solve_part_two(instr):

    def execute_instr(instr):
        i = 0
        prev_i = []
        acc = 0
        while i < len(instr):
            if i in prev_i:
                return False
            else:
                prev_i.append(i)
            if instr[i][0] == 'jmp':
                i = i + instr[i][2] if instr[i][1] == '+' else i - instr[i][2]
                continue
            elif instr[i][0] == 'acc':
                acc = acc + instr[i][2] if instr[i][1] == '+' else acc - instr[i][2]
            i += 1
        return acc

    for i in range(len(instr)):
        if instr[i][0] in {'jmp', 'nop'}:
            new_instr = instr.copy()
            new_instr[i] = list(new_instr[i])
            new_instr[i][0] = 'nop' if new_instr[i][0] == 'jmp' else 'jmp'
            executed = execute_instr(new_instr)
            if executed is not False:
                print(executed)
                return
            else:
                continue


if __name__ == '__main__':
    with open('input') as file:
        data = [(y[0], y[1][:1], int(y[1][1:])) for x in file.read().splitlines() for y in [x.split(' ')]]

    solve_part_one(data)
    solve_part_two(data)
