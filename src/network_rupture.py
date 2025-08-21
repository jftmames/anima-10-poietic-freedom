import networkx as nx

def graph_stats(G: nx.Graph):
    if G.number_of_nodes() == 0: return 0, 0.0
    lcc = max((len(c) for c in nx.connected_components(G)), default=0)
    clustering = nx.average_clustering(G) if G.number_of_nodes() > 1 else 0.0
    return lcc, clustering

def rupture_score(G0: nx.Graph, G1: nx.Graph) -> float:
    l0, c0 = graph_stats(G0); l1, c1 = graph_stats(G1)
    nmax = max(G0.number_of_nodes(), G1.number_of_nodes(), 1)
    return abs(l1 - l0) / nmax + abs(c1 - c0)

def load_edge_list_csv(path: str) -> nx.Graph:
    import csv
    G = nx.Graph()
    with open(path, 'r', encoding='utf-8') as f:
        for row in csv.reader(f):
            if not row or row[0].startswith('#'): continue
            u, v = row[0], row[1]
            G.add_edge(u, v)
    return G
