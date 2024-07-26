from time import sleep

num = int(input("Digite um numero: "))
cont = 0
while cont <= num:
    print(cont)
    sleep(0.2)
    cont += 1

print("Fim do Programa")