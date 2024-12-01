def solve_part_one(lists):

    def ins_sort(li, el):
        for i in range(len(li) - 1, -1, -1):
            if el >= li[i]:
                return i + 1
        return 0

    left = []
    right = []

    for pair in lists:
        left.insert(ins_sort(left, pair[0]), pair[0])
        right.insert(ins_sort(right, pair[1]), pair[1])

    total_dist = 0
    for i in range(len(left)):
        total_dist += abs(left[i] - right[i])

    print(total_dist)


def solve_part_two(lists):

    left = []
    sim_dic = {}

    for pair in lists:
        left.append(pair[0])
        if pair[1] in sim_dic.keys():
            sim_dic[pair[1]] += 1
        else:
            sim_dic[pair[1]] = 1

    sim_score = 0
    for num in left:
        if num in sim_dic.keys():
            sim_score += num * sim_dic[num]

    print(sim_score)


if __name__ == '__main__':
    with open('input') as file:
        data = [[int(y) for y in x.split()] for x in file.read().splitlines()]

    solve_part_one(data)
    solve_part_two(data)
