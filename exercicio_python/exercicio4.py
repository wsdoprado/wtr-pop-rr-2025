"""
Exercício 4 - Dicionários em Python
-----------------------------------
Este exercício apresenta como criar e manipular dicionários em Python.
Também mostra como criar uma lista de dicionários.

Objetivos:
1. Criar dicionários com diferentes tipos de dados.
2. Acessar valores usando chaves.
3. Criar lista de dicionários.
4. Iterar sobre a lista e acessar dados internos.
"""

# Dicionários com dados de alunos
dados_aluno1 = {
    "nome": "William Prado",
    "idade": 32,
    "altura": 1.82,
    "casado": True,
    "filhos": ["Miguel", "José"]
}

dados_aluno2 = {
    "nome": "Eduardo Pereira",
    "idade": 40,
    "altura": 1.75,
    "casado": False,
    "filhos": []
}

# Mostrar dicionários no terminal
print("--- Dados Aluno 1 ---")
print(dados_aluno1)

print("\n--- Dados Aluno 2 ---")
print(dados_aluno2)

# Acessar valor específico usando chave
print("\nFilhos do Aluno 1:", dados_aluno1["filhos"])
print("Filhos do Aluno 2:", dados_aluno2["filhos"])

# Criar lista de dicionários
lista_alunos = [dados_aluno1, dados_aluno2]

# Mostrar lista de dicionários
print("\n--- Lista de Alunos ---")
print(lista_alunos)

# Iterar sobre lista de dicionários e mostrar dados
print("\n--- Iterando sobre lista de alunos ---")
for aluno in lista_alunos:
    print(f"Nome: {aluno['nome']}, Idade: {aluno['idade']}, Casado: {aluno['casado']}")