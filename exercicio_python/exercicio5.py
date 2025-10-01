"""
Exercício 5 - Dicionários Aninhados e Listas em Python
------------------------------------------------------
Este exercício apresenta como criar e manipular dicionários aninhados e listas.

Objetivos:
1. Criar dicionários com diferentes tipos de dados.
2. Inserir listas dentro de dicionários.
3. Iterar sobre listas de dicionários.
4. Acessar dados aninhados.
"""

# Dicionários representando filhos
filho1_aluno1 = {"nome": "Miguel Guedes", "idade": 5, "altura": 0.80, "casado": False}
filho2_aluno1 = {"nome": "José Guedes", "idade": 2, "altura": 0.60, "casado": False}

# Dicionários representando alunos
dados_aluno1 = {
    "nome": "William Prado",
    "idade": 32,
    "altura": 1.82,
    "casado": True,
    "filhos": [filho1_aluno1, filho2_aluno1]
}

dados_aluno2 = {
    "nome": "Eduardo Pereira",
    "idade": 40,
    "altura": 1.75,
    "casado": False,
    "filhos": []
}

# Lista contendo os dicionários dos alunos
lista_alunos = [dados_aluno1, dados_aluno2]

# Mostrar dados completos no terminal
print("\n--- Lista Completa de Alunos ---")
print(lista_alunos)

# Loop na lista de alunos
print("\n--- Informações dos Alunos ---")
for aluno in lista_alunos:
    print(f"Aluno: {aluno['nome']} - Idade: {aluno['idade']} - Altura: {aluno['altura']}m")
    
    # Verificar se o aluno tem filhos
    if aluno["filhos"]:
        print("Filhos:")
        for filho in aluno["filhos"]:
            print(f"  Nome: {filho['nome']} - Idade: {filho['idade']} anos - Altura: {filho['altura']}m")
    else:
        print("Sem filhos.")
