ROUNDED_ROCK = "O"
FREE_SPACE = "."

TOTAL_CYCLES = 1_000_000_000


def part_1_answer(lines):
    grid = [list(line) for line in lines]
    tilt_north(grid)
    return total_load(grid)


def tilt_north(grid):
    top_row = 0
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == ROUNDED_ROCK:
                nx, ny = x, y
                while (ny > top_row) and (grid[ny - 1][nx] == FREE_SPACE):
                    ny -= 1
                move_rounded_rock(grid, (x, y), (nx, ny))


def tilt_west(grid):
    left_column = 0
    for y, row in enumerate(grid):
        for x, c in enumerate(row):
            if c == ROUNDED_ROCK:
                nx, ny = x, y
                while (nx > left_column) and (grid[ny][nx - 1] == FREE_SPACE):
                    nx -= 1
                move_rounded_rock(grid, (x, y), (nx, ny))


def tilt_south(grid):
    height = len(grid)
    bottom_row = height - 1
    for y, row in reversed_enumerate(grid):
        for x, c in enumerate(row):
            if c == ROUNDED_ROCK:
                nx, ny = x, y
                while (ny < bottom_row) and (grid[ny + 1][nx] == FREE_SPACE):
                    ny += 1
                move_rounded_rock(grid, (x, y), (nx, ny))


def tilt_east(grid):
    width = len(grid[0])
    right_column = width - 1
    for y, row in enumerate(grid):
        for x, c in reversed_enumerate(row):
            if c == ROUNDED_ROCK:
                nx, ny = x, y
                while (nx < right_column) and (grid[ny][nx + 1] == FREE_SPACE):
                    nx += 1
                move_rounded_rock(grid, (x, y), (nx, ny))


def move_rounded_rock(grid, old_pos, new_pos):
    if old_pos != new_pos:
        old_x, old_y = old_pos
        new_x, new_y = new_pos
        grid[old_y][old_x] = FREE_SPACE
        grid[new_y][new_x] = ROUNDED_ROCK


def total_load(grid):
    height = len(grid)
    total = 0
    for y, row in enumerate(grid):
        row_load = height - y
        num_rounded_rocks = row.count(ROUNDED_ROCK)
        total_row_load = num_rounded_rocks * row_load
        total += total_row_load
    return total


def part_2_answer(lines):
    grid = [list(line) for line in lines]

    seen = {grid_summary(grid): 0}

    num_cycles = 0
    while num_cycles < TOTAL_CYCLES:

        spin_cycle(grid)
        num_cycles += 1

        new_state = grid_summary(grid)
        if new_state in seen:
            cycle_length = num_cycles - seen[new_state]
            num_complete_cycles_to_add = (TOTAL_CYCLES - num_cycles) // cycle_length
            num_cycles += num_complete_cycles_to_add * cycle_length
        else:
            seen[new_state] = num_cycles

    return total_load(grid)


def spin_cycle(grid):
    tilt_north(grid)
    tilt_west(grid)
    tilt_south(grid)
    tilt_east(grid)


def grid_summary(grid):
    return tuple(tuple(row) for row in grid)


def reversed_enumerate(seq):
    for i in reversed(range(len(seq))):
        yield i, seq[i]
