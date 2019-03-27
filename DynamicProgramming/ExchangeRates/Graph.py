
class Graph:

    def __init__(self):
        self.vertices = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vertices.values())

    def add_vertex(self, node):
        self.num_vertices = self.num_vertices + 1

        new_vertex = Vertex(node)

        self.vertices[node] = new_vertex

        return new_vertex

    def get_vertex(self, n):
        if n in self.vertices:
            return self.vertices[n]
        else:
            return None

    def add_edge(self, fromNode, toNode, weight=0: int):
        if fromNode not in self.vertices:
            self.add_vertex(fromNode)
        if toNode not in self.vertices:
            self.add_vertex(toNode)

        self.vertices[fromNode].add_neighbor(toNode, weight)
        self.vertices[toNode].add_neighbor(fromNode, weight)

    def get_vertices(self):
        return self.vert_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous
