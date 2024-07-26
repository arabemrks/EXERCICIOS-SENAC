num = int(input("Digite um numero: "))

#utilizando for
for i in range (1,11):
    res = i*num
    print(f"{num} X {i} = {res}")
    i = i+1

#utilizando while
cont = 1
while cont <= 10:
    print(f"{num} X {cont} = {num * cont}")
    cont = cont + 1