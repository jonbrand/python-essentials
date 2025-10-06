#!/usr/bin/env python3
"""
    Calculadora Prefix

    Funcionamento:

    [operação] [n1] [n2]

    Operações:
    sum -> +
    sub -> -
    mul -> *
    div -> /

    Uso:
    $ prefixcalc.py sum 5 2
    --> 7

    $ prefixcalc.py mul 5 2
    --> 10
"""
___version__ = "0.1.1"
__author__ = "Jonatas Brandão"
__license__ = "Unlicense"

import sys

arguments = sys.argv[1:]

if not arguments:
    operation = input("Digite a operação: ")
    n1 = input("Digite n1: ")
    n2 = input("Digite n2: ")
    operations = [operation, n1, n2]
elif len(arguments) != 3:
    print("Argumentos inválidos!")
    print("Exemplo correto: sum 5 5")
    sys.exit(1)

operation, *nums = arguments

# TODO -> Validar Operações

# TODO -> Validar números

# operation = sys.argv[1]
# n1 = int(sys.argv[2]) 
# n2 = int(sys.argv[3])

# Função de soma
def sum(n1, n2):
    result = n1 + n2
    return result

# Função de subtração
def sub(n1, n2):
    result = n1 - n2
    return result

# Função de multiplicação
def mul(n1, n2):
    result = n1 * n2
    return result

# Função de divisão
def div(n1, n2):
    result = n1 / n2
    return result

# TODO -> Integrar dicionário com operações

operations = {
    "sum": sum,
    "sub": sub,
    "mul": mul,
    "div": div
}

# TODO -> Formatar resultado

print(arguments)