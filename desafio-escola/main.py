#!/usr/bin/env python3
"""Exibe relatório de crianças por atividade.
Imprimir a lista de crianças agrupadas por sala
que frequentas cada uma das atividades.
"""
__version__ = "0.1.2"

data = {
    'classRooms': {
      'class01': ['Erik', 'Maia', 'Gustavo', 'Manuel', 'Sofia', 'Joana'],
      'class02': ['Joao', 'Antonio', 'Carlos', 'Maria', 'Isolda']
    },
    'extraClass': {
      'aula_ingles': ['Erik', 'Maia', 'Joana', 'Carlos', 'Antonio'],
			'aula_musica': ['Erik', 'Carlos', 'Maria'],
			'aula_danca': ['Gustavo', 'Sofia', 'Joana', 'Antonio'],
		},
    'activities': {
      ('Inglês', 'aula_ingles'),
    	('Música', 'aula_musica'),
    	('Dança', 'aula_danca'),
		}
}

for nome_atividade, atividade in data['activities']:

    print(f"Alunos da atividade {nome_atividade}\n")
    print("-" * 40)

    atividade_sala1 = set(data['classRooms']['class01']) & set(data['extraClass'][atividade])
    atividade_sala2 = set(data['classRooms']['class02']).intersection(data['extraClass'][atividade])

    print("Sala1 ", atividade_sala1)
    print("Sala2 ", atividade_sala2)

    print()
    print("#" * 40)