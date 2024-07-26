# A nota final de um estudante e calculada a partir de três notas atribuídas entre o intervalo de 0
# até 10, respectivamente, a um trabalho de laboratório, a uma avaliação semestral e a um exame
# final. A média das três notas mencionadas anteriormente obedece aos pesos: Trabalho de
# Laboratório: 2; Avaliação Semestral: 3; Exame Final: 5. De acordo com o resultado, mostre na tela
# se o aluno está reprovado (média entre 0 e 2,9), de recuperação (entre 3 e 5,9) ou se foi
# aprovado. Crie todas as verificações necessárias

not1 = float(input("Digite a nota da primeira prova: "))
not2 = float(input("Digite a nota da segunda prova: "))
not3 = float(input("Digite a nota da terceira prova: "))

if 0 <= not1 <= 2 and 0 <= not2 <= 3 and 0 <= not3 <= 5:
    med = (not1 + not2 + not3)

    if 0 <= med <= 2.9:
        print("Reprovado")

    elif 0 <= med <= 2.9:
        print("Reprovado")

    elif 3 <= med <= 5.9:
        print("Recuperação")

    elif 6 <= med <= 10:
        print("Aprovado")

else:
    print("Nota Inválida")