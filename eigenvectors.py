from eigenvalues import calculate_eigenvalues


def calculate_eigenvectors(matrix: list[list[float|int]], eigenvalues: list[float]) -> list[list[float]]: 
    a, b = matrix[0]
    c, d = matrix[1]
    eigenvectors = []
    for eigenvalue in eigenvalues:
      if abs(b) > abs(c):
        v = [b, eigenvalue-a]
      else:
        v = [eigenvalue -d, c]
      magnitude = (v[0]**2 + v[1]**2)**0.5
      v = [v[0]/magnitude, v[1]/magnitude]
      eigenvectors.append(v)
    return eigenvectors



matrix = [[5,2], [8,4]]
print(calculate_eigenvectors(matrix, calculate_eigenvalues(matrix)))