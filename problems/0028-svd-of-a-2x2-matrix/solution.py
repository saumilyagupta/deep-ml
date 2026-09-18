import numpy as np

def svd_2x2(A: np.ndarray) -> tuple:
    """
    Compute SVD of a 2x2 matrix.
    
    Args:
        A: 2x2 numpy array
    
    Returns:
        U: 2x2 orthogonal matrix (left singular vectors)
        s: 1D array of singular values
        V: 2x2 matrix (right singular vectors)
    """
    ata = A.T @ A 
    eigenvalue, V_cols = np.linalg.eigh(ata)

    idx = np.argsort(eigenvalue)[::-1]
    eigenvalue = np.maximum(eigenvalue[idx],0.0)
    V_cols = V_cols[:,idx]


    s = np.sqrt(eigenvalue)

    u0 = (A @ V_cols[:,0]) / s[0] if s[0] > 1e-12 else np.array([1.0,0.0])


    if s[1] > 1e-12:
        u1 = (A @ V_cols[:, 1]) / s[1]
    else:

        u1 = np.array([-u0[0],u0[0]])
    
    U = np.column_stack([u0, u1])


    V = V_cols.T 

    return U, s, V


