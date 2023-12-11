def part_1_answer(lines):
    return answer(lines, 2)


def part_2_answer(lines, scale_factor=1_000_000):
    return answer(lines, scale_factor)


def answer(grid, scale_factor):
    width = len(grid[0])
    height = len(grid)

    empty_rows, empty_columns = find_empty_rows_and_columns(grid, width, height)
    galaxies = find_galaxies(grid, width, height)

    col_dists = step_dists(width, empty_columns, scale_factor)
    row_dists = step_dists(height, empty_rows, scale_factor)

    dists = []
    for i in range(len(galaxies)):
        for j in range(i + 1, len(galaxies)):
            dists.append(distance(galaxies, i, j, col_dists, row_dists))
    return sum(dists)


def find_empty_rows_and_columns(grid, width, height):
    empty_rows = set()
    for y in range(height):
        if set(grid[y]) == {"."}:
            empty_rows.add(y)

    empty_columns = set()
    for x in range(width):
        if set(row[x] for row in grid) == {"."}:
            empty_columns.add(x)

    return empty_rows, empty_columns


def find_galaxies(grid, width, height):
    galaxies = []
    for y in range(height):
        for x in range(width):
            pos = (x, y)
            if grid[y][x] == "#":
                galaxies.append(pos)
    return galaxies


def step_dists(length, empty_positions, scale_factor):
    dists = [0]
    for i in range(1, length):
        dists.append(dists[-1] + (scale_factor if (i in empty_positions) else 1))
    return dists


def distance(galaxies, i, j, col_dists, row_dists):
    x1, y1 = galaxies[i]
    x2, y2 = galaxies[j]
    horizontal_dist = abs(col_dists[x2] - col_dists[x1])
    vertical_dist = abs(row_dists[y2] - row_dists[y1])
    return horizontal_dist + vertical_dist
