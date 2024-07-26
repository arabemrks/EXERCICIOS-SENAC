matriz = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

matriz_transposta = list(zip(*matriz))

print(f"A matriz transposta é:\n{matriz_transposta[0]}\n{matriz_transposta[1]}\n{matriz_transposta[2]}")