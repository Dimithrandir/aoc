def solve_part_one(data):

    links = [ (x.split('-')[0], x.split('-')[1] ) for x in data ]
    graph = { key: [ y for x in links for y in x if key in x and key != y ] for key in set([ x for y in links for x in y]) }
    visited = []
    cur_path = []
    paths = []

    def find_paths(start, end):
        if start in visited and start.islower():
            return
        visited.append(start)
        cur_path.append(start)
        if start == end:
            paths.append(cur_path.copy())
            visited.remove(start)
            cur_path.pop()
            return
        for node in graph[start]:
            find_paths(node, end)
        cur_path.pop()
        visited.remove(start)
    
    find_paths('start', 'end')

    print(len(paths))

def solve_part_two(data):

    links = [ (x.split('-')[0], x.split('-')[1] ) for x in data ]
    graph = { key: [ y for x in links for y in x if key in x and key != y ] for key in set([ x for y in links for x in y]) }
    visited = []
    cur_path = []
    paths = []

    def find_paths(start, end):
        if start in visited and start.islower():
            if start in ('start', 'end'):
                return
            else:
                small_caves_nums = {key: len([ x for x in visited if x == key]) for key in set(visited) if key.islower() and key not in ('start', 'end')}
                visited_twice = [ x for x in small_caves_nums if small_caves_nums[x] > 1 ]
                if visited_twice:
                    return
        visited.append(start)
        cur_path.append(start)
        if start == end:
            paths.append(cur_path.copy())
            visited.remove(start)
            cur_path.pop()
            return
        for node in graph[start]:
            find_paths(node, end)
        cur_path.pop()
        visited.remove(start)
    
    find_paths('start', 'end')

    print(len(paths))

if __name__ == '__main__':
    with open('input') as file:
        data = file.read().splitlines()

    solve_part_one(data)
    solve_part_two(data)
