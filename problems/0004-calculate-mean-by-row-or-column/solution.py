import numpy as np
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
	mat = np.array(matrix)


	return np.mean(mat,axis= 1 if mode == "row" else 0)