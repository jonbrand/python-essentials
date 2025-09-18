#!/usr/bin/env python3
"""
    Relatório de crianças por atividade.

    - Imprime a lista de crianças agrupadas por sala que frequentam cada uma das atividades.
    - Utilize os tipos de dados de Tuplas e Listas.
"""
__version__ = "0.1.0"

clasroom01 = ["João", "Ricardo", "Roberto", "Aline", "Yuri", "Tereza", "Bruna", "Fernanda"]
clasroom02 = ["Antônio", "Vitor", "Rodrigo", "Alice", "Yara", "Tamara", "Ana", "Leandro"]
clasroom03 = ["Laura", "Lisa", "Vivian", "Alex", "Carlos", "Rafael", "Hugo", "Cláudia"]

english_extra_class = ["Vitor", "Rodrigo", "Alice", "Yara", "Tamara", "Ana", "Hugo", "Bruna", "Fernanda"]
music_extra_class = ["João", "Ricardo", "Roberto", "Aline", "Yuri", "Tereza", "Ana", "Leandro", "Hugo", "Cláudia"]
sports_extra_class = ["João", "Ricardo", "Roberto", "Carlos", "Rafael", "Hugo", "Cláudia", "Yara"]
dance_extra_class = ["Laura", "Lisa", "Vivian", "Aline", "Yuri", "Tereza", "Bruna", "Fernanda", "Alice"]

def generatingStudentList(classroom, extraClass, extraClassName):
    list = set(classroom) & set(extraClass)
    
    report = f"\nAlunos da Atividade {extraClassName}:\n{40*'-'}\n{list}\n{40*'#'}\n"
    
    return report

print("=" * 50)
print("RELATÓRIO GERAL - ALUNOS POR ATIVIDADE")
print("=" * 50)

# Sala 01
print(f"\n{'='*20} SALA 01 {'='*20}")
print(generatingStudentList(clasroom01, dance_extra_class, "Aula de Dança"))
print(generatingStudentList(clasroom01, music_extra_class, "Aula de Música"))
print(generatingStudentList(clasroom01, sports_extra_class, "Aula de Esportes"))
print(generatingStudentList(clasroom01, english_extra_class, "Aula de Inglês"))

# Sala 02
print(f"\n{'='*20} SALA 02 {'='*20}")
print(generatingStudentList(clasroom02, dance_extra_class, "Aula de Dança"))
print(generatingStudentList(clasroom02, music_extra_class, "Aula de Música"))
print(generatingStudentList(clasroom02, sports_extra_class, "Aula de Esportes"))
print(generatingStudentList(clasroom02, english_extra_class, "Aula de Inglês"))

# Sala 03
print(f"\n{'='*20} SALA 03 {'='*20}")
print(generatingStudentList(clasroom03, dance_extra_class, "Aula de Dança"))
print(generatingStudentList(clasroom03, music_extra_class, "Aula de Música"))
print(generatingStudentList(clasroom03, sports_extra_class, "Aula de Esportes"))
print(generatingStudentList(clasroom03, english_extra_class, "Aula de Inglês"))