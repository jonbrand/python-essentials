#!/usr/bin/env python3
"""
Alarme de temperatura

Faça um script que pergunta ao usuário qual a temperatura atual e o indice de umidade do ar para que seja exibida uma mensagem de alerta dependendo 
das condições:

- temp maior 45: "ALERTA!!! 🥵 Perigo calor extremo"

- temp maior que 30 e temp vezes 3 for maior ou igual a umidade: "ALERTA!!! 🥵♒ Perigo de calor úmido"

- temp entre 10 e 30: "😀 Normal"

- temp entre 0 e 10: "🥶 Frio"

- temp <0: "ALERTA!!! ⛄ Frio Extremo."

ex:

python3 temp.py 
temperatura: 30
umidade: 90
... 
"ALERTA!!! 🥵 Perigo calor extremo"
"""
import os
import sys
import logging
from logging import handlers

log_level = os.getenv("LOG_LEVEL", "WARNING").upper()

log = logging.Logger("Jonatas", log_level)

fh = handlers.RotatingFileHandler(
    "logs.log",
    maxBytes=10**6,
    backupCount=10
)

fh.setLevel(log_level)

fmt = logging.Formatter(
    '%(asctime)s  %(name)s  %(levelname)s '
    'l:%(lineno)d f:%(filename)s: %(message)s'
)

fh.setFormatter(fmt)

log.addHandler(fh)

info = {
    "temperatura": None,
    "umidade": None
}

keys = info.keys()

for key in keys:
    try:
        info[key] = float(input(f"Qual é a {key.title()}: ").strip())
    except ValueError as e:
        log.error(f"{key.title()} invalida!")
        print(f"[ERROR] {str(e)}!\nPor favor, digite um valor válido para a {key}: 10, 22.3, 25.0")
        sys.exit(1)

temp = info["temperatura"]
moise = info["umidade"]
temp_mois = temp * 0.3

if temp >= 45:
    print("ALERTA!!! 🥵 Perigo calor extremo")
elif temp > 30 and temp_mois >= moise:
    print("ALERTA!!! 🥵♒ Perigo de calor úmido")
elif temp >= 30 and temp_mois < moise:
    print("ALERTA!!! 🥵♒ Perigo de calor")
elif temp >= 10 and temp <= 30:
    print("😀 Normal")
elif temp >= 0 and temp <= 10:
    print("🥶 Frio")
elif temp < 0:
    print("ALERTA!!! ⛄ Frio Extremo.")