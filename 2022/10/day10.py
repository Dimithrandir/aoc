def solve_part_one(insts):
    
    reg_x, i = 2 * [1]
    sig_str = 0
    while i <= 220:
        if i in [ x for x in range(20, 230, 40) ]:
            sig_str += i * reg_x
        inst = insts.pop(0)
        if inst[0] == 'addx' and i < 219:
            reg_x += inst[1]
            i += 1
        i += 1
    print(sig_str)

def solve_part_two(insts):
    
    crt_n = 6
    crt_m = 40
    crt = [ ['.' for y in range(crt_m)] for x in range(crt_n) ]
    reg_x, clock = 2 * [1]
    addr = 0
    while clock <= crt_n * crt_m:
        i = (clock - 1) // crt_m
        j = (clock - 1) % crt_m
        if j in range(reg_x - 1, reg_x + 2):
            crt[i][j] = '#'
        if not addr:
            inst = insts.pop(0)
            if inst[0] == 'addx':
                addr = inst[1]
        else:
            reg_x += addr
            addr = 0
        clock += 1
    for row in crt:
        print(row)

if __name__ == '__main__':
    with open('input') as file:
        data = [ (x.split(' ')[0], '' if len(x.split(' ')) == 1 else int(x.split(' ')[1])) for x in file.read().splitlines() ]

    solve_part_one(data)
    solve_part_two(data)
