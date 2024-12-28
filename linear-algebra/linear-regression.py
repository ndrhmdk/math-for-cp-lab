import numpy as np
# Coefficients matrix (A)
A = np.array([
    [1, 3, -2],
    [3, 5, 6],
    [2, 4, 3]
])
# Constants vector (B)
B = np.array([5, 7, 8])
print(f"Solution: {np.linalg.solve(A, B)}")