#caminho e nome do arquivo guardado na variável

filename = "arquivo.txt"

#abrindo um arquivo como leitura
with open(filename, "r", encoding="utf-8") as file_object:

    #criando uma "repetição" para ler por linhas
    for linha in file_object:

        #imprimindo a linha lida
        print(linha.rstrip())