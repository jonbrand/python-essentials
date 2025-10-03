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
___version__ = "0.1.0"
__author__ = "Jonatas Brandão"
__license__ = "Unlicense"

import sys

operation = sys.argv[1]
n1 = int(sys.argv[2])
n2 = int(sys.argv[3])

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

operations = {
    "sum": sum,
    "sub": sub,
    "mul": mul,
    "div": div
}

print(operations[operation](n1, n2))