#!/usr/bin/env python3
"""
    Relatório de crianças por atividade.

    - Imprime a lista de crianças agrupadas por sala que frequentam cada uma das atividades.
    - Utilize os tipos de dados de Tuplas e Listas.
"""
__version__ = "0.1.0"

students = {
    "extraClassNames": {
        "english": "Inglês",
        "music": "Música",
        "sports": "Esportes",
        "dance": "Dança",
    },
    "classroom": {
        "clasroom01": ["João", "Ricardo", "Roberto", "Aline", "Yuri", "Tereza", "Bruna", "Fernanda"],
        "clasroom02": ["Antônio", "Vitor", "Rodrigo", "Alice", "Yara", "Tamara", "Ana", "Leandro"],
        "clasroom03": ["Laura", "Lisa", "Vivian", "Alex", "Carlos", "Rafael", "Hugo", "Cláudia"],
    },
    "extraClass": {
        "english_extra_class": ["Vitor", "Rodrigo", "Alice", "Yara", "Tamara", "Ana", "Hugo", "Bruna", "Fernanda"],
        "music_extra_class": ["João", "Ricardo", "Roberto", "Aline", "Yuri", "Tereza", "Ana", "Leandro", "Hugo", "Cláudia"],
        "sports_extra_class": ["João", "Ricardo", "Roberto", "Carlos", "Rafael", "Hugo", "Cláudia", "Yara"],
        "dance_extra_class": ["Laura", "Lisa", "Vivian", "Aline", "Yuri", "Tereza", "Bruna", "Fernanda", "Alice"],
    },
}

def generatingStudentList(classroom, extraClass, extraClassName):
    list = set(classroom) & set(extraClass)
    
    report = f"\nAlunos da Atividade {extraClassName}:\n{40*'-'}\n{list}\n{40*'#'}\n"
    
    return report

print("=" * 50)
print("RELATÓRIO GERAL - ALUNOS POR ATIVIDADE")
print("=" * 50)

# Sala 01
print(f"\n{'='*20} SALA 01 {'='*20}")
print(generatingStudentList(students["classroom"]["clasroom01"], students["extraClass"]["dance_extra_class"], students["extraClassNames"]["dance"]))
print(generatingStudentList(students["classroom"]["clasroom01"], students["extraClass"]["music_extra_class"], students["extraClassNames"]["music"]))
print(generatingStudentList(students["classroom"]["clasroom01"], students["extraClass"]["sports_extra_class"], students["extraClassNames"]["sports"]))
print(generatingStudentList(students["classroom"]["clasroom01"], students["extraClass"]["english_extra_class"], students["extraClassNames"]["english"]))

# Sala 02
print(f"\n{'='*20} SALA 02 {'='*20}")
print(generatingStudentList(students["classroom"]["clasroom02"], students["extraClass"]["dance_extra_class"], students["extraClassNames"]["dance"]))
print(generatingStudentList(students["classroom"]["clasroom02"], students["extraClass"]["music_extra_class"], students["extraClassNames"]["music"]))
print(generatingStudentList(students["classroom"]["clasroom02"], students["extraClass"]["sports_extra_class"], students["extraClassNames"]["sports"]))
print(generatingStudentList(students["classroom"]["clasroom02"], students["extraClass"]["english_extra_class"], students["extraClassNames"]["english"]))

# Sala 03
print(f"\n{'='*20} SALA 03 {'='*20}")
print(generatingStudentList(students["classroom"]["clasroom03"], students["extraClass"]["dance_extra_class"], students["extraClassNames"]["dance"]))
print(generatingStudentList(students["classroom"]["clasroom03"], students["extraClass"]["music_extra_class"], students["extraClassNames"]["music"]))
print(generatingStudentList(students["classroom"]["clasroom03"], students["extraClass"]["sports_extra_class"], students["extraClassNames"]["sports"]))
print(generatingStudentList(students["classroom"]["clasroom03"], students["extraClass"]["english_extra_class"], students["extraClassNames"]["english"]))