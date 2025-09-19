#!/usr/bin/env python3
"""Hello World Multi Languages.
  
	This is a simple Python script that prints "Hello, World!" depending on the 
  language configured in the environment.
  
  Usage:
  
  Have the LANG variable properly configured:
		export LANG=pt_BR
                    
  Run:
		python3 hello.py
    or
    ./hello.py
  
"""
# metadata
__version__ = "0.0.1"
__author__ = "Jonatas Brandão"
__license__ = "Unlicense"

import os

current_language = os.getenv("LANG", "en_US")[:5]
msg = {
    "pt_BR": "Olá, Mundo!",
    "en_US": "Hello, World!",
    "ru_RU": "Привет, Мир!",
    "es_SP": "¡Hola mundo!",
}

print(msg[current_language]);
