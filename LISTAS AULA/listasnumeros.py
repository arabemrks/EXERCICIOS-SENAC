numeros = [4,5,99,11,48,256]
numeros.append(1.5)
numeros.append(65.8)
numeros.append(37.2)
numeros.append(22.4)
numeros.append(88.8)
numeros.append(66.6)
print(numeros)

numeros.pop()
numeros.pop()
print(numeros)

numeros.insert(1, 10)
numeros.insert(2, 11)
print(numeros)

numeros.sort()
print(numeros)

print(f"O maior numero é: {max(numeros)} e o menor numero é: {min(numeros)}")

print(f"A soma dos números é: {sum(numeros)}")
print(f"A média dos números é {sum(numeros)/len(numeros)}")

numeros.remove(10)
numeros.index(11)
print(numeros)

print(f"A multiplicação do quinto e sexto elemento da lista é: {numeros[5]*numeros[6]}")

numeros.sort(reverse=True)
print(numeros)