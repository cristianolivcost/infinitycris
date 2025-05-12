num_alunos = int(input("Digite o número de alunos: "))

soma_medias = 0  

for i in range(num_alunos):
    print(f"\nAluno {i + 1}:")
    nome = input("Nome do aluno: ")

 
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    nota3 = float(input("Digite a terceira nota: "))

   
    media = (nota1 + nota2 + nota3) / 3
    soma_medias += media

    
    status = "Aprovado" if media >= 7.0 else "Reprovado"

  
    print(f"Nome: {nome}")
    print(f"Notas: {nota1}, {nota2}, {nota3}")
    print(f"Média: {media:.2f}")
    print(f"Status: {status}")


media_geral = soma_medias / num_alunos
print(f"\nMédia geral da turma: {media_geral:.2f}")