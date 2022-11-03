def contador_palavras(filename):

    with open(filename, "r", encoding="utf-8") as file_object:
        conteudo = file_object.read()

    palavras = conteudo.split()

    return len(palavras)

while True:
    opcao = int(input(
        "1- the_prince\n"
        "2- Children_of_destiny_by_Molly_Elliot_Seawell\n"
        "3- A_bird_of_passage_by_B_M_Croker\n"
        "0 - sair\n"
    ))

    if opcao ==1:
        print(contador_palavras("the_prince.txt"))
    elif opcao == 2:
        print(contador_palavras("A_bird_of_passage_by_B_M_Croker.txt"))
    elif opcao ==3:
        print(contador_palavras("Children_of_destiny_by_Molly_Elliot_Seawell.txt"))
    elif opcao== 0:
        break