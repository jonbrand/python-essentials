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
import logging
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

arguments = {
    "lang": None,
    "count": 1,
}

for args in sys.argv[1:]:
    try:
        key, value = args.split("=")
    except ValueError as e:
        log.error(
            "Por favor, utilize o sinal de `=` para o melhor aproveitamento do comando!\nVocê utilizou %s ao invés de `--key=value` \n%s",
            args,
            str(e)
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
    log.error(
        "Você Escolheu uma opção inválida: %s\nPor favor, escolha uma opção de linguagem válida: %s",
        str(e),
        list(msg.keys()),
    )
    sys.exit(1)
print((message + "\n") * int(arguments['count']))