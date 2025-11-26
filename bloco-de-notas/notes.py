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

actions = {
    "read": "ler",
    "new": "criar"
}

if not arguments:
    print(f"Invalid command usage!\nPor favor, escolha um dos seguintes comandos: {list(cmds)}")
    sys.exit(1)

if arguments[0] not in cmds:
    print(f"Invalid command {arguments[0]}!\nPor favor, escolha um dos seguintes comandos: {list(cmds)}")

while True:
    if arguments[0] == "read":
        try:
            for line in open(filepath):
                try:
                    title, tag, text = line.split("\t")
                    arg_tag = arguments[1].lower()
                except IndexError as e:
                    #TODO: Resolver problema de loop neste erro.
                    arg_tag = input("Por Favor, digite uma tag para executar a busca: ").strip().lower()
                if tag.lower() == arg_tag:
                    print(f"title: {title}")
                    print(f"text: {text}")
        except FileNotFoundError as e:
            print(f"[ERROR] {str(e)}!\nPor favor, crie uma nota utilizando o comando `new` antes de buscar.")
        
        

    if arguments[0] == "new":
        try:
            title = arguments[1]
        except IndexError :
            title = input("Por favor, adicione um Título: ")
        
        text = [
            f"{title}",
            input("tag:").strip(),
            input("text:\n").strip(),
            
        ]

        with open(filepath, "a") as file_:
            file_.write("\t".join(text) + "\n")
    
    next_step = input(f"Você gostaria de {'criar' if arguments[0] == actions['new'] else actions['read']} mais uma nota? [Y/n]").strip().lower()

    if next_step != "y":
        break
    else:
        continue
