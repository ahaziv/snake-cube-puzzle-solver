class ConnectivityGraph:
    def __init__(self, side_length):
        self._side_length = side_length
        self.graph = {}
        self.neighbor_nodes_base = {(-1, 0, 0), (1, 0, 0),
                                    (0, -1, 0), (0, 1, 0),
                                    (0, 0, -1), (0, 0, 1)}
        for i in range(side_length):
            for j in range(side_length):
                for k in range(side_length):
                    self.graph[(i, j, k)] = self._get_neighbor_nodes((i, j, k))

    def delete_node(self, node):
        edges = self.graph.pop(node)
        for neighbor in edges:
            self.graph[neighbor].remove(node)

    def _get_neighbor_nodes(self, nd):
        neighbor_nodes = {(nd[0] + ndb[0], nd[1] + ndb[1], nd[2] + ndb[2]) for ndb in self.neighbor_nodes_base
                          if -1 < nd[0] + ndb[0] < self._side_length
                          and -1 < nd[1] + ndb[1] < self._side_length
                          and -1 < nd[2] + ndb[2] < self._side_length}
        for node in neighbor_nodes:
            if -1 in node or self._side_length in node:
                neighbor_nodes.remove(node)
        return neighbor_nodes

    def is_connected(self):
        """ uses BFS to check for graph connectivity """
        non_tested_nodes = {key for key in self.graph.keys()}
        queue = [non_tested_nodes.pop()] if non_tested_nodes else []
        while True:
            if not non_tested_nodes:
                return True
            for node in self.graph.get(queue[0]):
                if node in non_tested_nodes:
                    queue.append(node)
                    non_tested_nodes.remove(node)
            queue.pop(0)
            if not queue:
                return False
