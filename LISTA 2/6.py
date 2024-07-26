# Crie um Programa que pergunte em que turno você estuda. Peça para digitar M - Matutino ou VVespertino ou N - Noturno. Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou
# "Valor Inválido!", conforme o caso.

turn = print("Digite o turno que você estuda\nDigite M - Matutino ou V - Vespertino ou N - Noturno")
tur = input("Digite o turno: ")

if tur == "M":
    print("Bom dia!")
    
elif tur == "V":
    print("Boa tarde!")

elif tur == "N":
    print("Boa Noite!")

else:
    print("Valor Inválido.")