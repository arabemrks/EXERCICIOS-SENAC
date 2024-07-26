# Crie um algoritmo que calcule a média ponderada das notas de 3 provas. A primeira e a segunda
# prova têm peso 1 e a terceira tem peso 2. Ao final, mostrar a média do aluno e indicar se o aluno
# foi aprovado ou reprovado. A nota para aprovação deve ser igual ou superior a 60 pontos.

not1 = float(input("Digite a nota da primeira prova: "))
not2 = float(input("Digite a nota da segunda prova: "))
not3 = float(input("Digite a nota da terceira prova: "))

soma = not1+not2+not3

if soma > 60:
    print("Aprovado")

else:
    print("Reprovado")