class Node():

    def __init__(self, value='', level=0, next_node=None):
        self.value = value
        self.level = level
        self.next = next_node


def calculate(expr_list):
    result = int(expr_list[0])
    for i in range(1, len(expr_list) - 1, 2):
        if expr_list[i] == '+':
            result += int(expr_list[i+1])
        if expr_list[i] == '*':
            result *= int(expr_list[i+1])
    return result


def calculate_diff_prec(expr_list):
    expr_list = ''.join(expr_list).split('*')
    result = 1
    for item in expr_list:
        result *= int(item) if not item.count('+') else eval(item)
    return result


def solve_part_one(expressions, diff_precedence=False):
    total = 0
    for expr in expressions:
        result = 0
        # create linked list
        level = expr[0].count('(')
        max_level = level
        first_el = Node(expr[0].lstrip('('), level)
        last_el = first_el
        for i in range(1, len(expr)):
            level += expr[i].count('(')
            max_level = max(max_level, level)
            new_node = Node(expr[i].strip('()'), level)
            last_el.next = new_node
            last_el = new_node
            level -= expr[i].count(')')
        # calculate expression
        while True:
            el = first_el
            # go though list and simplify every higher level
            while max_level >= 0:
                if el.next and el.next.level == max_level:
                    new_el = Node()
                    sub_el = el if el == first_el else el.next
                    expr_list = []
                    while True:
                        expr_list.append(sub_el.value)
                        if not sub_el.next or sub_el.next.level < max_level:
                            break
                        else:
                            sub_el = sub_el.next
                    new_el.value = str(calculate_diff_prec(expr_list) if diff_precedence else calculate(expr_list))
                    new_el.level = max_level - 1
                    new_el.next = sub_el.next
                    if el == first_el:
                        el = new_el
                        first_el = el
                    else:
                        el.next = new_el
                else:
                    el = el.next

                if not el:
                    break
            max_level -= 1
            # calculate last level
            if max_level <= 0:
                expr_list = []
                while True:
                    expr_list.append(first_el.value)
                    if not first_el.next:
                        break
                    else:
                        first_el = first_el.next
                result = calculate_diff_prec(expr_list) if diff_precedence else calculate(expr_list)
                total += result
                break
    print(total)


def solve_part_two(expressions):
    solve_part_one(expressions, diff_precedence=True)


if __name__ == '__main__':
    with open('input') as file:
        data = [y for x in file.read().splitlines() for y in [x.split()]]

    solve_part_one(data)
    solve_part_two(data)
