# _*_ coding utf-8 _*_
"""Test the Simple Graph Data Structure."""
import pytest

LIST = [1, 2, 3, 4, 5]

GRAPH = {2: [], 3: [], 4: [], 5: []}

GRAPH2 = {1: [], 2: [3], 3: [], 4: [], 5: []}

NODE_TEST = [(LIST, LIST)]

EDGE_TEST = [(LIST, [(1, 4), (2, 3)])]

DEL_NODE = [(LIST, GRAPH)]

DEL_EDGE = [(LIST, GRAPH2)]

HAS_NODE = [(LIST, 1, True), (LIST, 2, True), (LIST, 32, False)]

NEIGHBOR_TEST = [(LIST, 1, [1, 4]), (LIST, 3, [5]), (LIST, 4, [2])]

# ***************************************************


@pytest.mark.parametrize('node, result', NODE_TEST)
def test_add_nodes(node, result):
    """Test to check if all nodes are there."""
    from simple_graph import Graph
    g = Graph()
    for idx in node:
        g.add_node(idx)
    assert g.nodes() == result


def test_empty():
    """Test empty graph."""
    from simple_graph import Graph
    g = Graph()
    assert g.nodes() == []


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


def test_add_edge():
    from simple_graph import Graph
    g = Graph()
    g.add_node(2)
    g.add_node(3)
    g.add_edge(2, 3)
    assert g.graph == {2: [3], 3: []}


@pytest.mark.parametrize('node, result', DEL_NODE)
def test_del_nodes(node, result):
    """Test to check the deleted nodes aren't there."""
    from simple_graph import Graph
    g = Graph()
    for idx in node:
        g.add_node(idx)
    g.del_node(1)
    assert g.graph == result


@pytest.mark.parametrize('node, result', DEL_EDGE)
def test_del_edge(node, result):
    """Test to check the deleted edges aren't there."""
    from simple_graph import Graph
    g = Graph()
    for idx in node:
        g.add_node(idx)
    g.add_edge(2, 3)
    g.add_edge(1, 4)
    g.del_edge(1, 4)
    assert g.graph == result
    with pytest.raises(KeyError):
        g.del_edge(6, 2)
    with pytest.raises(ValueError):
        g.del_edge(3, 200)


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
    with pytest.raises(KeyError):
        g.neighbors(99)
