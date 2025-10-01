"""
Exercício 2 - Entrada de Dados em Python
----------------------------------------
Este exercício mostra como capturar informações digitadas pelo usuário
utilizando a função `input()`.

Objetivos:
1. Solicitar ao usuário seu nome e salário.
2. Converter o salário para número decimal (float).
3. Exibir as informações no terminal de forma formatada.
"""

# Entrada de dados
nome = input("Qual seu nome? ")

# Entrada de dados (sempre retorna string, por isso convertemos para float)
salario = float(input("Qual seu salário (em R$)? "))

# Mostrar dados no terminal
print("\n--- Dados do Usuário ---")
print(f"Nome: {nome}")
print(f"Salário: R$ {salario:.2f}")  # :.2f formata com 2 casas decimais