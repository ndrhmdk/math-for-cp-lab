class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])

    def find(self, parent, i):
        if parent[i] != i:
            parent[i] = self.find(parent, parent[i])
        return parent[i]

    def union(self, parent, rank, x, y):
        if rank[x] < rank[y]:
            parent[x] = y
        elif rank[x] > rank[y]:
            parent[y] = x
        else:
            parent[y] = x
            rank[x] += 1

    def KruskalMST(self, node_labels):
        result = []
        i = 0
        e = 0
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i = i + 1
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e = e + 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        minimumCost = 0
        print("Edges in the constructed MST:")
        for u, v, weight in result:
            minimumCost += weight
            print(f"{node_labels[u]}{node_labels[v]}   =   {weight}")
        print("Minimum Spanning Tree Cost:", minimumCost)


if __name__ == '__main__':
    node_labels = ['A', 'B', 'C', 'D', 'E', 'F']
    g = Graph(6)
    g.addEdge(0, 1, 3)  # AB
    g.addEdge(0, 2, 5)  # AC
    g.addEdge(0, 5, 9)  # AF
    g.addEdge(1, 2, 3)  # BC
    g.addEdge(1, 3, 4)  # BD
    g.addEdge(3, 4, 2)  # DE
    g.addEdge(3, 5, 2)  # DF
    g.addEdge(2, 4, 6)  # CE
    g.addEdge(4, 5, 5)  # EF
    g.KruskalMST(node_labels)