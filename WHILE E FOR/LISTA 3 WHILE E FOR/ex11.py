x = []
cont = 0
par = 0
while cont < 50:
    print(par)
    x.append(par)
    cont += 1
    par += 2

print(f"A soma dos primeiros 50 pares é: {sum(x)}")