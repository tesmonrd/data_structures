# _*_ coding utf-8 _*_
"""Test the Simple Graph Data Structure."""
import pytest

LIST = [1, 2, 3, 4, 5]

GRAPH = {2: [], 3: [], 4: [], 5: []}

GRAPH2 = {1: [], 2: [3], 3: [], 4: [], 5: []}

NODE_TEST = [(LIST, LIST)]

EDGE_TEST = [(LIST, [4, 3])]

DEL_NODE = [(LIST, GRAPH)]

DEL_EDGE = [(LIST, GRAPH2)]

HAS_NODE = [(LIST, 1, True), (LIST, 2, True), (LIST, 32, False)]

NEIGHBOR_TEST = [(LIST, 1, [1, 4]), (LIST, 3, [5]), (LIST, 4, [2])]

# ***************************************************


@pytest.mark.parametrize('node, result', NODE_TEST)
def test_nodes(node, result):
    """Test to check if all nodes are there."""
    from simple_graph import Graph
    g = Graph()
    for idx in node:
        g.add_node(idx)
    assert g.nodes() == result


@pytest.mark.parametrize('node, result', EDGE_TEST)
def test_edge(node, result):
    """Test to check if all edges are there."""
    from simple_graph import Graph
    g = Graph()
    for idx in node:
        g.add_node(idx)
    g.add_edge(2, 3)
    g.add_edge(1, 4)
    assert g.edges() == result


@pytest.mark.parametrize('node, result', DEL_NODE)
def test_del_nodes(node, result):
    """Test to check the deleted nodes aren't there."""
    from simple_graph import Graph
    g = Graph()
    for idx in node:
        g.add_node(idx)
    assert g.del_node(1) == result


@pytest.mark.parametrize('node, result', DEL_EDGE)
def test_del_edge(node, result):
    """Test to check the deleted edges aren't there."""
    from simple_graph import Graph
    g = Graph()
    for idx in node:
        g.add_node(idx)
    g.add_edge(2, 3)
    g.add_edge(1, 4)
    assert g.del_edge(1, 4) == result


@pytest.mark.parametrize('node, n, result', HAS_NODE)
def test_has_node(node, n, result):
    """Test to check if a node exists in graph."""
    from simple_graph import Graph
    g = Graph()
    for idx in node:
        g.add_node(idx)
    assert g.has_node(n) == result


@pytest.mark.parametrize('node, n, result', NEIGHBOR_TEST)
def test_neighbor(node, n, result):
    """Test to check that the correct node have the right edge."""
    from simple_graph import Graph
    g = Graph()
    for idx in node:
        g.add_node(idx)
    g.add_edge(1, 1)
    g.add_edge(1, 4)
    g.add_edge(4, 2)
    g.add_edge(3, 5)
    assert g.neighbors(n) == result
