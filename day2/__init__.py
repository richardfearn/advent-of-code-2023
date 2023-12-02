import math

RED, GREEN, BLUE = "red", "green", "blue"


def part_1_answer(lines):
    def game_possible(draws):
        return all(draw_possible(draw) for draw in draws)

    def draw_possible(draw):
        return (draw.get(RED, 0) <= 12) and (draw.get(GREEN, 0) <= 13) and (draw.get(BLUE, 0) <= 14)

    games = parse_games(lines)
    return sum(game_id for game_id, draws in games if game_possible(draws))


def part_2_answer(lines):
    def find_min_counts(draws):
        return {colour: max(draw.get(colour, 0) for draw in draws) for colour in (RED, GREEN, BLUE)}

    def power(draws):
        min_counts = find_min_counts(draws)
        return math.prod(min_counts.values())

    games = parse_games(lines)
    return sum(power(draws) for _, draws in games)


def parse_games(lines):
    return [parse_game(line) for line in lines]


def parse_game(line):
    game_id, draws = line.split(": ")
    game_id = int(game_id.split(" ")[1])
    draws = [parse_draw(draw) for draw in draws.split("; ")]
    return game_id, draws


def parse_draw(draw):
    counts = draw.split(", ")
    counts = [count.split(" ") for count in counts]
    return {count[1]: int(count[0]) for count in counts}
