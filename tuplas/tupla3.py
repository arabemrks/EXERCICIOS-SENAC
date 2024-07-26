tupla = (3, 6, 2, 9, 1, 7, 5, 8)
pares = []

pos = 0
i = 0
while i < len(tupla):
    if tupla[pos] % 2 == 0:
        pares.append(tupla[pos])
    i += 1
    pos += 1

print(f"Tupla: {tupla}")
print(f"Numeros pares na tupla: {pares}")

