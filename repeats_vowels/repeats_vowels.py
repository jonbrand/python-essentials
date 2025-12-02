#!/usr/bin/env python3
"""
Repete vogais

Faça um programa que pede ao usuário que digite uma ou mais palavras e imprime cada uma das palavras com suas vogais duplicadas.

python repete_vogal.py
'Digite uma palavra (ou enter para sair):' Python
'Digite uma palavra (ou enter para sair):' Bruno
'Digite uma palavra (ou enter para sair):' <enter>
Pythoon
Bruunoo
"""
__version__ = "0.0.1"
__author__ = "Jonatas"
__license__ = "Unlicense"

# lista de palavras
words = []
new_words = []

# Inicia a sessão
while True:
    # Pergunta ao usuário a palavra e captura ela.
    response = input("Digite uma palavra (ou enter para sair): ").strip()
    if response == "":
        break

    words.append(response)

for word in words:
    # TODO: Remover acentos usando Função
    new_word = word.replace("a", "aa").replace("e", "ee").replace("i", "ii").replace("o", "oo").replace("u", "uu")
    new_words.append(new_word)

print(*new_words, sep="\n")