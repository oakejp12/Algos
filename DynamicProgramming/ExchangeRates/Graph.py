
from Vertex import Vertex
import collections


class Graph:

    def __init__(self):
        self.vertices = collections.OrderedDict()
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, node):
        self.num_vertices += 1

        new_vertex = Vertex(node)

        self.vertices[node] = new_vertex

        return new_vertex

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def add_edge(self, fromNode, toNode, weight=0):
        if fromNode not in self.vertices:
            self.add_vertex(fromNode)
        if toNode not in self.vertices:
            self.add_vertex(toNode)

        self.vertices[fromNode].add_neighbor(toNode, weight)

    def get_vertices(self):
        return self.vertices.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous

    def __str__(self):
        string = ""
        V = set(self.get_vertices())
        for node in V:
            vertex = self.get_vertex(node)
            string = string + vertex.__str__() + '\n'
        return string

    @staticmethod
    def reverse_graph(G):
        '''
        Reverse the graph so that out-going edges become in-going edges
        Useful for the Bellman-Ford algorithm
        '''

        G_new = Graph()

        V = G.get_vertices()

        # For each vertex in G, we'll grab their neighbors
        # Add the neighbors as a new vertex (if they don't exist)
        # to the new graph G_new, then add the source vertex as
        # a neighbor to the neighbors
        for node in V:
            sourceVertex = G.get_vertex(node)
            neighbors = sourceVertex.get_connections()
            for neighbor in neighbors:
                if G_new.get_vertex(neighbor) is None:
                    G_new.add_vertex(neighbor)
                weightFromSource = sourceVertex.get_weight(neighbor)
                G_new.add_edge(neighbor, node, weightFromSource)

        return G_new
