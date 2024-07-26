numeros = []
n = int(input("Digite um numero: "))
 
cont = -2
if n % 2 == 0:
    while cont < n:
        cont = cont + 2
        numeros.append(cont)
        
else:
    print("Número digitado é ímpar")

numeros.sort(reverse=True)
print(numeros)

print("Fim do Programa")