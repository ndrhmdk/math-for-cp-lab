import sys

class Graph():
    def __init__(self, vertices, vertex_labels):
        self.V = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
        self.vertex_labels = vertex_labels

    def printSolution(self, dist, predecessors, src):
        def printPath(j):
            path = []
            while j != -1:
                path.insert(0, self.vertex_labels[j])
                j = predecessors[j]
            return " - ".join(path)

        print("Vertex\t Distance from Source")
        for i in range(self.V):
            print(f"{self.vertex_labels[i]}\t {dist[i]}")

        print("\nPaths from source:")
        for i in range(self.V):
            if i != src:
                print(f"Path to {self.vertex_labels[i]}: {printPath(i)}")

    def minDistance(self, dist, sptSet):
        min = sys.maxsize
        min_index = -1

        for u in range(self.V):
            if dist[u] < min and sptSet[u] == False:
                min = dist[u]
                min_index = u

        return min_index

    def dijkstra(self, src):
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        sptSet = [False] * self.V
        predecessors = [-1] * self.V

        for cout in range(self.V):
            x = self.minDistance(dist, sptSet)
            sptSet[x] = True

            for y in range(self.V):
                if self.graph[x][y] > 0 and sptSet[y] == False and dist[y] > dist[x] + self.graph[x][y]:
                    dist[y] = dist[x] + self.graph[x][y]
                    predecessors[y] = x

        self.printSolution(dist, predecessors, src)

if __name__ == "__main__":
    vertex_labels = ['a', 'b', 'c', 'd', 'e', 'g', 'h', 'k', 'm', 'n']
    g = Graph(10, vertex_labels)
    g.graph = [[0, 1, 0, 0, 3, 0, 0, 0, 3, 2],
               [1, 0, 4, 0, 1, 0, 0, 0, 0, 0],
               [0, 4, 0, 6, 2, 2, 0, 0, 0, 0],
               [0, 0, 6, 0, 0, 2, 2, 0, 0, 0],
               [3, 1, 2, 0, 0, 4, 0, 0, 5, 3],
               [0, 0, 2, 2, 4, 0, 3, 0, 5, 0],
               [0, 0, 0, 2, 0, 3, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 1, 0, 3, 0],
               [3, 0, 0, 0, 5, 5, 0, 3, 0, 6],
               [2, 0, 0, 0, 3, 0, 0, 0, 6, 0]]

    # 'A' to every thing else
    g.dijkstra(0)