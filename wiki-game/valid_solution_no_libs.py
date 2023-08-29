class Graph(object):
    def __init__(self, nodes, init_graph):
        self.nodes = nodes
        self.graph = init_graph

    def get_nodes(self):
        "Returns the nodes of the graph."
        return self.nodes

    def get_outgoing_edges(self, node):
        "Returns the neighbors of a node."
        connections = []
        for out_node in self.nodes:
            if self.graph[node].get(out_node, False) is not False:
                connections.append(out_node)
        return connections

    def value(self, node1, node2):
        "Returns the value of an edge between two nodes."
        return self.graph[node1][node2]


def dijkstra_algorithm(graph, start_node):
    unvisited_nodes = list(graph.get_nodes())

    # We'll use this dict to save the cost of visiting each node and update it as we move along the graph   
    shortest_path = {}

    # We'll use this dict to save the shortest known path to a node found so far
    previous_nodes = {}

    max_value = 9223372036854775807
    for node in unvisited_nodes:
        shortest_path[node] = max_value
    # However, we initialize the starting node's value with 0
    shortest_path[start_node] = 0

    # The algorithm executes until we visit all nodes
    while unvisited_nodes:
        # The code block below finds the node with the lowest score
        current_min_node = None
        for node in unvisited_nodes:  # Iterate over the nodes
            if current_min_node is None:
                current_min_node = node
            elif shortest_path[node] < shortest_path[current_min_node]:
                current_min_node = node

        # The code block below retrieves the current node's neighbors and updates their distances
        neighbors = graph.get_outgoing_edges(current_min_node)
        for neighbor in neighbors:
            tentative_value = shortest_path[current_min_node] + graph.value(current_min_node, neighbor)
            if tentative_value < shortest_path[neighbor]:
                shortest_path[neighbor] = tentative_value
                # We also update the best path to the current node
                previous_nodes[neighbor] = current_min_node

        # After visiting its neighbors, we mark the node as "visited"
        unvisited_nodes.remove(current_min_node)

    return previous_nodes, shortest_path


def get_target_path():
    """
    Get source and target input()rom input

    :return: tuple of (source, target)
    """

    last_line = input()
    source_vertice, target_vertice = map(str, last_line.split(' '))

    return source_vertice, target_vertice


def get_totals():
    """
    Get a tuple of edges from input

    :return: list of tuples of edges
    """

    line = input()
    total_vertices = int(line.split(" ")[0])
    total_edges = int(line.split(" ")[1])

    return total_vertices, total_edges


def get_nodes_graph(total_num_edges):
    """
    Get a tuple of edges from input

    :return: list of tuples of edges
    """
    num_edges = 0
    init_graph = {}
    nodes = []
    edges = []

    while num_edges < total_num_edges:
        line = input()
        edge = line.split(' ')
        edges.append(edge)

        if edge[0] not in nodes:
            nodes.append(edge[0])

        if edge[1] not in nodes:
            nodes.append(edge[1])

        num_edges += 1

    for node in nodes:
        init_graph[node] = {}

    for edge in edges:
        init_graph[edge[0]][edge[1]] = 1

    return nodes, init_graph


def print_result(previous_nodes, shortest_path, start_node, target_node):
    path = []
    node = target_node

    try:
        while node != start_node:
            path.append(node)
            node = previous_nodes[node]

        # Add the start node manually
        path.append(start_node)

        if len(path) <= 7:
            print("YES")
        else:
            print("NO")
    except Exception:
        print("NO")


num_tests_read = 0
total_num_tests = int(input())

while num_tests_read < total_num_tests:
    total_nodes, total_edges = get_totals()
    nodes, init_graph = get_nodes_graph(total_edges)
    graph = Graph(nodes, init_graph)
    (source, destination) = get_target_path()

    # print(f"Number of vertices (nodes): {total_nodes}")
    # print(f"Number of edges: {total_edges}")
    # print(f"Source: {source}; Target: {destination}")
    # print(f"Edges are: {edges}")
    # print(init_graph)
    previous_nodes, shortest_path = dijkstra_algorithm(graph=graph, start_node=source)

    print_result(previous_nodes, shortest_path, start_node=source, target_node=destination)

    num_tests_read += 1

# FINALLY:
# SEKAI{hyp3rL1nk_cha115_4r3_EZ}
