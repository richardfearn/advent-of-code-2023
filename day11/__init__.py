from heapq import heappop, heappush


def part_1_answer(lines):
    return answer(lines, 2)


def part_2_answer(lines, scale_factor=1_000_000):
    return answer(lines, scale_factor)


def answer(grid, scale_factor):
    width = len(grid[0])
    height = len(grid)

    empty_rows, empty_columns = find_empty_rows_and_columns(grid, width, height)
    galaxies = find_galaxies(grid, width, height)

    all_galaxy_distances = find_galaxy_distances(galaxies, empty_rows, empty_columns, scale_factor, width, height)
    return sum(all_galaxy_distances) // 2


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


def find_galaxy_distances(galaxies, empty_rows, empty_columns, scale_factor, width, height):
    # pylint: disable=too-many-arguments,too-many-locals

    all_galaxy_distances = []

    for start_pos in galaxies:

        dist = {start_pos: 0}
        q = [(0, start_pos)]

        while len(q) > 0:
            u = heappop(q)[1]
            for v in neighbours(u, width, height):
                nx, ny = v
                step_dist = scale_factor if ((ny in empty_rows) or (nx in empty_columns)) else 1
                alt = dist[u] + step_dist
                if (v not in dist) or (alt < dist[v]):
                    dist[v] = alt
                    heappush(q, (alt, v))

        galaxy_distances = [dist[g] for g in galaxies]
        all_galaxy_distances.extend(galaxy_distances)

    return all_galaxy_distances


def neighbours(pos, width, height):
    x, y = pos
    for ox, oy in (-1, 0), (1, 0), (0, -1), (0, 1):
        nx, ny = (x + ox), (y + oy)
        if (0 <= nx < width) and (0 <= ny < height):
            yield nx, ny
