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

# Path dos arquivos e diretório atual
path = os.curdir
room_filepath = os.path.join(path, "rooms.txt")
reservation_filepath = os.path.join(path, "reservation.txt")

# Estrutura de dados (Dicionários) que lidam com os quartos e as reservas
rooms = {}
reservation = {}

# Loop que inicia o script

while True:
    user_name = input("Seja bem-vindo ao Hotel_Terminal!\n(Caso queira sair pressione enter para sair)\n\nQual é o seu nome?\n").strip()
    
    if user_name == "":
        break

    # Tenta ler o arquivo com as reservas existentes
    try:
        with open(reservation_filepath) as file_:
            for line in file_:
                client, code, days_reserved, booking_total = line.strip().split(',')
                reservation[code] = {"Nome do Cliente": client, "Dias de Reserva": days_reserved, "Total da Reserva": booking_total}
    except:
        print("Arquivo vázio.")

    # Tenta ler o arquivo contendo todos os quartos do hotel e outras informações 
    try:
        with open(room_filepath) as file_:
            for line in file_:
                code, room_name, price = line.strip().split(',')
                rooms[code] = {"Nome da Suíte": room_name, "Preço": int(price)}
    except:
        print("Arquivo vázio.")

    # Como posso acessar o valor do preço do quarto selecionado pelo usuário?
    
    # Cópia da estrutura de dados que lida com os quartos
    rooms_available = rooms.copy()
    
    # Percorre a estrutura de dados que lida com os quartos para remover dali quando um quarto for reservado
    for line in rooms:
        if line in reservation:
            rooms_available.pop(line)

    # Inputs do usuário
    # TODO: Mudar formato de apresentação dos quartos disponíveis
    print(f"Quartos disponíveis: {rooms_available.keys()}")
    room_number = input("Selecione um número de quarto: ")
    days_reserved = input("Quantos dias você gostaria de reservar o quarto?: ").strip()
    booking_total = int(rooms[room_number]["Preço"]) * int(days_reserved)
    # reservation = (user_name, room_number, days_reserved, booking_total)
    # Tenta adicionar uma reserva ao arquivo de reservas
    try:
        with open(reservation_filepath, "a") as file_:
            file_.write(f"{user_name},{room_number},{days_reserved},{booking_total}\n")

    except PermissionError as e:
        log.error(
            "%s O arquivo não foi encontrado",
            str(e)
        )

    finish_booking = input(f"A reserva vai ficar no valor de {booking_total}, gostaria de finalizar a sua compra? [Y,n]").strip()

    if finish_booking == "n":
        break
    else:

        next_step = input("Gostaria de fazer mais alguma reserva? [Y,n]").strip()
        
        if next_step == "n":
            break
        else:
            continue