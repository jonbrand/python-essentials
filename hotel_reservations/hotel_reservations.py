"""
Faça um programa de terminal que exiba para os usuários uma lista dos quartos disponíveis para alugar e o preço de cada quarto, esta informação está disponível
em um arquivo de texto separado por vírgulas.

`rooms.txt`
# código, nome, preço
1,Suite Master,500
2,Quarto Família,200
3,Quarto Single,100
4,Quarto Simples,50

O programa pergunta ao usuário o nome, qual o número do quarto a ser reservado e a quantidade de dias e no final exibe o valor 
estimado a ser pago.

O programa deve salvar esta escolha em outro arquivo contendo as reservas

`reservation.txt`
# cliente, quarto, dias
Bruno,3,12

Se outro usuário tentar reservar o mesmo quarto o programa vai exibir uma mensagem informando que já está reservado.
"""
__version__ = "0.0.1"
__author__ = "Jonatas"
__license__ = "Unlicense"

import os

path = os.curdir
room_filepath = os.path.join(path, "rooms.txt")
reservation_filepath = os.path.join(path, "reservation.txt")

rooms = {}
reservation = {}

while True:
    user_name = input("Seja bem-vindo ao Hotel_Terminal!\n(Caso queira sair pressione enter para sair)\n\nQual é o seu nome?\n").strip()
    if user_name == "":
        break

    with open(reservation_filepath) as file_:
        for line in file_:
          client, code, days_reserved = line.strip().split(',')
          reservation[code] = {"Nome do Cliente", client, "Dias de Reserva", days_reserved}

    with open(room_filepath) as file_:
      for line in file_:
          code, room_name, price = line.strip().split(',')
          rooms[code] = {"Nome da Suíte", room_name, "Preço", int(price)}
    

    # Como posso descobrir os qaurtos ocupados? Comparando reservation com room
    for line in rooms:
        if line == reservation[code]:
            print(reservation)

    # TODO: Verificar os quartos disponíveis
    print("Quartos disponíveis:")
    room_number = input("Selecione um número de quarto: ")
    days_reserved = input("Quantos dias você gostaria de reservar o quarto?: ")
    reservation = (user_name, room_number, days_reserved)
    print(reservation)
    

    try:
        with open(filepath, "a") as file_:
            file_.write(f"{user_name},{room_number},{days_reserved}\n")

    except PermissionError as e:
        log.error(
            "%s O arquivo não foi encontrado",
            str(e)
        )

    next_step = input("Gostaria de fazer mais alguma reserva? [Y,n]").strip()
    
    if next_step == "n":
        break
    else:
        continue