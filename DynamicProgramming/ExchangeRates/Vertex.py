import sys


class Vertex:

    def __init__(self, node):
        self.id = node
        self.adjacent = {}

        # Set distance to INFINITY for all nodes
        self.distance = sys.maxsize

        # Mark all nodes unvisited
        self.visited = False

        # Predecessor
        self.previous = None

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

    def set_distance(self, dist):
        self.distance = distance

    def set_previous(self, previousNeighbor):
        self.previous = previousNeighbor

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return str(self.id) + ' adjacent:' + str([x for x in self.adjacent])
