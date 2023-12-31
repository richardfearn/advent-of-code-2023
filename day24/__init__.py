from itertools import combinations
import numpy as np
from sympy import symbols, solve


def part_1_answer(lines, use_example_limits):
    paths = parse(lines)
    limits = (7, 27) if use_example_limits else (200000000000000, 400000000000000)
    return sum(1 for (path1, path2) in combinations(paths, 2) if intersect(path1, path2, limits))


def intersect(path1, path2, limits):
    min_val, max_val = limits

    p1 = np.array(path1[0][:2]).T
    v1 = np.array(path1[1][:2]).T

    p2 = np.array(path2[0][:2]).T
    v2 = np.array(path2[1][:2]).T

    intersection = seg_intersect(segment(p1, v1), segment(p2, v2))

    if intersection is not None:
        x, y = intersection

        if all(min_val <= n <= max_val for n in (x, y)):

            t1 = (intersection - p1) / v1
            t2 = (intersection - p2) / v2

            if (t1[0] > 0) and (t2[0] > 0):
                # both arrive at intersection point in the future
                return True

    return False


def segment(p, v):
    return p, (p + v)


# Based on https://stackoverflow.com/a/3252222/200609
def seg_intersect(segment1, segment2):
    a1, a2 = segment1
    b1, b2 = segment2

    da = a2 - a1
    db = b2 - b1
    dp = a1 - b1
    dap = perpendicular(da)
    denominator = np.dot(dap, db)
    if denominator == 0:
        return None
    numerator = np.dot(dap, dp)
    return (numerator / denominator.astype(float)) * db + b1


def perpendicular(a):
    b = np.empty_like(a)
    b[0] = -a[1]
    b[1] = a[0]
    return b


def part_2_answer(lines):
    paths = parse(lines)
    solution = find_solution(paths)
    return sum(solution)


def find_solution(paths):
    # pylint:disable=too-many-locals

    # Based on https://www.reddit.com/r/adventofcode/comments/18pnycy/comment/kf4mh2l/

    # Naming convention:
    #
    #   (px<n>, py<n>, pz<n>) is the initial position of hailstone n
    #   (pxr, pyr, pzr) is the initial position of the rock
    #
    #   (vx<n>, vy<n>, vz<n>) is the velocity of hailstone n
    #   (vxr, vyr, vzr) is the velocity of the rock

    (px1, py1, pz1), (vx1, vy1, vz1) = paths[0]
    (px2, py2, pz2), (vx2, vy2, vz2) = paths[1]
    (px3, py3, pz3), (vx3, vy3, vz3) = paths[2]

    pxr = symbols("pxr")
    pyr = symbols("pyr")
    pzr = symbols("pzr")

    vxr = symbols("vxr")
    vyr = symbols("vyr")
    vzr = symbols("vzr")

    # Taking just the x coordinate of the 1st hailstone:
    # We need the time t1 where the rock / hailstone are at the same x position.
    #
    # This is where:
    #   px1 + (t1 * vx1) = pxr + (t1 * vxr)
    #
    # So:
    #   t1 = (pxr - px1) / (vx1 - vxr)
    #
    # Similarly, for y/z:
    #   t1 = (pyr - py1) / (vy1 - vyr)
    #   t1 = (pzr - pz1) / (vz1 - vzr)
    #
    # Combining the x/y equations:
    #   (pxr - px1) / (vx1 - vxr) = (pyr - py1) / (vy1 - vyr)
    #
    # Multiplying to remove the division:
    #   (pxr - px1) * (vy1 - vyr) = (pyr - py1) * (vx1 - vxr)
    #
    # Which means:
    #   (pxr - px1) * (vy1 - vyr) - (pyr - py1) * (vx1 - vxr) = 0
    #
    # Similarly, for y/z:
    #   (pyr - py1) * (vz1 - vzr) - (pzr - pz1) * (vy1 - vyr) = 0
    #
    # We can then form two more pairs (x/y and y/z) - one for hailstone 2, and one for hailstone 3.

    system = [
        (pxr - px1) * (vy1 - vyr) - (pyr - py1) * (vx1 - vxr),
        (pyr - py1) * (vz1 - vzr) - (pzr - pz1) * (vy1 - vyr),

        (pxr - px2) * (vy2 - vyr) - (pyr - py2) * (vx2 - vxr),
        (pyr - py2) * (vz2 - vzr) - (pzr - pz2) * (vy2 - vyr),

        (pxr - px3) * (vy3 - vyr) - (pyr - py3) * (vx3 - vxr),
        (pyr - py3) * (vz3 - vzr) - (pzr - pz3) * (vy3 - vyr),
    ]

    solutions = solve(system, [pxr, pyr, pzr, vxr, vyr, vzr], dict=True)

    for solution in solutions:
        if all(is_integer(solution[n]) for n in (vxr, vyr, vzr)):
            return tuple(solution[i] for i in (pxr, pyr, pzr))

    return None


def is_integer(n):
    return n == int(n)


def parse(lines):
    paths = [line.split("@") for line in lines]
    paths = [[part.split(",") for part in path] for path in paths]
    paths = [[[int(n) for n in part] for part in path] for path in paths]
    return paths
