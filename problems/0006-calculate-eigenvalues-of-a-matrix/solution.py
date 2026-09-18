import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
	m = np.array(matrix)
	tr = m.trace()
	det = np.linalg.det(m)

	D = np.sqrt(tr**2 - 4* det)



	return [(tr+D)/2 , (tr-D)/2]