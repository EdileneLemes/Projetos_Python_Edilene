# Projeto Boletim Escolar - Edilene Lemes
print(" Projeto - Boletim Escolar")
print("============================================================================")
print("")

alunos = []

# Usar input() para cadastrar os dados.
quantidade = int(input("Quantos alunos deseja cadastrar?"))

# Usar laço de repetição.
for i in range(quantidade):
    print(f" \nCadastro do {i+1}º aluno:")

# Entrada de das notas através do input() e armazenar na variável.
    nome = input("Nome: ")
    nota1 = float(input("Nota1:  "))
    nota2 = float(input("Nota2:  "))
    nota3 = float(input("Nota3:  "))
    
# Criar um dicionário para cada aluno.
    aluno = {
        "nome" : nome,
        "nota1" : nota1,
        "nota2" : nota2,
        "nota3" : nota3
    }
    
# Adiciona o dicionario aluno na lista alunos.
    alunos.append(aluno)
   
print("====================================================")
print("Boletim de Estudantes:")
print("====================================================")

for aluno in alunos:
    nome = aluno["nome"]
    nota1 = aluno["nota1"]
    nota2 = aluno["nota2"]
    nota3 = aluno["nota3"]
    media = (nota1 + nota2 + nota3) / 3
    status = "Aprovado" if media >= 4 else "Reprovado"
    print(f"{nome} - Média: {media:.1f} - {status}")
