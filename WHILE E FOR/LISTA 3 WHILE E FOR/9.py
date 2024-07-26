lista = []

cont = 0
while cont < 10:
    x = int(input("Digite um valor: "))
    lista.append(x)
    cont = cont + 1

print(f"O menor valor lido é {min(lista)}")
print(f"O maior valor lido é {max(lista)}")