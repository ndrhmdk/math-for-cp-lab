import numpy as np

def euclidean_distance(v1, v2):
    """
    Calculate the Euclidean distance between two vectors.
    
    Parameters:
    v1 (array-like): First vector.
    v2 (array-like): Second vector.
    
    Returns:
    float: Euclidean distance between v1 and v2.
    """
    v1 = np.array(v1)
    v2 = np.array(v2)
    distance = np.linalg.norm(v1 - v2)
    return distance

# Example usage
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

distance = euclidean_distance(vector1, vector2)
print(f"Euclidean distance: {distance:.4f}")