# Leia um número fornecido pelo usuário. Se esse número for positivo, calcule a raiz quadrada do
# número. Se o número for negativo, mostre uma mensagem dizendo que o número é inválido.
import math

num = int(input("Digite um número: "))

if num > 0:
    raiz = math.sqrt(num)
    print(f"A raiz quadrada é: {raiz}")

else:
    print("O número é inválido")