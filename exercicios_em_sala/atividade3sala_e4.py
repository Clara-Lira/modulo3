import os
from loguru import logger


def contador_palavras(filename):
    with open(filename, "r", encoding="utf-8") as file_object:
        conteudo = file_object.read()

    palavras = conteudo.split()

    return len(palavras)


def guardar_info(titulo, quant_palavras, quant_bytes):
    info = f"" \
           f"Titulo: {titulo}; " \
           f"Qtd Palavras: {quant_palavras}, " \
           f"Qtd bytes: {quant_bytes}\n"

    with open("database.txt", "a", encoding="utf-8") as file_object:
        file_object.write(info)


def ler_database():
    with open("database.txt", "r", encoding="utf-8") as file_object:
        for linha in file_object:
            print(linha.rstrip())


while True:
    try:

        opcao = int(input(
            "1- the_prince\n"
            "2- Children_of_destiny_by_Molly_Elliot_Seawell\n"
            "3- A_bird_of_passage_by_B_M_Croker\n"
            "4- ler o database\n"
            "0 - sair\n"
        ))

        if opcao == 1:
            print(contador_palavras("the_prince.txt"))
            guardar_info("the_prince",
                         contador_palavras("the_prince.txt"),
                         (os.path.getsize("the_prince.txt") / 1000000))
        elif opcao == 2:
            print(contador_palavras("A_bird_of_passage_by_B_M_Croker.txt"))
            guardar_info("A_bird_of_passage_by_B_M_Croker",
                         contador_palavras("A_bird_of_passage_by_B_M_Croker.txt"),
                         (os.path.getsize("A_bird_of_passage_by_B_M_Croker.txt") / 1000000))
        elif opcao == 3:
            print(contador_palavras("Children_of_destiny_by_Molly_Elliot_Seawell.txt"))
            guardar_info("Children_of_destiny_by_Molly_Elliot_Seawell",
                         contador_palavras("Children_of_destiny_by_Molly_Elliot_Seawell.txt"),
                         (os.path.getsize("Children_of_destiny_by_Molly_Elliot_Seawell.txt") / 1000000))
        elif opcao == 4:
            ler_database()
        elif opcao == 0:
            break

    except Exception as error:
        logger.error(error)
