#Dicionário - dict
filho1_aluno1 = {"nome": "Miguel Guedes", "idade": 5, "altura": 0.80, "casado": False}
filho2_aluno1 = {"nome": "José Guedes", "idade": 2, "altura": 0.60, "casado": False}

#Dicionário - dict + Listas - list
dados_aluno1 = {"nome": "William Prado", "idade": 32, "altura": 1.82, "casado": True, "filhos": [filho1_aluno1,filho2_aluno1]}
dados_aluno2 = {"nome": "Eduardo Pereira", "idade": 40, "altura": 1.75, "casado": False, "filhos": []}

#Lista
lista_alunos = [dados_aluno1,dados_aluno2]

#Mostrar dados no Terminal
print(lista_alunos)

#Loop na Lista alunos
for aluno in lista_alunos:
    print(f"Aluno: {aluno['nome']} - Idade: {aluno['idade']} - Altura: {aluno['altura']}")
    for filho in aluno['filhos']:
        print(f"Nome filho: {filho['nome']} - Idade: {filho['idade']}")
