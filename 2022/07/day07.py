dirs = {}
sizes = {}

def find_size(node):
    size = 0
    for file in dirs[node]:
        if file.isdigit():
            size += int(file)
    for d in dirs[node]:
        if not d.isdigit():
            size += find_size(node + ('/' if node != '/' else '') + d)

    sizes[node] = size
    return size

def solve_part_one(commands):

    cur_dir = ''
    i = 0

    while i < len(commands):
        cmd = commands[i]
        if cmd[:4] == '$ cd':
            if cmd[-2:] == '..':
                cur_dir = cur_dir.rsplit('/', 1)[0]
                if not cur_dir:
                    cur_dir = '/'
                i += 1
            else:
                if not cur_dir:
                    cur_dir = cmd[5:]
                elif cur_dir == '/':
                    cur_dir += cmd[5:]
                else:
                    cur_dir += '/' + cmd[5:]

                if cur_dir not in dirs:
                    dirs[cur_dir] = []
                j = i + 2
                while j < len(commands) and commands[j][0] != '$':
                    if commands[j][:3] == 'dir':
                        dirs[cur_dir].append(commands[j][4:])
                    else:
                        dirs[cur_dir].append(commands[j].split(' ')[0])
                    j += 1
                i = j

    find_size('/')

    print(sum([ x for x in sizes.values() if x <= 100000 ]))

def solve_part_two(commands):
    total = 70000000
    update = 30000000
    unused = total - max([ x for x in sizes.values() ])
    required = update - unused
    print(sorted([ x for x in sizes.values() if x > required ])[0])

if __name__ == '__main__':
    with open('input') as file:
        data = file.read().splitlines()

    solve_part_one(data)
    solve_part_two(data)
