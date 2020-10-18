from random import sample, seed

import networkx as nx
import pytest


@pytest.fixture
def graph():
    seed(42)
    graph = nx.grid_2d_graph(10, 10)
    graph = graph.subgraph(sample(graph.nodes(), 80))
    graph = graph.subgraph(max(nx.connected_components(graph), key=len))
    return graph
