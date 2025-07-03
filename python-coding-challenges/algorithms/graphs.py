class Graph:
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

    def get_path(self,start, end, path=None):
        if path is None:
            path = []

        path = path + [start]
        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []

        paths = []
        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_path(node, end, path)
                for p in new_paths:
                    paths.append(p)

        return paths
    def get_short_path(self,start,end,path=None):
        if not path:
            path = []
        path = path + [start]
        if start == end:
            return path
        if start not in self.graph_dict:
            return None

        shortest_path = None
        for node in self.graph_dict[start]:
            if node not in path:
                sp = self.get_short_path(node, end, path)
                if sp:
                    if not shortest_path or len(sp) < len(shortest_path):
                        shortest_path = sp
        return shortest_path

#basically, numbers are just cities
routes = [
    ("Mumbai", "Paris"),
    ("Mumbai", "Dubai"),
    ("Paris", "Dubai"),
    ("Paris", "New York"),
    ("Dubai", "New York"),
    ("New York", "Toronto")
]

graf = Graph(routes)
print(graf.get_path('Mumbai', 'New York'))