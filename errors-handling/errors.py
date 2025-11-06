#!/usr/bin/env python3
import os
import sys

# EAFP - Easy to  Ask Forgiveness than permission

try:
    names = open("names.txt").readlines()
except FileExistsError as e:
    print(f"{str(e)}.")
    sys.exit(1)
else:
    print("Sucesso!")
finally:
    print("Execute isso sempre!")