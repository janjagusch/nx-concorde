"""
Dummy test - delete later.
"""

import random

import pytest
from nx_concorde import calc_distance_matrix, calc_path_matrix, calc_tour
from nx_concorde.tsp import solve


def monkey_solve(edge_weights, dimension, edge_weight_format):
    return random.shuffle(range(dimension))


solve = monkey_solve


def test_calc_path_matrix(graph):
    path_matrix = calc_path_matrix(graph)
    assert isinstance(path_matrix, dict)
    assert all(isinstance(key, frozenset) for key in path_matrix.keys())
    assert all(isinstance(value, tuple) for value in path_matrix.values())
    assert len(path_matrix) == sum(range(len(graph)))


def test_calc_distance_matrix(graph):
    distance_matrix = calc_distance_matrix(graph)
    assert isinstance(distance_matrix, dict)
    assert all(isinstance(key, frozenset) for key in distance_matrix.keys())
    assert all(isinstance(value, float) for value in distance_matrix.values())
    assert len(distance_matrix) == sum(range(len(graph)))
