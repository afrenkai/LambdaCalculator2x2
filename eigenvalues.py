def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
  eigenvalues = []
  a, b = matrix[0]
  c, d = matrix[1]
    

  trace = a + d
  det = (a*d) - (b*c)

  l1 = (trace + (trace **2 - (4 * det))**0.5)/2
  eigenvalues.append(round(l1, 4))
  l2 = (trace - (trace **2 - (4 * det))**0.5)/2
  eigenvalues.append(round(l2, 4))
  return eigenvalues

# matrix = [[5,2], [8,4]]
# calculate_eigenvalues(matrix)


