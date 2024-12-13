def read_diskmap(diskmap):
    files = []
    frees = []
    for i in range(len(diskmap)):
        if i % 2:
            frees.append(diskmap[i])
        else:
            files.append(diskmap[i])
    return files, frees


def checksum(fs):
    result = 0
    for i in range(len(fs)):
        if type(fs[i]) is int:
            result += i * fs[i]
    return result


def solve_part_one(diskmap):
    files, frees = read_diskmap(diskmap)

    blocks = [0] * files[0]
    for i in range(1, len(files)):
        blocks += (['.'] * frees[i-1]) + [i] * files[i]

    j = len(blocks) - 1
    for i in range(len(blocks)):
        if i < j and blocks[i] == '.':
            for k in range(j, i, -1):
                if type(blocks[k]) is int:
                    j = k
                    break
            blocks[i] = blocks[j]
            blocks[j] = '.'
            j -= 1

    print(checksum(blocks))


def solve_part_two(diskmap):
    files, frees = read_diskmap(diskmap)

    blocks = [0] * files[0]
    files_inds = [0]
    frees_inds = []
    for i in range(1, len(files)):
        frees_inds.append(len(blocks))
        blocks += (['.'] * frees[i-1])
        files_inds.append(len(blocks))
        blocks += [i] * files[i]

    for i in range(len(files) - 1, -1, -1):
        for j in range(i):
            if frees[j] and files[i] <= frees[j]:
                frees[j] -= files[i]
                blocks[frees_inds[j]:frees_inds[j]+files[i]] = files[i] * [i]
                blocks[files_inds[i]:files_inds[i]+files[i]] = files[i] * ['.']
                files_inds[i] = frees_inds[j] + files[i]
                frees_inds[j] += files[i]
                files[i] = 0

    print(checksum(blocks))


if __name__ == '__main__':
    with open('input') as file:
        data = [int(x) for x in file.read().strip('\n')]

    solve_part_one(data)
    solve_part_two(data)
