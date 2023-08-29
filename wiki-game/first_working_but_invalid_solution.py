# This solution worked locally, and I prefer it as an actual solution,
# but the submission page didn't support any libraries.

import networkx as nx

num_tests_read = 0


def is_acceptable_path(edges, source, target):
    """
    Returns if there is a directed path from source
    to target of path length 6 or less

    :edges: list of tuples of edges in directed graph
    :source: source vertice (start of path)
    :target: target vertice (end of path)
    :return: "YES" or "NO"
    """

    graph = nx.DiGraph()
    graph.add_edges_from(edges)

    try:
        path = nx.shortest_path(graph, source=source, target=target)
        if len(path) <= 7:
            return "YES"
    except Exception:
        return "NO"

    return "NO"


def get_edges():
    """
    Get a tuple of edges from input

    :return: list of tuples of edges
    """

    total_num_edges = int(input().split(" ")[1])

    num_edges = 0
    edges = []

    while num_edges < total_num_edges:
        line = input()
        edge = tuple(map(int, line.split(' ')))
        edges.append(edge)
        num_edges += 1

    return edges


def get_target_path():
    """
    Get source and target from input

    :return: tuple of (source, target)
    """

    last_line = input()
    source_vertice, target_vertice = map(int, last_line.split(' '))

    return source_vertice, target_vertice


total_num_tests = int(input())

while num_tests_read < total_num_tests:
    edges = get_edges()
    source, target = get_target_path()
    is_acceptable = is_acceptable_path(edges, source, target)
    print(is_acceptable)
    num_tests_read += 1
