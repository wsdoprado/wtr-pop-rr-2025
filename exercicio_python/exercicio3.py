"""
Exercício 3 - Listas em Python
-------------------------------
Este exercício apresenta como criar e manipular listas em Python.

Objetivos:
1. Criar uma lista de strings.
2. Acessar elementos por índice.
3. Iterar sobre uma lista usando loop.
4. Verificar se um elemento existe na lista.
"""

# Declaração de variáveis
aluno1 = "William Prado"
aluno2 = "Miguel Prado"
aluno3 = "Jose Prado"
aluno4 = "Eduardo Reis"
aluno5 = "Carlos Andre"
aluno6 = "Pedro Elias"

# Lista de strings
lista_alunos = [aluno1, aluno2, aluno3, aluno4, aluno5]
# Índices:         0        1        2        3        4

# Mostrar lista completa no terminal
print("--- Lista de Alunos ---")
print(lista_alunos)

# Mostrar elemento no índice 4
print("\nAluno no índice 4:")
print(lista_alunos[4])

# Loop de repetição na lista
print("\n--- Iterando sobre a lista ---")
for aluno in lista_alunos:
    print(aluno)

# Validação: verificar se aluno6 está na lista
print("\n--- Verificação de presença ---")
if aluno6 in lista_alunos:
    print("Aluno encontrado!")
else:
    print(f"Aluno: {aluno6} não encontrado na lista")