

import pytest

LIST = [1, 2, 3, 4, 5]

NODE_TEST = [(LIST, LIST)]


@pytest.mark.parametrize("node, result", NODE_TEST)
def test_nodes(node, result):
    """Test to check if all nodes are there."""
    from simple_graph import Graph
    g = Graph()
    for idx in node:
        g.add_node(idx)
    assert g.nodes() == result


@pytest.mark.parametrize()
def test_nodes():
	from simple_graph import Graph
	g = Graph()


# @pytest.mark.parametrize()
# def test_nodes():
# 	from simple_graph import Graph
# 	g = Graph()

# @pytest.mark.parametrize()
# def test_nodes():
# 	from simple_graph import Graph
# 	g = Graph()

# @pytest.mark.parametrize()
# def test_nodes():
# 	from simple_graph import Graph
# 	g = Graph()

# @pytest.mark.parametrize()
# def test_nodes():
# 	from simple_graph import Graph
# 	g = Graph()

# @pytest.mark.parametrize()
# def test_nodes():
# 	from simple_graph import Graph
# 	g = Graph()

# @pytest.mark.parametrize()
# def test_nodes():
# 	from simple_graph import Graph
# 	g = Graph()

