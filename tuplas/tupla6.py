alunos = [("João", 8.0), ("Maria", 9.5), ("Pedro", 7.5), ("Ana", 8.5)]
maior_nota = 0
aluno_maior_nota = ""

for aluno,nota in alunos:
    if nota > maior_nota:
        maior_nota = nota
        aluno_maior_nota = aluno

print(f"Aluno com a maior nota é: {aluno_maior_nota}")