import numpy as np

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    dim = data.shape[0]
    v = np.random.randn(dim)
    v = v / np.linalg.norm(v) 
    l = 0  

    for _ in range(num_steps):
        v = data @ v
        v = v / np.linalg.norm(v)
        l = float(v.T @ data @ v)  

    return l, v
 