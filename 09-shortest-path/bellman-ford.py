# Python program to find single source shortest path using
# Bellman-Ford algorithm

import os


def bellmanFord(V, edges, src):
    
    # Initially distance from source to all other vertices 
    # is not known(Infinite).
    dist = [100000000] * V
    dist[src] = 0

    # Relaxation of all the edges V times, not (V - 1) as we
    # need one additional relaxation to detect negative cycle
    for i in range(V):
        for edge in edges:
            u, v, wt = edge
            if dist[u] != 100000000 and dist[u] + wt < dist[v]:
                
                # If this is the Vth relaxation, then there 
                # is a negative cycle
                if i == V - 1:
                    return [-1]
                
                # Update shortest distance to node v
                dist[v] = dist[u] + wt
    return dist

if __name__ == '__main__':
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
    ans = bellmanFord(V, edges, src)
    os.system('cls')
    print(edges)
    print('\t'.join(map(str, ans)))
