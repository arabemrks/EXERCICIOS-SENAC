x = 0
cont = 0
while cont < 10:
    y = int(input("Digite um valor: "))
    if y > 0:
        x = x + y
        cont = cont + 1
        
    elif y < 0:
        cont = cont + 1

print(f"A média dos números digitados é {x/10}")