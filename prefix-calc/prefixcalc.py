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
___version__ = "0.1.2"
__author__ = "Jonatas Brandão"
__license__ = "Unlicense"

import sys
import os
import logging
from datetime import datetime
from logging import handlers

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

log = logging.Logger("Jonatas", log_level)

fileHandle = handlers.RotatingFileHandler(
    "logs.log",
    maxBytes=10**6,
    backupCount=10
)

fileHandle.setLevel(log_level)

fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)

fileHandle.setFormatter(fmt)

log.addHandler(fileHandle)

arguments = sys.argv[1:]

if not arguments:
    operation = input("Digite a operação: ")
    n1 = input("Digite n1: ")
    n2 = input("Digite n2: ")
    arguments = [operation, n1, n2]
elif len(arguments) != 3:
    print("Argumentos inválidos!")
    print("Exemplo correto: sum 5 5")
    sys.exit(1)

operation, *nums = arguments

valid_operations = { "sum", "sub", "div", "mul" }

if operation not in valid_operations:
    print("Operação inválida!")
    print(valid_operations)
    sys.exit(1)

valid_numbers = []

for num in nums:
    if not num.replace(".","").isdigit():
        print("Número inválido {num}!")
        sys.exit(1)
    if "." in num:
        num = float(num)
    else:
        num = int(num)
    valid_numbers.append(num)

n1, n2 = valid_numbers

def sum(n1, n2):
    result = n1 + n2
    return result

def sub(n1, n2):
    result = n1 - n2
    return result

def mul(n1, n2):
    result = n1 * n2
    return result

def div(n1, n2):
    result = n1 / n2
    return result

operations = {
    "sum": sum,
    "sub": sub,
    "mul": mul,
    "div": div
}

result = operations[operation](n1, n2)

print(f"O resultado é: {result}")

path = os.curdir
filepath = os.path.join(path, "prefixcalc.log")
timestamp = datetime.today()
user = os.getenv("USER", "Anonymous")


try:
    with open(filepath, "a") as file_:
        file_.write(f"{timestamp} - {user} - {operation} {n1} {n2} = {result}\n")

except PermissionError as e:
    log.error(
        "%s O arquivo não foi encontrado",
        str(e)
    )