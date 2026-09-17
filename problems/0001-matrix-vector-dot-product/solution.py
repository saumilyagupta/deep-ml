import numpy as np
def matrix_dot_vector(a: list[list[int|float]], b: list[int|float]) -> list[int|float]:
    if not a or len(a[0]) != len(b):
        return -1
    return np.dot(a,b).tolist()
    
    