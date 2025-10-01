"""
Exercício 1 - Tipos de Variáveis em Python
------------------------------------------
Este exercício apresenta como criar e utilizar diferentes tipos de variáveis
em Python: string, inteiro, float e booleano.

Objetivos:
1. Declarar variáveis de diferentes tipos.
2. Exibir seus valores no terminal.
3. Mostrar o tipo de cada variável utilizando a função `type()`.
"""

# String (texto)
nome = "William Stephan do Prado"

# Inteiro (número inteiro, sem casas decimais)
idade = 32

# Float (número decimal)
altura = 1.82

# Boolean (verdadeiro ou falso)
futebol = True

# Lista (coleção ordenada e mutável)
hobbies = ["futebol", "pescaria", "viagens"]

# Dicionário (coleção de pares chave-valor)
dados_pessoais = {
    "nome": nome,
    "idade": idade,
    "altura": altura
}

# Tupla (coleção ordenada e imutável)
cores_favoritas = ("azul", "verde", "preto")

# Conjunto (coleção não ordenada e sem duplicatas)
numeros1 = {1, 2, 3, 3, 4}

# None (valor nulo)
variavel_vazia = None

# Mostrar conteúdo das variáveis
print("--- Conteúdo das Variáveis ---")
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Altura: {altura}")
print(f"Gosta de futebol: {futebol}")
print(f"Hobbies: {hobbies}")
print(f"Dados Pessoais: {dados_pessoais}")
print(f"Cores Favoritas: {cores_favoritas}")
print(f"Números: {numeros1}")
print(f"Variável Vazia: {variavel_vazia}")

# Mostrar tipos das variáveis
print("\n--- Tipos de Variáveis ---")
print(f"nome: {type(nome)}")
print(f"idade: {type(idade)}")
print(f"altura: {type(altura)}")
print(f"futebol: {type(futebol)}")
print(f"hobbies: {type(hobbies)}")
print(f"dados_pessoais: {type(dados_pessoais)}")
print(f"cores_favoritas: {type(cores_favoritas)}")
print(f"numeros: {type(numeros1)}")
print(f"variavel_vazia: {type(variavel_vazia)}")