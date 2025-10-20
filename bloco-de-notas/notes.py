"""Bloco de notas

Este programa consiste em implementar as funcionalidades minimas de blocos de notas,
permitindo a criação de uma nota com título e um texto de até uma linha e a leitura de
notas criadas.

# Criação de notas

$ notes.py new "Title"
tag: new-tag
text:
Text Note...

# Leitura de Notas

$ notes.py read --tag=new-tag
..
..

"""
__version__ = "0.1.0"
__author__ = "Jonatas Brandão"
__license__ = "Unlicense"

import os
import sys

path = os.curdir
filepath = os.path.join(path, "notes.txt")

arguments = sys.argv[1:]
cmds = ("read", "new")
subCmds = ("--tag")

if not arguments:
    print(f"Invalid command usage!")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}!")

if arguments[0] == "read":
    print("Deu certo!")
        

if arguments[0] == "new":
    tag = input("tag:")
    text = input("text:")

    with open(filepath, "a") as file_:
        file_.write(f"tag: {tag}\n text:\n{text}\n")