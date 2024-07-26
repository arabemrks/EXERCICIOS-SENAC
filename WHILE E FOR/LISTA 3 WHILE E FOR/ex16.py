numeros = []
n = int(input("Digite um numero: "))
 
cont = -1
if n % 2 == 1:
    while cont < n:
        cont = cont + 2
        numeros.append(cont)
        
else:
    print("Número digitado é par")

print(numeros)

print("Fim do Programa")