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

$ notes.py read new-tag
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

if not arguments:
    print(f"Invalid command usage!\nPor favor, escolha um dos seguintes comandos: {list(cmds)}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}!\nPor favor, escolha um dos seguintes comandos: {list(cmds)}")

if arguments[0] == "read":
    for line in open(filepath):
        title, tag, text = line.split("\t")

        if tag.lower() == arguments[1].lower():
            print(f"title: {title}")
            print(f"text: {text}")
        

if arguments[0] == "new":

    try:
        title = arguments[1]
    except IndexError as e:
        print(f"[ERROR] {str(e)}!\nPor favor, adicione um título ao arquivo neste formato 'file name'")
        sys.exit(1)
    
    text = [
        f"{title}",
        input("tag:").strip(),
        input("text:\n").strip(),
        
    ]

    with open(filepath, "a") as file_:
        file_.write("\t".join(text) + "\n")
