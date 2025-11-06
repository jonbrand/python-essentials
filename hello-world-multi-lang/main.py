#!/usr/bin/env python3
"""Hello World Multi Languages.
  
    This is a simple Python script that prints "Hello, World!" depending on the 
    language configured in the environment.
  
    Usage:
  
    Have the LANG variable properly configured:
        
        export LANG=pt_BR

    Or inform through arguments such as "--lang=" for languages and "--count=" for amount of times to print.
  
    Or the user will have to type.
                    
    Run:
        python3 hello.py
        or
        ./hello.py
  
"""
# metadata
__version__ = "0.1.4"
__author__ = "Jonatas Brandão"
__license__ = "Unlicense"

import os
import sys

arguments = {
    "lang": None,
    "count": 1,
}

for args in sys.argv[1:]:
    try:
        key, value = args.split("=")
    except ValueError as e:
        # TODO Logging
        print(
            f"[ERROR] {str(e)}!\nVocê utilizou `{args}` ao invés de `--key=value`\n"
            f"Por favor, utilize o sinal de `=` para o melhor aproveitamento do comando!"
        )
        sys.exit(1)

    key = key.lstrip("-").strip()
    value = value.strip()

    if key not in arguments:
        print(f"Invalid Option `{key}`")
        sys.exit()
    arguments[key] = value

current_language = arguments["lang"]

if current_language is None:
    if "LANG" in os.environ:
        current_language = os.getenv("LANG")
    else:
        current_language = input("Choose a language:")
        
current_language = current_language[:5]

msg = {
    "pt_BR": "Olá, Mundo!",
    "en_US": "Hello, World!",
    "ru_RU": "Привет, Мир!",
    "es_SP": "¡Hola mundo!",
}

try:
    message = msg[current_language]
except KeyError as e:
    print(f"Escolha uma opção de linguagem válida\nPor favor, escolha entre estas opções: {list(msg.keys())}")
    sys.exit(1)
print(message = int(arguments['count']))