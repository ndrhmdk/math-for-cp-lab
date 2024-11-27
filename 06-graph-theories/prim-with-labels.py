import sys


class Graph():
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]

    def printMST(self, parent, node_labels):
        print("Edge  \t Weight")
        total_weight = 0
        for i in range(1, self.V):
            print(f"{node_labels[parent[i]]}{node_labels[i]} \t\t {self.graph[i][parent[i]]}")
            total_weight += self.graph[i][parent[i]]
        print(f"Minimum Weight of MST: {total_weight}")

    def minKey(self, key, mstSet):
        min = sys.maxsize
        for v in range(self.V):
            if key[v] < min and mstSet[v] == False:
                min = key[v]
                min_index = v

        return min_index

    def primMST(self, node_labels):
        key = [sys.maxsize] * self.V
        parent = [None] * self.V
        key[0] = 0
        mstSet = [False] * self.V

        parent[0] = -1

        for cout in range(self.V):
            u = self.minKey(key, mstSet)

            mstSet[u] = True

            for v in range(self.V):
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        self.printMST(parent, node_labels)


if __name__ == '__main__':
    node_labels = ['A', 'B', 'C', 'D', 'E', 'F']
    g = Graph(5)
    g.graph = [
        [0, 3, 5, 0, 0, 9],  # A
        [3, 0, 3, 4, 0, 0],  # B
        [5, 3, 0, 0, 6, 0],  # C
        [0, 4, 0, 0, 2, 2],  # D
        [0, 0, 6, 2, 0, 5],  # E
        [9, 0, 0, 2, 5, 0],  # F
    ]
    g.primMST(node_labels)