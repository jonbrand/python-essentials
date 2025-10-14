#!/usr/bin/env python3
""" Script para práticar a Interpolação
    Imprime e envia uma mensagem de Email
"""
__version__ = "0.1.1"
__author__ = "Jonatas"
__license__ = "Unlicense"

import os
import sys

arguments = sys.argv[1:]

if not arguments:
    print("Insira o arquivo de leitura desejado.")
    sys.exit(1)

filename = arguments[0]
email_template = arguments[1]

path = os.curdir
filepath = os.path.join(path, filename)
email_template_path = os.path.join(path, email_template)

for line in open(filepath):
    nome, email = line.split(",")
    #TDO: Substituir por envio de Email
    print(f"Email enviado com sucesso para {email}!")
    print(
        open(email_template_path).read()
        % {
            "nome": nome,
            "produto": "caneta",
            "texto": "Escrever muito bem!",
            "link": "http//www.canetaboaa.com.br/unidades",
            "quantidade": 5,
            "preco": 60.0,
        }
    )
    print("-" * 50)
