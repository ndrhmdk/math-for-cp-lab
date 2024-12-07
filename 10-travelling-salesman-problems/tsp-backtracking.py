def totalCost(cost, visited, currPos, n, count, costSoFar, ans, path, bestPath):
    """
    Calculate the minimum cost to visit all cities starting and ending at the starting point using Backtracking.
    :param cost: 2D list representing the cost matrix where cost[i][j] is the cost to travel from city i to city j
    :param visited: List indicating whether a city has been visited
    :param currPos: Current position in the path (city index)
    :param n: Total number of cities
    :param count: Current count of cities visited
    :param costSoFar: Cost accumulated so far
    :param ans: List containing the minimum cost found (to pass by reference)
    :param path: Current path taken
    :param bestPath: List containing the best path found (to pass by reference)
    """

    # If all nodes are visited and there's an edge to the start node
    if count == n and cost[currPos][0] != 0:
        # Update the minimum cost and path
        if costSoFar + cost[currPos][0] < ans[0]:
            ans[0] = costSoFar + cost[currPos][0]
            bestPath[:] = path[:] + [0]
        return

    # Try visiting each node from the current position
    for i in range(n):
        # If node not visited and has and edge
        if not visited[i] and cost[currPos][i] != 0:
            visited[i] = True
            path.append(i)
            totalCost(cost, visited, i, n, count + 1, costSoFar + cost[currPos][i], ans, path, bestPath)
            path.pop()
            visited[i] = False

def tsp(cost):
    n = len(cost)
    visited = [False] * n
    visited[0] = True

    # `ans` for the minimum cost and `bestPath` for the minimum path
    ans = [float('inf')]
    bestPath = []

    totalCost(cost, visited, 0, n, 1, 0, ans, [0], bestPath)
    return ans[0], bestPath

if __name__ == '__main__':
    cost = [
        [0, 85, 26, 81],
        [85, 0, 77, 97],
        [26, 77, 0, 26],
        [81, 97, 26, 0]
    ]
    res, path = tsp(cost)
    print("Minimum cost: ", res)
    print("Path: ", [p + 1 for p in path])
