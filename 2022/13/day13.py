def compare(left_pack, right_pack):

    while left_pack and right_pack:
        left = left_pack.pop(0)
        right = right_pack.pop(0)
        if type(left) == int and type(right) == int:
            if left < right:
                return True
            if left > right:
                return False
        else:
            cmp = compare(left if type(left) == list else [left], right if type(right) == list else [right])
            if cmp != None:
                return cmp

    if not left_pack and not right_pack:
        return None
    if right_pack:
        return True
    if left_pack:
        return False

def solve_part_one(packets):
    in_order = []
    for (i, pair) in enumerate(packets):
        if compare(pair[0], pair[1]):
            in_order.append(i + 1)
    print(sum(in_order))

def solve_part_two(packets):
    divs = ['[[2]]', '[[6]]']
    all_packs = [ str(y) for x in packets for y in x ]
    all_packs.extend(divs)
    
    while True:
        swapped = False
        for i in range(len(all_packs)-1):
            if not compare(eval(all_packs[i]), eval(all_packs[i+1])):
                temp = all_packs[i]
                all_packs[i] = all_packs[i+1]
                all_packs[i+1] = temp
                swapped = True
        if not swapped:
            break

    print((all_packs.index(divs[0]) + 1) * (all_packs.index(divs[1]) + 1)) 

if __name__ == '__main__':
    with open('input') as file:
        data = [ [ eval(y) for y in x.splitlines() ] for x in file.read().split('\n\n')]

    solve_part_one(data)
    solve_part_two(data)
