import numpy as np

def pca(data: np.ndarray, k: int) -> np.ndarray:
    """
    Perform PCA and return the top k principal components.
    
    Args:
        data: Input array of shape (n_samples, n_features)
        k: Number of principal components to return
    
    Returns:
        Principal components of shape (n_features, k), rounded to 4 decimals.
        Each eigenvector's sign is fixed so its first non-zero element is positive.
    """
    n, m = np.shape(data)
    

    mean = np.mean(data, axis=0, keepdims=True)
    std = np.std(data, axis=0, keepdims=True)

    std[std == 0] = 1.0
    X_std = (data - mean) / std
    C = (1 / (n - 1)) * (X_std.T @ X_std)
    eigenvalues, eigenvectors = np.linalg.eigh(C)
    idx = np.argsort(eigenvalues)[::-1]
    eigenvectors = eigenvectors[:, idx]
    top_k_eigenvectors = eigenvectors[:, :k]
    for col_idx in range(top_k_eigenvectors.shape[1]):
        col = top_k_eigenvectors[:, col_idx]
        mask = np.abs(col) > 1e-10
        if np.any(mask):
            if col[mask][0] < 0:
                top_k_eigenvectors[:, col_idx] *= -1

    return np.round(top_k_eigenvectors, 4)





