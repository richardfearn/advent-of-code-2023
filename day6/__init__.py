import re
import math


def part_1_answer(lines):
    times = [int(n) for n in re.findall(r"\d+", lines[0])]
    distances = [int(n) for n in re.findall(r"\d+", lines[1])]
    races = zip(times, distances)
    return math.prod(ways_to_beat_record(t, d) for (t, d) in races)


def ways_to_beat_record(race_time, best_distance):
    return sum(1 for charging_time in range(race_time + 1)
               if distance(race_time, charging_time) > best_distance)


def part_2_answer(lines):
    race_time, best_distance = [int(line.split(":")[1].replace(" ", "")) for line in lines]

    min_time = 0
    while distance(race_time, min_time) <= best_distance:
        min_time += 1

    max_time = race_time
    while distance(race_time, max_time) <= best_distance:
        max_time -= 1

    return max_time - min_time + 1


def distance(race_time, charging_time):
    return (race_time - charging_time) * charging_time
