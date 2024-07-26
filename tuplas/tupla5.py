tupla = (3, 6, 2, 9, 1, 7, 5, 8)
num = []

pos = 0
i = 0
while i < len(tupla):
    if tupla[pos] > 5:
        num.append(tupla[pos])
    i += 1
    pos += 1

print(tupla)
print(f"Numeros maiores que 5 na tupla: {num}")   