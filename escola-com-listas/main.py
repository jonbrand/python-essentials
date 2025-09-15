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
sports_extra_class = ["João", "Ricardo", "Roberto", "Carlos", "Rafael", "Hugo", "Cláudia"]
dance_extra_class = ["Laura", "Lisa", "Vivian", "Aline", "Yuri", "Tereza", "Bruna", "Fernanda"]

def generatingStudentList(classroom, extraClass):
    classList = []
    for student in classroom:
        if student in extraClass:
            classList.append(student)
    return classList

print("Alunos da Classe 01 na Aula de Inglês", generatingStudentList(clasroom01, english_extra_class))
print("Alunos da Classe 01 na Aula de Música", generatingStudentList(clasroom01, music_extra_class))
print("Alunos da Classe 01 na Aula de Esportes", generatingStudentList(clasroom01, sports_extra_class))
print("Alunos da Classe 01 na Aula de Dança", generatingStudentList(clasroom01, dance_extra_class))
print("Alunos da Classe 02 na Aula de Inglês", generatingStudentList(clasroom02, english_extra_class))
print("Alunos da Classe 02 na Aula de Música", generatingStudentList(clasroom02, music_extra_class))
print("Alunos da Classe 02 na Aula de Esportes", generatingStudentList(clasroom02, sports_extra_class))
print("Alunos da Classe 02 na Aula de Dança", generatingStudentList(clasroom02, dance_extra_class))
print("Alunos da Classe 03 na Aula de Inglês", generatingStudentList(clasroom03, english_extra_class))
print("Alunos da Classe 03 na Aula de Música", generatingStudentList(clasroom03, music_extra_class))
print("Alunos da Classe 03 na Aula de Esportes", generatingStudentList(clasroom03, sports_extra_class))
print("Alunos da Classe 03 na Aula de Dança", generatingStudentList(clasroom03, dance_extra_class))