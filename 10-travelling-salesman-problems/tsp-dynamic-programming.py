import sys

inf = 999

def total_cost(mask, pos, n, cost, memo, parent):
    # Base case: if all cities are visited, return the cost to return to the starting city
    if mask == (1 << n) - 1:
        return cost[pos][0]

    # If the answer is already computed, return it
    if memo[mask][pos] != -1:
        return memo[mask][pos]

    ans = sys.maxsize

    # Try visiting every city that has not been visited yet
    for i in range(n):
        if (mask & (1 << i)) == 0:
            new_cost = cost[pos][i] + total_cost(mask | (1 << i), i, n, cost, memo, parent)
            if new_cost < ans:
                ans = new_cost
                parent[mask][pos] = i

    memo[mask][pos] = ans
    return ans

def tsp(cost):
    n = len(cost)
    memo = [[-1] * n for _ in range(1 << n)]
    parent = [[-1] * n for _ in range(1 << n)]

    min_cost = total_cost(1, 0, n, cost, memo, parent)

    # Reconstruct the path
    mask = 1
    pos = 0
    path = [0]

    while mask != (1 << n) - 1:
        pos = parent[mask][pos]
        path.append(pos)
        mask |= (1 << pos)

    path.append(0)  # Returning to the starting city

    return min_cost, path

if __name__ == "__main__":
    cost = [
        [inf, 31, 15, 23, 10, 171],
        [16, inf, 24, 7, 12, 12],
        [34, 3, inf, 25, 54, 25],
        [15, 20, 33, inf, 50, 40],
        [16, 10, 32, 3, inf, 23],
        [18, 20, 13, 28, 21, inf]
    ]

    result, path = tsp(cost)
    print("Minimum cost:", result)
    print("Path Taken:", ', '.join(map(str, [p + 1 for p in path])))
