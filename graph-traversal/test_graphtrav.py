import pytest

GRAPH = {'A': ['B', 'C'], 'B': ['D', 'C'], 'C': [], 'D': ['E'], 'E': []}

VISITED = ['A', 'B', 'C', 'D', 'E']

DEPTH_TEST = [(GRAPH, 'A', VISITED)]


@pytest.mark.parametrize("graph, start, result", DEPTH_TEST)
def test_breadth_first(graph, start, result):
    from graphtrav import breadth_first
    assert breadth_first(graph, start) == result
