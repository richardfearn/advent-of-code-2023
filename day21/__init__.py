import numpy as np


def part_1_answer(lines, steps):
    _, garden_plots, start_pos = parse(lines)

    current = {start_pos}

    for _ in range(steps):
        new_positions = set()
        for pos in current:
            for n in neighbour(pos):
                if n in garden_plots:
                    new_positions.add(n)
        current = new_positions

    return len(current)


def neighbour(pos):
    x, y = pos
    yield x, (y - 1)
    yield x, (y + 1)
    yield (x + 1), y
    yield (x - 1), y


def part_2_answer(lines, steps):
    (width, height), garden_plots, start_pos = parse(lines)

    current = {start_pos}

    data = []

    for i in range(1, 65 + 131 + 131 + 1):
        new_positions = set()
        for pos in current:
            for n in neighbour(pos):
                if is_garden_plot(n, width, height, garden_plots):
                    new_positions.add(n)
        current = new_positions
        if ((i - 65) % 131) == 0:
            data.append(len(current))

    fn = fit(data)
    return fn((steps - 65) // 131)


def fit(data):
    fn = np.polynomial.Polynomial.fit([0, 1, 2], data, deg=2)
    c, b, a = [round(n) for n in fn.convert().coef]
    return lambda x: (a * x * x) + (b * x) + c


def is_garden_plot(pos, width, height, garden_plots):
    x, y = pos
    return (x % width, y % height) in garden_plots


def parse(lines):
    width, height = len(lines[0]), len(lines)

    garden_plots = set()
    start_pos = None

    for y, row in enumerate(lines):
        for x, c in enumerate(row):
            pos = (x, y)
            if c in {".", "S"}:
                garden_plots.add(pos)
            if c == "S":
                start_pos = pos

    return (width, height), garden_plots, start_pos
