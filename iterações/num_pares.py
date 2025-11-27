#!/usr/bin/env python3
"""
Faça um programa que imprime na tela os números pares de 1 a 200

ex:
    `python3 num_pares.py`
    2
    4
    6
    8
    10
    ...
"""

num_pares = [x for x in range(2, 201, 2)]

for index in num_pares:
    print(index)