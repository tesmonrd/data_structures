import pytest

GRAPH = {'A': ['B', 'C'], 'B': ['D', 'C'], 'C': [], 'D': ['E'], 'E': []}

VISITED_B = ['A', 'B', 'C', 'D', 'E']

VISITED_D = ['A', 'C', 'B', 'D', 'E']

BREADTH_TEST = [(GRAPH, 'A', VISITED_B)]

DEPTH_TEST = [(GRAPH, 'A', VISITED_D)]


@pytest.mark.parametrize("graph, start, result", BREADTH_TEST)
def test_breadth_first(graph, start, result):
    from graphtrav import breadth_first
    assert breadth_first(graph, start) == result


@pytest.mark.parametrize("graph, start, result", DEPTH_TEST)
def test_depth_first(graph, start, result):
    from graphtrav import depth_first
    assert depth_first(graph, start) == result
