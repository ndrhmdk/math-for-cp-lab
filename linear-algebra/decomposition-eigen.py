import numpy as np
def is_symmetric(matrix):
    return np.array_equal(matrix, matrix.T)

def symmetric_eigen(matrix):
    eigenvalues, eigenvectors = np.linalg.eigh(matrix)
    return eigenvalues, eigenvectors

def nonsymmetric_eigen(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)
    return eigenvalues, eigenvectors

if __name__ == "__main__":
    matrix = np.array([
        [4, 1, 1],
        [1, 2, 3],
        [1, 3, 6]
    ])
    if (is_symmetric(matrix)):
        print("Symmetric matrix")
        eigenvalues, eigenvectors = symmetric_eigen(matrix)
    else:
        print("Nonsymmetric matrix")
        eigenvalues, eigenvectors = nonsymmetric_eigen(matrix)
    print(f"Eigenvalues: {eigenvalues}\nEigenvectors:\n{eigenvectors}")
