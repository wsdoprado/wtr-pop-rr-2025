aluno1 = "William Prado"
aluno2 = "Miguel Prado"
aluno3 = "Jose Prado"
aluno4 = "Eduardo Reis"
aluno5 = "Carlos Andre"
aluno6 = "Pedro Elias"

#Lista de Strings
lista_alunos = [aluno1,aluno2,aluno3,aluno4,aluno5]
#index             0      1      2      3      4

#Mostrar Lista no Terminal
print(lista_alunos)

#Mostrar Lista no Terminal no index 4
print(lista_alunos[4])

#Loop de Repetição na Lista
for aluno in lista_alunos:
    print(aluno)

#Validação
if aluno6 in lista_alunos:
    print("Aluno Encontrado")
else:
    print(f"Aluno: {aluno6} não encontrado na lista")
