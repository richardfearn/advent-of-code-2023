from collections import defaultdict, deque
from itertools import pairwise, product


# "Each brick is made up of a single straight line of cubes"
# In the example, bricks are 2 or 3 cubes
# In the input, bricks are 1-5 cubes

# Overall volume for example is 0..2 / 0..2 / 1..9 (3 × 3, 9 high)
# Overall volume for input is 0..9 / 0..9 / 1..376 (10 × 10, 376 high)


class Brick:
    # pylint: disable=too-few-public-methods

    def __init__(self, i, x, y, z):
        self.i = i
        self.x = x
        self.y = y
        self.z = z


def part_1_answer(lines):
    bricks = parse(lines)
    add_floor(bricks)
    fall(bricks)
    under = find_bricks_immediately_under(bricks)
    return sum(1 for brick in bricks[1:] if can_disintegrate_safely(brick.i, under))


def part_2_answer(lines):
    bricks = parse(lines)
    add_floor(bricks)
    fall(bricks)
    under = find_bricks_immediately_under(bricks)
    return sum(disintegrate(brick.i, under) for brick in bricks[1:])


def add_floor(bricks):
    x_range = overall_range(lambda brick: brick.x, bricks)
    y_range = overall_range(lambda brick: brick.y, bricks)

    floor = Brick(0, x_range, y_range, range(0, 1))

    bricks.insert(0, floor)


def fall(bricks):
    bricks_below = find_bricks_below(bricks)
    fall_order = find_fall_order(bricks_below)

    for next_to_fall in fall_order:
        brick = bricks[next_to_fall]
        min_z_pos = max(bricks[other].z.stop for other in bricks_below[brick.i])
        distance_to_fall = brick.z.start - min_z_pos
        brick.z = range(brick.z.start - distance_to_fall, brick.z.stop - distance_to_fall)


def find_bricks_below(bricks):
    x_range = overall_range(lambda b: b.x, bricks)
    y_range = overall_range(lambda b: b.y, bricks)

    grid = [[[] for _ in x_range] for _ in y_range]

    for brick in bricks:
        for x, y in product(brick.x, brick.y):
            grid[y][x].append(brick)

    for x, y in product(x_range, y_range):
        grid[y][x].sort(key=lambda b: b.z.start)

    bricks_below = {b.i: set() for b in bricks}

    for x, y in product(x_range, y_range):
        for upper, lower in pairwise(grid[y][x]):
            bricks_below[lower.i].add(upper.i)

    return bricks_below


def find_fall_order(bricks_below):
    bricks_below = {k: v.copy() for (k, v) in bricks_below.items()}

    fall_order = []
    nodes_without_edges = deque(i for (i, edges) in bricks_below.items() if len(edges) == 0)

    while len(nodes_without_edges) > 0:
        n = nodes_without_edges.popleft()
        fall_order.append(n)

        for m, edges in bricks_below.items():
            if n in edges:
                edges.remove(n)
                if len(edges) == 0:
                    nodes_without_edges.append(m)

    return fall_order[1:]  # don't include floor


def can_disintegrate_safely(i, under):
    # If there are no bricks supported only by this one, it can be disintegrated safely
    return {i} not in under.values()


def find_bricks_immediately_under(bricks):
    occupancy_map = make_occupancy_map_without_floor(bricks)

    under = defaultdict(set)

    for brick in bricks:
        z = brick.z.start
        for x, y in product(brick.x, brick.y):
            pos_below = (x, y, z - 1)
            if pos_below in occupancy_map:
                under[brick.i].add(occupancy_map[pos_below])

    return under


def make_occupancy_map_without_floor(bricks):
    occupied = {}

    for brick in bricks[1:]:  # exclude floor
        for pos in product(brick.x, brick.y, brick.z):
            occupied[pos] = brick.i

    return occupied


def disintegrate(i, under):
    fallen = 0
    under = {k: v.copy() for (k, v) in under.items()}

    for edges in under.values():
        edges.discard(i)

    nodes_without_edges = deque(n for (n, edges) in under.items() if len(edges) == 0)

    while len(nodes_without_edges) > 0:
        n = nodes_without_edges.popleft()
        fallen += 1

        for m, edges in under.items():
            if n in edges:
                edges.remove(n)
                if len(edges) == 0:
                    nodes_without_edges.append(m)

    return fallen


def parse(lines):
    bricks = [line.split("~") for line in lines]
    bricks = [[pos.split(",") for pos in brick] for brick in bricks]
    bricks = [[[int(n) for n in pos] for pos in brick] for brick in bricks]
    bricks = [list(zip(*vals)) for vals in bricks]
    bricks = [[range(vals[0], vals[1] + 1) for vals in brick] for brick in bricks]
    bricks = [Brick(i + 1, *values) for i, values in enumerate(bricks)]
    return bricks


def overall_range(coord_function, bricks):
    min_val = min(coord_function(b).start for b in bricks)
    max_val = max(coord_function(b).stop for b in bricks)
    return range(min_val, max_val)
