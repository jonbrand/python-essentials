#!/usr/bin/env python3
"""Imprime a tabuada do 1 ao 10."""
__version__ = "0.1.0"
__author__ = "Jonatas"

factors = list(range(1,11))

for factor in factors:
    print("Tabuada do número:", factor)
    for newFactor in factors:
        print(factor, " x ", newFactor, " = ", factor * newFactor)
print("----------------------------")
