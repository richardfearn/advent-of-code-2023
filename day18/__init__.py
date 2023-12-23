OFFSETS = {
    "U": (0, -1),
    "D": (0, 1),
    "L": (-1, 0),
    "R": (1, 0),
}


def part_1_answer(lines):
    instructions = [line.split(" ") for line in lines]
    instructions = [(line[0], int(line[1])) for line in instructions]

    return lagoon_volume(instructions)


def part_2_answer(lines):
    hex_codes = [line.split(" ")[2][1:-1] for line in lines]
    instructions = [("RDLU"[int(code[6])], int(code[1:6], 16)) for code in hex_codes]

    return lagoon_volume(instructions)


def lagoon_volume(instructions):
    vertices, trench_length = determine_vertices(instructions)
    return (polygon_area(vertices) + trench_length // 2) + 1


def determine_vertices(instructions):
    pos = (0, 0)
    vertices = [pos]
    trench_length = 0

    for direction, length in instructions:
        offset = OFFSETS[direction]
        pos = (pos[0] + offset[0] * length), (pos[1] + offset[1] * length)
        vertices.append(pos)
        trench_length += length

    return vertices, trench_length


def polygon_area(vertices):
    # https://en.wikipedia.org/wiki/Shoelace_formula

    sum1 = sum2 = 0

    for i in range(len(vertices) - 1):
        sum1 += vertices[i][0] * vertices[i + 1][1]
        sum2 += vertices[i][1] * vertices[i + 1][0]

    return abs(sum1 - sum2) // 2
