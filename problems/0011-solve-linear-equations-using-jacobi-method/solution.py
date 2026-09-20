import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:

	A = np.array(A,dtype=float)
	b = np.array(b,dtype=float)

	x = np.zeros_like(b)

	d = np.diag(A)
	R = A - np.diag(d)

	for _ in range(n):
		x = (b - np.dot(R,x)) / d  

	return np.round(x,4).tolist()