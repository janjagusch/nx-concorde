"""
Tests for the nx_concorde.nx module.
"""

from nx_concorde import calc_distance_matrix, calc_path_matrix, calc_tour


def test_calc_path_matrix(graph):
    """
    Tests the calc_path_matrix function.
    """
    path_matrix = calc_path_matrix(graph)
    assert isinstance(path_matrix, dict)
    assert all(isinstance(key, frozenset) for key in path_matrix.keys())
    assert all(isinstance(value, tuple) for value in path_matrix.values())
    assert len(path_matrix) == sum(range(len(graph)))


def test_calc_distance_matrix(graph):
    """
    Tests the calc_distance_matrix function.
    """
    distance_matrix = calc_distance_matrix(graph)
    assert isinstance(distance_matrix, dict)
    assert all(isinstance(key, frozenset) for key in distance_matrix.keys())
    assert all(isinstance(value, float) for value in distance_matrix.values())
    assert len(distance_matrix) == sum(range(len(graph)))


def test_calc_tour(graph, mocker):
    start_node, end_node = list(graph.nodes())[:2]
    visit_nodes = list(graph.nodes())[2:5]
    mocker.patch("nx_concorde.nx.solve", return_value=range(6))
    tour = calc_tour(graph, start_node, end_node, visit_nodes)
    assert isinstance(tour, tuple)
    assert all(node in tour for node in visit_nodes)
