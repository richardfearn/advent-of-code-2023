def part_1_answer(lines, tile_at_start):
    grid, start_pos = parse_grid(lines, tile_at_start)
    tiles_in_loop = find_loop(grid, start_pos)
    return len(tiles_in_loop) // 2


def find_loop(grid, start_pos):
    visited = set()
    visited.add(start_pos)
    to_explore = [start_pos]

    while len(to_explore) > 0:
        current_pos = to_explore.pop(0)
        x, y = current_pos
        current_tile = grid[y][x]
        for neighbour in neighbours(current_pos, current_tile):
            if neighbour not in visited:
                visited.add(neighbour)
                to_explore.append(neighbour)

    return visited


def neighbours(pos, tile):
    x, y = pos

    west = (x - 1, y)
    east = (x + 1, y)
    north = (x, y - 1)
    south = (x, y + 1)

    if tile == "|":
        yield from (north, south)
    elif tile == "-":
        yield from (east, west)
    elif tile == "L":
        yield from (north, east)
    elif tile == "J":
        yield from (north, west)
    elif tile == "7":
        yield from (south, west)
    elif tile == "F":
        yield from (south, east)


def part_2_answer(lines, tile_at_start):
    grid, start_pos = parse_grid(lines, tile_at_start)
    tiles_in_loop = find_loop(grid, start_pos)
    clear_tiles_not_in_loop(grid, tiles_in_loop)
    tiles_inside_loop = find_tiles_inside_loop(grid, tiles_in_loop)
    return len(tiles_inside_loop)


def clear_tiles_not_in_loop(grid, tiles_in_loop):
    # Replace tiles that aren't part of the loop with "."
    # (so we only encounter properly-connected pipes)
    for y, row in enumerate(grid):
        for x in range(len(row)):
            if (x, y) not in tiles_in_loop:
                grid[y][x] = "."


def find_tiles_inside_loop(grid, tiles_in_loop):
    width = len(grid[0])
    tiles_inside = set()

    for y, row in enumerate(grid):

        crossings = 0
        x = 0

        while x != width:

            pos = (x, y)
            tile = row[x]

            if tile in "FL":

                left = tile

                # Move along to the next J/7
                while row[x] not in "J7":
                    x += 1

                right = row[x]

                if (left, right) in (("L", "7"), ("F", "J")):
                    crossings += 1

            elif tile == "|":
                crossings += 1

            else:
                if (pos not in tiles_in_loop) and ((crossings % 2) == 1):
                    tiles_inside.add(pos)

            x += 1

    return tiles_inside


def parse_grid(lines, tile_at_start):
    grid = [list(line) for line in lines]

    sy = next(y for (y, row) in enumerate(grid) if "S" in row)
    sx = grid[sy].index("S")
    start_pos = (sx, sy)
    grid[sy][sx] = tile_at_start

    return grid, start_pos
