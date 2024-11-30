import os
inf = float('inf')

# Bellman - Ford's algorithm
def bellman_ford(V, edges, src):
    # Step 1: Initialize distances from src to all other vertices as infinite, except the source itself
    L = [inf] * V
    L[src] = 0
    P = [None] * V

    # Step 2: Relax edges |V| - 1 times
    for i in range(1, V):
        for u, v, w in edges:
            if L[u] != inf and L[v] > L[u] + w:
                L[v] = L[u] + w
                P[v] = u

    # Step 3: Check for negative-weight cycles
    for u, v, w in edges:
        if L[u] != inf and L[v] > L[u] + w:
            # Negative cycle detected
            return -1       
    
    # Return distance and predecessor arrays
    return L, P

if __name__ == '__main__':
    os.system('cls')
    
    V = 6
    edges = [[0, 1, 1],
             [1, 2, 5],
             [1, 5, 7],
             [1, 3, 2],
             [2, 5, 1],
             [3, 2, 1],
             [3, 0, 2],
             [3, 4, 4],
             [4, 3, 3],
             [5, 4, 1]]

    src = 0
    result = bellman_ford(V=V, edges=edges, src=src)
    if result != -1:
        L, P = result
        print(f"Vertex distances from source: {L}")
        print(f"Predecessor in shortest path tree: {P}")
    else:
        print("Graph contains a negative weight cycle")