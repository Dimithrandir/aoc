def combo_operand(reg, op):
    return op if op < 4 else reg[op-4]


def adv(reg, op):
    reg[0] //= 2**combo_operand(reg, op)


def bxl(reg, op):
    reg[1] ^= op


def bst(reg, op):
    reg[1] = combo_operand(reg, op) % 8


def jnz(reg, op):
    if reg[0]:
        return op


def bxc(reg, op):
    reg[1] ^= reg[2]


def out(reg, op):
    return str(combo_operand(reg, op) % 8) + ','


def bdv(reg, op):
    reg[1] = reg[0] // 2**combo_operand(reg, op)


def cdv(reg, op):
    reg[2] = reg[0] // 2**combo_operand(reg, op)


def run(reg, prog, p):
    return (adv(reg, prog[p+1]) if not prog[p]
            else bxl(reg, prog[p+1]) if prog[p] == 1
            else bst(reg, prog[p+1]) if prog[p] == 2
            else jnz(reg, prog[p+1]) if prog[p] == 3
            else bxc(reg, prog[p+1]) if prog[p] == 4
            else out(reg, prog[p+1]) if prog[p] == 5
            else bdv(reg, prog[p+1]) if prog[p] == 6
            else cdv(reg, prog[p+1]))


def solve_part_one(registers, program):
    output = ''
    p = 0
    while p < len(program):
        result = run(registers, program, p)
        if type(result) is int:
            p = result
            continue
        if type(result) is str:
            output += result
        p += 2
    print(output[:-1])


def solve_part_two(registers, program):
    solve_part_one(registers, program)
    pass


if __name__ == '__main__':
    with open('input') as file:
        data = file.read().split('\n\n')
        regs = [int(x.split(':')[1].strip()) for x in data[0].splitlines()]
        program = [int(x) for x in data[1].split()[1].split(',')]

    solve_part_one(regs.copy(), program)
    # solve_part_two(regs.copy(), program)
