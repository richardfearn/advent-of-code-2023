from collections import deque

LEFT, RIGHT, UP, DOWN = (-1, 0), (1, 0), (0, -1), (0, 1)


def part_1_answer(lines):
    return num_energized_tiles(lines, (0, 0), RIGHT)


def num_energized_tiles(grid, start_pos, start_direction):
    # pylint: disable=too-many-locals

    width, height = len(grid[0]), len(grid)
    grid_size = (width, height)

    energized_tiles = set()

    start = (start_pos, start_direction)
    seen = set(start)
    to_explore = deque([start])

    while len(to_explore) > 0:
        pos, direction = to_explore.popleft()
        x, y = pos
        energized_tiles.add(pos)
        tile = grid[y][x]
        for neighbour in neighbours(pos, direction, tile):
            if in_grid(neighbour[0], grid_size) and (neighbour not in seen):
                seen.add(neighbour)
                to_explore.append(neighbour)

    return len(energized_tiles)


def neighbours(pos, direction, tile):
    # pylint: disable=too-many-branches

    x, y = pos
    dx, dy = direction

    if tile == ".":
        yield (x + dx, y + dy), direction

    elif tile == "/":
        if direction == RIGHT:
            yield up(x, y), UP
        elif direction == LEFT:
            yield down(x, y), DOWN
        elif direction == DOWN:
            yield left(x, y), LEFT
        elif direction == UP:
            yield right(x, y), RIGHT

    elif tile == "\\":
        if direction == RIGHT:
            yield down(x, y), DOWN
        elif direction == LEFT:
            yield up(x, y), UP
        elif direction == DOWN:
            yield right(x, y), RIGHT
        elif direction == UP:
            yield left(x, y), LEFT

    elif tile == "|":
        if dy == 0:
            yield up(x, y), UP
            yield down(x, y), DOWN
        elif dx == 0:
            yield (x + dx, y + dy), direction

    elif tile == "-":
        if dx == 0:
            yield left(x, y), LEFT
            yield right(x, y), RIGHT
        elif dy == 0:
            yield (x + dx, y + dy), direction


def left(x, y):
    return (x - 1), y


def right(x, y):
    return (x + 1), y


def up(x, y):
    return x, (y - 1)


def down(x, y):
    return x, (y + 1)


def in_grid(pos, grid_size):
    x, y = pos
    width, height = grid_size
    return (0 <= x < width) and (0 <= y < height)


def part_2_answer(lines):
    return max(energized_tile_counts(lines))


def energized_tile_counts(lines):
    width, height = len(lines[0]), len(lines)

    for y in range(0, height):
        yield num_energized_tiles(lines, (0, y), RIGHT)
        yield num_energized_tiles(lines, (width - 1, y), LEFT)

    for x in range(0, width):
        yield num_energized_tiles(lines, (x, 0), DOWN)
        yield num_energized_tiles(lines, (x, height - 1), UP)
