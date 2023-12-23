from collections import deque, defaultdict
from heapq import heappush, heappop

LEFT, RIGHT, UP, DOWN = (-1, 0), (1, 0), (0, -1), (0, 1)

REVERSE_OF = {
    LEFT: RIGHT,
    RIGHT: LEFT,
    UP: DOWN,
    DOWN: UP,
}


def part_1_answer(lines):
    end_pos, distances = find_distances(lines, part_1_neighbours)
    return min(dist for ((pos, _, _), dist) in distances.items() if pos == end_pos)


def part_2_answer(lines):
    end_pos, distances = find_distances(lines, part_2_neighbours)
    return min(dist for ((pos, _, current_len), dist) in distances.items() if (pos == end_pos) and (current_len >= 4))


def find_distances(lines, neighbour_function):
    grid = [[int(n) for n in row] for row in lines]

    width, height = len(grid[0]), len(grid)
    end_pos = (width - 1), (height - 1)

    edges = build_graph(width, height, neighbour_function)

    return end_pos, shortest_path(grid, edges)


def build_graph(width, height, neighbour_function):
    start = ((0, 0), None, 0)

    seen = set()
    to_explore = deque()

    edges = defaultdict(set)

    seen.add(start)
    to_explore.append(start)

    while len(to_explore) > 0:
        current = to_explore.popleft()
        pos, current_dir, current_len = current
        for neighbour in neighbour_function(pos, current_dir, current_len, width, height):
            edges[current].add(neighbour)
            if neighbour not in seen:
                seen.add(neighbour)
                to_explore.append(neighbour)

    return edges


def part_1_neighbours(pos, current_dir, current_len, width, height):
    if current_dir is None:
        yield from initial_moves()
    elif current_len < 3:
        yield from continue_or_change_direction(pos, current_dir, current_len, width, height)
    elif current_len == 3:
        yield from change_direction(pos, current_dir, width, height)


def part_2_neighbours(pos, current_dir, current_len, width, height):
    if current_dir is None:
        yield from initial_moves()
    elif current_len < 4:
        yield from continue_in_same_direction(pos, current_dir, current_len, width, height)
    elif 4 <= current_len < 10:
        yield from continue_or_change_direction(pos, current_dir, current_len, width, height)
    elif current_len == 10:
        yield from change_direction(pos, current_dir, width, height)


def initial_moves():
    for offset in RIGHT, DOWN:
        yield offset, offset, 1


def continue_or_change_direction(pos, current_dir, current_len, width, height):
    yield from continue_in_same_direction(pos, current_dir, current_len, width, height)
    yield from change_direction(pos, current_dir, width, height)


def continue_in_same_direction(pos, current_dir, current_len, width, height):
    x, y = pos
    nx, ny = (x + current_dir[0]), (y + current_dir[1])
    if (0 <= nx < width) and (0 <= ny < height):
        yield (nx, ny), current_dir, (current_len + 1)


def change_direction(pos, current_dir, width, height):
    x, y = pos

    for offset in LEFT, RIGHT, UP, DOWN:
        if offset not in {current_dir, REVERSE_OF[current_dir]}:
            nx, ny = (x + offset[0]), (y + offset[1])
            if (0 <= nx < width) and (0 <= ny < height):
                yield (nx, ny), offset, 1


def shortest_path(grid, edges):
    start = ((0, 0), None, 0)

    dist = {start: 0}
    q = [(0, start)]

    while len(q) > 0:
        u = heappop(q)[1]
        for v in edges[u]:
            alt = dist[u] + heat_loss(grid, v[0])
            if (v not in dist) or (alt < dist[v]):
                dist[v] = alt
                heappush(q, (alt, v))

    return dist


def heat_loss(grid, pos):
    x, y = pos
    return grid[y][x]
