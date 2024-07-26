def quantidade_digitos(digito):
    quant = len(str(abs(digito)))
    print(f"O número {digito} tem {quant} dígitos.")

quantidade_digitos(int(input("Digite um numero: ")))