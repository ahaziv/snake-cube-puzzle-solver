import unittest

from connectivity_graph import ConnectivityGraph


class ConnectivityGraphTests(unittest.TestCase):
    def test_1(self):       # no deleted nodes
        deleted_nodes = []
        side_length = 3
        self.assertTrue(self.connectivity_test(deleted_nodes, side_length))

    def test_2(self):       # isolated corner
        deleted_nodes = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
        side_length = 3
        self.assertFalse(self.connectivity_test(deleted_nodes, side_length))

    def test_3(self):       # missing central plane
        deleted_nodes = [(1, 0, 0), (1, 0, 1), (1, 0, 2),
                         (1, 1, 0), (1, 1, 1), (1, 1, 2),
                         (1, 2, 0), (1, 2, 1), (1, 2, 2)]
        side_length = 3
        self.assertFalse(self.connectivity_test(deleted_nodes, side_length))

    def test_4(self):       # missing central plane with one connection
        deleted_nodes = [(1, 0, 0), (1, 0, 1), (1, 0, 2),
                         (1, 1, 0), (1, 1, 2),
                         (1, 2, 0), (1, 2, 1), (1, 2, 2)]
        side_length = 3
        self.assertTrue(self.connectivity_test(deleted_nodes, side_length))

    @staticmethod
    def connectivity_test(deleted_nodes: list, side_length: int):
        graph = ConnectivityGraph(side_length)
        for node in deleted_nodes:
            graph.delete_node(node)

        return graph.is_connected()

