import csv
from typing import Dict, Set, Tuple

Graph = Dict[str, Set[str]]


def _empty_graph() -> Graph:
    return {}


def _add_edge(graph: Graph, u: str, v: str) -> None:
    graph.setdefault(u, set()).add(v)
    graph.setdefault(v, set()).add(u)


def _num_nodes(graph: Graph) -> int:
    return len(graph)


def _connected_components(graph: Graph):
    visited = set()
    for node in graph:
        if node in visited:
            continue
        stack = [node]
        component = set()
        while stack:
            current = stack.pop()
            if current in visited:
                continue
            visited.add(current)
            component.add(current)
            stack.extend(graph.get(current, set()) - visited)
        yield component


def _average_clustering(graph: Graph) -> float:
    if _num_nodes(graph) <= 1:
        return 0.0

    coeff_sum = 0.0
    for node, neighbors in graph.items():
        k = len(neighbors)
        if k < 2:
            continue
        links = 0
        neighbor_list = list(neighbors)
        for i in range(len(neighbor_list)):
            for j in range(i + 1, len(neighbor_list)):
                a = neighbor_list[i]
                b = neighbor_list[j]
                if a in graph.get(b, set()):
                    links += 1
        coeff_sum += (2 * links) / (k * (k - 1))

    return coeff_sum / _num_nodes(graph)


def graph_stats(graph: Graph) -> Tuple[int, float]:
    if _num_nodes(graph) == 0:
        return 0, 0.0
    largest_component = max((len(component) for component in _connected_components(graph)), default=0)
    clustering = _average_clustering(graph)
    return largest_component, clustering


def rupture_score(graph_0: Graph, graph_1: Graph) -> float:
    l0, c0 = graph_stats(graph_0)
    l1, c1 = graph_stats(graph_1)
    nmax = max(_num_nodes(graph_0), _num_nodes(graph_1), 1)
    return abs(l1 - l0) / nmax + abs(c1 - c0)


def load_edge_list_csv(path: str) -> Graph:
    graph = _empty_graph()
    with open(path, "r", encoding="utf-8") as f:
        for row in csv.reader(f):
            if not row or row[0].startswith("#"):
                continue
            if len(row) < 2:
                continue
            _add_edge(graph, row[0], row[1])
    return graph
