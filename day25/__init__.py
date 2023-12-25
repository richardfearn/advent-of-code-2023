import math
from itertools import combinations
import networkx as nx


def part_1_answer(lines):
    connections = parse(lines)

    nodes = set()
    graph = nx.Graph()
    for source, destinations in connections.items():
        nodes.add(source)
        for destination in destinations:
            nodes.add(destination)
            graph.add_edge(source, destination, capacity=1.0)

    # https://en.wikipedia.org/wiki/Minimum_cut
    # Try different source/sink nodes until we find a cut with value 3
    for s, t in combinations(nodes, 2):
        cut_value, partition = nx.minimum_cut(graph, s, t)
        if cut_value == 3:
            return math.prod(len(p) for p in partition)

    return None


def parse(lines):
    connections = [line.split(": ") for line in lines]
    connections = dict([line[0], set(line[1].split(" "))] for line in connections)
    return connections
