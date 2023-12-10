import re
import math


def part_1_answer(lines):
    times = [int(n) for n in re.findall(r"\d+", lines[0])]
    distances = [int(n) for n in re.findall(r"\d+", lines[1])]
    races = zip(times, distances)
    return math.prod(ways_to_beat_record(t, d) for (t, d) in races)


def part_2_answer(lines):
    race_time, best_distance = [int(line.split(":")[1].replace(" ", "")) for line in lines]
    return ways_to_beat_record(race_time, best_distance)


def ways_to_beat_record(race_time, best_distance):
    min_time, max_time = find_min_max_times(race_time, best_distance)
    return max_time - min_time + 1


def find_min_max_times(race_time, best_distance):
    """
    Let t be the time allowed for the race
    Let x be the charging time
    Let y be the distance travelled
    Let d be the best distance ever recorded

      y = (t - x) * x
        = tx - x²
        = -x² + tx

    Best distance d is where y = -x² + tx = d
    Subtracting d from both sides gives -x² + tx - d = 0
    This is a quadratic equation with a = -1, b = t, c = -d
    """

    min_time, max_time = solve_quadratic(-1, race_time, -best_distance)
    return math.floor(min_time + 1), math.ceil(max_time - 1)


def solve_quadratic(a, b, c):
    return (
        (-b + math.sqrt(b * b - 4 * a * c)) / (2 * a),
        (-b - math.sqrt(b * b - 4 * a * c)) / (2 * a),
    )
