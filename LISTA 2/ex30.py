# Uma empresa vende o mesmo produto para quatro diferentes estados. Cada estado possui uma
# taxa diferente de imposto sobre o produto (MG 7%; SP 12%; RJ 15%; MS 8%). Crie um programa
# em que o usuário entre com o valor e o estado destino do produto e o programa retorne o preço
# final do produto acrescido do imposto do estado em que ele será vendido. Se o estado digitado
# não for válido, mostrar uma mensagem de erro.

prod = float(input("Digite o valor do produto: "))

print("Estados de destino:\nMG 7%\nSP 12%\nRJ 15%\nMS 8%")

estado = input("Digite para qual estado irá enviar: ")

if estado == "MG":
    x = prod + (prod * 0.07)
    print(f"Valor final é {x}")

elif estado == "SP":
    x = prod + (prod * 0.12)
    print(f"Valor final é {x}")

elif estado == "RJ":
    x = prod + (prod * 0.15)
    print(f"Valor final é {x}")

elif estado == "MS":
    x = prod + (prod * 0.08)
    print(f"Valor final é {x}")

else:
    print("Valor inválido")