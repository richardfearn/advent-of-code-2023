from collections import defaultdict, deque

LEFT, RIGHT, UP, DOWN = (-1, 0), (1, 0), (0, -1), (0, 1)

OFFSETS = {
    ".": {LEFT, RIGHT, UP, DOWN},
    "^": {UP},
    ">": {RIGHT},
    "v": {DOWN},
    "<": {LEFT},
}


def part_1_answer(lines):
    grid = parse(lines)
    return find_max_path_length(grid)


def part_2_answer(lines):
    grid = parse(lines)
    treat_slopes_as_paths(grid)
    return find_max_path_length(grid)


def treat_slopes_as_paths(grid):
    for row in grid:
        for x, c in enumerate(row):
            if c in "^>v<":
                row[x] = "."


def find_max_path_length(grid):
    width, height = len(grid[0]), len(grid)

    start_pos = (1, 0)
    end_pos = (width - 2, height - 1)

    edges = find_edges(grid, (width, height), start_pos)

    # Based on https://www.reddit.com/r/adventofcode/comments/18oy4pc/comment/kektr4z/
    edges = collapse_edges(edges)

    max_path_length = [0]
    dfs(max_path_length, end_pos, edges, start_pos, set(start_pos), 0)
    return max_path_length[0]


def find_edges(grid, grid_size, start_pos):
    edges = defaultdict(set)

    to_explore = deque()
    seen = set()

    to_explore.append(start_pos)
    seen.add(start_pos)

    while len(to_explore) > 0:

        current = to_explore.popleft()

        for n in neighbours(grid, grid_size, current):
            edges[current].add(n)
            if n not in seen:
                seen.add(n)
                to_explore.append(n)

    return edges


def neighbours(lines, grid_size, pos):
    width, height = grid_size
    x, y = pos
    c = lines[y][x]

    for offset in OFFSETS[c]:
        nx, ny = (x + offset[0]), (y + offset[1])
        if (0 <= nx < width) and (0 <= ny < height):
            if lines[ny][nx] != "#":
                yield nx, ny


def collapse_edges(edges):
    new_edges = {}

    for source, source_edges in edges.items():
        if len(source_edges) != 2:
            new_edges[source] = [measure(edges, source, adjacent) for adjacent in source_edges]

    return new_edges


def measure(edges, source, adjacent):
    distance = 1

    while len(edges[adjacent]) == 2:
        distance += 1
        next_pos = next(pos for pos in edges[adjacent] if pos != source)
        source, adjacent = adjacent, next_pos

    return distance, adjacent


def dfs(max_path_length, end_pos, edges, pos, visited, length):
    # pylint: disable=too-many-arguments

    if end_pos == pos:
        max_path_length[0] = max(max_path_length[0], length)
        return

    for weight, next_pos in edges[pos]:
        if next_pos not in visited:
            next_visited = visited | {next_pos}
            next_length = length + weight
            dfs(max_path_length, end_pos, edges, next_pos, next_visited, next_length)


def parse(lines):
    return [list(line) for line in lines]
