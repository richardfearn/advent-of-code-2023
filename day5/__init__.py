from collections import namedtuple, deque
from functools import reduce
from itertools import batched
import utils

Mapping = namedtuple("Mapping", ["source_range", "destination_range_start", "range_length"])


def part_1_answer(lines):
    seeds, maps = parse(lines)
    locations = [reduce(apply_map_to_number, maps, seed) for seed in seeds]
    return min(locations)


def apply_map_to_number(n, mappings):
    for mapping in mappings:
        if n in mapping.source_range:
            return n - mapping.source_range.start + mapping.destination_range_start
    return n


def part_2_answer(lines):
    seeds, maps = parse(lines)
    seed_ranges = [range(pair[0], pair[0] + pair[1]) for pair in batched(seeds, 2)]
    location_ranges = reduce(apply_map_to_ranges, maps, seed_ranges)
    return min(r.start for r in location_ranges)


def apply_map_to_ranges(input_ranges, mappings):
    remaining_ranges = deque(input_ranges)
    output_ranges = []

    while len(remaining_ranges) > 0:
        r = remaining_ranges.popleft()
        convert_range(r, mappings, output_ranges, remaining_ranges)

    return output_ranges


def convert_range(r, mappings, output_ranges, remaining_ranges):
    for mapping in mappings:

        s = mapping.source_range

        # Range being converted is entirely within the source range:
        #
        #   SSSSSSSSSSSSSSS
        #        RRRRR
        #
        if (r.start in s) and (r.stop in s):
            output_ranges.append(adjust_range(r, mapping))
            return

        # Left of range being converted is within source range, but right isn't:
        #
        #   SSSSSSSSSS
        #        RRRRRRRRRR
        #
        if (r.start in s) and (r.stop not in s):
            overlap = range(r.start, s.stop)
            right = range(s.stop, r.stop)
            output_ranges.append(adjust_range(overlap, mapping))
            remaining_ranges.append(right)
            return

        # Right of range being converted is within source range, but left isn't:
        #
        #        SSSSSSSSSS
        #   RRRRRRRRRR
        #
        if (s.start in r) and (s.stop not in r):
            left = range(r.start, s.start)
            overlap = range(s.start, r.stop)
            remaining_ranges.append(left)
            output_ranges.append(adjust_range(overlap, mapping))
            return

        # Range being converted extends beyond the source range at both ends:
        #
        #        SSSSS
        #   RRRRRRRRRRRRRRR
        #
        if (s.start in r) and (s.stop in r):
            left = range(r.start, s.start)
            right = range(s.stop, r.stop)
            remaining_ranges.append(left)
            output_ranges.append(adjust_range(s, mapping))
            remaining_ranges.append(right)
            return

    output_ranges.append(r)


def adjust_range(r, mapping):
    offset = mapping.destination_range_start - mapping.source_range.start
    return range(r.start + offset, r.stop + offset)


def parse(lines):
    groups = utils.group_lines(lines)

    seeds = groups[0][0].split(": ")[1].split(" ")
    seeds = [int(s) for s in seeds]

    maps = groups[1:]
    maps = [m[1:] for m in maps]
    maps = [[line.split(" ") for line in m] for m in maps]
    maps = [[tuple(int(n) for n in line) for line in m] for m in maps]
    maps = [[Mapping(range(line[1], line[1] + line[2]), line[0], line[2]) for line in m] for m in maps]

    return seeds, maps
