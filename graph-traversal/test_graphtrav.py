import pytest

GRAPH = {'A': ['B', 'C'], 'B': ['D', 'C'], 'D': ['E'], 'E': []}

VISITED = ['C', 'E', 'D', 'B', 'A']

DEPTH_TEST = [(GRAPH, 'A', VISITED)]


@pytest.mark.parametrize("graph, start, result", DEPTH_TEST)
def test_depth_first(graph, start, result):
    from graphtrav import depth_first
    assert depth_first(graph, start) == result
