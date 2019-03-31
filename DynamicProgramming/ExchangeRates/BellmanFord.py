'''
An implementation of the Bellman-Form algorithm:
Finding the shortest path in a directed graph G
from a starting node s to all nodes z in the set
of vertices V.
'''

from Graph import Graph
from Vertex import Vertex
import sys


class BellmanFord:

    @staticmethod
    def shortest_pairs(G: Graph, s):
        '''
        A shortest pairs from starting node s 
        implementation of the Bellman-Ford algorithm
        for a directed graph G
        '''

        # Let V be the set of vertices in G
        V = G.get_vertices()

        num_vertices = len(V)

        # Initialize a 2D array to hold
        # distances from starting node s to
        # all nodes z
        D = [[sys.maxsize for n in range(num_vertices)]
             for n in range(num_vertices)]

        # Base case for starting node s
        # D(0, s) = 0
        for index in range(num_vertices):
            D[index][0] = 0

        # In order to inspect the weighted edges out
        # of a source node, we need to reverse G
        G_reverse = Graph.reverse_graph(G)

        # Since the shortest path P will
        # only visit each vertex at most once,
        # |P| <= 1
        # Iterate on a prefix of P
        for i in range(1, num_vertices):
            for index_i, vertex in enumerate(V):

                # Consider the case where shortest
                # path is i - 1 edges
                D[i][index_i] = D[i - 1][index_i]

                # Now, consider the case where the
                # shortest path is i edges

                # Get the neighbors of vertex and
                # solve for the minimal of shortest paths
                vertexNode = G_reverse.get_vertex(vertex)
                neighbors = vertexNode.get_connections()

                for neighbor in neighbors:
                    index_j = list(V).index(neighbor)
                    print("Inspect shortest path from " + vertex +
                          " to " + neighbor)
                    current_value = D[i][index_i]
                    possible_value = D[i - 1][index_j] + \
                        vertexNode.get_weight(neighbor)
                    if current_value > possible_value:
                        D[i][index_i] = possible_value

        return D


if __name__ == "__main__":
    print("Running main()")

    G = Graph()
    G.add_vertex("s")
    G.add_vertex("a")
    G.add_vertex("b")
    G.add_vertex("c")
    G.add_vertex("d")
    G.add_vertex("e")

    G.add_edge("s", "a", 5)
    G.add_edge("a", "b", 3)
    G.add_edge("b", "c", -6)
    G.add_edge("c", "a", 2)
    G.add_edge("b", "d", 4)
    G.add_edge("c", "e", 5)

    D = BellmanFord.shortest_pairs(G, "s")

    print(D)
