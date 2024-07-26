lista = [2,99,28,27,32,38,44,55,666,1,24]
cont = 0

while cont < len(lista):
    print(lista[cont])
    if lista[cont] == 44:
        print("Encontramos o numero 44")
        break
    else:
        cont = cont + 1

print("Fim do programa")